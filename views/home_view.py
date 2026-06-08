import flet as ft

class HomeView:
    def __init__(self, page: ft.Page, navegar_fun):
        self.page = page
        self.navegar_fun = navegar_fun

        titulo = ft.Text("¡Bienvenidos al Restaurante!", size=28, weight="bold", color=ft.Colors.GREEN_900)
        subtitulo = ft.Text("Selecciona una categoría para ver el menú", size=14, color=ft.Colors.BLACK54)

        self.menu_clientes = ft.Column(
            spacing=12,
            expand=True,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
        self.cargar_menu_publico()

        btn_admin = ft.ElevatedButton(
            content=ft.Text("Panel Administrador", color=ft.Colors.WHITE),
            style=ft.ButtonStyle(bgcolor="#2D5A27"),
            on_click=lambda _: self.navegar_fun("/admin_login")
        )

        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Row([titulo, btn_admin], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                    subtitulo,
                    ft.Divider(height=20),
                    self.menu_clientes
                ],
                expand=True
            ),
            expand=True,
            bgcolor="#FDF5E6",
            padding=20
        )

    def cargar_menu_publico(self):
        self.menu_clientes.controls.clear()

        def ir_a_menu(categoria):
            self.page.categoria_actual = categoria
            self.navegar_fun("/menu")

        botones = [
            ("Comida", "COMIDA", ft.Icons.RESTAURANT_MENU),
            ("Bebida", "BEBIDAS", ft.Icons.LOCAL_DRINK),
            ("Postres", "POSTRES", ft.Icons.ICECREAM),
        ]

        for texto, categoria, icono in botones:
            boton = ft.ElevatedButton(
                content=ft.Row(
                    [
                        ft.Icon(icono, color=ft.Colors.WHITE, size=20),
                        ft.Text(texto, color=ft.Colors.WHITE, weight="bold"),
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=10,
                ),
                width=240,
                height=50,
                style=ft.ButtonStyle(
                    bgcolor="#2D5A27",
                    shape=ft.RoundedRectangleBorder(radius=10),
                ),
                on_click=lambda _, cat=categoria: ir_a_menu(cat),
            )
            self.menu_clientes.controls.append(
                ft.Row([boton], alignment=ft.MainAxisAlignment.CENTER)
            )