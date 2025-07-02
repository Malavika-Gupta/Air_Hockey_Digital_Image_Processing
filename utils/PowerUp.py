import random
import cv2
import time

class PowerUp:
    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type  # e.g., "speed", "freeze", "multi-ball"
        self.radius = 15  # Size of the power-up
        self.active = False
        self.spawn_time = time.time()  
        self.lifespan = 8  # seconds until it expires

    def draw(self, frame):
        if self.type == "speed":
            color = (0, 255, 0)  # Green
        elif self.type == "freeze":
            color = (0, 0, 255)  # Blue
        elif self.type == "multi-ball":
            color = (255, 0, 0)  # Red

        # Draw as an outline circle, thickness = 3
        cv2.circle(frame, (int(self.x), int(self.y)), self.radius, color, 3)

    def apply(self, ball, left_paddle, right_paddle):
        # Apply the power-up effect
        if self.type == "speed":
            ball.x_vel *= 1.5  # Increase ball speed
            ball.y_vel *= 1.5
        elif self.type == "freeze":
            right_paddle.freeze()  # Freeze the opponent's paddle
        elif self.type == "multi-ball":
            # Spawn an additional ball (you'll need to handle multiple balls)
            pass
    