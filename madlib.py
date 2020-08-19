#Create mad lib options for user to choose from
story1 = """
Get excited for the brand new submarine base, the S.S. {ship1}.
It has a 24 hour fitness center, unlimited dining, phenomenal views of
underwater sealife, and over {ship2} rooms, which can be used for lounging, {ship3},
entertainment, and dining.
At about 100 miles below the surface and off the coast of {ship4},
the S.S. {ship5} is a state of the art mobile conference center and vacation spot.
Forget travelling to {ship6} or {ship7} for your summer vacation. Choose Yempton's
Top Rated holiday get away tour for over {ship8} years. Book your tickets today,
start at ${ship9}.99!
"""

story2 = """
{book1} {book2} {book3} is a renowned {book4} in the field of {book5}.
Born in {book6}, their biggeset contribution to {book7} was inventing {book8}.
Growing up in {book9}, Nebraska enabled a helpful environment for them to foster
their interest in {book10}.
They attended {book11} University and majored in {book12} and then got their Masters degree
in {book13} from the University of {book14}. After graduation, {book15} went on to make {book16}
Enterprises, a middle size company of {book17} - {book18} people.
"""

story3 = """
Beware of the Haunted House off the intersection of {house1} Street and {house2} Boulevard.
The owners of the house, the {house3} family, sold if off years ago and moved East.
I heard that after the pet {house4} died, the family was devastated. The week
following the pet's death, the atmosphere of the house became {house5}:
cabinets {house6} open and shut, random objects {house7} down, and chilling
temperatures, despite the thermostat being set to {house8} degrees Fahrenheit.
After a while, all these {house9} happenings grew too much and forced the family out.
A new family has recently has been looking at {house10} the house, so good luck
to them!
"""

story4 = """
A HERO'S WELCOME! A new hero has emerged on the scene. Say hello to Captain {super1}.
No one knows where they came from, but they've sworn to protect {super2} City. They claim
to have the coolest superpowers, like {super3}, {super4}, and {super5}. Their uniform chose the
colors {super6} blue and {super7} grey to {super8} their lost world. In a statement to the public,
Captain {super9} detailed their commitment to truth, liberty, and {super10} for all those
who live in {super11} City.
"""

story5 = """
In the Wild West, there are many legendary cowboys and outlaws. None compare to
the person we'll discuss today. This is the ballad of {west1} {west2}.
Originating and operating out of {west3}, Texas, {west4}.
Renowned for their record-time {west5} skills, {west6} was hard to beat in a duel.
With this reputation, {west7} traveled across the West Coast, winning duel after duel.
Records indicate that over the course of over {west8} duels, {west9} {west10} only lost once.
Eventually, the duels took their toll and {west11} allegedly retired to the {west12} region.
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
    ship1.capitalize() = ship5.capitalize() = input("Proper noun: ")
    ship2 = input("Number: ")
    ship3 = input("Verb (present): ")
    ship4.capitalize() = input("Country: ")
    ship6.capitalize() = input("Country: ")
    ship7.capitalize() = input("Country: ")
    ship8 = input("Number: ")
    ship9 = input("Number: ")
    print(story1.format(ship1, ship2, ship3, ship4, ship5, ship6, ship7, ship8, ship9))
elif preference == "2":
    book1 = input("Name: ")
    book2 = input("Name: ")
    book3 = book15 = input("Name: ")
    book4.capitalize() = input("Occupation: ")
    book5.capitalize() = book7.capitalize() = book10.capitalize() = book12.capitalize() = input("Proper noun: ")
    book6 = input("Year: ")
    book8 = input("Noun: ")
    book9 = input("City: ")
    book11.capitalize() = input("Proper noun: ")
    book13.capitalize() = input("Proper noun: ")
    book14.capitalize() = input("Proper noun: ")
    book16.capitalize() = input("Proper noun: ")
    book17 = input("Number: ")
    book18 = input("Number: ")
    print(story2.format(book1, book2, book3, book4, book5, book6, book7, book8, book9, book10, book11, book12, book13, book14, book15, book16, book17, book18))
elif preference == "3":
    house1.capitalize() = input("Proper noun: ")
    house2.capitalize() = input("Proper noun: ")
    house3.capitalize() = input("Proper noun: ")
    house4 = input("Noun: ")
    house5 = input("Adjective: ")
    house6 = input("Verb (present): ")
    house7 = input("Verb (present): ")
    house8 = input("Number: ")
    house9 = input("Adjective: ")
    house10 = input("Verb (present): ")
    print(story3.format(house1, house2, house3, house4, house5, house6, house7, house8, house9, house10))
elif preference == "4":
    super1.capitalize() = super9.capitalize() = input("Proper noun: ")
    super2.capitalize() = super11.capitalize() = input("Proper noun: ")
    super3 = input("Noun: ")
    super4 = input("Noun: ")
    super5 = input("Noun: ")
    super6.capitalize() = input("Proper noun: ")
    super7.capitalize() = input("Proper noun: ")
    super8 = input("Verb: ")
    super10 = input("Noun: ")
    print(story4.format(super1, super2, super3, super4, super5, super6, super7, super8, super9, super10, super11))
elif preference == "5":
    west1.capitalize() = west9.capitalize() = input("Proper noun: ")
    west2.capitalize() = west4.capitalize() = west6.capitalize() = west7.capitalize() = west10.capitalize() = west11.capitalize() = input("Proper noun: ")
    west3.capitalize() = input("City: ")
    west5 = input("Verb (present): ")
    west8 = input("Number: ")
    west12.capitalize() = input("Cardinal direction: ")
    print(story5.format(west1, west2, west3, west4, west5, west6, west7, west8, west9, west10, west11, west12))
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
