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

    scene bg_forest_landscape1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show aria
    A "Hey, it is me. Aria!"
    show aria supprised
    A "Now I am supprised!"
    show aria smiling
    A "Now I am smiling."
    show aria
    A "Good testing!"

    # These display lines of dialogue.

    
    # This ends the game.

    return
