define A = Character("Aria")
define S = Character("Sam")
define AD = Character("Aria’s dad")
define AM = Character("Aria’s mom")
define SD = Character("Sam’s dad")
define BGU = Character("???")

image aria supprised = "aria_supprised.png"
image aria smiling = "aria_smiling.png"
image aria = "aria.png"
#image open_chest = "openchest.png"


label start:


    scene bg_forest_landscape2

    BGU "Quickly! After her!"
    "Aria runs as fast as she can through the woods desperately trying to stay ahead of the men chasing her."
    "She sees a clearing in the woods ahead."
    "As she gets to the clearing suddenly her footing is lost. In front of her is a cliff over a lake."
    label first_choice:
    menu the_cliff:
        "What should I do?"
        "I could try jumping and swimming ashore. The fall is too big I might not make it!":
            jump jump_and_swim
        "Or I could stand and fight I might be able to get the upper hand.":
            jump stand_and_fight
    
    label stand_and_fight:
    "Aria decides to fight."
    "Aria manages a swift kick on the first man to approach her but the others surround and grab her. "
    show aria_supprised at right
    "Violent murder happens maybe some blood sqleching sounds and a scream *YOU DEAD BITCH*"
    "Game Over"
    return
    
    label jump_and_swim:
    show aria_supprised at right
    "Aria decides to jump."
    show aria_supprised at right
    "Aria crashes into the lake"
    "Aria is finding it hard to keep going, She feels like all the energy is zapped out of her."
    hide aria_supprised
    "She needs to power through and continue. She needs to get to safety and find out why this all happened."
    "Aria swims to shore and catches her breath. "
    scene bg_forest_landscape1
    "After a brief rest Aria continues on."
    show aria
    "She moves though the forest at a slower pace, looking out for her pursuers."
    "Aria comes to a road and sees a car passing by."
    hide aria
    "She waves frantically for help."
    show aria_supprised at right
    A "Help!"
    "As the vehicle comes to a stop her pursuers catch up to her."
    hide aria_supprised
    show aria
    "Aria notices the man in the vehicle looks familiar."
    "The truck screeches to a halt."
    hide aria
    #scene bg_truck_stops
    show aria at right
    show sam at left #I need a sprite for Sam
    BGU "Do you need help?"
    A "Yes please there are people after me."
    BGU "Well as sketch as that sounds get in."
    "The man unlocks the truck door."
    "Aria gets in the truck."
    "They drive off quickly."
    #scene bg_truck_driving_in_woods
    BGU "So Aria? What are you doing here?"
    A "Ye, yes….. do I know you?"
    hide aria
    show aria_supprised at right
    "The tires screech as the man suddenly stops the truck."
    hide aria_supprised
    show aria_confused at right #I need a confused sprite for Aria
    BGU "…….. You really don’t remember me?"
    A "I mean you seem familiar but no. Sorry?"
    BGU "…….ugh I can’t believe you."
    S "Sam.…..You remember we used to play together as kids?"
    A "Sam!? Really!? What are you doing I thought you wanted to go live the city life?"
    "Sam starts the truck again."
    S "Yeah that's me. Still is but I got some business to take care of."
    S "I should be the one asking you the questions though."
    S "What is going on? Why were those people chasing you?"
    A "I’m not sure. I think they want this though..."
    "Aria pull out a chest"
    A "Grams left it for me. It was the last thing she gave me before….."
    S "I’m sorry for your loss."
    A "Thanks…. I don’t know what to do now."
    S "I know what I would do..."
    "Sam looks at the box."
    A "I’m not sure. Whatever it is may not be valuable but those guys certainly wanted it."
    S "Won’t know till we look? Will we?"
    A "Yeah but I’m not sure it is worth the risk. Maybe I should just chuck it and skip town?"
    S "That’s one option or we could go to the police?"
    S "Or here’s a thought..."
    S "open it?"

    label choice_open_the_box:
    menu open_the_box:
        "What should I do?"
        "Leave the chest and skip town.":
            jump options2_choice1
        "Go to the cops":
            jump options2_choice2
        "Open the box":
            jump options2_choice3
    
    label options2_choice1:
    label options2_choice2:
    label options2_choice3:
    A "Yeah you are right Let's open it."
    "Aria opens the chest"
    #show open_chest #need a sprite for this
    "Inside is a branch."
    "Aria picks it up."
    A "Well they must be mistaken. This couldn’t have any value could it?"
    "Sam glances over and slams on the breaks"
    A "Again!? can’t you drive?"
    "Sam looks at the branch like he just realized something was missing."
    S "I’m not sure what this is all about..."
    S "But I have a feeling I know where that goes."
    A "It goes to a tree….?"
    S "Yes a tree of course it goes to a tree; but Not just any TREE!"
    "Sam pulls out a map"
    S "This tree!"
    "Sam points at a crude drawing of a branch and an x"
    A "What is this? Where did you get this?"
    S "My dad gave it to me before I left for college."
    S "He said it would be better off far away from here."
    A "I don’t get it! Why all the mystery who cares about some branch and a tree."
    S "I’m not sure but I think that's what your granny wanted you to find out."
    S "I was actually coming back into town to see her. I got a letter from her just the other day."
    A "You couldn’t have!"
    A "There is no way..."
    A "She past away a month ago!"
    S "So you’re saying someone was pretending to be her?"
    A "I don’t know, but I don’t think its a coincidence."
    S "Well I’m sure the end of this map will have some clue."
    A "I hope you are right so we can get out of this nightmare!"




    return
