import pygame
import time

pygame.init()
pygame.joystick.init()

if pygame.joystick.get_count() == 0:
    print("No controller detected!")
    exit()

joystick = pygame.joystick.Joystick(0)
joystick.init()
print(f"Connected to: {joystick.get_name()}")
print("\nMove a stick, press a button, or use D-pad.\n(Press Ctrl+C to quit)\n")

# store previous values to detect changes
prev_axes = [0] * joystick.get_numaxes()
prev_buttons = [0] * joystick.get_numbuttons()
prev_hats = [(0, 0)] * joystick.get_numhats()

while True:
    pygame.event.pump()

    # Axes
    for i in range(joystick.get_numaxes()):
        axis = joystick.get_axis(i)
        if abs(axis - prev_axes[i]) > 0.1:
            print(f"Axis {i}: {axis:.2f}")
            prev_axes[i] = axis

    # Buttons
    for i in range(joystick.get_numbuttons()):
        state = joystick.get_button(i)
        if state != prev_buttons[i]:
            print(f"Button {i}: {'Pressed' if state else 'Released'}")
            prev_buttons[i] = state

    # Hats (D-pad)
    for i in range(joystick.get_numhats()):
        hat = joystick.get_hat(i)
        if hat != prev_hats[i]:
            print(f"Hat {i}: {hat}")
            prev_hats[i] = hat

    time.sleep(0.05)
