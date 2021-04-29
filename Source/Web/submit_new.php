<html>
<body>

<form method="post" action="submitted.php">
  Title: <input type="text" name="title">
  <br>
  <label for="category">Select a Category:</label>
  Category:<select id="category" name="category">
                <option value="1">Feature Request</option>
                <option value="2">Bug Report</option>
                <option value="3">Other</option>
            </select>
  <br>
 <label for="priority">Select a Priority:</label>
  Priority: <select id="priority" name="priority">
                <option value="0">0 (highest)</option>
                <option value="1">1</option>
                <option value="2">2</option>
            </select>
  <br>
  <label for="details">Details 2:</label>
  Details:  <textarea id="details" rows="5" cols="60" name="content"></textarea><br>
  <br>
 <input type="submit">
</form>
