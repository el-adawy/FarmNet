<?php
	//Pour la démo on évite d'utiliser mysql
	if (isset($_POST['pseudo'])&&isset($_POST['password'])){
	   if($_POST['pseudo']=='admin'&&$_POST['password']=='admin'){
		header('Location: dashboard.php');
	   }
	   else{
		echo 'Identifiant ou mot de passe incorrect';
	   }
	}
?>