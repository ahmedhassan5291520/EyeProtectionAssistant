"""
EyeCareAssistant can be used as a remainder to keep your eye healthy by giving a 1 minute timeout after 20 minutes.
"""

import time

import numpy as np
import pygame
import sounddevice as sd


def play_beep():
    """Function to play a beep sound"""
    fs = 4410  # Sampling frequency
    duration = 0.7  # Duration in seconds
    frequency = 300  # Frequency in Hz
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, fs)
    sd.wait()


def open_full_black_screen():
    """Function to open a full black screen"""
    # Initialize Pygame
    pygame.init()

    # TODO adjust screen width/height dynamically
    # Set screen dimensions
    screen_width = 800
    screen_height = 600

    # Set up the display
    screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)

    # Fill the screen with black
    screen.fill((0, 0, 0))

    # Update the display
    pygame.display.flip()

    # Wait for 60 seconds
    time.sleep(60)

    # Close Pygame
    pygame.quit()


def main():
    """
    Main function to call other functions.
    """
    while True:
        # Wait for 10 minute before repeating
        time.sleep(1000)
        play_beep()
        time.sleep(10)
        # Open full black screen
        open_full_black_screen()
        print("Black screen opened for eye protection.")

        # Play a beep sound
        play_beep()


if __name__ == "__main__":
    """
    Program Execution Starts Here.
    """
    main()
