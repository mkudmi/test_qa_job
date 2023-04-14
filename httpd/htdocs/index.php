<?php
include_once('config.php');

function countData(mysqli $mysqli): int{
	$result = $mysqli->query("SELECT COUNT(*) as count FROM phonelist");
	return $result->fetch_assoc()['count'];
}

function getData(mysqli $mysqli, int|null $limit = 10, int|null $offset = 0, $id = null): array{
	if ($id) {
		$sql = "SELECT * FROM phonelist WHERE id = $id LIMIT $limit OFFSET $offset";
	} else {
		$sql = "SELECT * FROM phonelist LIMIT $limit OFFSET $offset";
	}
	$result = $mysqli->query($sql);
	$data = [];
	while ($row = $result->fetch_assoc()) {
		$data[] = $row;
	}
	return $data;
}

function connect(array $conf): mysqli{
	$mysqli = new mysqli($conf['host'], $conf['username'], $conf['password'], $conf['database']);
	
	if ($mysqli->connect_error) {
		die("Connection failed: " . $mysqli->connect_error);
	}
	return $mysqli;
}

function extract_id(array $arr): array {
	$res = [];

	foreach ($arr as $key => $val) {
		if ($key == 'id')
			continue;
		$res[$key] = $val;
	}
	return $res;
}

function updateData(mysqli $mysqli, int|string $id, array $data): bool {
	$res = false;
	$updStmt = [];

	foreach ($data as $k => $v) {
		$updStmt[] = "$k = '$v'";
	}
	$updStmt = implode(', ', $updStmt);
	$sql = "UPDATE phonelist SET $updStmt WHERE id=$id";
	$res = $mysqli->query($sql);
	return $res;
}

function isGetRequest(): bool {
	return getRequestMethod() == GET_METHOD;
}

function isPostRequest(): bool {
	return getRequestMethod() == POST_METHOD;
}

function isPutRequest(): bool {
	return getRequestMethod() == PUT_METHOD;
}

function isDeleteRequest(): bool {
	return getRequestMethod() == DELETE_METHOD;
}

function parseGetRequest(): array|null {
	return [
		'items' => $_GET['items'] ?? 10,
		'page' => $_GET['page'] ?? 1,
		'id' => $_GET['id'] ?? null,
		'offset' => (($_GET['page'] ?? 1) - 1) * ($_GET['items'] ?? 10)
	];
}

function parseJsonRequest(): array|null {
	return json_decode(file_get_contents('php://input'), true);
}

function parseInputData(string $method): array|null {
	if ($method == GET_METHOD)
		$res = parseGetRequest();
	else
		$res =  parseJsonRequest();
	if ($res == null)
		die(json_encode(['success' => false, 'message' => 'illegal request']));
	return $res;
}

function postData(mysqli $mysqli, array $data): bool {
	$fields = implode(', ', array_keys($data));
	$values = '\'' . implode('\', \'', array_values($data)). '\'';
	$sql = "INSERT INTO phonelist ($fields) VALUES ($values)";
	return $mysqli->query($sql);
}

function writeResponse(mixed $response, string $method) {
	if ($method == GET_METHOD) {
		echo json_encode($response);
	}
	else {
		if (gettype($response) == 'boolean')
			echo json_encode(['success' => $response]);
		else
			echo json_encode(['success' => false]);
	}
	exit(0);
}

function getRequestMethod(): string {
	return $_SERVER['REQUEST_METHOD'];
}

$mysqli = connect($dbconf);
if (isGetRequest()) {
	$getData = parseInputData(GET_METHOD);

	$count = countData($mysqli);
	$data = getData($mysqli, $getData['items'], $getData['offset'], $getData['id']);
	$response = ['total' => $count, 'data' => $data];
} elseif (isPostRequest()) {
	$postData = parseInputData(POST_METHOD);
	$response = postData($mysqli, $postData);
} elseif (isPutRequest()) {
	$putData = parseInputData(PUT_METHOD);
	if (!key_exists('id', $putData))
		die(json_encode(['success' => false, 'message' => 'id is required']));
	$id = $putData['id'];
	$putData = extract_id($putData);
	$response = updateData($mysqli, $id, $putData);
} elseif (isDeleteRequest()) {
	$delete_data = parseInputData(DELETE_METHOD);
	if (!key_exists('id', $delete_data))
		die(json_encode(['success' => false, 'message' => 'id is required']));
	$id = $delete_data['id'];
	$sql = "DELETE FROM phonelist WHERE id=$id";
	$response = $mysqli->query($sql);
}
$mysqli->close();
writeResponse($response, getRequestMethod());
?>