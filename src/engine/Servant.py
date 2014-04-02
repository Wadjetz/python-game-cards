
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
    
    def fight(self, ID_target, ennemy):
        '''
        Le serviteur inflige des degats
        '''
        #if self.effect == "provocation":
            #self.provocation(ID_target, ennemy)
        if self.action == True:
            if int(ID_target) > 3000000:
                #la cible est un serviteur
                servantEnnemy = ennemy.getServiteur(ID_target)
                print(self.name + " attaque " + servantEnnemy.name + " de " + str(self.attack) + "dmg et " + servantEnnemy.name + " replique de " + str(servantEnnemy.attack))
                
                servantEnnemy.domage(self.attack, self.damage)
                self.domage(servantEnnemy.attack, servantEnnemy.damage)
                self.action = False
            else:
                #la cible est un joueur
                print(self.name + " attaque " + ennemy.name + " de " + str(self.attack) + "dmg")
                ennemy.domage(self.attack)
                self.action = False
        else:
            raise GameException(self.name + " : Je ne peux plus attaquer")
     
    def provocation(self, ID_target, ennemy):
        '''
        
        '''
        print("self.effect")
        
    def domage(self, domage, typeDomage):
        '''
        Gestion des type de degats
        '''
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
            self.health -= int(domage)
    
    def toString(self):
        txt = "ID:" + str(self.ID) + "-" + str(self.name)
        txt += ":[health=" + str(self.health) + " pv, degats=" + str(self.attack) + ", action=" + str(self.action) + ", damage=" + str(self.damage)
        #txt += ", Type=" + str(self.Type) + ", description=" + str(self.description) + ", dialog=" + str(self.dialog) + ", vulnerability=" + str(self.vulnerability) + "]"
        return txt
    
    def __str__(self):
        return self.toString()
    
    
