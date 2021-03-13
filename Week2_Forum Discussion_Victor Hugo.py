#Example1
fruits: [] #Paramenters is the variables inputed in the paretheses in a functiom.
a = input("Write the number of Bananas") #First Paramenter
#Arguments is the value going into the function when we using the''print''.
print("Total of Banana is:", " ", a) #First argument.

#Example2
fruits: [] #Paramenters is the variables inputed in the paretheses in a functiom.
a = input("Write the number of Bananas") #First Paramenter [Value]
b = 2 + 4                                #Second Paramenter [Value]
c = input("Write the number of Orange")  #Third Paramenter [Value]
Total = a + b + c                        #Expression & Variables (in a fourth argument)
#Arguments is the value going into the function when we using the''print''.
print("Total of Banana is:", " ", a) #First argument.
print("Total of Apple is:", " ", b) #Second argument.
print("Total of Orange is:", " ", c) #Third argument.
print("Total of fruits is:", " ", Total) #Fourth argument.

#Exmple3
def myfunc():
    x = 212
    print(x)
print(x) #NameError: name 'x' is not defined;

#Exmple4

a = 12 #Variable outside main-function;

def func(b): #Local variable (in-fucntion);
    a = 23 + b
    print("great", a)

print(func(1999)) #Fisrt that will be called.

print(a) #it will print the ''a'' outside, 12.

#Comment: parameter-unique-name outside of the main-function can't be called, except if
# it be called by apart.

Exemple5

destiny = "Justin"

def my_function(destiny) -> str:  # given a name to the function-parameter "destiny"
    print("This is your unique name, " + destiny + "!")
my_function("Anna")
#It will be sent to variable into the function above.
#As for calling the variable with same name placed outside of the function, it must need to be
#call once again, as the script-ordering. Otherwise, if trying to call the function for picking the
#second argument out ot function it will present an error: ''the value is not defined''.

print(destiny) # calling the outside paramenter beyond the function,it prints
#Justin.

#Comment: variables outside-function with same name is the same as exmaple four,
# the paramenter wil send the value set into the function it is in excempt if it be determinided as
a global variable.





