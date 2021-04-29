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
    echo $ticket_count;
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
        <form action="./../../ticket_access.py" method="post">
        	<input type="submit" name="upvote" class="button" value="Upvote" />
        	<input type="submit" name="close" class="button" value="Close" />
        </form> <?php
    }
    
?>
</body>
</html>
