import pygame

pygame.init() # Для автоматической инициализации всех модулей Pygame, это команда, которая запускает pygame

# ФПС
clock = pygame.time.Clock() # clock, чтобы убедиться, что игра работает с заданной частотой кадров.
fps = 60  # частота кадров в секунду

BLACK = (0,0,0)
WIDTH = 800  # ширина игрового окна
HEIGHT = 600 # высота игрового окна

image_target = pygame.image.load('') # Загружаем изображение

running = True  # Зададим переменную running → пропишем, что она равна True
while running:  # → создадим цикл while
    pass

pygame.quit()  #