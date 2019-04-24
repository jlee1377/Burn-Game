import newCard

suites = ["S", "C", "D", "H"]
numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
# class deck:
def listDeck():
    deck = []
    for x in numbers:
        for y in suites:
            a = newCard.card(y,x)
            deck.append(a)
    deck.append(newCard.card("","Joker1"))
    deck.append(newCard.card("","Joker2"))
    return deck
# def tupleDeck():
#     for x in suites:
#         for y in range(3,15):
#             deck.append(Card(suites[x],y))
#     return deck
# def setDeck():
#     for x in suites:
#         for y in range(3,15):
#             deck.append(Card(suites[x],y))
#     return deck
# def dicDeck():
#     for x in suites:
#         for y in range(3,15):
#             deck.append(Card(suites[x],y))
    # return deck

# # def setDeck():
# listDeck = ["SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK","CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK","DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK","HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK"]
# tupleDeck = ("SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK","CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK","DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK","HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK")
# setDeck = {"SA", "S2", "S3", "S4", "S5", "S6", "S7", "S8", "S9", "S10", "SJ", "SQ", "SK","CA", "C2", "C3", "C4", "C5", "C6", "C7", "C8", "C9", "C10", "CJ", "CQ", "CK","DA", "D2", "D3", "D4", "D5", "D6", "D7", "D8", "D9", "D10", "DJ", "DQ", "DK","HA", "H2", "H3", "H4", "H5", "H6", "H7", "H8", "H9", "H10", "HJ", "HQ", "HK"}
# dictDeck = {
#     1: "SA",
#     2: "S2",
#     3: "S3",
#     4: "S4",
#     5: "S5",
#     6: "S6",
#     7: "S7",
#     8: "S8",
#     9: "S9",
#     10: "S10",
#     11: "SJ",
#     12: "SQ",
#     13: "SK",
#     14: "CA",
#     15: "C2",
#     16: "C3",
#     17: "C4",
#     18: "C5",
#     19: "C6",
#     20: "C7",
#     21: "C8",
#     22: "C9",
#     23: "C10",
#     24: "CJ",
#     25: "CQ",
#     26: "CK",
#     27: "DA",
#     28: "D2",
#     29: "D3",
#     30: "D4",
#     31: "D5",
#     32: "D6",
#     33: "D7",
#     34: "D8",
#     35: "D9",
#     36: "D10",
#     37: "DJ",
#     38: "DQ",
#     39: "DK",
#     40: "HA",
#     41: "H2",
#     42: "H3",
#     43: "H4",
#     44: "H5",
#     45: "H6",
#     46: "H7",
#     47: "H8",
#     48: "H9",
#     49: "H10",
#     50: "HJ",
#     51: "HQ",
#     52: "HK"
# }
