#!/usr/bin/env python3

#Create list
icecream = ["flavors", "salty"]

tlgclass= ["Adrian","Bikash","Chas","Chathula","Chris","Hongyi","Jauric","Joe L.","Joe V.","Josh","Justin","Karlo","Kerri-Leigh","Jason","Nicholas","Peng","Philippe","Pierre","Stephen","Yun"]

icecream.append(int(99)) # append the integer 99 to the list
print(icecream) # print results of appended list
print(tlgclass) # print tlg class members
question = input("Give me a number between 0 - 19")

print(icecream[-1], ", and ", tlgclass[int(question)], " chooses to be ", icecream[1], sep="")
