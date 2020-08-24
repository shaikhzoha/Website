<html>
<body>
<table>
<tbody>
<?php
require('dbconnect.php');
$query="select * from example";
$result=mysqli_query($connection, $query) or die(mysqli_error($connection));
$row = mysqli_fetch_array($result);
$i=0;
while($i<mysqli_num_fields($result)){
	echo"<tr>";
	$meta=mysql_fetch_field($result);
	echo'<td>'.meta->name.'</td>';
	$value=$row["&meta->name"];
	echo'<td>'.$value.'</td>';
	$i=$i+1;
	echo "</tr>";
}
?>
</tbody>
</table?
</body>
</html>