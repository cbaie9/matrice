# -*- coding: utf-8 -*-
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
   position (i,j). Par défaut, on assume que les lignes et les colonnes sont
   indicées à partir de zéro. Donc l'entrée à la position (0,0) est
   l'entrée en haut à gauche dans la matrice. On accède à cet élément en
   écrivant  ``M[0,0]`` (en pratique, c'est la méthode ``__getitem__`` qui
   est utilisée).

L'exercice consiste à compléter le code des autres méthodes.

"""
class Matrice:
    def __init__(self, ncols, nrows, entries):
        r"""
        INPUT:

        - ``ncolumns`` -- entier, nombre de colonnes
        - ``nrows`` -- entier, nombre de lignes
        - ``entries`` -- liste, les ``ncolumns*nrows`` entrées de la matrice 

        EXAMPLES::

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

            >>> m = Matrice(3, 3, [1,2,3,4,5,6,7,8,9])
            >>> m
            [1 2 3]
            [4 5 6]
            [7 8 9]
            >>> repr(m)
            "[1 2 3]\n[4 5 6]\n[7 8 9]"

        """
        result = ""
        for i in range(0, self._nrows):
            result += "["
            for j in range(0, self._ncols):
                if j > 0:
                    result += " "
                result += str(self._L[i * self._ncols + j])
                if j < self._ncols - 1:
                    result += " "
            result += "]\n"
        return result

    def __add__(self, other):
        r"""
        Retourne l'addition de deux matrice en chaîne de caractères de la matrice.

        EXAMPLES::

            >>> m = Matrice(3, 3, [1,2,3,4,5,6,7,8,9])
            >>> n= Matrice(3, 3, [1,2,3,4,5,6,7,8,9])
            >>> n+m
            [2 4 6]
            [8 10 12]
            [14 16 18]

        """
        res = Matrice(self._nrows, self._ncols, self._entries)
        for i in range(0,self._nrows):
            for j in range(0,self._ncols):
                x = self._entries[self._ncols * i + j] + other._entries[self._ncols * i + j]
                res._entries[self._ncols * i + j]=x
        return res
    def __sub__(self, other):
        return Matrice.__add__(self,Matrice.__neg__(other))
    def __mul__(self, other):
        r"""ipyt
        Retourne le résultat de la multiplication de la matrice courant par une
        autre matrice.

        EXAMPLES::

            >>> m1 = Matrice(3, 2, [1, 3, 8,-2, 1, 10])
            >>> m2 = Matrice(2, 3, [5, 1, 4, 7, 7, 2])
            >>> m1 * m2
            [73 38]
            [64 25]

        """
        if self._ncols != other._nrows:
            raise ValueError(
                "Dimensions de matrices incompatibles pour la multiplication!"
            )
        result = [0] * (self._nrows * other._ncols)
        for i in range(0, self._nrows):
            for j in range(0, self._ncols):
                for k in range(0, other._ncols):
                    result[i * other._ncols + k] +=self._L[i * self._ncols + j] *other._L[j * other._ncols + k] 
        return Matrice(self._nrows, other._ncols, result)

    def nombre_de_colonnes(self):
        return self._ncols

    def nombre_de_lignes(self):
        return self._nrows

    def transpose(self):
        r"""
        Retourne la matrice transposée.
        
        EXAMPLES::

            >>> m1 = Matrice(3, 2, [1, 3, 8,-2, 1, 10])
            >>> m1.transpose()
            [1  -2]
            [3  1]
            [8  10]
        """
        result = [0] * (self._nrows * self._ncols)
        for i in range(0, self._nrows):
            for j in range(0, self._ncols):
                result[j * self._nrows + i] = self._L[i * self._ncols + j]
        return Matrice(self._nrows, self._ncols, result)

    def __neg__(self):
        r"""
        Retourne l'inverse additif de la matrice

        EXAMPLES::

            >>> m = Matrice(3, 3, [1,2,3,4,5,6,7,8,9])
            >>> -m
            [-1 -2 -3]
            [-4 -5 -6]
            [-7 -8 -9]
        """
        entries = []
        for element in self._entries:
            entries.append((-1)*element)
        return Matrice(self._ncols, self._nrows, entries)

    def determinant(self):
        raise NotImplementedError

    def inverse(self):
        raise NotImplementedError

    def polynome_caracteristique(self):
        raise NotImplementedError

    def valeurs_propres(self):
        raise NotImplementedError
