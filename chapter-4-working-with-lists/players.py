players  = ["charles","martina","michael","florence","eli"]
# the starting index and total num
print(players[1:4]);

# without start index

print(players[:4]);

# without the ending 
print(players[3:]);

#  loop through the slice list
print("Here are the first three players on my team.");
for player in players[:3]:
    print(player.title())