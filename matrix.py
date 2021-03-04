
class Matrice:
    def __init__(self, ncolumns, nrows, L):
        self._L = L
        self._ncols = ncols
        self._nrows = nrows

    def __repr__(self):
        raise NotImplementedError

    def __add__(self, other):
        raise NotImplementedError

    def __mul__(self, other):
        raise NotImplementedError

    def nombre_de_colonnes(self, other):
        raise NotImplementedError

    def nombre_de_lignes(self, other):
        raise NotImplementedError

