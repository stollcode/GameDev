"""
                                                                Game_dev_oop_ex2

DEFINITIONS

Attribute:  Each class below, has at least one attribute defined.  They hold
    data for each object created from the class.

The self keyword:  The first parameter of each method created in a Python program must be "self".  Self specifies the current instance of the class.

Instance Variable - A variable (attribute) defined within a class constructor method
    defined using the "self." prefix.  Instance variables may have a different value for each object.

Constructor method - A special method called when an object instance is created. 
    Constructors accept parameters and typically are used to set instance variables
    with default values.  Constructors are used to do anything that needs to be done
    when an Object is created.

Getters and Setters - Methods that allow instances of other objects to access (getters)
    or store (setters) values of object variables.


Directions: Create a Python module on your Z:\GameDev folder named oop_ex2.py.
Add the following code to the module.  Do not forget to test!!!


*** Rectangle Class ***
1. Define a class named Rectangle. This class should have two attributes and one method:
    a. Attributes
        i. length
        ii. width
    b. Methods
        i. __init__(self, length, width):
            self.****** = ******
            ...

        ii. area(), A method that calculates and returns the calculated area of the rectangle (look it up if you do not know)
            - This method has no parameters other than the self keyword.

Write the code below the triple quotes below.
"""
# Your code goes here.




"""
*** Teacher class ***
1. Define a class named Teacher containing the following attributes set within a constructor method.
    a. Attributes (Instance variables - defined and set in the constructor):
        i. name
        ii. gender
        iii. primary_subject
        iv. years_taught

Sample code for your constructor:
    def __init__(self, name, gender, primary_subject, years_taught)

Write the code below the triple quotes below.
"""
# Your code goes here.




"""
*** Student Class ***
1. Define a class named Student. This class will have three attributes and six methods:
    a. Attributes
        i. student_id
        ii. grad_year
        iii. gender
    b. Methods (DO NOT USE THE input() function for these methods)
        i. set_student_id (), A method that changes the studentId based upon the value passed into the method.
        ii. set_grad_year(),  A method that changes the gradYear based upon the value passed into the method.
        iii. set_gender(),  A method that changes the gender based upon the value passed into the method.
        vii. Three methods, one for each attribute that returns the value.
            1. get_studentId()   get_grad_year()   get_gender()

2. Create a constructor method in the Student class.  Code this method to accept
parameter values for the three attributes (student_id, grad_year, and gender). Set
the properties based upon the parameters passed into the constructor method.

Write the code below the triple quotes below.
"""
# Your code goes here.




"""
*** Testing ***
5. For each class:
    a. Print a message describing the class being tested (ie. "Testing the Teacher Class:").
    b. Create an object instance passing appropriate values to the constructor.
    c. Print the attribute values using descriptive headings.
        Use the getter methods to retrieve values for the Student class.
    d. Modify all attribute values. (Use setter methods for the Student class).
    e. Print the attribute values using descriptive headings.
        use the getter methods to retrieve values for the Student class.
    f. Rectangle class only - Call the area() method and print the value returned.

Write the tests below the triple quotes below.
"""
# Test the Rectangle class here (don't forget to call the area() method and print the returned value)




# Test the Teacher class here




# Test the Student class here (do not forget to use setters to set values and getters to retrieve them)


