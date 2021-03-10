=============================
Création d'une classe matrice
=============================

Exercice 1
----------

Dans le fichier ``matrix.py`` Écrire le code permettant:

 - d'afficher une matrice (la méthode ``__repr__``), cette méthode doit
   retourner une chaîne de caractères de type ``str``
 - d'additionner une matrice avec une autre (la méthode ``__add__``)
 - de soustraire une matrice avec une autre (la méthode ``__sub__``)
 - de multiplier une matrice avec une autre (la méthode ``__mul__``)
 - de retourner le nombre de colonne d'une matrice (la méthode ``nombre_de_colonnes``)
 - de retourner le nombre de lignes d'une matrice (la méthode ``nombre_de_lignes``)
 - de retourner la matrice transposée d'une matrice (la méthode ``transpose``)

Pour chaque méthode, conserver les exemples que vous effectuez et
copiez-collez ces exemples dans la documentation qui accompagne chaque
méthode en immitant la syntaxe utilisée pour les méthodes ``__init__`` et
``__getitem__`` ci-bas. Ce contenu et ces exemples serviront par la suite
pour tester le fonctionnement et générer la documentation automatiquement.

Comme vous faîtes ce projet en groupe, vous allez tout d'abord diviser les
tâches parmi vous. Vous allez partager vos contributions en utilisant le
logiciel de contrôle de version ``git`` et le dépôt de votre équipe sur le
gitlab de l'Université de Bordeaux.

Rappels sur ``git``
-------------------

Une fois que vous avez fini une modification et que vous voulez la partager
aux autres de votre groupe, **fermez d'abord le fichier contenant vos
modifications!!** et faites les commandes suivantes. 

D'abord, assurez-vous que vous êtes à jour, c'est-à-dire que vous avez les
plus récentes modifications faites par les autres::

    git pull

Si vous n'êtes pas à jour et que vous avez des modifications locales non
commitées, vous pouvez faire ceci::

    git stash            # remiser vos modifications
    git pull             # mettre à jour votre dépôt
    git stash apply      # réappliquer vos modifications
    
Ensuite vous pouvez consulter vos modifications::

    git diff
    git status

Ensuite vous pouvez ajouter les fichiers dont les modifications feront
partie du prochain commit::

    git add <files>
    
Ensuite vous pouvez consulter ce qui sera commité::

    git status
    git diff --cached

Vous faîtes votre commit en ajoutant un message décrivant vos modifications::

    git commit -m "<message>"

Ensuite vous publiez vos modifications sur le serveur::

    git push

Vous pouvez maintenant dire à vos collègues de faire ``git pull`` afin
qu'ils bénéficient de vos contributions::

    git pull

Exercice 2
----------

Si vous avez terminé avant les autres groupes, vous pouvez écrire le code
permettant de retourner l'inverse additif d'une matrice (la méthode
``__neg__``) de calculer le déterminant, l'inverse, le polynôme
caractéristique et les valeurs propres d'une matrice.
