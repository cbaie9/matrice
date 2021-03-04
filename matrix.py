
class Matrice:
    def __init__(self, ncolumns, nrows, L):
        r"""
        INPUT:

        - ``ncolumns`` -- entier, nombre de colonnes
        - ``nrows`` -- entier, nombre de lignes
        - ``L`` -- liste, les ``ncolumns*nrows`` entrées de la matrice 

        EXAMPLES::

            >>> Matrice(3, 3, [1,2,3,4,5,6,7,8,9])

        """
        self._L = L
        self._ncols = ncols
        self._nrows = nrows

    def __repr__(self):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
        raise NotImplementedError

    def nombre_de_colonnes(self):
        raise NotImplementedError

    def nombre_de_lignes(self):
        raise NotImplementedError

