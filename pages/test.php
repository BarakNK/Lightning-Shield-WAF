<form action="" method = "POST" enctype = "multipart/form-data">
    <h1>WAF testing Lightning Shield</h1>
    <hr>
    <div class="form-group">
        <h6>Enter an input:</h6>
        <input name = "input" id = "email" class="form-control" required/>
    </div>

    <button type = "submit" class = "btn btn-outline-primary" name="enter" >Enter</button>
</form>
<hr>

<?php
if (isset($_POST["enter"]))
{
    echo $_POST["input"];
}

?>