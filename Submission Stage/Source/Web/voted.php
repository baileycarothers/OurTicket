<?php 
    $upvote = $_POST['upvote'];
    $upvote_e = explode(",", $upvote);
    $close = $_POST['close'];
    $close_e = explode(",", $close);
    
    echo($upvote_e[1]);
    echo($upvote_e[0]);
    echo(($upvote==NULL));
    print("doggi");
    
    if($upvote){
        $out = shell_exec("./../ticket_access.py -v -f ".$upvote_e[1]."  2>&1");
        echo($out);
    }
?>