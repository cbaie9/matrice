r"""
Matrice

Ce module contient une classe qui représente une matrice.

https://fr.wikipedia.org/wiki/Matrice_(mathématiques)

Une classe contient un certain nombre de fonctions. Une fonction
dans une classe est appelée *méthode*.

Dans la classe Matrice ci-bas, le code de deux méthodes a déjà été écrit: 

 - la méthode ``__init__`` (appelé constructeur) qui permet de créer un
   objet de type ``Matrice``. En effet, la méthode ``__init__`` est appelée
   lorsqu'un utilisateur écrit ``Matrice(3, 3, [1,2,3,4,5,6,7,8,9])`` par
   exemple.

 - la méthode ``__getitem__`` qui retourne l'entrée de la matrice à la
   position (i,j). Par défaut, on assume que les lignes et les colones sont
   indicées à partir de zéro. Donc l'entrée à la position (0,0) est
   l'entrée en haut à gauche dans la matrice. On accède à cet élément en
   écrivant  ``M[0,0]`` (en pratique, c'est la méthode ``__getitem__`` qui
   est utilisée).

EXERCICE:

Écrire le code permettant:

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

Une fois que vous avez fini une modification et que vous voulez la partager
aux autres de votre groupe, **fermez d'abord le fichier contenant vos
modifications!!** et faites les commandes suivantes. 

D'abord, assurez-vous que vous êtes à jour, c'est-à-dire que vous avez les
plus récentes modifications faites par les autres::

    git pull

Si vous n'êtes pas à jour et que vous avez des modifications locales non
commitées, vous pouvez faire ceci:

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

Si vous avez terminé avant les autres groupes, vous pouvez écrire le code
permettant de retourner l'inverse additif d'une matrice (la méthode
``__neg__``) de calculer le déterminant, l'inverse, le polynôme
caractéristique et les valeurs propres d'une matrice.

"""
class Matrice:
    def __init__(self, ncols, nrows, entries):
        r"""
        INPUT:

        - ``ncolumns`` -- entier, nombre de colonnes
        - ``nrows`` -- entier, nombre de lignes
        - ``entries`` -- liste, les ``ncolumns*nrows`` entrées de la matrice 

        EXAMPLES::

            >>> #from matrix import Matrice
            >>> m = Matrice(3, 3, [1,2,3,4,5,6,7,8,9])

        """
        self._entries = entries
        self._ncols = ncols
        self._nrows = nrows

    def __getitem__(self, args):
        r"""
        Return the entry at position (i,j) in the matrix.

        INPUT:

        - ``i`` -- entier, i-th line with `0<=i<n` where `n` is the number
          of lines
        - ``j`` -- entier, j-th column with `0<=j<m` where `m` is the number
          of columns

        EXAMPLES::

            >>> #from matrix import Matrice
            >>> m = Matrice(3, 3, [1,2,3,4,5,6,7,8,9])
            >>> m[0,0]
            1
            >>> m[0,1]
            2
            >>> m[0,2]
            3
            >>> m[1,0]
            4

        An error is raised if the input is out-of-bound::

            >>> m[0,3]
            Traceback (most recent call last):
            ...
            ValueError: column index (j=3) must be such that 0 <= j < 3
            >>> m[-1,1]
            Traceback (most recent call last):
            ...
            ValueError: row index (i=-1) must be such that 0 <= i < 3

        """
        (i,j) = args
        if not 0 <= i < self._nrows:
            raise ValueError("row index (i={}) must be such that "
                             "0 <= i < {}".format(i,self._nrows))
        if not 0 <= j < self._ncols:
            raise ValueError("column index (j={}) must be such that "
                             "0 <= j < {}".format(j,self._ncols))
        return self._entries[self._ncols * i + j]

    def __repr__(self):
        r"""
        Retourne la représentation en chaîne de caractères de la matrice.

        EXAMPLES::

            >>> #from matrix import Matrice
            >>> m = Matrice(3, 3, [1,2,3,4,5,6,7,8,9])
            >>> m
            [1 2 3]
            [4 5 6]
            [7 8 9]
            >>> repr(m)
            "[1 2 3]\n[4 5 6]\n[7 8 9]"

        """
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __sub__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
        raise NotImplementedError

    def nombre_de_colonnes(self):
        raise NotImplementedError

    def nombre_de_lignes(self):
        raise NotImplementedError

    def transpose(self):
        r"""
        Retourne la matrice transposée.
        """
        raise NotImplementedError

    def __neg__(self):
        r"""
        Retourne l'inverse additif de la matrice

        EXAMPLES::

            >>> #from matrix import Matrice
            >>> m = Matrice(3, 3, [1,2,3,4,5,6,7,8,9])
            >>> -m
            [-1 -2 -3]
            [-4 -5 -6]
            [-7 -8 -9]
        """
        raise NotImplementedError

    def determinant(self):
        raise NotImplementedError

    def inverse(self):
        raise NotImplementedError

    def polynome_caracteristique(self):
        raise NotImplementedError

    def valeurs_propres(self):
        raise NotImplementedError
