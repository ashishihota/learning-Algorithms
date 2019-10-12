game = [[1,0 ,0],
        [0,0,0,],
	[0,0,0,],]


def win(current_game):
	for row in game:
		print(row)
		if row.count(row[0]) == len(row) :
			print("winner")
