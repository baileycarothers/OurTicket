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
    $ticket_count = 5;
    for($i = 0; $i < $ticket_count; $i++){
        echo "Ticket No. " . $all_exp[$counter++] . "<br>"; 
        echo "Ticket Name:".$all_exp[$counter++]."<br>";
        echo "Ticket Category:".$all_exp[$counter++]."<br>";
        echo "Ticket Priority:".$all_exp[$counter++]."<br>";
        echo "Ticket Description:".$all_exp[$counter++]."<br><br>"; ?>
        <form action="./../../ticket_access.py" method="post">
        	<input type="submit" name="upvote" class="button" value="Upvote" />
        	<input type="submit" name="close" class="button" value="Close" />
        </form> <?php
    }
    
    echo "Ticket No."; 
    echo "Ticket Name:";
    echo "Ticket Category:";
    echo "Ticket Priority:";
    echo "Ticket Description:";
?>
</body>
</html>
