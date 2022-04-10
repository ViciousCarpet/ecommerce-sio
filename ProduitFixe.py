from Produit import Produit



class ProduitFixe(Produit):

    def __init__(self, uneRef, unLib, unPrix, uneQte):

        Produit.__init__(self, uneRef, unLib)

        self._prix = unPrix

        self._quantite = uneQte



    def affiche(self):

        print(super().affiche(), "Prix : ", self._prix, " - Quantité : ", self._quantite)



    def getPrix(self):

        return self._prix



    def getQuantite(self):

        return self._quantite
