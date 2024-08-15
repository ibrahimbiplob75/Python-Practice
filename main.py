import os

# users game choice history
u_1_in = []
u_2_in = []

# Game memory

mem = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
blank = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def result(mem, uc, info):
    # replacing blank space
    if uc == 1:
        mem[0][0] = info
        blank[0][0] = "-"
    elif uc == 2:
        mem[0][1] = info
        blank[0][1] = "-"
    elif uc == 3:
        mem[0][2] = info
        blank[0][2] = "-"
    elif uc == 4:
        mem[1][0] = info
        blank[1][0] = "-"
    elif uc == 5:
        mem[1][1] = info
        blank[1][1] = "-"
    elif uc == 6:
        mem[1][2] = info
        blank[1][2] = "-"
    elif uc == 7:
        mem[2][0] = info
        blank[2][0] = "-"
    elif uc == 8:
        mem[2][1] = info
        blank[2][1] = "-"
    else:
        mem[2][2] = info
        blank[2][2] = "-"

    # Checking if the value give won yet
    winning_val = ""

    if mem[0][0] == mem[0][1] and mem[0][0] == mem[0][2] and mem[0][0] != " ":
        winning_val = mem[0][0]

    elif mem[1][0] == mem[1][1] and mem[1][0] == mem[1][2] and mem[1][0] != " ":
        winning_val = mem[1][0]

    elif mem[2][0] == mem[2][1] and mem[2][0] == mem[2][2] and mem[2][0] != " ":
        winning_val = mem[2][0]

    elif mem[0][0] == mem[1][0] and mem[0][0] == mem[2][0] and mem[0][0] != " ":
        winning_val = mem[0][0]

    elif mem[0][1] == mem[1][1] and mem[0][1] == mem[2][1] and mem[0][1] != " ":
        winning_val = mem[0][1]

    elif mem[0][2] == mem[1][2] and mem[0][2] == mem[2][2] and mem[0][2] != " ":
        winning_val = mem[0][2]

    elif mem[0][0] == mem[1][1] and mem[0][0] == mem[2][2] and mem[0][0] != " ":
        winning_val = mem[0][0]

    elif mem[0][2] == mem[1][1] and mem[0][2] == mem[2][0] and mem[0][2] != " ":
        winning_val = mem[0][2]

    print(f"  {mem[0][0]}  |  {mem[0][1]}  |  {mem[0][2]}  ")
    print("-----|-----|-----")
    print(f"  {mem[1][0]}  |  {mem[1][1]}  |  {mem[1][2]}  ")
    print("-----|-----|-----")
    print(f"  {mem[2][0]}  |  {mem[2][1]}  |  {mem[2][2]}  ")

    return winning_val


def blank_space(mem):
    for a in range(0, 3):
        for b in range(0, 3):
            if mem[a][b] != " ":
                blank[a][b] = "-"
    return blank


def print_blank(blank):
    print("Enter Your Choice")
    for a in range(0, 3):
        for b in range(0, 3):
            print(blank[a][b], end=" ")
        print("")


def validate_inp(name):
    validate = 0
    while validate == 0:
        print("Your Turn ", end="")
        print(name)
        er = 1
        while er == 1:
            try:
                u1c = int(input())
            except:
                print("Enter a valid input(1-9):")
            else:
                er = 0

        if u1c not in range(1, 10):
            print("invalid input.try again")
        else:
            if (u1c == 1 and mem[0][0] != " ") or (u1c == 2 and mem[0][1] != " ") or (u1c == 3 and mem[0][2] != " "):
                print("Place is already filled.Try other option")
            elif (u1c == 4 and mem[1][0] != " ") or (u1c == 5 and mem[1][1] != " ") or (u1c == 6 and mem[1][2] != " "):
                print("Place is already filled.Try other option")
            elif (u1c == 7 and mem[2][0] != " ") or (u1c == 8 and mem[2][1] != " ") or (u1c == 9 and mem[2][2] != " "):
                print("Place is already filled.Try other option")
            else:
                validate = 1
    return u1c


def reset_pos(val, mem, blank):
    if val == 1:
        mem[0][0] = " "
        blank[0][0] = 1
    elif val == 2:
        mem[0][1] = " "
        blank[0][1] = 2
    elif val == 3:
        mem[0][2] = " "
        blank[0][2] = 3
    elif val == 4:
        mem[1][0] = " "
        blank[1][0] = 4
    elif val == 5:
        mem[1][1] = " "
        blank[1][1] = 5
    elif val == 6:
        mem[1][2] = " "
        blank[1][2] = 6
    elif val == 7:
        mem[2][0] = " "
        blank[2][0] = 7
    elif val == 8:
        mem[2][1] = " "
        blank[2][1] = 8
    else:
        mem[2][2] = " "
        blank[2][2] = 9


print("Welcome to Tic Tac Toe game!!!Hope you'll enjoy")

# name selection
user1 = input("Enter player 1's Name: ")
user2 = input("Enter player 2's Name: ")

# sign selection
print(f"Select Sign for {user1} (1/2): ")
print("1.X")
print("2.O")

err = 0
# Input validation
while err == 0:
    sign1 = input()
    if sign1 not in ("1", "2"):
        print("Select Valid Option")
    else:
        if sign1 == "1":
            sign1 = "X"
            sign2 = "O"
        else:
            sign1 = "O"
            sign2 = "X"
        break
user_info = {"name1": user1, "sign1": sign1, "name2": user2, "sign2": sign2}

# Showing current chart
print(f"  {mem[0][0]}  |  {mem[0][1]}  |  {mem[0][2]}  ")
print("-----|-----|-----")
print(f"  {mem[1][0]}  |  {mem[1][1]}  |  {mem[1][2]}  ")
print("-----|-----|-----")
print(f"  {mem[2][0]}  |  {mem[2][1]}  |  {mem[2][2]}  ")

# game time
match_case = 0
while match_case == 0:
    # user 1 input
    print_blank(blank)

    u1c = validate_inp(user_info["name1"])
    os.system('clear')
    if len(u_1_in) == 4:
        rem = u_1_in.pop(0)
        u_1_in.append(u1c)
        reset_pos(rem, mem, blank)
    else:
        u_1_in.append(u1c)
    test = result(mem, u1c, user_info["sign1"])
    if test != '':
        match_case = 1
        break

    # user 2 input
    print_blank(blank)
    u2c = validate_inp(user_info["name2"])
    os.system('clear')
    if len(u_2_in) == 4:
        rem = u_2_in.pop(0)
        u_2_in.append(u2c)
        reset_pos(rem, mem, blank)
    else:
        u_2_in.append(u2c)
    test = result(mem, u2c, user_info["sign2"])
    if test != '':
        match_case = 1

if user_info["sign1"] == test:
    print("Congratulations", end=" ")
    print(user_info["name1"], end="")
    print(". You have Won!!!")
else:
    print("Congratulations", end=" ")
    print(user_info["name2"], end="")
    print(". You have Won!!!")