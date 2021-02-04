import random
import discord



class Character:
    def __init__(self, name, score,savingthrow, mod,save,attack,hp,maxhp):
        self.name = name
        self.score = score
        self.savingthrow = savingthrow
        self.mod = mod
        self.save = save
        self.attack = attack
        self.hp = hp
        self.maxhp = maxhp

    def __str__(self):
        return f"**Details of** ***{self.name}***\n"\
        f"*Score:* {self.score}\n"\
        f"*Savingthrow:* {self.savingthrow}\n"\
        f"*Modifier:* {self.mod}\n"\
        f"*Spell save:* {self.save}\n"\
        f"*Attack:* {self.attack}\n"\
        f"*HP:* {self.hp}\n"\
        f"*Max HP:* {self.maxhp}\n"\

    ID = "player"
    #TODO ADD PLAYERID
    # owner = ctx.author



    def st(self,skill): ########### Saving throw ###########
        if skill == "str":
            pick = 0
        elif skill == "dex":
            pick = 1
        elif skill == "con":
            pick = 2
        elif skill == "int":
            pick = 3
        elif skill == "wis":
            pick = 4
        elif skill == "cha":
            pick = 5
                                                                                            #TODO ADD MISS AND CRIT
        roll = random.randint(1,20)
        print("Roll:",roll)
        st = roll+self.savingthrow[pick] #int
        print("Savingthrow ({}):".format(skill),st)

    def atkroll(self):  ######### To hit ###############
        roll = random.randint(1,20)
        print("Roll:",roll)
        if roll == 1:
            attack = 1
            print("Critical fail... ",attack)
        elif roll == 20:
            attack=roll+self.attack
            print("Critical hit!:",attack)
        else:
            attack=roll+self.attack
            print("Attack:",attack)


        
    
#sukakog = Character([16,16,16,16,16,16],[3,3,3,3,6,6],[3,3,3,3,3,3],15,7,48,48)

#sukakog.st("int")
#sukakog.atkroll()

#sukakog.dmg(<character>,<dmg>)



