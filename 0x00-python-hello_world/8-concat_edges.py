#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming\
<<<<<<< HEAD
 language that combines remarkable power with very clear syntax"
str = str[39:67] + str[107:112] + str[0:6]
=======
language that combines remarkable power with very clear syntax"
<<<<<<< HEAD
str = str[39:66] + str[-23:-17] + str[0:7]
>>>>>>> 50b0d4f83aeee89c73724f1a8cded317f4aae322
=======
str = str[39:66] + str[-23:-17] + str[0:6]
>>>>>>> 5b5ac0eb3b140a6883b13304b73fb6da16ccc5c1
print(str)
