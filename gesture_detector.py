class GestureDetector:

    def detect_gesture(self, finger_count):

        if finger_count == 0:
            return "FIST"

        elif finger_count == 1:
            return "ONE"

        elif finger_count == 2:
            return "PEACE"

        elif finger_count == 5:
            return "OPEN HAND"

        else:
            return "UNKNOWN"