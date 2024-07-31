print("welcome to the bunny game ")
field = [['🍃', '🍃', '🍃'],['🍃', '🍃', '🍃'],['🍃', '🍃', '🍃']]


print(f"{field[0]} \n{field[1]} \n{field[2]}")

position =(input(" please choose a row and column for the bunny to go "))

row = int(position[0])
column = int(position[1])

field[row-1][column-1] = "🐇"

print("\n")

print(f"{field[0]} \n{field[1]} \n{field[2]}")