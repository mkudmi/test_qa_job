<?php
    define('GET_METHOD', 'GET');
    define('POST_METHOD', 'POST');
    define('PUT_METHOD', 'PUT');
    define('DELETE_METHOD', 'DELETE');

    header("Content-Type: text/application-json; charset=UTF-8");

    $dbconf['host'] = getenv('MYSQL_SERVER');
    $dbconf['username'] = getenv('MYSQL_USER');
    $dbconf['password'] = getenv('MYSQL_PASSWORD');
    $dbconf['database'] = getenv('MYSQL_DATABASE');;
    $dbconf['dbport'] = 3306;
?>