<!DOCTYPE html>
<html lang="en-pt">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">
    <link rel="stylesheet" href="style.css">
    <title>PHP_Ficha4</title>
</head>
<body>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>
    <?php
        $username="nome_do_utilizador_que_quiser";

        password_hash("a_password_que_quiser_utilizar_mas_nao_utilize_passwords_ja_utilizadas_por_si_noutros_sistemas",PASSWORD_DEFAULT);
        $password_hash='valor_copiado_do_exercicio_anterior';
        
        if (password_verify ($_POST['password'], $password_hash)) {

            echo "Password correta!";
        
        }

    ?>
    <div class="container">
        <div class="row align-items-center" >
            <img src="https://ead.ipleiria.pt/2022-23/pluginfile.php/166632/question/questiontext/693297/7/4353030/estg_h.png" alt="estg">
            <form action="">
                <label for="username">Username: </label><br>
                <input type="text" id="username" name="username" value="username" required><br>
                <label for="password">Password</label><br>
                <input type="text" id="password" name="password" value="password" required><br><br>
                <input type="submit" value="Submit">
            </form>
        </div>
    </div>
</body>
</html>
