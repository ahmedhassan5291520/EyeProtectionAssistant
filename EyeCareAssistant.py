import pygame
import time
import numpy as np
import sounddevice as sd

# Function to play a beep sound
def play_beep():
    fs = 4410  # Sampling frequency
    duration = 0.7  # Duration in seconds
    frequency = 300  # Frequency in Hz
    t = np.linspace(0, duration, int(fs * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    sd.play(wave, fs)
    sd.wait()

# Function to open a full black screen
def open_full_black_screen():
    # Initialize Pygame
    pygame.init()

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
    main()
