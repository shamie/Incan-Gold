import random
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
#for i in range (1, 5):
#	play_round()
#	round_num = round_num - 1
#else:
#	end_game()

# actual game play
# things i need to learn:
# how to add relic
# how to flip top card of deck

# deck shuffling 
deck = ["one", "two", "three", "four", "five", "five", "seven", "seven", "nine", "eleven", "eleven", "thirteen", "fourteen", "fifteen", "seventeen", "goblin", "goblin", "goblin", "fire", "fire", "fire", "rocks", "rocks", "rocks", "snakes", "snakes", "snakes", "spiders", "spiders", "spiders"]
print deck

random.shuffle(deck)
print deck

# def play_round():
