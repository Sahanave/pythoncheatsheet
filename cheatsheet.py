import random
import sys
import os
#hey there!this is a some basic tutorial and some quick commands to help you in your
#work and in your project in case you are wondering how to use the commands 
#Getting Started
#1)Task:if you want to print something quick on the screen
#2)Task:learn how to use lists
#3)Task learn how to use tuples.
#4)learn how to use dictionaries
#5)learn how to use condtional statements
#6)Learn how to use logical operator
#7)Learning to use while statement
#8)Learning how to use functions
#9)User interaction
#10)working with strings  
#110Working with files
#12)Object oriented programming
#1###############################################################
#Task:if you want to print something quick on the screen

''''
#print("hello world")
#n123="sahana"
#print(n123)
#print("hello world",n123)
#qto="always remeber that you are unique"
#nto="thats what he said"
#to=qto+nto
#print(qto,nto)
#print('%s  %s'%("this is cool",to))
#print("i dont like this",end="")
#print("who i dee")


#2###############################################################

#Task:learn how to use lists

grocery=["apple","milk","baanana"]
we use [] in a list
subjects=["maths","science"]
together=[grocery,subjects]
print(together)#its getting printef like how i pass 2d arrays in c++
grocery.append("milky")
print(grocery)
grocery.insert(2,"coke")
grocery.sort()
print(grocery)
grocery.remove("coke")
print(grocery)
grocery.reverse()
print(grocery)

#3###############################################################

#Task learn how to use tuples.
#tuples are the same as the lists except you cannot cahnge yhem once ypou have created them

new_list=("apple","milk","baanana")
we use [] in a tupple
grocery=list(new_list)
grocery.append("milky")
listt=tuple(grocery)
print(listt)
#4###############################################################
#learn how to use dictionaries
#Dictionaries are made of value with unique keys ;you cannot join dictionaries
#like you joi#n list we use curly brackers in a dictionaries

supper_villains={'He':'Thor',
                 'last':'hammer',
                 'verdict':'time to let go'}
                 
print(supper_villains['He'])
del supper_villains['He']
len(supper_villains)
supper_villains['He']='Hulk'
print(supper_villains.get('He'))

#5###############################################################
#learn how to use condtional statements
#getting back to conditionals
#if elsee elif ==,<,>,<=,>=

age=16
if age>=21:
    print("you are old enough to drive alone")
elif age>=16:
    print("learners baby")
else:
 print("get good friends")    
#6###############################################################
#learn how to use logical operator
#using logical operator in the conditional if statements
#and or not

age=30
if(age>=1)and (age<=18):
  print("you get a bday party")
elif(age==21):
   print("okay old")
elif not(age==30):#negates the logical value"
   print("young!?")
else:
  print("whatever")  

  #learn how to work with for and while
  #working with the loops


for x in range(0,10):
      print(x,'',end="")

grocery=["apple","milk","baanana"]
 
for y in grocery:
   print(y)
subjects=["maths","science","okay"]
together=[grocery,subjects]
for x in range(0,2):
  for y in range(0,3):
      print(together[x][y])     

7###############################################################
#Learning to use while statement
i=random.randrange(0,100)
while(i!=20):
   if(i%2==0): 
        break
   else:
       i=i+1
 8###############################################################

 
 #learning how to use functions

def addnum(one,two):
   sumt=one+two
   return sumt     


   
   print(addnum(16,17))
Important thing to note is that sumnum is a variable created inside the function 
and it will not be availiable outside

 9###############################################################

#9User interaction

print('Whats your name')

name=sys.stdin.readline()



print("Hello",name)


 10###############################################################

#working with strings  
long_string="my name is -Sahana"


print(long_string[0:2])

#Interesting point is it is seen as a array of characters and so when i ask it to print
#long_string[0:2} it prints only my

print(long_string[-5:])


#it prints everything from (length-5 till the end)

print("my first letter  of my %s is %c and %d is my favourite %f number" %('name','S',16,1 ))


#do remember to keep the order in mind
# some basic things like


#if you want to check whether your string is all numbers
print(long_string.isalnum())


#if you want to check whether your string is alll letters
print(long_string.isalpha())


#replace a word with somethign else
print(long_string.replace('Sahana','bonjin'))


#find index of a woed
print(long_string.index('name'))


#convert group of strings into a list
quote=long_string.split(" ")


#how do you want to seperate them,space works out fine
print(quote)
11##############################################################
#working with file input and outputs
use ab+ to read and append a file
wb to write to a file and 
rb to read a file

file=open('sahana.txt','wb')
#mention the extension with the name
print(file.mode)
print(file.name)
file.write(bytes("this is my name\n",'UTF-8'))

#what if you want to read from a file
file=open('sahana.txt','r+')
fil=file.read()
print(fil)

12##############################################################
#Object oriented programming
'''
class animal:
    __name=""
    __height=2
    __weight=4
    __sound=0
    
    #by using-- i am making these variables private which means if i have to use the 
    #variables,i need to call a function and if i have to change the variable value inside 
    #the class I need to use  a function
    #encapsulation:is the way you are calling the object variables outside valid,if valid
    #we set it to variable you are interested in.
    #constructors are used to setup or initialize an object
    def __init__(self,name,height,weight,sound):
        self.__name=name
        self.__height=height
        self.__weight=weight
        self.__sound=sound

    def tostring(self):
     return"the name of the animail is {},its height is {},the weight is {} and the sound  its makes is {}" .format(self.__name,self.__height,self.__weight,self.__sound)

 
cat=animal("Whiskers",10,20,"meow")
 
print(cat.tostring())
#polymorphism using the details of the object created earlier

class dog(animal):
#inheriting from the animal class
  __owner=""
  def __init__(self,name,height,weight,sound,owner):    
        self.__owner=owner
        #if you want the other details to be handled by the parent class
        super(dog,self).__init__(name,height,weight,sound)
        
  def get_sound(): 
      return self.__sound()
      
  def tostring2(self):
     return "the  the owner is {}" .format(self.__owner)
  
     
  def multiple_sounds(self,how_many_times="None"):
      if(how_many_times=="None"):
          print(self.__getsound())
      else:
          print(self.__getsound()*how_many_times)   

     
     
mikey=dog("spot",10,20,"woof","me") 
print(mikey.tostring())
print(mikey.tostring2())

     
