import math


class FingerCounter:

    def calculate_angle_3d(self, p1, p2, p3):

        # Vector from p2 to p1
        v1 = (
            p1.x - p2.x,
            p1.y - p2.y,
            p1.z - p2.z
        )

        # Vector from p2 to p3
        v2 = (
            p3.x - p2.x,
            p3.y - p2.y,
            p3.z - p2.z
        )

        # Dot product
        dot = (
            v1[0] * v2[0] +
            v1[1] * v2[1] +
            v1[2] * v2[2]
        )

        # Magnitudes
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

        # Prevent math domain errors
        cos_angle = max(-1.0, min(1.0, cos_angle))

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


    def count_fingers(self, hand, handedness):

        fingers = 0

        # =========================
        # Thumb
        # =========================

        if handedness == "Right":

            if hand[4].x < hand[3].x:
                fingers += 1

        elif handedness == "Left":

            if hand[4].x > hand[3].x:
                fingers += 1


        # =========================
        # Index
        # =========================

        if self.is_finger_extended(
            hand, 5, 6, 8
        ):
            fingers += 1


        # =========================
        # Middle
        # =========================

        if self.is_finger_extended(
            hand, 9, 10, 12
        ):
            fingers += 1


        # =========================
        # Ring
        # =========================

        if self.is_finger_extended(
            hand, 13, 14, 16
        ):
            fingers += 1


        # =========================
        # Pinky
        # =========================

        if self.is_finger_extended(
            hand, 17, 18, 20
        ):
            fingers += 1


        return fingers