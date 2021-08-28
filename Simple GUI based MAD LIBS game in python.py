from tkinter import *
root = Tk()
root.geometry('300x300')
root.title('Mad Libs')
Label(root,text= 'Play Mad Libs \n Have Fun!!!', font = 'arial 20 bold').pack()
Label(root,text='Your Choice:', font = 'arial 15 bold').place(x=40,y=80)
Label(root,text='This is my first GUI based program', font='arialblack 10').place(x=40,y=300)

def story1():
    adjective= input("entre adjective: ")
    noun = input("entre noun")
    verb_past = input("entre verb_past tense")
    adverb = input("entre adverb")
    adjective1= input("entre adjective")
    noun1 = input("entre noun")
    noun2 = input("entre noun")
    adjective2 = input("entre adjective")
    verb = input("entre verb")
    adverb1 = input("entre adverb")
    verb_past1 = input("entre verb_past tense")
    adjective3 = input("entre adjective")

    zoo = f'''    Today I went to zoo. I saw a(n){adjective} {noun} jumping up and down in its tree.
 He {verb_past} {adverb} through the large tunnel that led to its {adjective1}
 {noun1}.I got some peanuts and passed them through the cage to a gigantic gray
 {noun2} towering above my head. Feeding that animal made me hungry.
 I went to get a {adjective2} scoop of ice cream. It filled my stomach. Afterwards
 I had to {verb} {adverb1} to catch our bus. When I got home I {verb_past1} my mom for a {adjective3} day at the zoo.'''

    print(zoo)

def story2():
    adjective = input("entre adjective: ")
    noun = input("entre plural noun")
    noun1 = input("entre noun")
    adverb = input("entre adverb")
    number = input("entre number")
    verb_past = input("entre verb_past tense")
    adjective1 = input("entre adjective")
    verb_past1 = input("entre verb_past tense")
    adverb1 = input("entre adverb")
    adjective2 = input("entre adjective")

    fun = f'''Today, my fabulous camp group went to a(an) {adjective} amusement park. It was a fun park with
 lots of cool {noun} and enjoyable play structures. When we got there, my kind counselor shouted loudly,
 "Everybody off the {noun1}. "We all pushed out in a terrible hurry. My counselor handed out
 yellow tickets, and we scurried in. I was so excited! I couldn't figure out what exciting thing to do first. I saw a scary
 roller coaster I really liked so, I {adverb} ran over to get in the long line that had about
  {number} people in it. When I finally got on the roller coaster I was {verb_past}. In fact I was so nervous
 my two knees were knocking together. This was the {adjective1} ride I had ever been on! In about
 two minutes I heard the crank and grinding of the gears. That's when the ride began! When I got to the bottom,
 I was a little {verb_past1}but I was proud of myself. The rest of the day went {adverb1}. It was a(n)
 {adjective2}day at the fun park.'''

    print(fun)

def story3():
    adjective = input("entre adjective: ")
    adjective1 = input("entre adjective")
    first_name = input("a first name")
    verb_past = input("entre verb_past tense")
    first_name1 = input("a first name")
    adjective2 = input("entre adjective")
    noun = input("entre plural noun")
    animal = input("large animal")
    animal2 = input("small animal")
    name = input("girl's name")
    adjective3 = input("entre adjective")
    noun1 = input("entre plural noun")
    adjective4 = input("entre adjective")
    noun2 = input("entre noun")
    number = input("entre number 1-50")
    first_name2 = input("first name's")
    number1 = input("entre number")
    noun3 = input("entre plural noun")
    number2 = input("entre number")
    noun4 = input("entre plural noun")
    adjective5 = input("entre adjective")

    video_game = f'''I, the {adjective} and {adjective1} {first_name} has {verb_past}
 {first_name1}'s {adjective2} sister and plans to steal her {adjective3} {noun}! what
 are a {animal} and backpacking {animal2} to do? Before you can help {name}, you'll have to collect the 
 {adjective4} {noun1} and {adjective5} {noun2} that open up the {number} worlds connected to a
  {first_name2} lair. There are {number1} {noun3} and {number2} {noun4} in the game, along
 with hundreds of other goodies for you to find.'''
    print(video_game)


Button(root, text= 'A Day At The Zoo', font = 'arial 15', command= story1, bg = 'ghost white').place(x=60, y=120)
Button(root, text= 'The Fun Park', font = 'arial 15', command= story2, bg = 'ghost white').place(x=60, y=180)
Button(root, text= 'Make Me A Video Game', font = 'arial 15', command= story3, bg = 'ghost white').place(x=60, y=240)

root.mainloop()
