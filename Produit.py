#class Produit:
#    def __init__(self, uneRef, uneDesc,unType, unPrix,uneQuantite):
#        self._reference=uneRef
#        self._desc= uneDesc
#        self._type1=unType
#        self._prix = unPrix
#        self._quantite = uneQuantite
#
 #   def afficher(self):
  #      chaine="ref:"+self._refe
   #     rence+" desc:"+self._desc+" type:"+self._type1+" prix:"+self._prix+" quantite:"+self._quantite
    #    return chaine
    #def getReference(self):
    #    return self._reference
   # 
   # def getDesc(self):
   #     return self._desc
#
#    def getType1(self):
#        return self._type1
#
#    def getPrix(self):
#        return self._prix
#
#    def getQuantite(self):
#        return self._quantite
#
#    def setReference(self, uneRef):
#        self._reference=uneRef
#    
#    def setDesc(self, uneDesc):
#        self._desc=uneDesc
#    
#    def setType1(self, unType):
#        self._type1=unType
#    
#    def setPrix(self, unPrix):
#        self._prix=unPrix
#    
#    def setQuantite(self,uneQuantite):
#        self._quantite=uneQuantite
class Produit:

    def __init__(self, uneRef, unLib):

        self._reference = uneRef

        self._libelle = unLib



    def affiche(self):

        print("Reférence : ", self._reference, " - Libellé : ", self._libelle)



    def getReference(self):

        return self._reference



    def getLibelle(self):

        return self._libelle