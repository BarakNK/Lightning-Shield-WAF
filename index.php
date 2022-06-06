<?php
require_once ("config.php");

$page = isset($_GET['page']) ? $_GET['page'] : "home";
include ("structure/header.php");


switch ($page)
{
    case "home":
        include_once("pages/home.php");
        break;
    case "sqli":
        include_once ("pages/sqli.php");
        break;
    case "csrf":
        include_once ("pages/csrf.php");
        break;
    case "xss":
        include_once ("pages/xss.php");
        break;
    case "about":
        include_once ("pages/about.php");
        break;
    case "test":
        include_once ("pages/test.php");
        break;
    default:
        echo "Page not found!";
        break;
}
include ("structure/footer.php");
?>