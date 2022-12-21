# P9 Réalisez une application de recommandation de contenu
![image](https://user-images.githubusercontent.com/54436066/208915668-5111ff5d-19f4-40df-acc7-770b45c01576.png)


Projet 9 Openclassrooms

My Content est une start-up qui veut encourager la lecture en recommandant des contenus pertinents pour ses utilisateurs.


Vous êtes le CTO et cofondateur de la start-up avec Samia qui est CEO. Vous êtes en pleine construction d’un premier MVP qui prendra la forme d’une application. 

Dans un premier temps, votre start-up souhaite tester une solution de recommandation d’articles et de livres à des particuliers.

Comme vous ne disposez pas à ce jour de données utilisateurs, vous allez utiliser des données disponibles en ligne pour développer votre MVP (en téléchargement direct à ce lien).

Ces données représentent les interactions des utilisateurs avec les articles disponibles. Elles contiennent des informations sur les articles (par exemple le nombre de mots dans l’article), ainsi que les informations sur les sessions des utilisateurs (par exemple heures de début et de fin) et les interactions des utilisateurs avec les articles (sur quel article l’utilisateur a-t-il cliqué lors de sa session ?).

Dans une logique de MVP, Samia et vous avez identifié la fonctionnalité la plus critique pour lancer votre application : 

"En tant qu’utilisateur de l’application, je vais recevoir une sélection de cinq articles."

Vous avez également identifié que la prise en compte de l’ajout de nouveaux utilisateurs et de nouveaux articles dans l’architecture cible de votre produit est déterminante.

Vous avez fait appel à Julien, développeur web en freelance, pour vous conseiller dans la réalisation d’une première version simplifiée de l’application. Il vous a fait le retour suivant par mail.

De : Julien

Envoyé : Hier 17:14

À : Vous 

Objet : Conseils de réalisation de l’application

Hello !

Je te propose deux types d’architectures simples à mettre en oeuvre. Je te conseille d’utiliser dans les deux cas une architecture serverless. Azure Functions est un service permettant de mettre en place rapidement ce type d’architecture serverless dans le cloud :

Dans la première architecture, tu crées une API pour développer puis exposer ton système de recommandation. Pour faire le lien entre l’application et le système de recommandation, tu crées une Azure Function
Dans la deuxième architecture, tu peux te passer de l’API, en exploitant les fonctionnalités “Azure Blob storage input binding” pour récupérer directement les fichiers et modèles, et en intégrant tes prédictions directement dans ton Azure Functions
Je te laisse choisir l’architecture que tu mettras en place !

Pour l’application, tu peux créer en local une simple interface qui liste les id des users et affiche les résultats des 5 suggestions d’articles, suite à appel de l’Azure Functions.

Une petite astuce : si tu veux mettre en production le fichier “embeddings” et qu’il est trop volumineux par rapport à tes limitations d’utilisation des services gratuits Azure, tu peux réaliser une réduction de dimension de ce fichier via une ACP.

Au plaisir de retravailler ensemble sur un prochain projet !

Julien

 

En résumé, votre mission est la suivante :

développer une première version de votre système de recommandation sous forme d’Azure Functions;
réaliser une application simple de gestion du système de recommandation (interface d’affichage d’une liste d’id utilisateurs, d’appel Azure functions pour l’id choisi, et d’affichage des 5 articles recommandés)
stocker les scripts développés dans un dossier GitHub ;
synthétiser vos premières réflexions sur :
l’architecture technique et la description fonctionnelle de votre application à date, et le système de recommandation,
l’architecture cible pour pouvoir prendre en compte l’ajout de nouveaux utilisateurs ou de nouveaux articles, que vous présenterez à Samia.
 

Livrables 
Une application simple (Flask, Streamlit), complétée avec le système de recommandation en serverless qui recevra en entrée un identifiant utilisateur et retournera les recommandations d’articles associées (par exemple le top 5).
Ce livrable permettra de démontrer les fonctionnalités de l’application à Samia et à de futurs utilisateurs.
Les scripts développés, stockés dans un système de gestion de version (Git en local avec push sur Github) permettant le déploiement de l’application de bout-en-bout.
Ce livrable vous servira à présenter le caractère “industrialisable” de votre travail.
Un support de présentation (PowerPoint ou équivalent, sauvegardé au format pdf, 15 à 25 slides), contenant une brève description fonctionnelle de l’application, une présentation des différents modèles analysés et de leurs avantages et inconvénients, un schéma de l’architecture retenue, une présentation du système de recommandation utilisé et un schéma de l’architecture cible permettant de prendre en compte la création de nouveaux utilisateurs et de nouveaux articles.
Ce livrable vous permettra de présenter votre travail à Samia.
Pour faciliter votre passage devant le jury, déposez sur la plateforme, dans un dossier zip nommé “Titre_du_projet_nom_prénom”, votre livrable nommé comme suit : Nom_Prénom_n° du livrable_nom du livrable_date de démarrage du projet. Cela donnera : 

Nom_Prénom_1_application_mmaaaa
Nom_Prénom_2_scripts_mmaaaa
Nom_Prénom_3_presentation_mmaaaa
Par exemple, votre premier livrable peut être nommé comme suit : Dupont_Jean_1_application_012022.

Soutenance
Pendant la soutenance, l’évaluateur jouera le rôle de Samia, la cofondatrice de My Content. Vous lui présenterez l’ensemble de votre travail. 

Présentation (20 minutes) 
des différentes approches de modélisation testées (10 minutes),
des fonctionnalités du système de recommandation dans l’application (6 minutes), 
de l’architecture technique cible retenue (2 minutes),
d’une démonstration de l’application (2 minutes).
Discussion (5 minutes)
L’évaluateur vous challengera sur vos choix. 
Débriefing (5 minutes)
À la fin de la soutenance, vous pourrez débriefer ensemble.
