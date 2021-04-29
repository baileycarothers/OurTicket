<html>
<body>
<?php 
    //echo "<h1>" . Big Nuts XD . "</h1>";
    //Some command for getting the number of tickets from the python
    
    #b r u h
    $all = shell_exec("./../ticket_access.py -z");
    $all_exp = explode("\n", $all);
    
    $counter =0;
    /*
    foreach($all_exp as $sure){
        echo $sure;
    }*/
    
    
    //for loop for each ticket
    $ticket_count = shell_exec("./../ticket_access.py -g 2>&1");
    //$ticket_count = 10;
    for($i = 0; $i < $ticket_count; $i++){
        $fields = array();
        for($j = 0; $j < 6; $j++){
            $fields[$j] = $all_exp[$counter++];
        }
        
        echo "Ticket No. " . $fields[0] . "<br>"; 
        echo "Ticket Name: ".$fields[1]."<br>";
        echo "Ticket Votes: ".$fields[2]."<br>";
        echo "Ticket Category: ".$fields[3]."<br>";
        echo "Ticket Priority: ".$fields[4]."<br>";
        echo "Ticket Description: ".$fields[5]."<br><br>"; ?>
        <form action="voted.php" method="post">
        	<input type="submit" name="<?php print("upvote,".$fields[0]);?>" class="button" value="upvote" />
        	<input type="submit" name="<?php print("close,".$fields[0]);?>" class="button" value="close" />
        </form> <?php
    }
    
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
</body>
</html>
