<form action="" method = "POST" enctype = "multipart/form-data">
    <h1>WAF testing Lightning Shield</h1>
    <h3>Note - this is a basic test of XSS and SQL INJECTION.</h3>
    <hr>
    <h2>Enter an input:</h2>
    <input name = "input" id = "email" required/>

    <button type = "submit" name="enter" >Enter</button><br>
    <strong>SQL QUERY: SELECT * FROM users WHERE name = '{YOUR_INPUT}'</strong>
    <p>SQLI for example: write "' OR 1=1-- " to print everyone</p>
</form>

<?php
if (isset($_POST["enter"]))
{
    $query = "SELECT * FROM users WHERE name = '".$_POST["input"]."'";
    $queryStatus = mysqli_query($con, $query) or die(mysqli_error($con));

    if (mysqli_num_rows($queryStatus) > 0) { // if found results
        while($row = mysqli_fetch_array($queryStatus)) { //print all of them
            for ($i = 0; $i < count($row); $i++)
                if (!empty($row[$i]))
                    echo $row[$i];
            echo "<br>";
        }
    }
    else
    {
        echo "No results for ".$_POST["input"];
    }
}

?>