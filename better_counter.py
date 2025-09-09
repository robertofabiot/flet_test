import flet as ft
from functools import partial

def main(page: ft.Page):
    #Configuración de la página
    page.bgcolor = "black"
    page.color = "white"
    page.title = "Triple Counter"

    #Lista de números y funciones usables para cualquiera de ellos
    numbers = [0, 0, 0]
    text_numbers = [ft.Text(str(numbers[i])) for i in range(len(numbers))]

    def minus(e, i): #la variable i es el número del contador. Para hacerlo más intuitivo, se recibirá comenzando en 1
        if (numbers[i-1] > 0):
            numbers[i-1] -= 1
            text_numbers[i-1].value = str(numbers[i-1])
        page.update()

    def plus(e, i):
        numbers[i-1] += 1
        text_numbers[i-1].value = str(numbers[i-1])
        page.update()

    def reset_all(e):
        nonlocal numbers
        numbers = [0, 0, 0]
        for i in range(len(text_numbers)):
            text_numbers[i].value = "0"
        page.update()

    #Crear los seis botones independientes
    first_minus_button = ft.FilledButton(text="-", on_click=partial(minus, i = 1))
    first_plus_button = ft.FilledButton(text="+", on_click=partial(plus, i = 1))
    second_minus_button = ft.FilledButton(text="-", on_click=partial(minus, i = 2))
    second_plus_button = ft.FilledButton(text="+", on_click=partial(plus, i = 2))
    third_minus_button = ft.FilledButton(text="-", on_click=partial(minus, i = 3))
    third_plus_button = ft.FilledButton(text="+", on_click=partial(plus, i = 3))

    #Crear botón para resetear todo
    reset_all_button = ft.FilledButton(text="Reset All", on_click=reset_all)

    #Crear filas para cada contador
    first_row = ft.Row(
        controls = [first_minus_button, text_numbers[0], first_plus_button],
        alignment = ft.MainAxisAlignment.CENTER,
        spacing = 20
    )

    second_row = ft.Row(
        controls = [second_minus_button, text_numbers[1], second_plus_button],
        alignment = ft.MainAxisAlignment.CENTER,
        spacing = 20
    )

    third_row = ft.Row(
        controls = [third_minus_button, text_numbers[2], third_plus_button],
        alignment = ft.MainAxisAlignment.CENTER,
        spacing = 20
    )

    #Todas las filas en una sola y agregarlas
    all_rows = ft.Row(
        controls = [first_row, second_row, third_row],
        alignment = ft.MainAxisAlignment.CENTER
    )

    reset_all_row = ft.Row(
        controls = [reset_all_button],
        alignment = ft.MainAxisAlignment.CENTER
    )

    page.add(all_rows)
    page.add(reset_all_row)

ft.app(target=main, view=ft.WEB_BROWSER)