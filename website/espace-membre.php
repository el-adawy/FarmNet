<!DOCTYPE html>
<html lang="fr">
<head>
	<meta charset="utf-8">
	<meta http-equiv="X-UA-Compatible" content="IE=edge">
	<meta name="viewport" content="width=device-width, initial-scale=1">
	<title>FarmNet</title>
	<link href="css/bootstrap.min.css" rel="stylesheet">
	<link href="css/font-awesome.min.css" rel="stylesheet">
	<link href="css/owl.carousel.css" rel="stylesheet">
	<link href="css/style.css" rel="stylesheet">
	<style>
</style>
	<!--[if lt IE 9]>
      <script src="https://oss.maxcdn.com/html5shiv/3.7.2/html5shiv.min.js"></script>
      <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
	<![endif]-->	
</head>

<?php include('header.php'); ?>

<body>




<div id="wrapper">
	
	<section id="features-list" class="separator top">
	  <div class="container">
	    <br><br>
	    <p> Identifiant: admin<br>Mot de passe: admin</p>
	    
		  <form action="login.php" method="POST">
		    <p><label>Identifiant: <input type="text" name="pseudo" /></label></p>
		    <p><label>Mot de passe: <input type="password" name="password" /></label></p>
		    <input type="submit" value="Se connecter" />
		  </form>
		  
		</div>
	</section>
</div>
</body>

<?php include('footer.php'); ?>

</html>
