<?php
// Данные для подключения к базе данных
$host = getenv("MYSQL_SERVER");
$username = getenv("MYSQL_USER");
$password = getenv("MYSQL_PASSWORD");
$database = getenv("MYSQL_DATABASE");

// Открываем файл с sql-запросами для чтения
while(true){
	try {
		$connection = mysqli_connect($host, $username, $password, $database);
		break;
	} catch (Exception $e) {
		continue;
	}
}
createDB($connection, "/tmp/db.sql");
insertData($connection, "/tmp/data.sql");
mysqli_close($connection);

function insertData($connection, $sqlFile) {
	$file = fopen($sqlFile, "r");
	if ($file) {
		$content = fread($file, filesize($sqlFile));
		fclose($file);
		$queries = explode(";", $content);
		foreach ($queries as $query) {
			if (($query = trim($query)) == "")
				continue;
			$res = mysqli_query($connection, $query);
			if($res instanceof mysqli_result && mysqli_num_rows($res) > 0) {
				echo "No need to insert values\n";
				break;
			}
		}
		echo "Миграция базы данных выполнена успешно!\n";
	} else {
		echo "Не удалось открыть файл с sql-запросами.\n";
	}
}

function createDB($connection, $sqlFile) {

	$file = fopen($sqlFile, "r");
	if ($file) {
		$content = fread($file, filesize($sqlFile));
		fclose($file);
		$queries = explode(";", $content);
		foreach ($queries as $query) {
			if (($query = trim($query)) == "")
				continue;
			mysqli_query($connection, $query);
		}
		echo "Миграция базы данных выполнена успешно!\n";
	} else {
		echo "Не удалось открыть файл с sql-запросами.\n";
	}
}
?>
