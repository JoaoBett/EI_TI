<!DOCTYPE html>
<html lang="en-pt">

<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Dashboard_PHP</title>
</head>

<body>
    <header>
        <h1></h1>
    </header>
    <?php
        session_start();
        if(!isset($_SESSION['username'])){
            header ("refresh:5;url=index.php");
            die("Acesso restrito.");
        }

    ?>
    <h1 id="CV">Curriculum Vitae</h1>
    <img id="imagem"
        src="https://us.123rf.com/450wm/mimagephotography/mimagephotography1511/mimagephotography151100038/48581692-close-up-horizontal-portrait-of-a-serious-man-with-beard-isolated-on-white-background.jpg?ver=6"
        alt="some text" width="150" height="100">
    <h2 id="nome"><b>Alexandre Lopes</b></h2>
    <hr>
    <h3>Informações pessoais:</h3>
    <p><b>Morada: </b>Rua General Norton de Matos, 2411-901 Leiria</p>
    <p><b>Telefone: </b>+351 244 820 300</p>
    <p><b>Email: </b>alexandre.lopes@ipleiria.pt</p>
    <hr>
    <h3>Formação académica:</h3>
    <ol>
        <li><b>Datas:</b> 2015-2018</li>
        <li><b>Nivel de Escolaridade: </b> 12º ano</li>
        <li><b>Escola: </b> <a href="https://www.ipleiria.pt/" target="_blank">Escola Secundária Dominges Sequeira</a>
        </li>
    </ol>
    <hr>
    <h3>Preferência Clubes Futebol:</h3>
    <ol type="i">
        <li>U.D.Leiria</li>
        <li>Liverpool</li>
        <li>Bayern</li>
    </ol>
    <hr>
    <a class="botao" href="videos.html">Portfolio</a>
    <a class="botao" href="idiomas.html">Idiomas</a>
    <footer>
        <p id="rodape">Engenharia Informática - Tecnlogias de Internet</p>
    </footer>
</body>

</html>