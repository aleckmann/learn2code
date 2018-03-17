import sys    #we'll get to this later

## Welcome to Python

## Here's a couple things you should know about 'syntax'
## Comments, like these, are helpful, because sometimes 
## it can be hard to remember all the intracies of your
## program, especially as it gets more complex.
## They'll also be the primary tool that use to intruct
## so you'll have something to reference when you're 
## working through the tiny problems

## The general way that these files will go is that I will
## develop alongside you, at first small things but later
## more fun programs.

## But for now, we're stuck on the basics.

## This is a variable. It's a place to put your stuff, basically,
## whether your stuff be numbers or letters or anything you possibly
## wish to store.

number = 3
letter = 'c'
word = 'wow'

## they are very helpful in facilitating the basic operations required
## for your workflow. For example, let's say that we have a list of fruits.

fruits = ["Apple", "Banana", "Pear", "Orange"]

## the list of fruits is stored in a variable, so that we may access it later

## lists, or arrays, are the medium by which you will store your data at first.
## They are the simplest kinds of boxes, or data structures, and are built
## specifically for low-level stuff, like counting, or indexing.

## Indexing is the trait of (most) data structures that allow you to 
## request an object in a certain spot, or index.

pear = fruits[2]

## Here, we set the pear variable to the second index in the fruits list.
## You may be wondering why it's not Banana instead. This is because all
## indexing done, in almost any language you use to develop, starts
## indexing at 0. Since Apple is the 0th item, Banana is the 1st, and 
## Pear is the 2nd.

## Retrieving data like this is exceptionally useful since it can be used
## to access the data in a data structure sequentially. If we want to ask,
## "Does _ item exist in the list?", we can iterate over the items in the list
## sequentially and check each and every one.

for i in range(len(fruits)):   ## here, we said "for every integer in the range equal to the length of the fruits list"
  print(fruits[i]))             ## and here, we printed out (to the console) the fruit in that spot in the list
  
## you can think of the range as its own array
## [ 0, 1, 2, 3 ] if you say range(4), it counts from 0 to 3. range(10) is 0 to 9. range(n) is 0 to n-1.
## our "for loop" looked at each individual item, or number, and put that data in "i", the iterator variable
## that way, when within the "scope" of our loop (notice the indentation), we can use the "i" variable to access the number
## that's why when we asked for the i'th element in fruits, it printed them in sequential order.

## in python, you can also iterate over array items with a shorthand syntax, like this

for item in array:
  print(item)
  
## this is almost the same as what we did above, but this time the indexing is implicit. there's a lot of
## complicated stuff behind this, but for right now, just know that it's convenient.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

## already, we almost have enough knowledge to build something a little interactive.
## For example, we could set up a fruit store program. Let's say we're running
## a fruit stand, and the list of fruits contains all the fruit we could sell.
## So if we run the program and request to buy a fruit and it isn't in our list,
## we have to get denied. This program will effectively demonstrate the general idea
## of logic in the context of programming.

## First, we're going to say hi
print("Welcome to my Fruit Stand")

## Then, we can ask a quick question.
print("Want to buy some fruit?")

## Here, we take the answer.
answer = input(">\n") # input is a function, like print or len, that asks for the user input from the console

## once the user presses Enter, the input will be submitted and stored in the variable "answer"
## now, since we want to sell fruit if the answer yes or say goodbye if no, we have to create an if/else block
## however, we have to account for all scenarios. the user can say "yes" or "no" as valid responses to proceed,
## but what if they type in "fuck your mother!". We don't want this but it is within the realm of possibilities.

## since we know that there's only one answer that sells fruit, we don't have to account for all the infinite possibilities

## we can just say
if answer.lower() == "yes":          ## .lower() is a function that turns the word all lowercase. what if they type in "YES"?
   print("What would you like to buy?")
else:                                ## literally any input other than "yes"
   print("Bye Felicia")
   sys.exit(1)                       ## exit the program
   
## as you can see, the if/else syntax also obeys the concept of a 'scope', or an indented block of code that
## signifies a specific environment. Only if the condition of the if is true will "What would you like to buy?"
## be printed out, and similarly, only if that same condition isn't met will the "Bye Felicia" message and the
## system exit be executed. These are known as conditional scopes.

## That's all for now! Study these basics and next time we'll pick up right here where we left off.



























