def handle_power_up_collision(ball, power_ups, left_paddle, right_paddle):
    for power_up in power_ups:
        distance = ((ball.x - power_up.x) ** 2 + (ball.y - power_up.y) ** 2) ** 0.5
        if distance <= ball.radius + power_up.radius:  # Collision detected
            power_up.apply(ball, left_paddle, right_paddle)
            power_ups.remove(power_up)  # Remove the power-up after applying