import math


class FingerCounter:

    def calculate_angle_3d(self, p1, p2, p3):

        v1 = (
            p1.x - p2.x,
            p1.y - p2.y,
            p1.z - p2.z
        )

        v2 = (
            p3.x - p2.x,
            p3.y - p2.y,
            p3.z - p2.z
        )

        dot = (
            v1[0] * v2[0] +
            v1[1] * v2[1] +
            v1[2] * v2[2]
        )

        mag1 = math.sqrt(
            v1[0] ** 2 +
            v1[1] ** 2 +
            v1[2] ** 2
        )

        mag2 = math.sqrt(
            v2[0] ** 2 +
            v2[1] ** 2 +
            v2[2] ** 2
        )

        if mag1 == 0 or mag2 == 0:
            return 0

        cos_angle = dot / (mag1 * mag2)

        cos_angle = max(-1, min(1, cos_angle))

        angle = math.degrees(
            math.acos(cos_angle)
        )

        return angle


    def is_finger_extended(self, hand, mcp, pip, tip):

        angle = self.calculate_angle_3d(
            hand[mcp],
            hand[pip],
            hand[tip]
        )

        return angle > 160


    def get_finger_states(self, hand, handedness):

        # Thumb
        if handedness == "Right":
            thumb = hand[4].x < hand[3].x
        else:
            thumb = hand[4].x > hand[3].x

        # Index
        index = self.is_finger_extended(
            hand,
            5,
            6,
            8
        )

        # Middle
        middle = self.is_finger_extended(
            hand,
            9,
            10,
            12
        )

        # Ring
        ring = self.is_finger_extended(
            hand,
            13,
            14,
            16
        )

        # Pinky
        pinky = self.is_finger_extended(
            hand,
            17,
            18,
            20
        )

        return [
            thumb,
            index,
            middle,
            ring,
            pinky
        ]


    def count_fingers(self, hand, handedness):

        finger_states = self.get_finger_states(
            hand,
            handedness
        )

        return sum(finger_states)