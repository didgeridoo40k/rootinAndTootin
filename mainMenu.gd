extends Control

# reference to the play button
onready var play_button = get_node("Start")
onready var options_button = get_node("Options")
onready var quit_button = get_node("Quit")

func _ready():
	# connect the pressed signal of the buttons to the corresponding function
	play_button.connect("pressed", self, "start_game")
	options_button.connect("pressed", self, "open_options")
	quit_button.connect("pressed", self, "quit_game")

func start_game():
	# code to start the game goes here
	print("Starting game...")

func open_options():
	# code to open the options menu goes here
	print("Opening options...")

func quit_game():
	# code to quit the game goes here
	get_tree().quit()
