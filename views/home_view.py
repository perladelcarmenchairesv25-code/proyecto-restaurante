import flet as ft

class HomeView:
    def __init__(self, page: ft.Page, navegar_fun):
        self.page = page
        self.navegar_fun = navegar_fun

        titulo = ft.Text("¡Bienvenidos al Restaurante!", size=28, weight="bold", color=ft.Colors.GREEN_900)
        subtitulo = ft.Text("Selecciona tus platillos favoritos del menú del día", size=14, color=ft.Colors.BLACK54)

        self.menu_clientes = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO, expand=True)
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
        
        for categoria, lista_items in self.page.productos.items():
            self.menu_clientes.controls.append(
                ft.Text(f"--- {categoria} ---", size=18, weight="bold", color=ft.Colors.GREEN_700)
            )
            for item in lista_items:
                if item["disponible"]:
                    tarjeta = ft.Container(
                        content=ft.Column([
                            ft.Text(item["nombre"], size=16, weight="bold", color=ft.Colors.BLACK),
                            ft.Text(item["desc"], size=13, color=ft.Colors.BLACK54),
                            ft.Text(item["precio"], size=14, weight="bold", color=ft.Colors.GREEN_800),
                        ]),
                        padding=10,
                        bgcolor=ft.Colors.WHITE,
                        border_radius=8,
                        border=ft.Border(
                            top=ft.BorderSide(1, ft.Colors.GREY_300),
                            bottom=ft.BorderSide(1, ft.Colors.GREY_300),
                            left=ft.BorderSide(1, ft.Colors.GREY_300),
                            right=ft.BorderSide(1, ft.Colors.GREY_300)
                        )
                    )
                    self.menu_clientes.controls.append(tarjeta)