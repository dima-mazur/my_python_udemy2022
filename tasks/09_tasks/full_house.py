def is_full_house(hand):
    hand_set = set(hand)
    if len(hand_set) == 2:
        for card in hand:
            if hand.count(card) == 3:
                return True
        else:
            return False

    else:
        return False


is_full_house(['3', '3', 'A', '3', '3'])