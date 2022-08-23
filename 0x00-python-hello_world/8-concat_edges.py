#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
<<<<<<< HEAD
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[0:6]
=======
language that combines remarkable power with very clear syntax"
str = str[39:66] + str[-23:-17] + str[0:7]
>>>>>>> 50b0d4f83aeee89c73724f1a8cded317f4aae322
print(str)
