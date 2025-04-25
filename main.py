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
target_y = random.randint(0, HEIGHT - T_HEIGHT)

running = True  # Зададим переменную running → пропишем, что она равна True
while running:  # → создадим цикл while
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    if event.type == pygame.MOUSEBUTTONDOWN:
        mouse_x, mouse_y = pygame.mouse.get_pos() # сохраняем координаты курсора мыши, куда мы кликнули
        # находится ли координата мыши mouse_ в пределах координаты мишени target_ и размером этой мишени (target_ + T_РАЗМЕРМИШЕНИ)
        if target_x < mouse_x < (target_x + T_WIDTH) and target_y < mouse_y < (target_y + T_HEIGHT):
            # новые рандомные координаты мишени - мишень меняет положение в окне
            target_x = random.randint(0, WIDTH - T_WIDTH)
            target_y = random.randint(0, HEIGHT - T_HEIGHT)

    screen.blit(image_target, (target_x, target_y))
    pygame.display.update()

pygame.quit()  # выходим так
sys.exit() # и эдак