<?php 
include_once("index.html"); 

$host = $_SERVER['HTTP_HOST'];

if ($host == 'www.summerfang.me') {
    header('Location: https://www.summerfang.me/index.html');
    exit;
} elseif ($host == 'www.weijiafang.com') {
    header('Location: https://www.weijiafang.com/home.html');
    exit;
} else {
    // Handle other cases or show an error message
}
?>