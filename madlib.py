#Create mad lib options for user to choose from
story1 = """
Get excited for the brand new submarine base, the S.S. {}.
It has a 24 hour fitness center, unlimited dining, phenomenal views of
underwater sealife, and over {} rooms, which can be used for lounging, {},
entertainment, and dining.
At about 100 miles below the surface and off the coast of {},
the S.S. {} is a state of the art mobile conference center and vacation spot.
Forget travelling to {} or {} for your summer vacation. Choose Yempton's
Top Rated holiday get away tour for over {} years. Book your tickets today,
start at ${}.99!
"""

story2 = """
{} {} {} is a renowned {} in the field of {}.
Born in {}, their biggeset contribution to {} was inventing {}.
Growing up in {}, Nebraska enabled a helpful environment for them to foster
their interest in {}.
They attended {} University and majored in {} and then got their Masters degree
in {} from the University of {}. After graduation, {} went on to make {}
Enterprises, a middle size company of {} - {} people.
"""

story3 = """
Beware of the Haunted House off the intersection of {} Street and {} Boulevard.
The owners of the house, the {} family, sold if off years ago and moved East.
I heard that after the pet {} died, the family was devastated. The week
following the pet's death, the atmosphere of the house became {}:
cabinets {}ing open and shut, random objects {}ing down, and chilling
temperatures, despite the thermostat being set to {} degrees Fahrenheit.
After a while, all these {} happenings grew too much and forced the family out.
A new family has recently has been looking at {}ing the house, so good luck
to them!
"""

story4 = """
A HERO'S WELCOME! A new hero has emerged on the scene. Say hello to Captain {}.
Noone where they came from, but they've sworn to protect {} City. They claim
to have the coolest superpowers, like {}, {}, and {}. Their uniform chose the
colors {} and {} to commemorate their lost world. In a statement to the public,
Captain {} detailed their commitment to truth, liberty, and {} for all those
who live in {} City.
"""

story5 = """
In the Wild West, there are many legendary cowboys and outlaws. None compare to
the person we'll discuss today. This is the ballad of {} {}.
Originating and operating out of {}, Texas, {}.
Renowned for their record-time {} skills, {} was hard to beat in a duel.
With this reputation, {} traveled across the West Coast, winning duel after duel.
Records indicate that over the course of over {} duels, {} {} only lost once.
Eventually, the duels took their toll and {} allegedly retired to the {} region.
"""

#Initialize array of stories to choose from and print options

dict_stories = {"Shiptime, Maritime (1)":story1,
                "The Achievement (2)":story2,
                "Haunted Horror (3)":story3,
                "Modern Superhero (4)":story4,
                "Western Cowboys (5)":story5
                }
print("Welcome to Mulligan Madlibs!\nMake your choice from the selections shown.")
print("-" * 45)
for x in dict_stories:
    print(x + "\n")

#Capture user selection and construct conditional statements
preference = input("Enter story selection: ")

choices = ["1", "2", "3", "4", "5"]

if preference == "1":
    print(dict_stories["Shiptime, Maritime (1)"])
elif preference == "2":
    print(dict_stories["The Achievement (2)"])
elif preference == "3":
    print(dict_stories["Haunted Horror (3)"])
elif preference == "4":
    print(dict_stories["Modern Superhero (4)"])
elif preference == "5":
    print(dict_stories["Western Cowboys (5)"])
else:
    while preference not in choices:
        print("Choose valid number entry")
        preference = input("Enter story selection: ")
        if preference in choices:
            if preference == "1":
                print(dict_stories["Shiptime, Maritime (1)"])
            elif preference == "2":
                print(dict_stories["The Achievement (2)"])
            elif preference == "3":
                print(dict_stories["Haunted Horror (3)"])
            elif preference == "4":
                print(dict_stories["Modern Superhero (4)"])
            elif preference == "5":
                print(dict_stories["Western Cowboys (5)"])
            break
                
