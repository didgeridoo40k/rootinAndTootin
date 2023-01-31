# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg_forest_landscape1

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.

    e "You've created a new Ren'Py game."
    e "This is the first background image."

    scene bg_forest_landscape2
    show eileen happy
    e "This is the second background image."

    scene bg_forest_landscape3
    show eileen happy
    e "This is the third background image."

    scene bg_forest_landscape4
    show eileen happy
    e "This is the forth background image."
    e "Thanks for testing!"
    e "The game is ending now."

    # This ends the game.

    return
