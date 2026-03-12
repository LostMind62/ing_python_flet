import flet as ft


def main(page: ft.Page):
    page.title = "Flet counter example"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    

    txt_number = ft.TextField(value="0", text_align=ft.TextAlign.RIGHT, width=100)

    def minus_click(e):
        valor = int(txt_number.value) - 1
        if valor < 0:
            valor = 0
            print("ya no puedes bajar ")
        txt_number.value = str(valor)
        page.update()

    def plus_click(e):
        valor = int(txt_number.value) + 1
        if valor > 10:
            valor = 10
            print("ya no puedes subir ")
        txt_number.value = str(valor)
        page.update()

    page.add(
        ft.Row(
            [
                ft.IconButton(ft.icons.REMOVE, on_click=minus_click),
                txt_number,
                ft.IconButton(ft.icons.ADD, on_click=plus_click),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        )
    )


ft.app(main)
