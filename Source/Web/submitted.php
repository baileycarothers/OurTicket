<?php 

$title = $_POST['title'];
$category = $_POST['category'];
$priority = $_POST['priority'];
$details = $_POST['details'];

$toss = shell_exec("./../ticket_access.py -a -n \"". $title . "\" -c \"" . $category . "\" -d \"" . $details . "\" 2>&1");

echo "<h3>Submission Received, code: " . $toss;
?>