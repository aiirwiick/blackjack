# Blackjack
import random
import time

def read_format(cards):
    new_cards = []
    for i in range(len(cards)):
        if cards[i] == 11:
            new_cards.append('J')
        elif cards[i] == 12:
            new_cards.append('Q')
        elif cards[i] == 13:
            new_cards.append('K')
        elif cards[i] == 1:
            new_cards.append('A')
        else:
            new_cards.append(str(cards[i]))
    return new_cards


def count_format(card):
    if card == 11 or card == 12 or card == 13:
        return 10
    elif card == 1:
        return 11
    else:
        return card

def current_cards(cards):
    for i in range(len(cards) - 1):
        print(cards[i], ",")
    print(cards[len(cards) - 1])

while True:
    deck = []
    for i in range(1, 14):
        for j in range(4):
            deck.append(i)
    random.shuffle(deck)

    # Dealer's Cards
    d_ace_count = 0
    dc = []
    for i in range(2):
        j = deck.pop(0)
        dc.append(j)
        if j == 1:
            d_ace_count += 1

    read_dc = read_format(dc)
    count_dc = []
    for k in range(2):
        count_dc.append(count_format(dc[k]))
    print("Dealer's cards are . and", read_dc[0])

    time.sleep(1)

    # Player's Cards
    p_ace_count = 0
    pc = []
    for i in range(2):
        j = deck.pop(0)
        pc.append(j)
        if j == 1:
            p_ace_count += 1

    read_pc = read_format(pc)
    count_pc = []
    for k in range(2):
        count_pc.append(count_format(pc[k]))
    print("Your cards are", read_pc[0], "and", read_pc[1])

    time.sleep(1)

    if sum(count_pc) == 21:
        print('Blackjack!')
        user_input = 's'
    elif sum(count_pc) > 21 and p_ace_count > 0:
        for k in range(len(count_pc)):
            if (count_pc[k] == 11):
                count_pc[k] = 1
                p_ace_count -= 1
                break
        user_input = input("Hit or Stand? (h/s) ")
    else:
        user_input = input("Hit or Stand? (h/s) ")

    i = 2
    while user_input == 'h':
        j = deck.pop(0)
        pc.append(j)
        # print(j)
        if j == 1:
            p_ace_count += 1
        read_pc = read_format(pc)
        count_pc.append(count_format(j))
        print("Your new card is", read_pc[i])
        print("Your current cards:", end=' ')
        for j in range(len(read_pc) - 1):
            print(read_pc[j], ", ", end=' ', sep='')
        print(read_pc[len(read_pc) - 1])
        if sum(count_pc) > 21 and p_ace_count > 0:
            for k in range(len(count_pc)):
                if (count_pc[k] == 11):
                    count_pc[k] = 1
                    p_ace_count -= 1
                    break
        elif sum(count_pc) > 21:
            print('Bust!')
            user_input = input('Play Another One? (y/n) ')
            break
        if sum(count_pc) == 21:
            print('Blackjack!')
            user_input = 's'
            break
        user_input = input("Hit or Stand? (h/s) ")
        i += 1

    time.sleep(1)

    if user_input == 's':
        print("Dealer's facedown card is", read_dc[1])
        time.sleep(1)
        print("Dealer's current cards:", read_dc[0], "and", read_dc[1])

        time.sleep(1)

        if sum(count_dc) > 21 and d_ace_count > 0:
            for k in range(len(count_dc)):
                if (count_dc[k] == 11):
                    count_dc[k] = 1
                    d_ace_count -= 1
                    break

        if sum(count_dc) == 21:
            print('Dealer gets blackjack.')
            if sum(count_pc) == 21:
                print('Tie.')
                user_input = input('Play Another One? (y/n) ')
            else:
                print('Dealer has higher number. You Lose.')
                user_input = input('Play Another One? (y/n) ')

        i = 2
        while user_input == 's' and (sum(count_dc) < 17 or sum(count_dc) < sum(count_pc)):

            time.sleep(1)

            j = deck.pop(0)
            dc.append(j)
            if j == 1:
                d_ace_count += 1

            read_dc = read_format(dc)
            count_dc.append(count_format(j))

            print("Dealer's new card is", read_dc[i])
            print("Dealer's current cards:", end=' ')
            # print(count_dc)
            for j in range(len(read_dc) - 1):
                print(read_dc[j], ", ", end=' ', sep='')
            print(read_dc[len(read_dc) - 1])

            if sum(count_dc) > 21 and d_ace_count > 0:
                for k in range(len(count_dc)):
                    if (count_dc[k] == 11):
                        count_dc[k] = 1
                        d_ace_count -= 1
                        break
            elif sum(count_dc) > 21:
                print('Dealer goes bust! You Win!')
                user_input = input('Play Another One? (y/n) ')
                break

            if sum(count_dc) == 21:
                print('Dealer gets blackjack.')

            if sum(count_dc) > sum(count_pc):
                print('Dealer has higher number. You Lose.')
                user_input = input('Play Another One? (y/n) ')
                break

            i += 1

        if sum(count_dc) == sum(count_pc):
            print('Tie.')
            user_input = input('Play Another One? (y/n) ')


    if user_input == 'n':
        break
