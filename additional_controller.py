import numpy as np


class FuzzyGasController:
    def __init__(self):
        self.high = None
        self.medium = None
        self.low = None

    def fuzzify(self, center):
        self.close = self.close(center)
        self.moderate = self.moderate(center)
        self.far = self.far(center)

    def close(self, x):
        return -x / 50 + 1 if 0 <= x < 50 else 0

    def moderate(self, x):
        if 40 <= x < 50:
            return x / 10 - 4
        if 50 <= x < 100:
            return -x / 50 + 2
        return 0

    def far(self, x):
        if 90 <= x < 200:
            return x / 110 - 90 / 110
        if x >= 200:
            return 1
        return 0

    def inference(self):
        self.low = self.close
        self.medium = self.moderate
        self.high = self.far

    def max_rotate(self, speed):
        return max(min(self.low, self.low_speed(speed)),
                   min(self.high, self.high_speed(speed)),
                   min(self.medium, self.medium_speed(speed)))

    def low_speed(self, x):
        if 0 <= x < 5:
            return x / 5
        if 5 <= x < 10:
            return -x / 5 + 2
        return 0

    def medium_speed(self, x):
        if 0 <= x <= 15:
            return x / 15
        if 15 < x <= 30:
            return -x / 15 + 2
        return 0

    def high_speed(self, x):
        if 25 <= x < 30:
            return x / 5 - 5
        if 30 <= x < 90:
            return -x / 60 + 9 / 6
        return 0

    def defuzzify(self):
        X = np.linspace(0, 90, 900)
        delta = X[1] - X[0]

        numerator = sum(self.max_rotate(i) * i * delta for i in X)
        denominator = sum(self.max_rotate(i) * delta for i in X)

        center = numerator / denominator if denominator != 0 else 0.0

        return center

    def decide(self, center_dist):
        self.fuzzify(center_dist)
        self.inference()

        return self.defuzzify()
