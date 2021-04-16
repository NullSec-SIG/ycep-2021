<?php
echo "HELLO<br>";
echo "dXNlIGdldCByZXF1ZXN0IHVzaW5nIHZpZXdzb3VyY2UgcGFyYW1ldGVy";
include("flag.php");

if (isset($_GET['viewsource'])) {
	show_source("index.php");
}

if (!isset($_GET['flag'])) {
	die("<br><br>whrs the flag");
}
echo "Its here";

if (!isset($_GET['secret'])) {
	die("<br><br>You are not Authorized!");
}
echo "<br>flag is not here";
echo "<!--$flag--Level 2>";

?>