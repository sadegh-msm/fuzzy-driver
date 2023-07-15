import numpy as np


class FuzzyController:
    def __init__(self):
        self.close_L = self.close_R = 0
        self.moderate_L = self.moderate_R = 0
        self.far_L = self.far_R = 0
        self.high_right = 0
        self.low_right = 0
        self.nothing = 0
        self.low_left = 0
        self.high_left = 0

    def fuzzy_membership(self, distance, a, b, c):
        if a <= distance <= b:
            return 1.0
        if b < distance <= c:
            return (c - distance) / (c - b)
        return 0.0

    def fuzzify(self, left_dist, right_dist):
        self.close_L = self.fuzzy_membership(left_dist, 0, 50, 50)
        self.close_R = self.fuzzy_membership(right_dist, 0, 50, 50)
        self.moderate_L = self.fuzzy_membership(left_dist, 35, 50, 65)
        self.moderate_R = self.fuzzy_membership(right_dist, 35, 50, 65)
        self.far_L = self.fuzzy_membership(left_dist, 50, 100, 100)
        self.far_R = self.fuzzy_membership(right_dist, 50, 100, 100)

    def inference(self):
        self.low_right = min(self.close_L, self.moderate_R)
        self.high_right = min(self.close_L, self.far_R)
        self.low_left = min(self.moderate_L, self.close_R)
        self.high_left = min(self.far_L, self.close_R)
        self.nothing = min(self.moderate_L, self.moderate_R)

    def rotate_membership(self, rotate, a, b, c):
        if a <= rotate <= b:
            return (rotate - a) / (b - a)
        if b < rotate <= c:
            return (c - rotate) / (c - b)
        return 0.0

    def max_rotate(self, rotate):
        max_rotate = 0.0
        max_rotate = max(max_rotate, self.rotate_membership(rotate, -50, -20, -5) * self.high_right)
        max_rotate = max(max_rotate, self.rotate_membership(rotate, -20, -10, 0) * self.low_right)
        max_rotate = max(max_rotate, self.rotate_membership(rotate, -10, 0, 10) * self.nothing)
        max_rotate = max(max_rotate, self.rotate_membership(rotate, 0, 10, 20) * self.low_left)
        max_rotate = max(max_rotate, self.rotate_membership(rotate, 5, 20, 50) * self.high_left)
        return max_rotate

    def defuzzify(self):
        soorat = 0.0
        makhraj = 0.0
        X = np.linspace(-50, 50, 1000)
        delta = X[1] - X[0]

        for i in X:
            max_rotate = self.max_rotate(i)
            soorat += max_rotate * i * delta
            makhraj += max_rotate * delta

        center = 0.0
        if makhraj != 0:
            center = 1.0 * float(soorat) / float(makhraj)

        return center

    def decide(self, left_dist, right_dist):
        self.fuzzify(left_dist, right_dist)
        self.inference()
        return self.defuzzify()
