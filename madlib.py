
def story_selection():
    """Asks user their choice in mad lib."""
    #Capture user selection and construct conditional statements

    print("Welcome to Mulligan Mad Libs!\nMake your choice from the selections shown.")
    print("-" * 45)

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
    cabinets {} open and shut, random objects {} down, and chilling
    temperatures, despite the thermostat being set to {} degrees Fahrenheit.
    After a while, all these {} happenings grew too much and forced the family out.
    A new family has recently has been looking at {} the house, so good luck
    to them!
    """

    story4 = """
    A HERO'S WELCOME! A new hero has emerged on the scene. Say hello to Captain {}.
    No one knows where they came from, but they've sworn to protect {} City. They claim
    to have the coolest superpowers, like {}, {}, and {}. Their uniform chose the
    colors {} blue and {} grey to {} their lost world. In a statement to the public,
    Captain {} detailed their commitment to truth, liberty, and {} for all those
    who live in {} City.
    """

    story5 = """
    In the Wild West, there are many legendary cowboys and outlaws. None compare to
    the person we'll discuss today. This is the ballad of {} {}.
    Originating and operating out of {}, Texas, {} was renowned for their
    record-time {} skills. {} was hard to beat in a duel.
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
    
    #Print story options
    for x in dict_stories:
        print(x + "\n")
    
    preference = input("Enter story selection: ")
    print("-" * 45)

    choices = ["1", "2", "3", "4", "5"]

    main_story = " "

    #Check if number is in valid story number choices
    while preference not in choices:
        print("Choose valid number entry.")
        preference = input("Enter story selection: ")
        if preference in choices:
            break
    if preference == "1":
        ship1 = ship5 = input("Proper noun: ")
        ship2 = input("Number: ")
        ship3 = input("Verb (present): ")
        ship4 = input("Country: ")
        ship6 = input("Country: ")
        ship7 = input("Country: ")
        ship8 = input("Number: ")
        ship9 = input("Number: ")
        main_story += story1.format(ship1.capitalize(),ship2,ship3,ship4.capitalize(),ship5.capitalize(),ship6.capitalize(),ship7.capitalize(),ship8,ship9)
    elif preference == "2":
        book1 = input("Name: ")
        book2 = input("Name: ")
        book3 = book15 = input("Name: ")
        book4 = input("Occupation: ")
        book5 = book7 = book10 = book12 = input("Proper noun: ")
        book6 = input("Year: ")
        book8 = input("Noun: ")
        book9 = input("City: ")
        book11 = input("Proper noun: ")
        book13 = input("Proper noun: ")
        book14 = input("Proper noun: ")
        book16 = input("Proper noun: ")
        book17 = input("Number: ")
        book18 = input("Number: ")
        main_story += story2.format(book1,book2,book3,book4.capitalize(),book5.capitalize(),book6,book7.capitalize(),book8,book9,book10.capitalize(),book11,book12.capitalize(),book13.capitalize(),book14.capitalize(),book15,book16.capitalize(),book17,book18)
    elif preference == "3":
        house1 = input("Proper noun: ")
        house2 = input("Proper noun: ")
        house3 = input("Proper noun: ")
        house4 = input("Noun: ")
        house5 = input("Adjective: ")
        house6 = input("Verb (present): ")
        house7 = input("Verb (present): ")
        house8 = input("Number: ")
        house9 = input("Adjective: ")
        house10 = input("Verb (present): ")
        main_story += story3.format(house1.capitalize(),house2.capitalize(),house3.capitalize(),house4,house5,house6,house7,house8,house9,house10)
    elif preference == "4":
        super1 = super9 = input("Proper noun: ")
        super2 = super11 = input("Proper noun: ")
        super3 = input("Noun: ")
        super4 = input("Noun: ")
        super5 = input("Noun: ")
        super6 = input("Proper noun: ")
        super7 = input("Proper noun: ")
        super8 = input("Verb: ")
        super10 = input("Noun: ")
        main_story += story4.format(super1.capitalize(),super2.capitalize(),super3,super4,super5,super6.capitalize(),super7.capitalize(),super8,super9.capitalize(),super10.capitalize(),super11.capitalize())
    elif preference == "5":
        west1 = west9 = input("Proper noun: ")
        west2 = west4 = west6 = west7 = west10 = west11 = input("Proper noun: ")
        west3 = input("City: ")
        west5 = input("Verb (present): ")
        west8 = input("Number: ")
        west12 = input("Cardinal direction: ")
        main_story += story5.format(west1.capitalize(),west2.capitalize(),west3.capitalize(),west4.capitalize(),west5,west6.capitalize(),west7,west8,west9,west10,west11,west12.capitalize())
    else:
        main_story += "NO STORY SELECTED!"
    print(main_story) #Print out story
    
def loop_output():
    """Loops through asking user if they want to continue."""
    #Ask users if they want to continue
    ask = input("Do you wish to continue (Y/N)?: ")
    #Loop question until user say they don't want to continue
    while ask.upper() == "Y":
        story_selection()
        ask = input("Do you wish to continue (Y/N)?: ")
        if ask.upper() == "N":
            break
    return "Thanks for playing..." #Return thank you message

#Execute functions
story_selection()
print(loop_output())
