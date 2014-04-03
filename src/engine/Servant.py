
'''
Created on 11 mars 2014

@author: egor
'''
from engine.GameException import GameException
from engine.Player import Entity


class Servant(Entity):

    def __init__(self, ID, Type, name, description, dialog, attack, damage, health, effect):
        '''
        Constructor
        @param ID: id unique de la carte
        @param Type: Type de la carte
        @param name: Nom
        @param description: Description
        @param dialog: dialog de la carte
        @param attack: Degats
        @param damage: type de degats
        '''
        Entity.__init__(self, ID, name, health, attack)
        self.Type = Type
        self.description = description
        self.dialog = dialog
        self.damage = damage
        self.effect = effect
        if self.effect == "camouflage":
            self.camouflage = True
        else:
            self.camouflage = False
    
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
                servTarget.domage(self.attack, self.damage)
            else:
                if int(ID_target) > 3000000:
                    #la cible est un serviteur
                    servantEnnemy = ennemy.getServiteur(ID_target)
                    self.camouflage = False
                    servantEnnemy.domage(self.attack, self.damage)
                    self.domage(servantEnnemy.attack, servantEnnemy.damage)
                else:
                    #la cible est un joueur
                    print(self.name + " attaque " + ennemy.name + " de " + str(self.attack) + "dmg")
                    ennemy.domage(self.attack)
            self.action = False
            self.camouflage = False
        else:
            raise GameException(self.name + " : Je ne peux plus attaquer")
        
    def domage(self, domage, typeDomage):
        '''
        Gestion des type de degats
        '''
        if self.camouflage == False:
            if self.damage == "magic" and typeDomage == "distance":
                print("CRITIQUE " + str(int(domage) * 2))
                self.health -= int(domage) * 2
            elif self.damage == "distance" and typeDomage == "physical":
                print("CRITIQUE " + str(int(domage) * 2))
                self.health -= int(domage) * 2
            elif self.damage == "physical" and typeDomage == "magic":
                print("CRITIQUE " + str(int(domage) * 2))
                self.health -= int(domage) * 2
            else:
                print(self.name + " ce prend " + str(self.attack) + "dmg et replique de " + str(self.attack))
                self.health -= int(domage)
        else:
            raise GameException(self.name + " est Comouflé il ne peut pas etre attaquer <ID=" + str(self.ID) + ">")
    
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)  + "\t"
        txt += ":[" + str(self.health) + "pv, " + str(self.attack) + "dmg, a=" + str(self.action) + ", " + str(self.damage) + ", " + self.effect + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    
    
