from flask import Flask, render_template, request, jsonify
# from flask_talisman import Talisman

import requests

import openai, os
import pandas as pd
import numpy as np
from ast import literal_eval
# from articledb.article import answer_question
from openai.embeddings_utils import distances_from_embeddings, cosine_similarity

def create_context(
    question, df, max_len=1800, size="ada"
):
    """
    Create a context for a question by finding the most similar context from the dataframe
    """

    # Get the embeddings for the question
    q_embeddings = openai.Embedding.create(input=question, engine='text-embedding-ada-002')['data'][0]['embedding']

    # Get the distances from the embeddings
    df['distances'] = distances_from_embeddings(q_embeddings, df['embeddings'].values, distance_metric='cosine')


    returns = []
    cur_len = 0

    # Sort by distance and add the text to the context until the context is too long
    for i, row in df.sort_values('distances', ascending=True).iterrows():
        
        # Add the length of the text to the current length
        cur_len += row['n_tokens'] + 4
        
        # If the context is too long, break
        if cur_len > max_len:
            break
        
        # Else add it to the text that is being returned
        returns.append(row["text"])

    # Return the context
    return "\n\n###\n\n".join(returns)

def answer_question(
    df,
    model="text-davinci-003",
    question="Am I allowed to publish model outputs to Twitter, without a human review?",
    max_len=1800,
    size="ada",
    debug=False,
    max_tokens=150,
    stop_sequence=None
):
    """
    Answer a question based on the most similar context from the dataframe texts
    """
    context = create_context(
        question,
        df,
        max_len=max_len,
        size=size,
    )
    # If debug, print the raw model response
    if debug:
        print("Context:\n" + context)
        print("\n\n")

    try:
        # Create a completions using the question and context
        response = openai.Completion.create(
            prompt=f"Answer the question based on the context below, and if the question can't be answered based on the context, say \"I don't know\"\n\nContext: {context}\n\n---\n\nQuestion: {question}\nAnswer:",
            temperature=0,
            max_tokens=max_tokens,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
            stop=stop_sequence,
            model=model,
        )
        return response["choices"][0]["text"].strip()
    except Exception as e:
        print(e)
        return ""


def send_message2Summer(question):
    webex_msg_api_url = 'https://webexapis.com/v1/messages'

    WEBEX_ACCESS_TOKEN = os.getenv("WEBEX_ACCESS_TOKEN")
    ASK_SUMMER_BOT_ID = os.getenv("ASK_SUMMER_BOT_ID")
    
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {WEBEX_ACCESS_TOKEN}'
    }

    msg = {
        "roomId": ASK_SUMMER_BOT_ID,
        "text": f'{question}'
    }

    requests.post(webex_msg_api_url, headers=headers, json = msg)

    return "I'm unsure, but I'll inform Summer."

openai.api_key = os.getenv("OPENAI_API_KEY")


df = pd.read_csv('./articledb/embeddings.csv', index_col=0)
df['embeddings'] = df['embeddings'].apply(literal_eval).apply(np.array)

app = Flask(__name__)
# Talisman(app)

@app.route('/') 
@app.route('/index')
@app.route('/home')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route('/architecture')
def architecture():
    return render_template('architecture.html')

@app.route('/engineering')
def engineering():
    return render_template('engineering.html')

@app.route('/askSummer', methods=['GET', 'POST'])
def askSummer():
    if request.method == 'POST':
        question = request.form['question']
        answer = answer_question(df, question=question)

        if answer == "I don't know.":
            return send_message2Summer(question)
    return answer
