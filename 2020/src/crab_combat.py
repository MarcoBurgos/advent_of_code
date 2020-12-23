import copy
import hashlib
from utils import read_and_load_input

prev_decks = dict()

def generate_decks(input_data):
    players = []
    deck = []
    for line in input_data:
        if line.startswith("Player"):
            key = line[0:-1]
        elif line.isdigit():
            deck.append(int(line))
        elif len(line) == 0:
            players_deck = copy.deepcopy(deck)
            deck.clear()
            players.append(players_deck)
    players_deck = copy.deepcopy(deck)
    deck.clear()
    players.append(players_deck)
    return players

def play_game(players):
    player_1 = players[0]
    player_2 = players[1]

    while (len(player_1) > 0) and (len(player_2) > 0):
        p1_card = player_1.pop(0)
        p2_card = player_2.pop(0)


        if p1_card > p2_card:
            player_1.append(p1_card)
            player_1.append(p2_card)
        else:
            player_2.append(p2_card)
            player_2.append(p1_card)

        # print(f"P1 {player_1} P2 {player_2}")

    if len(player_1) > len(player_2):
        winner = player_1
    else:
        winner = player_2

    return winner

def play_game_2(players, game):
    decks_string = ''.join([str(card) for player in players for card in player])
    deck_hash = hashlib.md5(decks_string.encode()).hexdigest()

    if deck_hash in prev_decks:
        print(f"round {round}")
        winner = player_1
        return winner
    else:
        player_1 = players[0]
        player_2 = players[1]
        round = 1
        print(f"=== Game {game} ===")
        while (len(player_1) > 0) and (len(player_2) > 0):
            print(f"-- Round {round} (Game {game}) --")
            print(f"Player 1's deck: {player_1}")
            print(f"Player 2's deck: {player_2}")
            p1_card = player_1.pop(0)
            p2_card = player_2.pop(0)
            print(f"Player 1 plays: {p1_card}")
            print(f"Player 2 plays: {p2_card}")

            if len(player_1) >= p1_card and len(player_2) >= p2_card:
                print(f"Playing a sub-game to determine the winner...\n")
                p1_sg = []
                p2_sg = []
                player_subgame = []
                for index in range(0,p1_card):
                    p1_sg.append(player_1[index])
                for index in range(0,p2_card):
                    p2_sg.append(player_2[index])
                player_subgame.append(p1_sg)
                player_subgame.append(p2_sg)
                game += 1
                result = play_game_2(player_subgame, game)

                if result[0] == 0:
                    player_1.append(p1_card)
                    player_1.append(p2_card)
                    print(f"Player 1 wins round {round} of game {game}!\n")
                else:
                    player_2.append(p2_card)
                    player_2.append(p1_card)
                    print(f"Player 2 wins round {round} of game {game}!\n")
            else:
                if p1_card > p2_card:
                    player_1.append(p1_card)
                    player_1.append(p2_card)
                    print(f"Player 1 wins round {round} of game {game}!\n")
                else:
                    player_2.append(p2_card)
                    player_2.append(p1_card)
                    print(f"Player 2 wins round {round} of game {game}!\n")

                round += 1

        if len(player_1) > len(player_2):
            winner = 0,player_1
            print(f"The winner of game {game} is player 1\n")
        else:
            winner = 1,player_2
            print(f"The winner of game {game} is player 2\n")
        if game > 1:
            print(f"...anyway, back to game {game - 1}.")
        return winner



def crab_combat_1():
    solution = 0
    input_data = read_and_load_input("Day22")
    players = generate_decks(input_data)
    winner = play_game(players)
    for index,val in enumerate(winner):
        solution += (val * (len(winner)-index))
    return solution

def crab_combat_2():
    solution = 0
    input_data = read_and_load_input("Day22")
    players = generate_decks(input_data)
    game = 1
    winner = play_game_2(players, game)
    print(winner[1])
    for index,val in enumerate(winner[1]):
        solution += (val * (len(winner[1])-index))
    return solution

if __name__ == '__main__':
    print(f"Solution 1: {crab_combat_1()}")
    print(f"Solution 2: {crab_combat_2()}")
