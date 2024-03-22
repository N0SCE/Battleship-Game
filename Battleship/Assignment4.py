# Berkay Örene b2210356017
import sys
import copy
try:
    result = "Battle of Ships Game\n\n"
    player1_ships = sys.argv[1]
    player2_ships = sys.argv[2]
    player1_shots = sys.argv[3]
    player2_shots = sys.argv[4]
    result_file = "Battleship.out"
    
    first_file = False
    with open(player1_ships, "r") as f:
        ship_positions_data_1 = f.readlines()
        first_file = True

    second_file = False
    with open(player2_ships, "r") as f:
        ship_positions_data_2 = f.readlines()
        second_file = True

    third_file = False
    with open(player1_shots, "r") as f:
        shots_data_1 = f.read()
        third_file = True

    fourth_file = False
    with open(player2_shots, "r") as f:
        shots_data_2 = f.read()
        fourth_file = True

    alphabet = list("ABCDEFGHIJ")
    alphabet_for_table = list("ABCDEFGHIJ")
    first_ship_positions_player1 = [] # I use these lists as the table of ship position
    first_ship_positions_player2 = []
    alphabet_list = alphabet_for_table
    alphabet_list.insert(0, " ")

    to_find_ships_1 = [] # I use these lists to make a group of ships
    to_find_ships_2 = []
    # I make the tables in here
    for a in range(10):
        first_ship_positions_player1.append([a+1] + ["-"]*10)
        to_find_ships_1.append([a+1] + ["-"]*10)
    for a in range(10):
        first_ship_positions_player2.append([a+1] + ["-"]*10)
        to_find_ships_2.append([a+1] + ["-"]*10)

    # These part for creating ship position table
    for i in range(10):
        counter_for_letters = 0
        for x in range(len(ship_positions_data_1[i])):
            list(ship_positions_data_1[i])
            if ship_positions_data_1[i][x] != ";" and ship_positions_data_1[i][x] in "CBDSP":
                counter_for_letters += 1
                index = x + 2 
                index -= counter_for_letters 
                first_ship_positions_player1[i][index] = ship_positions_data_1[i][x]
                to_find_ships_1[i][index] = ship_positions_data_1[i][x]
    first_ship_positions_player1.insert(0, alphabet_list)
    to_find_ships_1.insert(0, alphabet_list)

    for i in range(10):
        counter_for_letters = 0
        for x in range(len(ship_positions_data_2[i])):
            list(ship_positions_data_2[i])
            if ship_positions_data_2[i][x] != ";" and ship_positions_data_2[i][x] in "CBDSP":
                counter_for_letters += 1           
                index = x + 2 
                index -= counter_for_letters 
                first_ship_positions_player2[i][index] = ship_positions_data_2[i][x]
                to_find_ships_2[i][index] = ship_positions_data_2[i][x]
    first_ship_positions_player2.insert(0, alphabet_list)
    to_find_ships_2.insert(0, alphabet_list)


    # This part for learning ship places. I will use them later to find if ships has been sunk or not.
    number_and_place_of_ships_1 = []
    number_and_place_of_ships_2 = []
    for line in range(1, 11):
        for element in range(1, 11):
            if element < 10:
                if to_find_ships_1[line][element] == "C" and to_find_ships_1[line][element + 1] == "C":
                    number_and_place_of_ships_1.append([f"C:{line},{alphabet[element-1]}-{alphabet[element+3]}"])
                    to_find_ships_1[line][element] = "CC"
                    for i in range(4):
                        if to_find_ships_1[line][element + i + 1] == "C":
                            to_find_ships_1[line][element + i + 1] = "CC"
                elif to_find_ships_1[line][element] == "C" and to_find_ships_1[line + 1][element] == "C":
                    number_and_place_of_ships_1.append([f"C:{line}-{line+4},{alphabet[element-1]}"])
                    to_find_ships_1[line][element] = "CC"
                    for i in range(4):
                        if to_find_ships_1[line + i + 1][element] == "C":
                            to_find_ships_1[line + i + 1][element] = "CC"
            else:
                if to_find_ships_1[line][element] == "C" and to_find_ships_1[line + 1][element] == "C":
                    number_and_place_of_ships_1.append([f"C:{line}-{line+4},{alphabet[element-1]}"])
                    to_find_ships_1[line][element] = "CC"
                    for i in range(4):
                        if to_find_ships_1[line + i + 1][element] == "C":
                            to_find_ships_1[line + i + 1][element] = "CC"

            if element < 10:                
                if to_find_ships_2[line][element] == "C" and to_find_ships_2[line][element + 1] == "C":
                    number_and_place_of_ships_2.append([f"C:{line},{alphabet[element-1]}-{alphabet[element+3]}"])
                    to_find_ships_2[line][element] = "CC"
                    for i in range(4):
                        if to_find_ships_2[line][element + i + 1] == "C":
                            to_find_ships_2[line][element + i + 1] = "CC"
                elif to_find_ships_2[line][element] == "C" and to_find_ships_2[line + 1][element] == "C":
                    number_and_place_of_ships_2.append([f"C:{line}-{line+4},{alphabet[element-1]}"])
                    to_find_ships_2[line][element] = "CC"
                    for i in range(4):  
                        if to_find_ships_2[line + i + 1][element] == "C":
                            to_find_ships_2[line + i + 1][element] = "CC"
            else:
                if to_find_ships_2[line][element] == "C" and to_find_ships_2[line + 1][element] == "C":
                    number_and_place_of_ships_2.append([f"C:{line}-{line+4},{alphabet[element-1]}"])
                    to_find_ships_2[line][element] = "CC"
                    for i in range(4):  
                        if to_find_ships_2[line + i + 1][element] == "C":
                            to_find_ships_2[line + i + 1][element] = "CC"
            

            if element < 10:
                if line < 10:
                    if to_find_ships_1[line][element] == "B" and to_find_ships_1[line][element + 1] == "B" and not to_find_ships_1[line+1][element] == "B":
                        number_and_place_of_ships_1.append([f"B:{line},{alphabet[element-1]}-{alphabet[element+2]}"])
                        to_find_ships_1[line][element] = "BB"
                        for i in range(3):
                            if to_find_ships_1[line][element + i + 1] == "B":
                                to_find_ships_1[line][element + i + 1] = "BB"
                    else:
                        if to_find_ships_1[line][element] == "B" and to_find_ships_1[line + 1][element] == "B" and not to_find_ships_1[line][element + 1] == "B":
                                    number_and_place_of_ships_1.append([f"B:{line}-{line+3},{alphabet[element-1]}"])
                                    to_find_ships_1[line][element] = "BB"
                                    for i in range(3):
                                        if to_find_ships_1[line + i + 1][element] == "B":
                                            to_find_ships_1[line + i + 1][element] = "BB"
                        else:
                            if element < 7:
                                if to_find_ships_1[line][element+4] == "B":
                                    if to_find_ships_1[line][element] == "B" and to_find_ships_1[line + 1][element] == "B" and to_find_ships_1[line + 2][element] == "B":
                                        number_and_place_of_ships_1.append([f"B:{line}-{line+3},{alphabet[element-1]}"])
                                        to_find_ships_1[line][element] = "BB"
                                        for i in range(3):
                                            if to_find_ships_1[line + i + 1][element] == "B":
                                                to_find_ships_1[line + i + 1][element] = "BB"
                            if line < 7:
                                if to_find_ships_1[line+4][element] == "B":
                                    if to_find_ships_1[line][element] == "B" and to_find_ships_1[line][element + 1] == "B": 
                                        number_and_place_of_ships_1.append([f"B:{line},{alphabet[element-1]}-{alphabet[element+2]}"])
                                        to_find_ships_1[line][element] = "BB"
                                        for i in range(3):
                                            if to_find_ships_1[line][element + i + 1] == "B":
                                                to_find_ships_1[line][element + i + 1] = "BB"
                else:
                    if to_find_ships_1[line][element] == "B" and to_find_ships_1[line][element + 1] == "B" and to_find_ships_1[line][element + 2] == "B":
                        number_and_place_of_ships_1.append([f"B:{line},{alphabet[element-1]}-{alphabet[element+2]}"])
                        to_find_ships_1[line][element] = "BB"
                        for i in range(3):
                            if to_find_ships_1[line][element + i + 1] == "B":
                                to_find_ships_1[line][element + i + 1] = "BB"

            else:
                if to_find_ships_1[line][element] == "B" and to_find_ships_1[line + 1][element] == "B" and to_find_ships_1[line + 2][element] == "B":
                    number_and_place_of_ships_1.append([f"B:{line}-{line+3},{alphabet[element-1]}"])
                    to_find_ships_1[line][element] = "BB"
                    for i in range(3):
                        if to_find_ships_1[line + i + 1][element] == "B":
                            to_find_ships_1[line + i + 1][element] = "BB"


            if element < 10:
                if line < 10:
                    if to_find_ships_2[line][element] == "B" and to_find_ships_2[line][element + 1] == "B" and not to_find_ships_2[line+1][element] == "B":
                        number_and_place_of_ships_2.append([f"B:{line},{alphabet[element-1]}-{alphabet[element+2]}"])
                        to_find_ships_2[line][element] = "BB"
                        for i in range(3):
                            if to_find_ships_2[line][element + i + 1] == "B":
                                to_find_ships_2[line][element + i + 1] = "BB"
                    else:
                        if to_find_ships_2[line][element] == "B" and to_find_ships_2[line + 1][element] == "B" and not to_find_ships_2[line][element+1] == "B":
                            number_and_place_of_ships_2.append([f"B:{line}-{line+3},{alphabet[element-1]}"])
                            to_find_ships_2[line][element] = "BB"
                            for i in range(3):
                                if to_find_ships_2[line + i + 1][element] == "B":
                                    to_find_ships_2[line + i + 1][element] = "BB"
                        else:
                            if element < 7:
                                if to_find_ships_2[line][element+4] == "B":
                                    if to_find_ships_2[line][element] == "B" and to_find_ships_2[line + 1][element] == "B" and to_find_ships_2[line + 2][element] == "B":
                                        number_and_place_of_ships_2.append([f"B:{line}-{line+3},{alphabet[element-1]}"])
                                        to_find_ships_2[line][element] = "BB"
                                        for i in range(3):
                                            if to_find_ships_2[line + i + 1][element] == "B":
                                                to_find_ships_1[line + i + 1][element] = "BB"
                            if line < 7:
                                if to_find_ships_2[line+4][element] == "B":
                                    if to_find_ships_2[line][element] == "B" and to_find_ships_2[line][element + 1] == "B": 
                                        number_and_place_of_ships_2.append([f"B:{line},{alphabet[element-1]}-{alphabet[element+2]}"])
                                        to_find_ships_2[line][element] = "BB"
                                        for i in range(3):
                                            if to_find_ships_2[line][element + i + 1] == "B":
                                                to_find_ships_2[line][element + i + 1] = "BB"
                if to_find_ships_2[line][element] == "B" and to_find_ships_2[line][element + 1] == "B" and to_find_ships_2[line][element + 2] == "B":
                        number_and_place_of_ships_2.append([f"B:{line},{alphabet[element-1]}-{alphabet[element+2]}"])
                        to_find_ships_2[line][element] = "BB"
                        for i in range(3):
                            if to_find_ships_2[line][element + i + 1] == "B":
                                to_find_ships_2[line][element + i + 1] = "BB"
            else:
                if to_find_ships_2[line][element] == "B" and to_find_ships_2[line + 1][element] == "B" and to_find_ships_2[line + 2][element] == "B":
                    number_and_place_of_ships_2.append([f"B:{line}-{line+3},{alphabet[element-1]}"])
                    to_find_ships_2[line][element] = "BB"
                    for i in range(3):
                        if to_find_ships_2[line + i + 1][element] == "B":
                            to_find_ships_2[line + i + 1][element] = "BB"



            if element < 10:
                if to_find_ships_1[line][element] == "D" and to_find_ships_1[line][element + 1] == "D":
                    number_and_place_of_ships_1.append([f"D:{line},{alphabet[element-1]}-{alphabet[element+1]}"])
                    to_find_ships_1[line][element] = "DD"
                    for i in range(2):
                        if to_find_ships_1[line][element + i + 1] == "D":
                            to_find_ships_1[line][element + i + 1] = "DD"
                elif to_find_ships_1[line][element] == "D" and to_find_ships_1[line + 1][element] == "D":
                    number_and_place_of_ships_1.append([f"D:{line}-{line+2},{alphabet[element-1]}"])
                    to_find_ships_1[line][element] = "DD"
                    for i in range(2):
                        if to_find_ships_1[line + i + 1][element] == "D":
                            to_find_ships_1[line + i + 1][element] = "DD"
            else:
                if to_find_ships_1[line][element] == "D" and to_find_ships_1[line + 1][element] == "D":
                    number_and_place_of_ships_1.append([f"D:{line}-{line+2},{alphabet[element-1]}"])
                    to_find_ships_1[line][element] = "DD"
                    for i in range(2):
                        if to_find_ships_1[line + i + 1][element] == "D":
                            to_find_ships_1[line + i + 1][element] = "DD"
                

            if element < 10:
                if to_find_ships_2[line][element] == "D" and to_find_ships_2[line][element + 1] == "D":
                    number_and_place_of_ships_2.append([f"D:{line},{alphabet[element-1]}-{alphabet[element+1]}"])
                    to_find_ships_2[line][element] = "DD"
                    for i in range(2):
                        if to_find_ships_2[line][element + i + 1] == "D":
                            to_find_ships_2[line][element + i + 1] = "DD"
                elif to_find_ships_2[line][element] == "D" and to_find_ships_2[line + 1][element] == "D":
                    number_and_place_of_ships_2.append([f"D:{line}-{line+2},{alphabet[element-1]}"])
                    to_find_ships_2[line][element] = "DD"
                    for i in range(2):
                        if to_find_ships_2[line + i + 1][element] == "D":
                            to_find_ships_2[line + i + 1][element] = "DD"

            else:
                if to_find_ships_2[line][element] == "D" and to_find_ships_2[line + 1][element] == "D":
                    number_and_place_of_ships_2.append([f"D:{line}-{line+2},{alphabet[element-1]}"])
                    to_find_ships_2[line][element] = "DD"
                    for i in range(2):
                        if to_find_ships_2[line + i + 1][element] == "D":
                            to_find_ships_2[line + i + 1][element] = "DD"



            if element < 10:
                if to_find_ships_1[line][element] == "S" and to_find_ships_1[line][element + 1] == "S":
                    number_and_place_of_ships_1.append([f"S:{line},{alphabet[element-1]}-{alphabet[element+1]}"])
                    to_find_ships_1[line][element] = "SS"
                    for i in range(2):
                        if to_find_ships_1[line][element + i + 1] == "S":
                            to_find_ships_1[line][element + i + 1] = "SS"
                elif to_find_ships_1[line][element] == "S" and to_find_ships_1[line + 1][element] == "S":
                    number_and_place_of_ships_1.append([f"S:{line}-{line+2},{alphabet[element-1]}"])
                    to_find_ships_1[line][element] = "SS"
                    for i in range(2):
                        if to_find_ships_1[line + i + 1][element] == "S":
                            to_find_ships_1[line + i + 1][element] = "SS"
            else:
                if to_find_ships_1[line][element] == "S" and to_find_ships_1[line + 1][element] == "S":
                    number_and_place_of_ships_1.append([f"S:{line}-{line+2},{alphabet[element-1]}"])
                    to_find_ships_1[line][element] = "SS"
                    for i in range(2):
                        if to_find_ships_1[line + i + 1][element] == "S":
                            to_find_ships_1[line + i + 1][element] = "SS"


            if element < 10:
                if to_find_ships_2[line][element] == "S" and to_find_ships_2[line][element + 1] == "S":
                    number_and_place_of_ships_2.append([f"S:{line},{alphabet[element-1]}-{alphabet[element+1]}"])
                    to_find_ships_2[line][element] = "SS"
                    for i in range(2):
                        if to_find_ships_2[line][element + i + 1] == "S":
                            to_find_ships_2[line][element + i + 1] = "SS"
                elif to_find_ships_2[line][element] == "S" and to_find_ships_2[line + 1][element] == "S":
                    number_and_place_of_ships_2.append([f"S:{line}-{line+2},{alphabet[element-1]}"])
                    to_find_ships_2[line][element] = "SS"
                    for i in range(2):
                        if to_find_ships_2[line + i + 1][element] == "S":
                            to_find_ships_2[line + i + 1][element] = "SS"

            else:
                if to_find_ships_2[line][element] == "S" and to_find_ships_2[line + 1][element] == "S":
                    number_and_place_of_ships_2.append([f"S:{line}-{line+2},{alphabet[element-1]}"])
                    to_find_ships_2[line][element] = "SS"
                    for i in range(2):
                        if to_find_ships_2[line + i + 1][element] == "S":
                            to_find_ships_2[line + i + 1][element] = "SS"



            if element < 10:
                boolean = True
                if element < 7:
                    if to_find_ships_1[line][element+2] == "P":
                        if to_find_ships_1[line][element] == "P" and to_find_ships_1[line + 1][element] == "P":
                            boolean = False
                            number_and_place_of_ships_1.append([f"P:{line}-{line+1},{alphabet[element-1]}"])
                            to_find_ships_1[line][element] = "PP"
                            for i in range(1):
                                if to_find_ships_1[line + i + 1][element] == "P":
                                    to_find_ships_1[line + i + 1][element] = "PP"
                    else:
                        if to_find_ships_1[line][element] == "P" and to_find_ships_1[line][element + 1] == "P" and boolean:
                            boolean = False
                            number_and_place_of_ships_1.append([f"P:{line},{alphabet[element-1]}-{alphabet[element]}"])
                            to_find_ships_1[line][element] = "PP"
                            for i in range(1):
                                if to_find_ships_1[line][element + i + 1] == "P":
                                    to_find_ships_1[line][element + i + 1] = "PP"
                if to_find_ships_1[line][element] == "P" and to_find_ships_1[line][element + 1] == "P" and boolean:
                    number_and_place_of_ships_1.append([f"P:{line},{alphabet[element-1]}-{alphabet[element]}"])
                    to_find_ships_1[line][element] = "PP"
                    for i in range(1):
                        if to_find_ships_1[line][element + i + 1] == "P":
                            to_find_ships_1[line][element + i + 1] = "PP"
                elif to_find_ships_1[line][element] == "P" and to_find_ships_1[line + 1][element] == "P" and boolean:
                    number_and_place_of_ships_1.append([f"P:{line}-{line+1},{alphabet[element-1]}"])
                    to_find_ships_1[line][element] = "PP"
                    for i in range(1):
                        if to_find_ships_1[line + i + 1][element] == "P":
                            to_find_ships_1[line + i + 1][element] = "PP"
            else:
                if to_find_ships_1[line][element] == "P" and to_find_ships_1[line + 1][element] == "P":
                    number_and_place_of_ships_1.append([f"P:{line}-{line+1},{alphabet[element-1]}"])
                    to_find_ships_1[line][element] = "PP"
                    for i in range(1):
                        if to_find_ships_1[line + i + 1][element] == "P":
                            to_find_ships_1[line + i + 1][element] = "PP"


            if element < 10:
                boolean = True
                if element < 7:
                    if to_find_ships_2[line][element+2] == "P":
                        if to_find_ships_2[line][element] == "P" and to_find_ships_2[line + 1][element] == "P":
                            boolean = False
                            number_and_place_of_ships_2.append([f"P:{line}-{line+1},{alphabet[element-1]}"])
                            to_find_ships_2[line][element] = "PP"
                            for i in range(1):
                                if to_find_ships_2[line + i + 1][element] == "P":
                                    to_find_ships_2[line + i + 1][element] = "PP"
                    else:
                        if to_find_ships_2[line][element] == "P" and to_find_ships_2[line][element + 1] == "P" and boolean:
                            boolean = False
                            number_and_place_of_ships_2.append([f"P:{line},{alphabet[element-1]}-{alphabet[element]}"])
                            to_find_ships_2[line][element] = "PP"
                            for i in range(1):
                                if to_find_ships_2[line][element + i + 1] == "P":
                                    to_find_ships_2[line][element + i + 1] = "PP"
                if to_find_ships_2[line][element] == "P" and to_find_ships_2[line][element + 1] == "P" and boolean:
                    number_and_place_of_ships_2.append([f"P:{line},{alphabet[element-1]}-{alphabet[element]}"])
                    to_find_ships_2[line][element] = "PP"
                    for i in range(1):
                        if to_find_ships_2[line][element + i + 1] == "P":
                            to_find_ships_2[line][element + i + 1] = "PP"
                elif to_find_ships_2[line][element] == "P" and to_find_ships_2[line + 1][element] == "P" and boolean:
                    number_and_place_of_ships_2.append([f"P:{line}-{line+1},{alphabet[element-1]}"])
                    to_find_ships_2[line][element] = "PP"
                    for i in range(1):
                        if to_find_ships_2[line + i + 1][element] == "P":
                            to_find_ships_2[line + i + 1][element] = "PP"

            else:
                if to_find_ships_2[line][element] == "P" and to_find_ships_2[line + 1][element] == "P":
                    number_and_place_of_ships_2.append([f"P:{line}-{line+1},{alphabet[element-1]}"])
                    to_find_ships_2[line][element] = "PP"
                    for i in range(1):
                        if to_find_ships_2[line + i + 1][element] == "P":
                            to_find_ships_2[line + i + 1][element] = "PP"

    # These lists for showing tables to users every round
    hidden_board_player1 = []
    hidden_board_player2 = []
    for a in range(10):
        hidden_board_player1.append([a+1] + ["-"]*10)
    for a in range(10):
        hidden_board_player2.append([a+1] + ["-"]*10)

    hidden_board_player1.insert(0, alphabet_for_table)
    hidden_board_player2.insert(0, alphabet_for_table)

    shot_positions_1 = shots_data_1.split(";")[:-1]
    shot_positions_2 = shots_data_2.split(";")[:-1]
    total_round_number = 0
    if len(shot_positions_1) >=  len(shot_positions_2):
        total_round_number = len(shot_positions_1)
    elif len(shot_positions_2) >=  len(shot_positions_1):
        total_round_number = len(shot_positions_2)

    # These lists for showing the non hidden board at last
    non_hidden_board_player1 = copy.deepcopy(first_ship_positions_player1)
    non_hidden_board_player2 = copy.deepcopy(first_ship_positions_player2)


   
    wrong_rounds = 0
    
    print("Battle of Ships Game\n\n")
    # These variables for learning if ships have been sunk or not
    counter_of_getting_shot_1 = 0
    counter_of_getting_shot_2 = 0
    counter_of_getting_shot_C_1 = 0 
    counter_of_getting_shot_C_2 = 0
    counter_of_getting_shot_D_1 = 0 
    counter_of_getting_shot_D_2 = 0
    counter_of_getting_shot_S_1 = 0 
    counter_of_getting_shot_S_2 = 0

    for i in range(total_round_number):
        
        current_result_table = ""
        non_hidden_result = ""
        i += wrong_rounds 
        round_counter = i - wrong_rounds + 1 
        if i == total_round_number: 
            break

        current_result_table += f"Player1's Move\n\nRound : {round_counter}\t\t\t\t\tGrid Size: 10x10\n\nPlayer1's Hidden Board\t\tPlayer2's Hidden Board\n"



        # These parts for printing tables
        for line in range(11):        
            for element in range(11):
                if line==10 and element == 0:
                    current_result_table += str(hidden_board_player1[line][element])
                elif element == 10:
                    current_result_table += str(non_hidden_board_player1[line][element])
                else:
                    current_result_table += str(hidden_board_player1[line][element]) + " "  
            
            current_result_table += "\t\t" 

            for element in range(11):
                if line==10 and element == 0:
                    current_result_table += str(hidden_board_player2[line][element])
                elif element == 10:
                    current_result_table += str(hidden_board_player2[line][element])
                else:
                    current_result_table += str(hidden_board_player2[line][element]) + " "
            current_result_table += "\n"
        current_result_table += "\n"
      
        # These parts for printing the ships
        if counter_of_getting_shot_C_1 == 5:
            current_result_table += "Carrier\t\tX\t\t\t\t"
        else:
            current_result_table += "Carrier\t\t-\t\t\t\t"
        if counter_of_getting_shot_C_2 == 5:
            current_result_table += "Carrier\t\tX\n"
        else:
            current_result_table += "Carrier\t\t-\n"

        counter_of_getting_shot_B_list_1 = []
        for x in range(len(number_and_place_of_ships_1)):
            counter_of_getting_shot_B_1 = 0
            if number_and_place_of_ships_1[x][0].split(":")[0] == "B":
                if len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships
                    start, end = number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0].split("-")
                    column = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]) + 1                   
                    for l in range(int(start), int(end) + 1):               
                        if hidden_board_player1[l][column] == "X":                                                    
                            counter_of_getting_shot_B_1 += 1
                    if counter_of_getting_shot_B_1 == 4:
                        counter_of_getting_shot_B_list_1.append(1)                   
                else:
                    vertical_line = int(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0])
                    column_start, column_end = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                    for c in range(column_start, column_end + 1):
                        if hidden_board_player1[vertical_line][c] == "X":                                                    
                            counter_of_getting_shot_B_1 += 1                            
                    if counter_of_getting_shot_B_1 == 4:                        
                        counter_of_getting_shot_B_list_1.append(1)

        counter_of_getting_shot_B_list_2 = []
        for x in range(len(number_and_place_of_ships_2)):
            counter_of_getting_shot_B_2 = 0
            if number_and_place_of_ships_2[x][0].split(":")[0] == "B":
                if len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships
                    start, end = number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0].split("-")
                    column = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]) + 1                   
                    for l in range(int(start), int(end) + 1):               
                        if hidden_board_player2[l][column] == "X":                                                    
                            counter_of_getting_shot_B_2 += 1
                    if counter_of_getting_shot_B_2 == 4:
                        counter_of_getting_shot_B_list_2.append(1)                   
                else:
                    vertical_line = int(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0])
                    column_start, column_end = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                    for c in range(column_start, column_end + 1):
                        if hidden_board_player2[vertical_line][c] == "X":                                                    
                            counter_of_getting_shot_B_2 += 1                            
                    if counter_of_getting_shot_B_2 == 4:                        
                        counter_of_getting_shot_B_list_2.append(1)

        if len(counter_of_getting_shot_B_list_1) == 2:
            current_result_table += "Battleship\tX X\t\t\t\t"
        elif len(counter_of_getting_shot_B_list_1) == 1:
            current_result_table += "Battleship\tX -\t\t\t\t"
        else:
            current_result_table += "Battleship\t- -\t\t\t\t"
        if len(counter_of_getting_shot_B_list_2) == 2:
            current_result_table += "Battleship\tX X\n"
        elif len(counter_of_getting_shot_B_list_2) == 1:
            current_result_table += "Battleship\tX -\n"
        else:
            current_result_table += "Battleship\t- -\n"
        if counter_of_getting_shot_D_1 == 3:
            current_result_table += "Destroyer\tX\t\t\t\t"
        else:
            current_result_table += "Destroyer\t-\t\t\t\t"
        if counter_of_getting_shot_D_2 == 3:
            current_result_table += "Destroyer\tX\n"
        else:
            current_result_table += "Destroyer\t-\n" 
        if counter_of_getting_shot_S_1 == 3:
            current_result_table += "Submarine\tX\t\t\t\t"
        else:
            current_result_table += "Submarine\t-\t\t\t\t"
        if counter_of_getting_shot_S_2 == 3:
            current_result_table += "Submarine\tX\n"
        else:
            current_result_table += "Submarine\t-\n"

        
        counter_of_getting_shot_P_list_1 = []
        for x in range(len(number_and_place_of_ships_1)):
            counter_of_getting_shot_P_1 = 0
            if number_and_place_of_ships_1[x][0].split(":")[0] == "P":
                if len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships
                    start, end = number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0].split("-")
                    column = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]) + 1                   
                    for l in range(int(start), int(end) + 1):               
                        if hidden_board_player1[l][column] == "X":                                                    
                            counter_of_getting_shot_P_1 += 1
                    if counter_of_getting_shot_P_1 == 2:
                        counter_of_getting_shot_P_list_1.append(1)                   
                else:
                    vertical_line = int(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0])
                    column_start, column_end = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                    for c in range(column_start, column_end + 1):
                        if hidden_board_player1[vertical_line][c] == "X":                                                    
                            counter_of_getting_shot_P_1 += 1                            
                    if counter_of_getting_shot_P_1 == 2:                        
                        counter_of_getting_shot_P_list_1.append(1)

        counter_of_getting_shot_P_list_2 = []
        for x in range(len(number_and_place_of_ships_2)):
            counter_of_getting_shot_P_2 = 0
            if number_and_place_of_ships_2[x][0].split(":")[0] == "P":
                if len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships                 
                    start, end = number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0].split("-")
                    column = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]) + 1                                  
                    for l in range(int(start), int(end) + 1):               
                        if hidden_board_player2[l][column] == "X":                                                    
                            counter_of_getting_shot_P_2 += 1
                    if counter_of_getting_shot_P_2 == 2:
                        counter_of_getting_shot_P_list_2.append(1)                   
                else:                    
                    vertical_line = int(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0])
                    column_start, column_end = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                    for c in range(column_start, column_end + 1):
                        if hidden_board_player2[vertical_line][c] == "X":                                                    
                            counter_of_getting_shot_P_2 += 1                            
                    if counter_of_getting_shot_P_2 == 2:                        
                        counter_of_getting_shot_P_list_2.append(1)
                    
        if len(counter_of_getting_shot_P_list_1) == 4:
            current_result_table += "Patrol Boat\tX X X X\t\t\t"
        elif len(counter_of_getting_shot_P_list_1) == 3:
            current_result_table += "Patrol Boat\tX X X -\t\t\t"
        elif len(counter_of_getting_shot_P_list_1) == 2:
            current_result_table += "Patrol Boat\tX X - -\t\t\t"
        elif len(counter_of_getting_shot_P_list_1) == 1:
            current_result_table += "Patrol Boat\tX - - -\t\t\t"
        else:
            current_result_table += "Patrol Boat\t- - - -\t\t\t"
        if len(counter_of_getting_shot_P_list_2) == 4:
            current_result_table += "Patrol Boat\tX X X X\n\n"
        elif len(counter_of_getting_shot_P_list_2) == 3:
            current_result_table += "Patrol Boat\tX X X -\n\n"
        elif len(counter_of_getting_shot_P_list_2) == 2:
            current_result_table += "Patrol Boat\tX X - -\n\n"
        elif len(counter_of_getting_shot_P_list_2) == 1:
            current_result_table += "Patrol Boat\tX - - -\n\n"
        else:
            current_result_table += "Patrol Boat\t- - - -\n\n"
        

        try:
            # This part for player1 to make the shot
            boolean1 = True           
            def shot1():
                if len(shot_positions_1[i].split(",")) > 2:
                    raise ValueError        
                global first_index_1
                global second_index_1
                first_index_1 = True
                global shot_row_index
                shot_row_index  = int(shot_positions_1[i].split(",")[0])               
                first_index_1 = False               
                second_index_1 = True
                global shot_column_index_letter
                shot_column_index_letter = shot_positions_1[i].split(",")[1]
                assert 1<=shot_row_index<=10
                assert shot_column_index_letter in alphabet
                shot_column_index = alphabet.index(shot_positions_1[i].split(",")[1]) + 1
                second_index_1 = False
                global shot_row_index_printing
                shot_row_index_printing = shot_positions_1[i].split(",")[0] + "," + shot_positions_1[i].split(",")[1]
                if first_ship_positions_player2[shot_row_index][shot_column_index] == "-":
                    hidden_board_player2[shot_row_index][shot_column_index] = "O"
                    non_hidden_board_player2[shot_row_index][shot_column_index] = "O"
                else:
                    if first_ship_positions_player2[shot_row_index][shot_column_index] == "C":
                        global counter_of_getting_shot_C_2
                        counter_of_getting_shot_C_2 = counter_of_getting_shot_C_2 + 1
                    if first_ship_positions_player2[shot_row_index][shot_column_index] == "D":
                        global counter_of_getting_shot_D_2
                        counter_of_getting_shot_D_2 = counter_of_getting_shot_D_2 + 1    
                    if first_ship_positions_player2[shot_row_index][shot_column_index] == "S":
                        global counter_of_getting_shot_S_2
                        counter_of_getting_shot_S_2 = counter_of_getting_shot_S_2 + 1
                    hidden_board_player2[shot_row_index][shot_column_index] = "X"
                    non_hidden_board_player2[shot_row_index][shot_column_index] = "X"
                    global counter_of_getting_shot_2
                    counter_of_getting_shot_2 = counter_of_getting_shot_2 + 1
            if boolean1:
                shot1()
        except IndexError:
            boolean1 = False
            wrong_rounds += 1
            i += 1
            if first_index_1:             
                current_result_table += "IndexError: There is no first index of the input\n\n"
            if second_index_1:               
                current_result_table += "IndexError: There is no second index of the input\n\n"
            shot1()
        except ValueError:
            boolean1 = False
            wrong_rounds += 1
            i += 1
            if first_index_1:
                current_result_table += "ValueError: First index of the input is not valid\n\n"
            if second_index_1:
                current_result_table += "ValueError: First index of the input is not valid\n\n"
            shot1()
        except AssertionError:
            boolean1 = False
            wrong_rounds += 1
            i += 1
            current_result_table += f"Enter your move : {shot_row_index},{shot_column_index_letter}\n"
            current_result_table += "AssertionError: Invalid Operation.\n"
            shot1()
        except:
            current_result_table += "kaBOOM: Run for your life!\n\n"
        current_result_table += f"Enter your move: {shot_row_index_printing}\n\n"

    
        current_result_table += f"Player2's Move\n\nRound : {round_counter}\t\t\t\t\tGrid Size: 10x10\n\nPlayer1's Hidden Board\t\tPlayer2's Hidden Board\n"

        for line in range(11):        
            for element in range(11):
            
                if line==10 and element == 0:
                    current_result_table += str(hidden_board_player1[line][element])
                elif element == 10:
                    current_result_table += str(hidden_board_player1[line][element])
                else:
                    current_result_table += str(hidden_board_player1[line][element]) + " " 

            current_result_table += "\t\t" #current_result_table += " "*7


            for element in range(11):
                if line==10 and element == 0:
                    current_result_table += str(hidden_board_player2[line][element])
                elif element == 10:
                    current_result_table += str(hidden_board_player1[line][element])
                else:
                    current_result_table += str(hidden_board_player2[line][element]) + " "
            current_result_table += "\n"
        current_result_table += "\n"

        # this part prints the ships
        if counter_of_getting_shot_C_1 == 5:
            current_result_table += "Carrier\t\tX\t\t\t\t"
        else:
            current_result_table += "Carrier\t\t-\t\t\t\t"
        if counter_of_getting_shot_C_2 == 5:
            current_result_table += "Carrier\t\tX\n"
        else:
            current_result_table += "Carrier\t\t-\n"

        counter_of_getting_shot_B_list_1 = []
        for x in range(len(number_and_place_of_ships_1)):
            counter_of_getting_shot_B_1 = 0
            if number_and_place_of_ships_1[x][0].split(":")[0] == "B":
                if len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships
                    start, end = number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0].split("-")
                    column = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]) + 1                   
                    for l in range(int(start), int(end) + 1):               
                        if hidden_board_player1[l][column] == "X":                                                    
                            counter_of_getting_shot_B_1 += 1
                    if counter_of_getting_shot_B_1 == 4:
                        counter_of_getting_shot_B_list_1.append(1)                   
                else:
                    vertical_line = int(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0])
                    column_start, column_end = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                    for c in range(column_start, column_end + 1):
                        if hidden_board_player1[vertical_line][c] == "X":                                                    
                            counter_of_getting_shot_B_1 += 1                            
                    if counter_of_getting_shot_B_1 == 4:                        
                        counter_of_getting_shot_B_list_1.append(1)

        counter_of_getting_shot_B_list_2 = []
        for x in range(len(number_and_place_of_ships_2)):
            counter_of_getting_shot_B_2 = 0
            if number_and_place_of_ships_2[x][0].split(":")[0] == "B":
                if len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships
                    start, end = number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0].split("-")
                    column = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]) + 1                   
                    for l in range(int(start), int(end) + 1):               
                        if hidden_board_player2[l][column] == "X":                                                    
                            counter_of_getting_shot_B_2 += 1
                    if counter_of_getting_shot_B_2 == 4:
                        counter_of_getting_shot_B_list_2.append(1)                   
                else:
                    vertical_line = int(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0])
                    column_start, column_end = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                    for c in range(column_start, column_end + 1):
                        if hidden_board_player2[vertical_line][c] == "X":                                                    
                            counter_of_getting_shot_B_2 += 1                            
                    if counter_of_getting_shot_B_2 == 4:                        
                        counter_of_getting_shot_B_list_2.append(1)

        if len(counter_of_getting_shot_B_list_1) == 2:
            current_result_table += "Battleship\tX X\t\t\t\t"
        elif len(counter_of_getting_shot_B_list_1) == 1:
            current_result_table += "Battleship\tX -\t\t\t\t"
        else:
            current_result_table += "Battleship\t- -\t\t\t\t"
        if len(counter_of_getting_shot_B_list_2) == 2:
            current_result_table += "Battleship\tX X\n"
        elif len(counter_of_getting_shot_B_list_2) == 1:
            current_result_table += "Battleship\tX -\n"
        else:
            current_result_table += "Battleship\t- -\n"
        if counter_of_getting_shot_D_1 == 3:
            current_result_table += "Destroyer\tX\t\t\t\t"
        else:
            current_result_table += "Destroyer\t-\t\t\t\t"
        if counter_of_getting_shot_D_2 == 3:
            current_result_table += "Destroyer\tX\n"
        else:
            current_result_table += "Destroyer\t-\n" 
        if counter_of_getting_shot_S_1 == 3:
            current_result_table += "Submarine\tX\t\t\t\t"
        else:
            current_result_table += "Submarine\t-\t\t\t\t"
        if counter_of_getting_shot_S_2 == 3:
            current_result_table += "Submarine\tX\n"
        else:
            current_result_table += "Submarine\t-\n"
        
        
        counter_of_getting_shot_P_list_1 = []
        for x in range(len(number_and_place_of_ships_1)):
            counter_of_getting_shot_P_1 = 0
            if number_and_place_of_ships_1[x][0].split(":")[0] == "P":
                if len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships
                    start, end = number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0].split("-")
                    column = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]) + 1                   
                    for l in range(int(start), int(end) + 1):               
                        if hidden_board_player1[l][column] == "X":                                                    
                            counter_of_getting_shot_P_1 += 1
                    if counter_of_getting_shot_P_1 == 2:
                        counter_of_getting_shot_P_list_1.append(1)                   
                else:
                    vertical_line = int(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0])
                    column_start, column_end = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                    for c in range(column_start, column_end + 1):
                        if hidden_board_player1[vertical_line][c] == "X":                                                    
                            counter_of_getting_shot_P_1 += 1                            
                    if counter_of_getting_shot_P_1 == 2:                        
                        counter_of_getting_shot_P_list_1.append(1)

        counter_of_getting_shot_P_list_2 = []
        for x in range(len(number_and_place_of_ships_2)):
            counter_of_getting_shot_P_2 = 0
            if number_and_place_of_ships_2[x][0].split(":")[0] == "P":
                if len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships                 
                    start, end = number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0].split("-")
                    column = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]) + 1                                  
                    for l in range(int(start), int(end) + 1):               
                        if hidden_board_player2[l][column] == "X":                                                    
                            counter_of_getting_shot_P_2 += 1
                    if counter_of_getting_shot_P_2 == 2:
                        counter_of_getting_shot_P_list_2.append(1)                   
                else:                    
                    vertical_line = int(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0])
                    column_start, column_end = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                    for c in range(column_start, column_end + 1):
                        if hidden_board_player2[vertical_line][c] == "X":                                                    
                            counter_of_getting_shot_P_2 += 1                            
                    if counter_of_getting_shot_P_2 == 2:                        
                        counter_of_getting_shot_P_list_2.append(1)
                    
        if len(counter_of_getting_shot_P_list_1) == 4:
            current_result_table += "Patrol Boat\tX X X X\t\t\t"
        elif len(counter_of_getting_shot_P_list_1) == 3:
            current_result_table += "Patrol Boat\tX X X -\t\t\t"
        elif len(counter_of_getting_shot_P_list_1) == 2:
            current_result_table += "Patrol Boat\tX X - -\t\t\t"
        elif len(counter_of_getting_shot_P_list_1) == 1:
            current_result_table += "Patrol Boat\tX - - -\t\t\t"
        else:
            current_result_table += "Patrol Boat\t- - - -\t\t\t"
        if len(counter_of_getting_shot_P_list_2) == 4:
            current_result_table += "Patrol Boat\tX X X X\n\n"
        elif len(counter_of_getting_shot_P_list_2) == 3:
            current_result_table += "Patrol Boat\tX X X -\n\n"
        elif len(counter_of_getting_shot_P_list_2) == 2:
            current_result_table += "Patrol Boat\tX X - -\n\n"
        elif len(counter_of_getting_shot_P_list_2) == 1:
            current_result_table += "Patrol Boat\tX - - -\n\n"
        else:
            current_result_table += "Patrol Boat\t- - - -\n\n"

        try:
            # This part for player2 to make the shot
            boolean2 = True
            def shot2():        
                if len(shot_positions_2[i].split(",")) > 2:
                    raise ValueError
                global first_index_2
                global second_index_2
                first_index_2 = True
                global shot_row_index
                shot_row_index  = int(shot_positions_2[i].split(",")[0])
                first_index_2 = False
                second_index_2 = True
                assert 1<= shot_row_index <=10
                global shot_column_index_letter
                shot_column_index_letter = shot_positions_2[i].split(",")[1]
                assert shot_column_index_letter in alphabet
                shot_column_index = alphabet.index(shot_positions_2[i].split(",")[1]) + 1
                second_index_2 = False
                global shot_row_index_printing
                shot_row_index_printing = shot_positions_2[i].split(",")[0] + "," + shot_positions_2[i].split(",")[1]
                if first_ship_positions_player1[shot_row_index][shot_column_index] == "-":
                    hidden_board_player1[shot_row_index][shot_column_index] = "O"
                    non_hidden_board_player1[shot_row_index][shot_column_index] = "O"
                else:
                    if first_ship_positions_player1[shot_row_index][shot_column_index] == "C":
                        global counter_of_getting_shot_C_1
                        counter_of_getting_shot_C_1 = counter_of_getting_shot_C_1 + 1
                    if first_ship_positions_player1[shot_row_index][shot_column_index] == "D":
                        global counter_of_getting_shot_D_1
                        counter_of_getting_shot_D_1 = counter_of_getting_shot_D_1 + 1    
                    if first_ship_positions_player1[shot_row_index][shot_column_index] == "S":
                        global counter_of_getting_shot_S_1
                        counter_of_getting_shot_S_1 = counter_of_getting_shot_S_1 + 1
                    hidden_board_player1[shot_row_index][shot_column_index] = "X"
                    non_hidden_board_player1[shot_row_index][shot_column_index] = "X"
                    global counter_of_getting_shot_1
                    counter_of_getting_shot_1 = counter_of_getting_shot_1 + 1
            if boolean2:
                shot2()
        except IndexError:
            boolean2 = False
            wrong_rounds += 1
            i += 1
            if first_index_2:
                print(f"IndexError: There is no first index of the input")
                current_result_table += "IndexError: There is no first index of the input\n\n"
            if second_index_2:
                print(f"IndexError: There is no second index of the input")
                current_result_table += "IndexError: There is no second index of the input\n\n"
            shot2()
        except ValueError:
            boolean2 = False
            wrong_rounds += 1
            i += 1
            if first_index_2:
                current_result_table += "ValueError: First index of the input is not valid\n\n"
            if second_index_2:
                current_result_table += "ValueError: Second index of the input is not valid\n\n"
            shot2()
        except AssertionError:
            boolean2 = False
            wrong_rounds += 1
            i += 1
            current_result_table += f"Enter your move: {shot_row_index},{shot_column_index_letter}\n"
            current_result_table += "AssertionError: Invalid Operation\n"
            shot2()
        except:
            current_result_table += "kaBOOM: Run for your life!\n\n"
               
        current_result_table += f"Enter your move: {shot_row_index_printing}\n\n" 

        
        
        # it is looking for who won
        is_finished = False
        if counter_of_getting_shot_1 == 27 and counter_of_getting_shot_2 == 27: # draw
            is_finished = True          
            non_hidden_result += "It is a Draw!\n\nFinal Information\n\n"
        elif counter_of_getting_shot_1 == 27 and not counter_of_getting_shot_2 == 27:
            is_finished = True
            non_hidden_result += "Player'2 Wins!\n\nFinal Information\n\n"                       
        elif counter_of_getting_shot_2 == 27 and not counter_of_getting_shot_1 == 27:
            is_finished = True         
            non_hidden_result += "Player'1 Wins!\n\nFinal Information\n\n"

        # if it is finished i make the final result table
        if is_finished:
            non_hidden_result += "Player1's Board\t\t\t\tPlayer2's Board\n"
            for line in range(11):        
                for element in range(11):
                
                    if line==10 and element == 0:
                        non_hidden_result += str(non_hidden_board_player1[line][element])
                    elif element == 10:
                        non_hidden_result += str(non_hidden_board_player1[line][element])
                    else:
                        non_hidden_result += str(non_hidden_board_player1[line][element]) + " " 

                non_hidden_result += "\t\t"


                for element in range(11):
                    if line==10 and element == 0:
                        non_hidden_result += str(non_hidden_board_player2[line][element])
                    elif element == 10:
                        non_hidden_result += str(non_hidden_board_player1[line][element])
                    else:
                        non_hidden_result += str(non_hidden_board_player2[line][element]) + " "
                non_hidden_result += "\n"
            non_hidden_result += "\n"
        
            
            if counter_of_getting_shot_C_1 == 5:
                non_hidden_result += "Carrier\t\tX\t\t\t\t"
            else:
                non_hidden_result += "Carrier\t\t-\t\t\t\t"
            if counter_of_getting_shot_C_2 == 5:
                non_hidden_result += "Carrier\t\tX\n"
            else:
                non_hidden_result += "Carrier\t\t-\n"

            counter_of_getting_shot_B_list_1 = []
            for x in range(len(number_and_place_of_ships_1)):
                counter_of_getting_shot_B_1 = 0
                if number_and_place_of_ships_1[x][0].split(":")[0] == "B":
                    if len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships
                        start, end = number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0].split("-")
                        column = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]) + 1                   
                        for l in range(int(start), int(end) + 1):               
                            if hidden_board_player1[l][column] == "X":                                                    
                                counter_of_getting_shot_B_1 += 1
                        if counter_of_getting_shot_B_1 == 4:
                            counter_of_getting_shot_B_list_1.append(1)                   
                    else:
                        vertical_line = int(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0])
                        column_start, column_end = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                        for c in range(column_start, column_end + 1):
                            if hidden_board_player1[vertical_line][c] == "X":                                                    
                                counter_of_getting_shot_B_1 += 1                            
                        if counter_of_getting_shot_B_1 == 4:                        
                            counter_of_getting_shot_B_list_1.append(1)

            counter_of_getting_shot_B_list_2 = []
            for x in range(len(number_and_place_of_ships_2)):
                counter_of_getting_shot_B_2 = 0
                if number_and_place_of_ships_2[x][0].split(":")[0] == "B":
                    if len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships
                        start, end = number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0].split("-")
                        column = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]) + 1                   
                        for l in range(int(start), int(end) + 1):               
                            if hidden_board_player2[l][column] == "X":                                                    
                                counter_of_getting_shot_B_2 += 1
                        if counter_of_getting_shot_B_2 == 4:
                            counter_of_getting_shot_B_list_2.append(1)                   
                    else:
                        vertical_line = int(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0])
                        column_start, column_end = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                        for c in range(column_start, column_end + 1):
                            if hidden_board_player2[vertical_line][c] == "X":                                                    
                                counter_of_getting_shot_B_2 += 1                            
                        if counter_of_getting_shot_B_2 == 4:                        
                            counter_of_getting_shot_B_list_2.append(1)

            # it is for showing ships
            if len(counter_of_getting_shot_B_list_1) == 2:
                non_hidden_result += "Battleship\tX X\t\t\t\t"
            elif len(counter_of_getting_shot_B_list_1) == 1:
                non_hidden_result += "Battleship\tX -\t\t\t\t"
            else:
                non_hidden_result += "Battleship\t- -\t\t\t\t"
            if len(counter_of_getting_shot_B_list_2) == 2:
                non_hidden_result += "Battleship\tX X\n"
            elif len(counter_of_getting_shot_B_list_2) == 1:
                non_hidden_result += "Battleship\tX -\n"
            else:
                non_hidden_result += "Battleship\t- -\n"
            if counter_of_getting_shot_D_1 == 3:
                non_hidden_result += "Destroyer\tX\t\t\t\t"
            else:
                non_hidden_result += "Destroyer\t-\t\t\t\t"
            if counter_of_getting_shot_D_2 == 3:
                non_hidden_result += "Destroyer\tX\n"
            else:
                non_hidden_result += "Destroyer\t-\n" 
            if counter_of_getting_shot_S_1 == 3:
                non_hidden_result += "Submarine\tX\t\t\t\t"
            else:
                non_hidden_result += "Submarine\t-\t\t\t\t"
            if counter_of_getting_shot_S_2 == 3:
                non_hidden_result += "Submarine\tX\n"
            else:
                non_hidden_result += "Submarine\t-\n"
            
            
            counter_of_getting_shot_P_list_1 = []
            for x in range(len(number_and_place_of_ships_1)):
                counter_of_getting_shot_P_1 = 0
                if number_and_place_of_ships_1[x][0].split(":")[0] == "P":
                    if len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships
                        start, end = number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0].split("-")
                        column = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1]) + 1                   
                        for l in range(int(start), int(end) + 1):               
                            if hidden_board_player1[l][column] == "X":                                                    
                                counter_of_getting_shot_P_1 += 1
                        if counter_of_getting_shot_P_1 == 2:
                            counter_of_getting_shot_P_list_1.append(1)                   
                    else:
                        vertical_line = int(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[0])
                        column_start, column_end = alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_1[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                        for c in range(column_start, column_end + 1):
                            if hidden_board_player1[vertical_line][c] == "X":                                                    
                                counter_of_getting_shot_P_1 += 1                            
                        if counter_of_getting_shot_P_1 == 2:                        
                            counter_of_getting_shot_P_list_1.append(1)

            counter_of_getting_shot_P_list_2 = []
            for x in range(len(number_and_place_of_ships_2)):
                counter_of_getting_shot_P_2 = 0
                if number_and_place_of_ships_2[x][0].split(":")[0] == "P":
                    if len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0]) > len(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]): # it means you are looking for vertical ships                 
                        start, end = number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0].split("-")
                        column = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1]) + 1                                  
                        for l in range(int(start), int(end) + 1):               
                            if hidden_board_player2[l][column] == "X":                                                    
                                counter_of_getting_shot_P_2 += 1
                        if counter_of_getting_shot_P_2 == 2:
                            counter_of_getting_shot_P_list_2.append(1)                   
                    else:                    
                        vertical_line = int(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[0])
                        column_start, column_end = alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1].split("-")[0]) + 1, alphabet.index(number_and_place_of_ships_2[x][0].split(":")[1].split(",")[1].split("-")[1]) + 1
                        for c in range(column_start, column_end + 1):
                            if hidden_board_player2[vertical_line][c] == "X":                                                    
                                counter_of_getting_shot_P_2 += 1                            
                        if counter_of_getting_shot_P_2 == 2:                        
                            counter_of_getting_shot_P_list_2.append(1)
                         
            
            if len(counter_of_getting_shot_P_list_1) == 4:
                non_hidden_result += "Patrol Boat\tX X X X\t\t\t"
            elif len(counter_of_getting_shot_P_list_1) == 3:
                non_hidden_result += "Patrol Boat\tX X X -\t\t\t"
            elif len(counter_of_getting_shot_P_list_1) == 2:
                non_hidden_result += "Patrol Boat\tX X - -\t\t\t"
            elif len(counter_of_getting_shot_P_list_1) == 1:
                non_hidden_result += "Patrol Boat\tX - - -\t\t\t"
            else:
                non_hidden_result += "Patrol Boat\t- - - -\t\t\t"
            if len(counter_of_getting_shot_P_list_2) == 4:
                non_hidden_result += "Patrol Boat\tX X X X\n\n"
            elif len(counter_of_getting_shot_P_list_2) == 3:
                non_hidden_result += "Patrol Boat\tX X X -\n\n"
            elif len(counter_of_getting_shot_P_list_2) == 2:
                non_hidden_result += "Patrol Boat\tX X - -\n\n"
            elif len(counter_of_getting_shot_P_list_2) == 1:
                non_hidden_result += "Patrol Boat\tX - - -\n\n"
            else:
                non_hidden_result += "Patrol Boat\t- - - -\n\n"

        result += current_result_table
        print(current_result_table)
        
        if is_finished:
            print(non_hidden_result)
            result += non_hidden_result
        if counter_of_getting_shot_1 == 27 or counter_of_getting_shot_2 == 27: # it means game is over because all the ships have been sunk.
            break


# This part for handling IO errors.
except IOError:
    if not first_file:
        print(f"IOError: input file {player1_ships} is not reachable.")
        result += f"IOError: input file {player1_ships} is not reachable."
    elif not second_file:
        print(f"IOError: input file {player2_ships} is not reachable.")
        result += f"IOError: input file {player2_ships} is not reachable."
    elif not third_file:
        print(f"IOError: input file {player1_shots} is not reachable.")
        result += f"IOError: input file {player1_shots} is not reachable."
    elif not fourth_file:
        print(f"IOError: input file {player2_shots} is not reachable.")
        result += f"IOError: input file {player2_shots} is not reachable."

except:
    print("kaBOOM: run for your life!")
    result += "kaBOOM: run for your life!"
    
try:
    # This part for writing final result
    def write():
        with open(result_file, "w") as f:
            f.write(result)
    write()
except:
    pass