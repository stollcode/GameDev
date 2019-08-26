"""
                                                                Game_dev_oop_ex3

DEFINITIONS
Attribute:  Each class below, has at least one attribute defined.  They hold
    data for each object created from the class.

The self keyword:  The first parameter of each method created in a Python program
    must be "self".  Self specifies the current instance of the class.

Instance Variable - A variable (attribute) defined within a class constructor method
    that uses the "self." prefix.  Instance variables may have a different value for each object.

Constructor method - A special method called when an object instance is created. 
    Constructors accept parameters and typically are used to set instance variables
    with default values.  Constructors are used to do anything that needs to be done
    when an Object is created.


!!!!!!  NEW TERMS  !!!!!!
Inheritance: When a class copies all methods and properties from another class.

Superclass - The class from whom the methods and properties are being copied.  It is
    also called the parent or base class.  Note: the website author calls superclass
    "parent class"

Subclass - The class that is copying (inheriting) the methods and properties
    from the Superclass.  It is also called the child class. Note: The website author calls
    subclass "child "class.

Inheritance Example: In the class diagram below, the Player, Enemy, Bullet, and
    Explosion classes are subclasses of the Sprite class. When we create an instance
    of the Player class, all methods and properties from Sprite class are included
    in the Player class.  The same holds true for instances of the Enemy, Bullet
    and Explosion classes.

Example 2D Game Class Diagram (a type of UML diagram")
                   _____________
                   |  Sprite    |
                   |------------|
                   |   image    |
                   |     x      |
                   |     y      |
                   --------------
			            /\
					    / \
    				   // \\
                        | |
    ______________      | |      _______________
    |   Player    |     | |      |   Enemy      |
    |-------------|     | |      |--------------|
    |	speed     |     | |      |   name       |
    |   health    |-----  -------|    AI        |
    |   ...       |     | |      |   ...        |
    |_____________|     | |      |______________|
                        | |
    ______________      | |       _______________
    |   Bullet    |     | |      |   Explosion  |
    |-------------|     | |      |--------------|
    |   speed     |     | |      |    name      |
    | direction_x |--------------|animation_cycle|
    | direction_y |              |   images[]   |
    |   ...       |              |   ...        |
    |_____________|              |______________|



Directions: Create a Python module on your Z:\GameDev folder named oop_ex3.py.
Add the following code to the module.  Do not forget to test!!!


*** Sprite Class ***
1. Create a class named Sprite. This class should have all the attributes (instance variables)
    defined in the above diagram and some methods.
    a. Attributes:
        i.   image (String - path to image)
        ii.  x (integer describing position)
        iii. y (integer describing position)

	b. Constructor:
		Create a constructor for the Sprite class that:
			a. Accepts a value for each of the above attributes and creates an instance
				variable using the "self." prefix.

    c. __str__() method that returns the names, and the values of each instance variable.
			This will allow us to use the str() method to get a string representation of the object.
			  Note: In Java we use the toString() method to do this.

		** Use the following code for the  __str__() method **
		def __str__(self):
			return "Sprite Values - Image: " + self.image + " x: " + str(self.x) + " y: " + str(self.y)

	d. Other methods:
		ii. play_sound() method that prints "The Sprite makes a sound".
        iii. Getters and Setters for all instance variables.
			** Example Getter and Setter methods **
			 for the image attribute:

				def set_image(self, image):
					self.image = image

				def get_image(self):
					return self.image

            Don't Forget: get_x, set_x, get_y, set_y



Write the code for the Sprite class after the triple quotes below.
"""
# Code the Sprite class here.



"""
*** Player Class (subclass of Sprite) ***
1. Define a class named Player. This class must be a subclass of the Sprite class.
    a. Attributes:
        i. speed
        ii. health

	b. Constructor:
		Create a constructor for the Player class that:
			i. Accepts values for image, x, y, speed and health
			ii. Creates instance variables for speed and health using the "self." prefix.
			iii. Calls the constructor of the superclass (Sprite class) passing in values for the
				image, x, and y instance variables.  This must be done so the constructor can
				create and set the instance variables inherited from the Sprite class.

				** Use the following code to call the superclasses constructor.
				super(Player,self).__init__(image, x, y)

    c. __str__() method
		Create a method named __str__() that returns the names, and the values of each instance variable.
			  Note: The code you need to use is below.  It contains a special function named super()
				that is used to call the __str__() method of the superclass to format a more
				meaningful message.

				** Use the following code for the  __str__() method **
				def __str__(self):
					# Note the extra set of parenthesis allow us to wrap the code into multiple lines.
					return (super(Player, self).__str__() +
							" Player Values - speed: " + str(self.speed) +
							" health: " + str(self.health))
	d. Other Methods:
		i. get_speed() and set_speed()
		ii. get_health() and  set_health()
		iii. play_sound()  - Just print "The player makes a sound" in this method.


Write the code for the Player class after the triple quotes below
"""
# Code the Player class here




"""
*** Enemy class (subclass of Sprite) ***
1. Define a class named Enemy. This class that is a subclass of the Sprite class.
    a. Attributes:
        i. name
        ii. AI

	b. Constructor:
		Create a constructor for the Enemy class that:
			a. Accepts values for image, x, y, name and AI.
			b. Creates instance variables for name and AI using the "self." prefix.
            c. Creates/sets the instance variables name and AI.
			d. Calls the constructor of the superclass (Sprite class) passing in values for the
				image, x, and y instance variables. Look at the Player class if you need help.

	c. __str__() method
		Create a method named __str__() that returns the names, and the values of each instance variable.
			  See your code in the Player class for an example.

	d. Other Methods:
        i. get_name() and set_name()
		ii. get_AI() and set_AI()
		iii. fire_weapon()  - Just print "The enemy fires his weapon" in this method.

Write the code for the Player class after the triple quotes below
"""
# Code the Enemy class here




"""
*** Testing ***
5. For each class:
    a. Print a message describing the class being tested surrounded by asterisks.
		ie. "*** Testing the Sprite Class***"
    b. Create an instance of the object passing the values specified below (defined AFTER step "g").
	c. Print the string representation of the object using the str() method nested
        inside the print() method.
    d. Modify instance variables for each class instance using setters.
        - Sprite: Change the speed and health values to 10 and 20 respectively.
        - Player: Change the x, y, speed and health to 100, 200, 10 and 25 respectively.
        - Enemy:  Change the image, name and AI values to "\images\raider.png", "Tusken Raider", and
            "follow-player" respectively.
	f. Print the string representation of the object using the str() method.
    g. Call other methods for each class where appropriate.
        - play_sound() method for the Sprite object.
		- play_sound() method for the Player object.
		- fire_weapon() method for the Enemy object.

Write the tests after the triple quotes below.
"""


# *** Test the Sprite class here ***  (Test Values: "sprite.png", 100, 200)




# ***Test the Player class here***  (Test Values: "player.png", 300, 400, 5, 50)
	# Don't forget to test the PlaySound() method



# *** Test the Enemy class here ***  (Test Values: "enemy.png", 500, 600, 10, "run-from-player")
	# Don't forget to call the fireWeapon() method


