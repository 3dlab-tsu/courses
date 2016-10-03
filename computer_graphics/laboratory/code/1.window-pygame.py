"""
Простой пример созданий пустого окна с использование pygame.
В дальнейшем этот пример будет развиваться для использваония OpenGL

Необходимо поставить модули pyopengl pygame
Для wibdwos можно брать отсюда http://www.lfd.uci.edu/~gohlke/pythonlibs/
"""

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *


class Controller(object):
    """Основной класс для создания окна и запуска цикла рендеринга"""

    def __init__(self, w=800, h=600, name="Lab", frame_rate=60):
        """Конструктор нашего класса

        Принимает параметры размера окна, название окна и ограничение количества кадров всекунду
        """
        self.w = w
        self.h = h
        self.name = name
        self.frame_rate = frame_rate
        self.screen = None  # ссылка на созданное коно
        self.clock = None  # вспомогательный объект для контроля FPS

    def init(self):
        """Создание окна, инициализация"""
        self.screen = pygame.display.set_mode((self.w, self.h), HWSURFACE | OPENGL | DOUBLEBUF | RESIZABLE)
        pygame.display.set_caption(self.name)
        glEnable(GL_DEPTH_TEST)
        self.clock = pygame.time.Clock()

    def loop_step(self):
        """Обратока цикла рендеринга pygame"""
        # задаем максимальное количество кадров в секунду
        self.clock.tick(self.frame_rate)
        # считываем все произошедшие событие
        for event in pygame.event.get():
            # обробатываем выход из приложения
            if event.type == QUIT:
                self.quit()
                return
            if event.type == KEYUP and event.key == K_ESCAPE:
                self.quit()
                return
            # обрабатываем изменение размера окна
            if event.type == VIDEORESIZE:
                self.reshape(*event.size)
            # обработка события
            self.event(event)
        # что-то рисуем
        self.render()
        # показываем в залоговке окна FPS
        self.fps()
        # смена кадров, т.к. мы используем DOUBLEBUF ражим
        pygame.display.flip()

    def quit(self):
        """Выход из приложения, закрытие окна"""
        pygame.quit()
        quit()

    def loop(self):
        """Запускает бесконечный цикл рендеринга"""
        while True:
            self.loop_step()

    def reshape(self, width, height):
        """Обрабатываем изменение размера окна"""
        self.w = width
        self.h = height

    def event(self, e):
        """Обрабатываем события"""
        pass

    def fps(self):
        """Рисуем текущий FPS"""
        pygame.display.set_caption("%s FPS: %s" % (self.name, self.clock.get_fps()))

    def run(self):
        """Запуск приложения"""
        self.init()
        self.loop()

    def render(self):
        """Рисуем"""
        pass


if __name__ == '__main__':
    main = Controller()
    main.run()
