"""
*** The Rocket class ***
1. Define a class named Rocket. This class should have three attributes, four methods and a constructor:
	a. Attributes:
        - altitude
        - model
        - isFlying
    b. Create a constructor that accepts the model attribute. Within the constructor:
        - Create an instance variable named model and set it based upon the value
            passed to the constructor.
        - Create an instance variable named altitude and set it to 0.
        - Create an instance variable named isFlying and set it to False.
    C. Methods:
    	- launch() that, when called:
             i.  Sets the isFlying to True.
             ii. Prints the message "Rocket has launched successfully"
    	- land() that, when called:
             i.  Sets the isFlying to False.
             ii. Sets altitude to 0 using the correct setter.
             iii. Prints the message "Rocket has landed"
        - getAltitude()    #Returns the altitude attribute of the Rocket
        - setAltitude()    #Sets the altitude attribute of the Rocket
        - For the sake of berevity, we are not creating getters and
                setters for the model or isFlying attributes.

"""
# Define the Rocket class here




"""
* Testing the Rocket Class *
	1. Create an instance of Rocket passing the model "Mark 7" to the constructor.
    2. Print the attributes of your Rocket object using descriptive headings.
        - Please use the getter for the altitude attribute
    3. Launch the rocket using the launch() method.
    4. Set the altitude to 500 using the appropriate setter.
    5. Print the attributes of your Rocket object again using descriptive headings.
        - Please use the getter for the altitude attribute
    6. Call the land() method of the Rocket object instance.
"""
# Test the Rocket class here
print("*** Testing the Rocket Class ***")



"""
*** The Shape class ***
	1. Define a class named Shape. This class will have two
            attributes, four methods, and a constructor:
	   a. Attributes:
            - x     position of the shape on the screen.
            - y     position of the shape on the screen.
        b. Constructor:
            The constructor must set the values of the attributes mentioned
            above based on values passed into the constructor upon
            object creation.
        c. Methods:
            - setX(); getX(); setY(); getY() (getters and setters).

"""
# Define the Shape class here.
print("*** Testing the Shape Class ***")


"""
* Testing the Shape class *
	1. Create an instance of Shape passing into the constructor, the values:
           220 and 450 as the x and y properties.
    2. Print the attributes of your Shape object using descriptive headings.
        - Please use the getters for the attributes.
          i.e. Shape - x: 890  y: 100
    3. Using the setters, modify the values of x and y to 310 and 670 respectively.
    3. Print the values of your attributes using getters to get the values.
        Make sure they are formatted wih headings.
            i.e. Shape - x: 890  y: 100
"""
# Test the Shape class here



"""
***The Circle Class ***
	1. Define a class that represents a Circle. It MUST inherit THE attributes and
            methods OF THE Shape class. The Circle class will contain one attribute, one
            constructor and three methods:
	   a. Attributes:
	       - radius
        b. Constructor - must be coded as follows:
            i. The constructor must accept x, y, and radius attributes as parameters and
                create the radius instance variable.
        ii. Create the radius instance variable by setting it to the value passed into
                the constructor.
            iii. Call the constructor of it's superclass
                in order to create the instance variables defined in the superclass.
				super(Circle,self).__init__(x, y)

       c. Methods:
           - getRadius() and setRadius() methods
           - calcArea()
	           - Use the formula A = πr^2 and make π equal to 3.14
	           - Return the value from the method.
"""
# Define the Circle class here
print("*** Testing the Circle Class ***")




"""
* Testing the Circle class *
    1. Test your code:
        a. create an instance of the Circle class passing the values 500, 400, 30 as parameters
            to the constructor.
        b. Print the values of the object instance using the only methods:
            Example Output:   Circle Class - x: 999,  y: 999,  Radius: 99,  calcArea: 99.99
        c. Set the x and y coordinates to 10 and 50 using the appropriate setter methods.
        d. Set the radius to 35 using the appropriate setter method.
        e. Call the calcArea() method again and print the results with an appropriate heading.
        f. Print the values of the object instance using the only methods:
            Example Output:   Circle Class - x: 999,  y: 999,  Radius: 99,  calcArea: 99.99

"""
# Test the Circle class here



"""
** Question **
	1. In the example above, Circle inherits from Shape which makes Shape
        the _____________________   and Circle the ____________________.
        (Note: Parent and child will not be good enough.  I need the official terms.) 
End
"""