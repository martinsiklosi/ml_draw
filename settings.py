import pygame

FPS = 60
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
ROWS = 28
COLS = 28
WIDTH = 600
HEIGHT = 600
PIXEL_SIZE = WIDTH // COLS

def get_font(size):
    return pygame.font.SysFont("helvetica", size)