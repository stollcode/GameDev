class Sprite:
    def __init__(self, image, x, y):
        self.image = image
        self.x = x
        self.y = y

    def getImage(self):
        return self.image
    def setImage(self, image):
        self.image = image

    def getX(self):
        return self.x
    def setX(self, x):
        self.x = x

    def getY(self):
        return self.y
    def setY(self, y):
        self.y = y

    def playSound(self):
        print("The Sprite makes a sound.")

    def toString(self):
        return "Sprite Values - Image: " + self.image + " x: " + str(self.x) + " y: " + str(self.y)

s = Sprite("c:/images", 55, 100)
s.playSound()
print(s.getImage())

class Player(Sprite):
    def __init__(self, speed, health):
        self.speed = speed
        self.health = health

        """
            Add call to superclass constructor.
            Add call to superclass constructor.   """
        super(Player, self).__init__("no image specified", 20, 40)
        """
            Add call to superclass constructor.
            Add call to superclass constructor. """

        """
            #print("Constructor method for the Player class:", getSpeed(), getHealth())
            WARNING: Remove call to getters and setters in constructor.
            WARNING: Remove call to getters and setters in constructor.
            WARNING: Remove call to getters and setters in constructor.
        """

    def getSpeed(self):
        return self.speed
    def setSpeed(self, speed):
        self.speed = speed

    def getHealth(self):
        return self.health
    def setHealth(self, health):
        self.health = health

    def move(self):
        print("The Player moves.")

    def playSound(self):
        print("The Player makes a sound.")

    def toString(self):
        return "Player Values - speed: " + str(self.speed) + " health: " + str(self.health)

class Enemy(Sprite):
    def __init__(self, name, AI):
        self.name = name
        self.AI = AI

        """
        *** Add call to superclass constructor. ***
        *** Add call to superclass constructor. ***     """
        super(Enemy, self).__init__("/images/constructor_enemy.jpg", 9999, 9999)
        """
        *** Add call to superclass constructor. ***
        *** Add call to superclass constructor. ***     """

        """
            #print("Constructor method for the Enemy class:", getName(), getAI())
            *** WARNING: Remove call to getters and setters in constructor. ***
            *** WARNING: Remove call to getters and setters in constructor. ***
            *** WARNING: Remove call to getters and setters in constructor. ***
        """

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getAI(self):
        return self.AI
    def setAI(self, AI):
        self.AI = AI

    def move(self):
        print("The Enemy moves.")

    def playSound(self):
        print("The Enemy makes a sound.")

    def toString(self):
        return "Enamy Values - name: " + self.name + " AI: " + self.AI

s1 = Sprite("\images\sprite.png", 100, 300)
p1 = Player(25, 50)
p1.setImage("\images\player_ship.png")
p1.setX(20)
p1.setY(40)
print("Instance variables from step 2\n", p1.toString(), super(Player, p1).toString())

e1 = Enemy("Creeper", "follow-player")
e1.setAI("run-away")
e1.setImage("\images\enemy1.png")
e1.setX(500)
e1.setY(400)
print("Enemy AI:", e1.getAI())
print("Instance variables from step 2\n", e1.toString(), super(Enemy, e1).toString())