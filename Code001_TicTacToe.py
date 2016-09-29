'''
Design a Tic Tac Toe game.
'''
from random import randint

def draw_graph(graph,symbol=None,position=None):
    if position:
        graph[position-1] = symbol
    print " " + graph[6] + " | " + graph[7] + " | " + graph[8] + " "
    print "---|---|---"
    print " " + graph[3] + " | " + graph[4] + " | " + graph[5] + " "
    print "---|---|---"
    print " " + graph[0] + " | " + graph[1] + " | " + graph[2] + " "
    print "---|---|---"
    return graph

def first_player():
    nos = randint(0,1)
    first = ""
    second = ""
    if nos == 0 :
        first = "Player"
        second = "Computer"
    elif nos ==1 :
        first = "Computer"
        second = "Player"
    return first,second


def play_player():
    pass


def play_computer():
    pass


def is_winner():
    pass


def is_full():
    pass

graph = [' ']*10
import pdb;pdb.set_trace()
print ("##########TIC-TAC-TOE##########")
symbol = input("Select your symbol 'X' or 'O'")
player_symbol = ""
computer_symbol = ""
if symbol == "X":
    player_symbol = symbol
    computer_symbol = "O"
elif symbol == "O":
    player_symbol = symbol
    computer_symbol = "X"
graph = draw_graph(graph)
print("##########GAME START##########")
first,second = first_player()
print ("The first player is %s and the second player is %s."%(first,second))
count = 0
graph_is_full = False
while(graph_is_full==False):
    if (count%2 == 0 ):
        if first == "Player":
            play_player()
        elif first == "Computer":
            play_computer()
        if is_winner():
            break
    elif (count%2 == 1):
        if second == "Player":
            play_player()
        elif second == "Computer":
            play_computer()
        if is_winner():
            break

    count += 1
    if is_full():
        graph_is_full = True
        print ("Tough match but it's a TIE.")