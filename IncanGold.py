round_num = 5
roster = []
final_score = []
round_score = []

# add in check for correct number of players
player_count = raw_input("How many players (3-8)? ")

# create the player roster
for i in range (0, int(player_count)):
	roster.append("player" + str(i + 1))

# create a permentant score card
for i in range (0, int(player_count)):
	final_score.append(0)

# create a round by round score card
for i in range (0, int(player_count)):
	round_score.append(0)

def end_game():
	for i in roster(0, int(player_count)):
		print "%r: %r" % (roster(i), score(i))

# continue playing?
for i in range (1, 5):
	play_round()
	round_num = round_num - 1
else:
	end_game()

# actual game play
# things i need to learn:
# how to shuffle deck
# how to add relic
# how to flip top card of deck
def play_round():
	
def treasure_card():
	payout = value/current_players
# create a system for points to be given to each 
# player still in the game
# and skip returned players

def hazard_card():
# if a new hazard, next card
# if second hazard of the same type, round ends

def relic_card():
# if relic card 1-3, it is worth 5
# if relic card 4-5, it is worth 10
# while there is a relic card out
# if more than one person returns, relic is destroyed

# hazards
# goblins = 3
# fire = 3
# rocks = 3
# snakes = 3
# spiders = 3

relics = 5

# treasures
# one = 1
# two = 1
# three = 1
# four = 1 
# five = 2
# seven = 2
# nine = 1
# eleven = 2
# thirteen = 1
# fourteen = 1
# fifteen = 1
# seventeen = 1
