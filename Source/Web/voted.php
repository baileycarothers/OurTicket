<?php 
    $upvote = $_POST['upvote'];
    $upvote_e = explode(",", $upvote);
    $close = $_POST['close'];
    $close_e = explode(",", $close);
    
    print($upvote_e[1]);
    print($upvote_e[0]);
    
    if($upvote){
        $out = shell_exec("./../ticket_access.py -f ".$upvote_e[1]." -v 2>&1");
        print($out);
    }
?>