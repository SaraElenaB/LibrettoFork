import flet as ft

from UI.controller import Controller
from UI.view import View


def main(page: ft.Page):
    v = View(page)
    c = Controller(v)
    v.setController(c)  #cosi possono comunicare, la view si crea da sola
    v.loadInterface()

ft.app(target=main)