<!DOCTYPE html>

<head>
    <meta charset="UTF-8">
    <title>Lightning Shield</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js" integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js" integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1" crossorigin="anonymous"></script>
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.4.1/js/bootstrap.min.js" integrity="sha384-wfSDF2E50Y2D1uUdj0O3uMBJnjuUD4Ih7YwaYd1iqfktj0Uod8GCExl3Og8ifwB6" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="style/style.css">

</head>

<!--NAVBAR--->
<nav class="navbar navbar-expand-sm bg-dark navbar-dark">
    <button class="navbar-toggler collapsed" type="button" data-toggle="collapse" data-target="#main-navbar	" aria-controls="navbarsExampleDefault" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
    </button>

    <div class="navbar-collapse collapse" id="main-navbar">
        <ul class="nav navbar-nav mx-auto">
            <li class = "nav-item">
                <a class = "nav-link" href="index.php?page=sqli">Test Our SQLI Protection</a>
            </li>
            <li class = "nav-item">
                <a class = "nav-link" href="index.php?page=csrf">Test Our CSRF Protection</a>
            </li>
            <li class = "nav-item">
                <a class = "nav-link" href="index.php?page=xss">Test Our XSS Protection</a>
            </li>
            <li class="nav-item active">
                <a class="nav-link" href="index.php?page=home">Home<span class="sr-only">(current)</span></a>
            </li>
        </ul>
    </div>
</nav>

<div class="container">
    <div class="row">
        <div class="col-md-3 text-center" id="side_gadgets">
            <div class="widget widget-list" style="text-align: center;">


                <a class="btn btn-lg btn-danger" href="index.php?page=home" style="width: -webkit-fill-available;">
                    <span><b>Home Page</b><br><small></small></span>
                </a>
                <div class="widget-blob-sperator"></div>
                <a class="btn btn-lg btn-warning" href="index.php?page=test" style="width: -webkit-fill-available;">
                    <span><b>XSS DEFENCE</b><br><small></small></span>
                </a>
                <div class="widget-blob-sperator"></div>
                <a class="btn btn-lg btn-success" href="index.php?page=csrf" style="width: -webkit-fill-available;">
                    <span><b>CSRF PROTECTION</b><br><small></small></span>
                </a>
                <div class="widget-blob-sperator"></div>
                <a class="btn btn-lg btn-danger" href="index.php?page=sqli" style="width: -webkit-fill-available;">
                    <span><b>SQL INJECTION PROTECTION</b><br><small></small></span>
                </a>
                <div class="widget-blob-sperator"></div>
                <a class="btn btn-lg btn-warning" href="index.php?page=about" style="width: -webkit-fill-available;">
                    <span><b>About Page</b><br><small></small></span>
                </a>
            </div>
        </div>


        <div class="col-md-9">
            <div class="panel">
                <div class="m-5">



