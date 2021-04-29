<?php 

$title = $_POST['title'];
$category = $_POST['category'];
$priority = $_POST['priority'];
$details = $_POST['details'];

$toss = shell_exec("./../../Source/ticket_access.py -n \"". $title . "\" -c \"" . $category . "\" -d \"" . $details . "\"");

echo "<h3>Submission Received, code: " . $toss;
?>