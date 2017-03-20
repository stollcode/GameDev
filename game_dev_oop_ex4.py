"""
** The Rocket class **
	1. Define a class that represents a rocket. This class should have three 
        attributes, four methods and a constructor:
	   Attributes:
        - altitude
        - model
        - isFlying
	   Methods
    	- launch() that, when called, sets the isFlying to True.
    	- land() that, when called, sets the isFlying to False.
        - getModel()    #Returns the model attribute of the car
        - setModel()    #Sets the model attribute of the car
        - For the sake of berevity, we are not creating getters and 
                setters for altitude.
    2. Create a constructor that accepts the value for model and 
        set the appropriate instance variable. 
        Set isFlying to false and altitude to 0 in the constructor.
	3. Create an instance of Rocket.  It is a "Mark 7" model.
    4. Launch the rocket using the launch() method.
    5. Print the attributes of your Rocket object (use the getter for 
        the model attribute)

** The Shape class **
	1. Define a class that represents a Shape. This class will have two 
            attributes, a method, and a constructor:
	   Attributes:
            - x     position of the shape on the screen.
            - y     position of the shape on the screen.
        Methods:
            - setX(); getX(); setY(); getY() (getters and setters).
        Constructor:
            The constructor must set the values of the attributes mentioned
            above based on values passed into the constructor upon 
            object creation.
    2. Test your code by creating an instance of the class and calling the
            methods that change the values of the attributes.
    3. Print the values of your attributes as the last part of the test using
        your getters to get the values.

**The Circle Class **
	1. Define a class that represents a Circle. It MUST INHERIT THE ATTRIBUTES and
            METHODS OF THE Shape CLASS. This class will contain one attribute, one
            method, and one constructor:
	   Attributes:
	       - radius
       Method:
	       - calcArea()
	           - Use the formula A= πr^2 and make π equal to 3.14
	           - Return the value from the method.
        Constructor:
        The constructor must accept radius attribute as a parameter and set the
            attribute.
    2. Test your code by:
        a. creating an instance of the class and calling the calcArea()
            method.
        b. Set the x and y coordinates to 10 and 50 using the appropriate setter methods.
        c. Print the value returned by the calcArea() method.
        d. Print the x, y coordinates of your circle using the getX and getY getter methods.

** Question **
	1. In the example above, Circle inherits from Shape which makes Shape
        the _____________________   and Circle the ____________________.
        (Note: Parent and child will not be good enough.  I need the official terms.)
"""