//File: dbConnect.php
//Used to search the datbase for the query
//Created for the project WebCrawlerText

<?php
$notify = "";
$word  = $_POST['word'];
$boolean  = $_POST['boolean'];

echo $boolean;

//breaking query into keywords
$array = explode(' ', $word);

// send the data to the database
$username = "root";
$password = "";
$hostname = "localhost";

//connection to the database
$dbhandle = mysql_connect($hostname, $username, $password)
 or die("Unable to connect to MySQL");
echo "Connected to MySQL<br>";

//select a database to work with
$selected = mysql_select_db("searchEngine",$dbhandle)
  or die("Could not select search");

//execute the SQL query and return records
if($boolean)
{
  $result = mysql_query("SELECT DISTINCT m.sourceLink".
            " FROM metaData m JOIN keywords k".
            " WHERE k.keyword = '$array[0]' AND k.keyword = '$array[1]'".
            " ON m.sourceLink = k.sourceLink ");
}

else
{
  $result = mysql_query("SELECT DISTINCT m.sourceLink".
            " FROM metaData m JOIN keywords k".
            " WHERE k.keyword = '$array[0]' OR k.keyword = '$array[1]'".
            " ON m.sourceLink = k.sourceLink ");
}
//fetch tha data from the database
$i = 0;
while ($row = mysql_fetch_array($result)) {
   echo "Link "."$i".":";
   echo "<a href='$row'>'$row'</a>"; //display the results
   $i = $i + 1;
}
//close the connection
mysql_close($dbhandle);
?>