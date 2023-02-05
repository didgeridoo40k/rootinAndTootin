# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define A = Character("Aria")
define S = Character("Sam")
define AD = Character("Aria’s dad")
define AM = Character("Aria’s mom")
define SD = Character("Sam’s dad")
define BGU = Character("???")

image aria supprised = "aria_supprised.png"
image aria smiling = "aria_smiling.png"
image aria = "aria.png"

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_forest_landscape2

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    BGU "Quickly! After her!"
    "Aria runs as fast as she can through the woods desperately trying to stay ahead of the men chasing her."
    "She sees a clearing in the woods ahead."
    "As she gets to the clearing suddenly her footing is lost. In front of her is a cliff over a lake."
    label first_choice:
    menu optional_name:
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
    show aria at right
    show sam at left #I need a sprite for Sam
    BGU "Do you need help?"
    A "Yes please there are people after me."
    BGU "Well as sketch as that sounds get in."
    "The man unlocks the truck door."
    "Aria gets in the truck."
    "They drive off quickly."
    BGU "So Aria? What are you doing here?"
    A "Ye, yes….. do I know you?"
    hide aria
    show aria_supprised at right
    "The tires screech as the man suddenly stops the truck."
    show aria_confused at right #I need a confused sprite for Aria
    BGU "…….. You really don’t remember me?"
    A "I mean you seem familiar but no. Sorry?"


    return
