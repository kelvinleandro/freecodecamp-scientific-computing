import copy
import random
# Consider using the modules imported above.

class Hat:
    contents = []
    def __init__(self, **kwargs):
        self.contents = [k for k,v in kwargs.items() for _ in range(v)]

    def draw(self, n):
        if n >= len(self.contents):
            return self.contents

        balls = []
        for _ in range(n):
            ball = random.choice(self.contents)
            balls.append(ball)
            self.contents.remove(ball)

        return balls        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    m = 0
    for _ in range(num_experiments):
        temp_hat = copy.deepcopy(hat)
        balls_drawn = temp_hat.draw(num_balls_drawn)

        quant = 0
        for color, num in expected_balls.items():
            if balls_drawn.count(color) >= num:
                quant += 1

        if quant == len(expected_balls):
            m += 1

    return m / num_experiments
