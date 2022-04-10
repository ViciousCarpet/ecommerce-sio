from Produit import Produit



class ProduitDevis(Produit):

    def __init__(self, uneRef, unLib, unDelai):

        Produit.__init__(self, uneRef, unLib)

        self._delai = unDelai



    def affiche(self):

        print(super().affiche(), "Délai de réponse : ", self._delai)


