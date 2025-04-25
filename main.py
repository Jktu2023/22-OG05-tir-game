import pygame
import random
import sys

pygame.init() # Для автоматической инициализации всех модулей Pygame, это команда, которая запускает pygame

# ФПС
clock = pygame.time.Clock() # clock, чтобы убедиться, что игра работает с заданной частотой кадров.
fps = 60  # частота кадров в секунду

BLACK = (0,0,0)
WIDTH = 800  # ширина игрового окна
HEIGHT = 600 # высота игрового окна

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Игра Тир')
image_target = pygame.image.load('target.png') # Загружаем изображение
# размеры мишени
T_WIDTH = 80
T_HEIGHT = 80
# рандомные координаты мишени
target_x = random.randint(0, WIDTH - T_WIDTH)
target_x = random.randint(0, HEIGHT - T_HEIGHT)

running = True  # Зададим переменную running → пропишем, что она равна True
while running:  # → создадим цикл while
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:

            running = False
pygame.quit()  # выходим так
sys.exit() # и эдак