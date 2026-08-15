class FingerCounter:

    def count_fingers(self, hand, handedness):

        fingers = 0

        # Thumb
        if handedness == "Right":
            if hand[4].x < hand[3].x:
                fingers += 1

        elif handedness == "Left":
            if hand[4].x > hand[3].x:
                fingers += 1

        # Index
        if hand[8].y < hand[6].y:
            fingers += 1

        # Middle
        if hand[12].y < hand[10].y:
            fingers += 1

        # Ring
        if hand[16].y < hand[14].y:
            fingers += 1

        # Pinky
        if hand[20].y < hand[18].y:
            fingers += 1

        return fingers