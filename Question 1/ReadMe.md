**Vos mots de passe sont-ils vraiment sécurisés ❓**

**Plan 🗒 :**

• Complexité d'un mot de passe avec les combinatoires

Je montre le nombre de combinaisons pour plusieurs mots de passe : alphabet, majuscule, chiffre et caractère spéciaux. Utilisation d'un programme de brute force.

• Comment crée un mot de passe sécurisé ?

` 	`J'explique comment sécuriser un mot un mot de passe et je donne des chiffres de personne pirater par ans.

**Phrase d'accroche 🚀 :**

Un mot de passe de 12 chiffres peut être trouvé avec un algorithme de brute force en 2 secondes alors on peut se demander vos mots de passe sont-ils vraiment sécurisés ?

**Projet d'avenir 💻 :**

• Mon parcours

`	`Collège classique

Seconde général 

Première : Mathématiques, NSI, Physique 

Terminal : NSI, Mathématiques

• Ce que je veux faire

`	`Faculté des sciences, licence Mathématique Informatique

`	`Développeur









**Introduction :**

Aujourd’hui les mots de passe sont partout, sur vos applications de santé, sur vos comptes bancaires, sur vos réseaux sociaux, vos e-mails personnels ou bien encore sur vos sites de commerce en ligne. Et aujourd’hui leur sécurité est assurée essentiellement par vos mots de passe.

C’est pour cela que c’est devenu de nos jour super important de bien les choisir. D’après CYCLONIS près de 83% de personnes utilisent le même mot de passe sur plusieurs sites pour une question de simplicité mais cela n’est vraiment pas conseillé. 

Alors on peut se demander quand un mot de passe est-il sécurisé ?

**Partie 1 :**

Mais alors quelle est la complexité d’un mot de passe et comment le rendre plus complexe ?

Un mot de passe à 4 chiffres à 10 000 possibilités 104 car 10 chiffres : {0,1,2,3,4,5,6,7,8,9}

- Un mdp à 10 lettre minuscule à 2610 possibilité soit 1,41\*1014 : {abcdefghijklmnopqrstuvwxyz}

- Un mdp à 10 lettre minuscule, majuscule, caractère spéciaux chiffre à 9010 possibilité soit 3,4\*1019

{abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789@#$%^&\*()\_+-=[]{}|;':,./<>?}

Un mdp de la même taille mais avec des majuscules, des caractère spéciaux et le chiffre en plus est donc 246 996 fois plus complexe soit :

90102610

**Partie 2 :**

Autant de possibilité c’est surprenant ça nous semble énorme mais avec simple algorithme de brute force.

Brute force : Les attaques par brute force consistent à trouver un mot de passe ou une clé en testant successivement toutes les combinaisons possibles. L'attaque peut se faire par ordre alphabétique comme ici.

Ici vous avez une simple algorithme de brute réaliser par mes soins qui tient donc en 10 lignes et permet de trouver un mot de passe à 7 charactère composée de minuscule en 0,0070 seconde.
