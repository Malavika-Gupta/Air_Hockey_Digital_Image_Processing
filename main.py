import cv2
from utils.hand_detection import HandDetection
from utils.Ball import Ball
from utils.Paddle import Paddle
from utils.collision import handle_collision
from utils.constants import WIDTH, HEIGHT, LEFT_OFFSET, RIGHT_OFFSET
from utils.Score import Score
from utils.handle_power_up_collision import handle_power_up_collision
from utils.PowerUp import PowerUp
import random
import time

# Initialize video capture
vid = cv2.VideoCapture(0)

# Create an instance of HandDetection
hand_detection = HandDetection()
hand_detection.create_trackbars()

# Create an instance of Score
score = Score()

# Initialize power-up variables
power_ups = []  # List to store active power-ups
power_up_spawn_time = time.time()  # Timer for spawning power-ups

def spawn_power_up():
    x = random.randint(LEFT_OFFSET + 50, RIGHT_OFFSET - 50)  # Random x position
    y = random.randint(50, HEIGHT - 50)  # Random y position
    type = random.choice(["speed", "freeze", "multi-ball"])  # Random type
    power_ups.append(PowerUp(x, y, type))

def main():
    cv2.namedWindow("Hand Gesture Slider", cv2.WINDOW_NORMAL)
    cv2.moveWindow("Hand Gesture Slider", 10, 10)
    left_paddle = Paddle(LEFT_OFFSET, HEIGHT // 2, (255, 0, 0))
    right_paddle = Paddle(RIGHT_OFFSET, HEIGHT // 2, (0, 255, 0))
    ball = Ball(WIDTH // 2, HEIGHT // 2)
    right_paddle_freeze_time = None

    global power_ups, power_up_spawn_time  # Access global variables

    while vid.isOpened():
        ret, frame = vid.read()
        if not ret:
            break

        # Resize to defined size
        frame = cv2.resize(frame, (WIDTH, HEIGHT))

        # Flip the frame for mirror effect
        frame = cv2.flip(frame, 1)

        # Get Centroids of hands/color
        centroids = hand_detection.get_centroid(frame)

        # Assign centroids to paddles
        if len(centroids) == 1:
            left_paddle.move(left_paddle.x, centroids[0][1])
        elif len(centroids) == 2:
            # Sort by x-coordinate
            centroids = sorted(centroids, key=lambda c: c[0])
            left_paddle.move(left_paddle.x, centroids[0][1])
            right_paddle.move(right_paddle.x, centroids[1][1])
        
        # Draw paddles
        left_paddle.draw(frame)
        right_paddle.draw(frame)

        # Start move ball
        ball.move(frame)

        # Handle power-up collisions
        handle_power_up_collision(ball, power_ups, left_paddle, right_paddle)

        for power_up in power_ups:
            if power_up.type == "freeze" and right_paddle.frozen:
                if right_paddle_freeze_time is None:
                    right_paddle_freeze_time = time.time()

        if right_paddle.frozen and right_paddle_freeze_time is not None:
            if time.time() - right_paddle_freeze_time > 5:
                right_paddle.unfreeze()
                right_paddle_freeze_time = None

        # Display score on frame
        score.show(ball, frame)

        # Handle collision between ball and paddles
        handle_collision(ball, left_paddle, right_paddle, frame)

        # Spawn power-ups periodically
        if time.time() - power_up_spawn_time > 10:  # Spawn every 10 seconds
            spawn_power_up()
            power_up_spawn_time = time.time()  # Reset the timer

        # Draw power-ups
        for power_up in power_ups:
            power_up.draw(frame)

        power_ups = [p for p in power_ups if time.time() - p.spawn_time < p.lifespan]

        cv2.imshow("Hand Gesture Slider", frame)

        # Exit
        key = cv2.waitKey(10)
        if key == ord("q"):
            break

    # Release the video capture and close all OpenCV windows
    vid.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()