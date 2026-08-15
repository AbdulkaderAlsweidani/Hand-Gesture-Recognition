class GestureDetector:

    def detect_gesture(self, fingers):

        thumb = fingers[0]
        index = fingers[1]
        middle = fingers[2]
        ring = fingers[3]
        pinky = fingers[4]

        # FIST ✊
        if (
            not thumb
            and not index
            and not middle
            and not ring
            and not pinky
        ):
            return "FIST"

        # ONE ☝️
        if (
            not thumb
            and index
            and not middle
            and not ring
            and not pinky
        ):
            return "ONE"

        # PEACE ✌️
        if (
            not thumb
            and index
            and middle
            and not ring
            and not pinky
        ):
            return "PEACE"

        # OPEN HAND 🖐️
        if (
            thumb
            and index
            and middle
            and ring
            and pinky
        ):
            return "OPEN HAND"

        # Anything else
        return "UNKNOWN"