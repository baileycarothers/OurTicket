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
  <br>
  <label for="details">Details 2:</label>
  Details:  <textarea id="details" rows="5" cols="60" name="details"></textarea><br>
  <br>
 <input type="submit">
</form>
