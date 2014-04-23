
'''
Created on 11 mars 2014

@author: egor
'''
from engine.GameException import GameException
from engine.LivingEntity import LivingEntity


class Servant(LivingEntity):

    def __init__(self, ID, Type, name, attack, damageType, effect, description, dialog, health):
        '''
        Constructor
        '''
        LivingEntity.__init__(self, ID, Type, name, attack, damageType, effect, description, dialog, health)
        
        #camouflage
        if self.effect == "camouflage":
            self.camouflage = True
        else:
            self.camouflage = False
        #shield
        if self.effect == "shield":
            self.shield = int(self.health)
        else:
            self.shield = 0
    
    def fight(self, ID_target, ennemy):
        '''
        Le serviteur inflige des degats
        '''
        #if self.effect == "provocation":
            #self.provocation(ID_target, ennemy)
        if self.action == True:
            isHasP, servTarget = ennemy.isHasProvocation()
            if isHasP == True:
                print("Provocation " + self.name + " : attaque " + servTarget.name + " de " + str(self.attack) + "dmg")
                servTarget.domage(self.attack, self.damageType)
                self.action = False
            else:
                if int(ID_target) > 3000000:
                    #la cible est un serviteur
                    servantEnnemy = ennemy.getServiteur(ID_target)
                    self.camouflage = False
                    servantEnnemy.domage(self.attack, self.damageType)
                    self.domage(servantEnnemy.attack, servantEnnemy.damageType)
                    self.action = False
                else:
                    #la cible est un joueur
                    print(self.name + " attaque " + ennemy.name + " de " + str(self.attack) + "dmg")
                    ennemy.domage(self.attack)
                    self.action = False
            self.action = False
            self.camouflage = False
        else:
            raise GameException(self.name + " : Je ne peux plus attaquer")
        
    def domage(self, domage, typeDomage):
        '''
        Gestion des type de degats
        '''
        if self.shield > 0:
            print("Shield")
        if self.camouflage == False:
            if self.damageType == "magic" and typeDomage == "distance":
                print("CRITIQUE " + str(int(domage) * 2))
                self.health -= int(domage) * 2
            elif self.damageType == "distance" and typeDomage == "physical":
                print("CRITIQUE " + str(int(domage) * 2))
                self.health -= int(domage) * 2
            elif self.damageType == "physical" and typeDomage == "magic":
                print("CRITIQUE " + str(int(domage) * 2))
                self.health -= int(domage) * 2
            else:
                print(self.name + " ce prend " + str(domage) + "dmg et replique de " + str(self.attack))
                self.health -= int(domage)
        else:
            raise GameException(self.name + " est Comouflé il ne peut pas etre attaquer <ID=" + str(self.ID) + ">")
    
    def toString(self):
        txt = str(self.ID) + " : " + str(self.name)  + "\t"
        txt += ":[" + str(self.health) + "pv, " + str(self.attack) + "dmg, a=" + str(self.action) + ", " + str(self.damageType) + ", "
        if self.effect == "camouflage":
            txt += self.effect + "=" + str(self.camouflage) + "]"
        else:
            txt += self.effect + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    
    
