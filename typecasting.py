#Typecasting = the process of converting a variable from one data type to another str(), int() ,float() ,bool()

name="feitan"
age=23
gpa=3.2
is_zoldyck=False


#To print the variable type we use the function type()
print(type(name))
print(type(age))
print(type(gpa))
print(type(is_zoldyck))

gpa=int(gpa)
print(gpa)   #sortie : 3
print(type(gpa))   #sortie : <class 'int'>

age=float(age)
print(age)   #sortie : 23.0
print(type(age))   #sortie : <class 'float'>

age=str(age)
print(age)   #sortie : 23.0  - it's a string not a float
print(type(age))   #sortie : <class 'str'>

age+="1" 
print(age) #sortie : 23.01


name=bool(name)
print(name)  #sortie : True -> pour le boolean on obtient false que si la chaine de caractère est vide sinon true

gpa=bool(gpa)   #sortie : True -> pour le boolean on obtient false que si le int ou float egal a 0 est vide sinon true
print(gpa)