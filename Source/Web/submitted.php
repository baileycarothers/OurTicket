<?php 

$title = $_POST['title'];
$category = $_POST['category'];
$priority = $_POST['priority'];
$details = $_POST['details'];

echo "/usr/bin/python3 ../ticket_access.py -a -n \"". $title . "\" -c \"" . $category . "\" -d \"" . $details . "\" 2>&1"
echo "<br>"
$toss = shell_exec("/usr/bin/python3 ../ticket_access.py -a -n \"". $title . "\" -c \"" . $category . "\" -d \"" . $details . "\" 2>&1");

echo "<h3>Submission Received, code: " . $toss;
?>