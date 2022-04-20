1) PYTHON CLASS:
    A class is a blueprint for objects - one class for any number of objects of that type.
    You can also call it an abstract data type.
    
    Python is an object oriented programming language
    Almost everything in Python is an object, with its properties and methods.
    Object is simply a collection of data (variables) and methods (functions) that act on those data.
    And class is a blueprint for the object.
    An object is also called an instance of a class, and the process of creating this object is called instantiation.

2) DOCSTRING:
    A docstring is a string literal that we use to explain the functinoality of a class, function or module.
    It is the first statement in any of these constructs, and while the interpretor ignores them, it retains them at runtime.
    We can access it using the __doc__ attribute of such an object.
 
3) PYTHON ARGUMENT:
   An argument is a value we pass to a function or a method when calling it.
   In python, we have the following kinds of arguments.
   
   a) Default Arguments:
       When defining a function we can provide default values for arguments.
       This way, when we call it without any missing arguments, the default values will fill in for them.
       Default arguments can only follow non-default ones.
#       >>>def sayhello(name='User'):
#           print('Hello, {}'.format(name))
#       >>>sayhello('Ayushi') - Returns 'Hello, Ayushi'
#       >>>sayhello()         - Returns 'Hello, User'

    b) Keyword Arguments:
        Keyword arguments pertain to calling a function.
        When we call the function, we can pass it arguments in any order.
#       >>>def subtract(a, b):
#       >>>subtract(3, 2)
#       >>>subtract(b=2, a=3)

    c) Arbitrary Arguments:
        When we don't know how many arguments we'll get,m we use an asterisk to denote an arbitrary argument.
#       >>>def sum_all(*nums):
#               total = 0
#               for i in nums:
#                    total += i

    d) Positional Arguments:
        These are regular arguments that aren't keyword arguemnts.
        Python Positional Argument Example:
#       >>>def add(a, b):

4) ATTRIBUTE:
    An attribute is a value an object holds. We can access an object's attributes using the dot operator(.)
    In our examples, we have done this as following:
#           >>>orange.color

5) DESCRIPTOR:
    If an object defines methods __get__(), __set__(), or __delet__(),
    we can call it a descriptor. On looking up an attribute from a class, the descriptor
    attribute's special binding behaviour activates.
    Using 'a.b' looks up the object 'b' in the class dictionary for 'a'.
    If 'b' is a descriptor, then the respective descriptor methods is called.

6) PYTHON EXPRESSION:
    An expression is a piece of code that we can evaluate to a value. It is an aggregation of expression elements like:
        literals = a value written exactly as it's meant to be interpreted.
        names,
        attribute access,
        operators,
        function calls.
    All of these return a value.
    An if statement is not an expression, and neither is an assignment, because these do not retur a value.
    
7) FUNCTION:
    A function is a sequence of statements that may return a value to the caller.
    It may take zero or more arguments.

8) IDLE:
    The IDLE is an Integrated Development Environment for Python.
    It is a basic editor and interpreter environment that ships with Python.

9) DUCK-TYPING:
    This means that Python does not look at an object's type to determine if it has the right interface.
    It simply calls or uses the method or attribute.
    'If it looks like a duck, quacks like a duck, then it must be a duck'
    This imrpoves flexibility by allowing polymorhpic substitution.
    With duck-typing, you don't need tests like type() or instance(): instead you use hasattr() tests or EAFP programming.

10) 