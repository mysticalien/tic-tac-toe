values = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print("---------")
print("|" + " " + values[0][0] + " " + values[0][1] + " " + values[0][2] + " " + "|")
print("|" + " " + values[1][0] + " " + values[1][1] + " " + values[1][2] + " " + "|")
print("|" + " " + values[2][0] + " " + values[2][1] + " " + values[2][2] + " " + "|")
print("---------")
i = 0
while True:
    number = input().split()
    try:
        a = int(number[0])
        b = int(number[1])
        if a not in range(1, 4) or b not in range(1, 4):
            print("Coordinates should be from 1 to 3!")
        elif values[a - 1][b - 1] != ' ':
            print("This cell is occupied! Choose another one!")
        else:
            if i % 2 == 0:
                values[a - 1][b - 1] = "X"
            else:
                values[a - 1][b - 1] = "O"
            print("---------")
            print("|" + " " + values[0][0] + " " + values[0][1] + " " + values[0][2] + " " + "|")
            print("|" + " " + values[1][0] + " " + values[1][1] + " " + values[1][2] + " " + "|")
            print("|" + " " + values[2][0] + " " + values[2][1] + " " + values[2][2] + " " + "|")
            print("---------")
            i += 1
            values1 = [values[0][0] + values[0][1] + values[0][2],
                       values[1][0] + values[1][1] + values[1][2],
                       values[2][0] + values[2][1] + values[2][2],
                       values[0][0] + values[1][0] + values[2][0],
                       values[0][1] + values[1][1] + values[2][1],
                       values[0][2] + values[1][2] + values[2][2],
                       values[0][0] + values[1][1] + values[2][2],
                       values[0][2] + values[1][1] + values[2][0]]
            if "XXX" in values1:
                print("X wins")
                break
            elif "OOO" in values1:
                print("O wins")
                break
            elif " " not in [cell for row in values for cell in row]:
                print("Draw")
                break
    except ValueError:
        print("You should enter numbers!")
    except IndexError:
        print("You must enter two numbers separated by a space!")