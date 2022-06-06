<h3>Notice - this is a csrf test, you must run it from a different website than the one the WAF is defending</h3><br>
<h3>change the URL form action to your website's addresss</h3>
<form action="http://fbi.com:8000/" method = "POST" enctype = "multipart/form-data">
    <input name = "input" required/>
    <button type = "submit" name="enter" >Enter</button>
</form