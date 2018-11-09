import re, sys, os
"""Checks if program and text file and inputted correctly"""
if(len(sys.argv)) != 2:
	sys.exit("Usage: %s filename" % sys.argv[0])

filename=sys.argv[1]
"""checks if file exists"""
if not os.path.exists(filename):
	sys.exit("Error: File '%s' not found" % sys.argv[1])

file = open(filename, "r")
players = []
"""regular expression line"""
regex = re.compile('(?P<name>.*) batted (?P<bats>[0-9]*) times with (?P<hits>[0-9]*) hits and (?P<runs>[0-9]*) runs')
"""player object"""
class Player:
	def __init__(self,name,bats,hits,runs):
		self.name=name
		self.bats=bats
		self.hits=hits
		self.runs=runs
"""makes player"""
def make_player(name,bats,hits,runs): 
	new = Player(name,bats,hits,runs)
	players.append(new)
"""goes through each line and adds the player to the array or updates their bats, hits and runs"""
for line in file:
	found = 0
	each_line = regex.match(line)
	if each_line:
		player_name = each_line.group('name')
		player_bats = int(each_line.group('bats'))
		player_hits= int(each_line.group('hits'))
		player_runs = int(each_line.group('runs'))

		for player in players:
			if player_name==player.name:
				player.bats+=player_bats
				player.hits+=player_hits
				player.runs+=player_runs
				found = 1

		if found == 0:	
			make_player(player_name,player_bats,player_hits,player_runs)

file.close()
"""class for player and average"""
class Sorted:
	def __init__(self,name,avg):
		self.name=name
		self.avg=avg

players_avg=[]
"""calculates average and puts the player into an array"""
for player in players:
	if player.hits!=0:
		average = round(player.hits/player.bats,3)
	new = Sorted(player.name,average)
	players_avg.append(new)
sorted_players=[]
"""sorts the array based on average"""
sorted_players = sorted(players_avg,key=lambda player:player.avg,reverse=True)
"""prints out the player name and batting average rounded to three decimal points"""
for player in sorted_players:
	print('{}: {:.3f}'.format(player.name,player.avg))