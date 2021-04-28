from random import shuffle


def createDeck():
    Deck = []

    facevalues = ["A", "J", "Q", "K"]
    for i in range(4):      # there are four different suits
        for card in range(2, 11):  # Adding numbers 2-10
            Deck.append(str(card))

        for card in facevalues:
            Deck.append(card)
    shuffle(Deck)
    return Deck


cardDeck = createDeck()
# shuffle(cardDeck)   # Shuffles the vales of cards
print(cardDeck)


class Player:
    def __init__(self, hand=[], money=100):
        self.hand = hand
        self.score = self.setScore()
        # print(self.score)
        self.money = money
        self.bet = 0

    def __str__(self):
        currentHand = " "
        for card in self.hand:
            currentHand += str(card) + " "
        finalStatus = currentHand + "score: " + str(self.score)
        return finalStatus

    def setScore(self):
        self.score = 0

        faceCardDict = {"A": 11, "J": 10, "Q": 10, "K": 10, "2": 2,
                        "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10}
        aceCounter = 0
        for card in self.hand:
            self.score += faceCardDict[card]
            if card == "A":
                aceCounter += 1
            if self.score > 21 and aceCounter != 0:
                self.score -= 10
                aceCounter -= 1
        return self.score

    def hit(self, card):
        self.hand.append(card)
        self.score = self.setScore()

    def play(self, newHand):
        self.hand = newHand
        self.score = self.setScore()

    def betMoney(self, amount):
        self.money -= amount
        self.bet += amount

    def win(self, result):
        if result == True:
            if self.score == 21 and len(self.hand) == 2:
                self.money += 2.5 * self.bet
            else:
                self.money += 2 * self.bet
            self.bet = 0
        else:
            self.bet = 0


cardDeck = createDeck()

firstHand = [cardDeck.pop(), cardDeck.pop()]
secondHand = [cardDeck.pop(), cardDeck.pop()]
Player1 = Player(firstHand)
House = Player(secondHand)
print(cardDeck)
print(House)
print(Player1)
while(True):
    action = input("Do you want another card?(Y/N): ")
    if action == "Y":
        Player1.hit(cardDeck.pop())
        print(Player1)
        print(House)
    else:
        break

'''

Player1 = Player(["3", "7", "5"])
print(Player1)
# Player1.hit("K")
Player1.hit("A")
Player1.hit("A")
print(Player1)
Player1.betMoney(20)
print(Player1.money, Player1.bet)
Player1.win(True)
print(Player1.money, Player1.bet)
Player1.play(["A", "K"])
print(Player1)
Player1.betMoney(20)
Player1.win(True)
print(Player1.money, Player1.bet)
'''
