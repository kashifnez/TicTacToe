import os

spl = "\n\n\t\t\t,•••••••••••,\n\t\t\t| 1 | 2 | 3 |\n\t\t\t|---|---|---|\n\t\t\t| 4 | 5 | 6 |\n\t\t\t|---|---|---|\n\t\t\t| 7 | 8 | 9 |\n\t\t\t`•••••••••••`"




def playground():
	print("\n\t\t\t,•••••••••••,\n\t\t\t", end="")
	
	print(f"| {m[0]} | {m[1]} | {m[2]} |\n\t\t\t|---|---|---|")
	print("\t\t\t", end ="")
	print(f"| {m[3]} | {m[4]} | {m[5]} |")
	print("\t\t\t|---|---|---|\n\t\t\t", end="")
	print(f"| {m[6]} | {m[7]} | {m[8]} |")
	
	print("\t\t\t`•••••••••••`")
	
	
m= [" ", " ", " ", " ", " ", " ", " ", " ", " "]
over =1
turn = 1
#print("\n\n\t++++++++++++++   PLAYER-1 Turn  ++++++++++++++\n")
print(spl)
playground()


while True:
	draw = "a"
	for i in m:
		if i == " ":
			draw = i
			break
		
	
					#### Game winning ####
	if ((m[0] == m[1] == m[2] =="X") or (m[3] == m[4] == m[5] =="X") or (m[6] == m[7] == m[8] == "X") or (m[0] == m[4] == m[8] == "X") or (m[2] == m[4] == m[6] == "X") or (m[0] == m[3] == m[6] == "X") or (m[1] == m[4] == m[7] == "X")or (m[2] == m[5] == m[8] == "X")):
		print("\n\n######## HIP HIP HURRAH!!! PLAYER-1 Won the game  ######")
		exit()
	
	if ((m[0] == m[1] == m[2] =="O") or (m[3] == m[4] == m[5] =="O") or (m[6] == m[7] == m[8] == "O") or (m[0] == m[4] == m[8] == "O") or (m[2] == m[4] == m[6] == "O") or (m[0] == m[3] == m[6] == "O") or (m[1] == m[4] == m[7] == "O")or (m[2] == m[5] == m[8] == "O")):
		print("\n\n######## HIP HIP HURRAH!!! PLAYER-2 Won the game ######")
		exit()
			##---xx-------Gamewinning-----XXX
		
		   		### Game Draw ##
	if draw == "a":
			print("\n\t\t------ Game DRAW ---------\n\n")	
			exit()
				#Xxxx--------xxxxx-----xxxxxx
		
	print("\n\t++++++  ENTER Number for corresponding Spaces ++++++\n\n")
		
	if turn == 1:
		yturn = int(input("PLAYER 1: "))
		os.system('clear')
		print(spl)
		if m[yturn-1] == " ":
			m[yturn-1] = "X"
			playground()
		else:
			print("\n\t----Already Filled!! You LOST your TURN-----")
			playground()
		
		turn = 2
	else:
		xturn = int(input("PLAYER 2: "))
		os.system('clear')
		print(spl)
		if m[xturn-1] == " ":
			m[xturn-1] = "O"
			playground()
		else:
			print("\n\t-------Already Filled, you LOST your TURN-----\n")
			playground()
		turn = 1
