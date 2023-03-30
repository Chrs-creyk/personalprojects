#!/usr/bin/python3
import curses
import random
import time
import unicodedata

chars = "abcdefghijklmnopqrstuvwxyz1234567890абвгдеёжзийклмнопрстуфхцчшщъыьэюя你好我是谁今天天气很好안녕하세요오늘날씨좋네요こんにちは今日は天気がいいですね"

screen = curses.initscr()
curses.curs_set(False)
curses.start_color()

curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)
curses.init_pair(2, curses.COLOR_CYAN, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_MAGENTA, curses.COLOR_BLACK)
curses.init_pair(4, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(5, curses.COLOR_WHITE, curses.COLOR_BLACK)
colors = [curses.color_pair(i) for i in range(1, 6)]

height, width = screen.getmaxyx()

speeds = [0.2, 0.25, 0.3, 0.35, 0.4]

try:
    while True:
        # Generar un nuevo caracter aleatorio
        char = random.choice(chars)

        # Generar una posición aleatoria en la parte superior de la pantalla
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        # Generar una velocidad aleatoria para el caracter
        speed = random.choice(speeds)

        # Imprimir el caracter en la pantalla y esperar la velocidad correspondiente
        color = random.choice(colors)
        screen.addstr(y, x, char, color)
        screen.refresh()
        time.sleep(speed)

        # Mover el caracter hacia abajo y borrar el anterior
        screen.addstr(y, x, " ")
        y += 1

        # Si el caracter llega al final de la pantalla, regresarlo a la parte superior
        if y > height - 1:
            y = 0

        # Imprimir el caracter en la nueva posición y esperar la velocidad correspondiente
        color = random.choice(colors)
        screen.addstr(y, x, char, color)
        screen.refresh()
        time.sleep(speed)

except KeyboardInterrupt:
    pass

curses.endwin()
