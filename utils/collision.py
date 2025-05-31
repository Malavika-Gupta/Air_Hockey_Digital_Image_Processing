from utils.constants import HEIGHT, LEFT_OFFSET, RIGHT_OFFSET
import pygame
pygame.mixer.init()

hit_sound = pygame.mixer.Sound("sounds/hit.wav")      # Paddle hit sound
wall_sound = pygame.mixer.Sound("sounds/wall.wav")    # Wall bounce sound
reset_sound = pygame.mixer.Sound("sounds/score.wav")  # Goal/score sound

def handle_collision(ball, left_paddle, right_paddle, frame):
    # Collision with side edges
    if ball.x - ball.radius < LEFT_OFFSET or ball.x + ball.radius > RIGHT_OFFSET:
        reset_sound.play()
        ball.reset()

    # Collision with top edge
    if ball.y - ball.radius <= 0:
        ball.y_vel = -ball.y_vel
        wall_sound.play()

    # Collision with bottom edge
    if ball.y + ball.radius >= HEIGHT:
        ball.y_vel = -ball.y_vel
        wall_sound.play()

    # Collision with the right slider
    if ball.x + ball.radius >= right_paddle.x - right_paddle.width // 2 and (
        ball.y + ball.radius >= right_paddle.y - right_paddle.height // 2 
        and ball.y - ball.radius <= right_paddle.y + right_paddle.height // 2
    ):
        ball.x_vel = -ball.x_vel
        ball.increase_speed()
        hit_sound.play()

    # Collision with left slider
    if ball.x - ball.radius <= left_paddle.x + left_paddle.width // 2 and (
        ball.y + ball.radius >= left_paddle.y - left_paddle.height // 2
        and ball.y - ball.radius <= left_paddle.y + left_paddle.height // 2
    ):
        ball.x_vel = -ball.x_vel
        ball.increase_speed()
        hit_sound.play()

    ball.move(frame)

