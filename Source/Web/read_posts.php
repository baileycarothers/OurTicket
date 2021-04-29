<html>
<body>
<?php 
    //echo "<h1>" . Big Nuts XD . "</h1>";
    //Some command for getting the number of tickets from the python
    
    #b r u h
    $id = shell_exec("./../../ticket_access.py ")
    
    
    //for loop for each ticket
    $ticket_count = 10;
    for($i = 0; $i < $ticket_count; $i++){
        echo "Ticket No.<br>"; 
        echo "Ticket Name:<br>";
        echo "Ticket Category:<br>";
        echo "Ticket Priority:<br>";
        echo "Ticket Description:<br><br>";
    }
    
    echo "Ticket No."; 
    echo "Ticket Name:";
    echo "Ticket Category:";
    echo "Ticket Priority:";
    echo "Ticket Description:";
?>
</body>
</html>
