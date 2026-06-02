import flet as ft

class MenuView:
    def __init__(self, page: ft.Page, categoria: str, navegar_fun):
        self.page = page
        self.categoria = categoria
        self.navegar_fun = navegar_fun

        self.btn_volver = ft.IconButton(
            icon=ft.Icons.ARROW_BACK_IOS_NEW,
            icon_color=ft.Colors.GREEN_900,
            icon_size=20,
            on_click=lambda _: self.navegar_fun("/home")
        )

        self.titulo = ft.Text(
            self.categoria,
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.GREEN_900
        )

        def crear_tarjeta_producto(nombre, descripcion, precio):
            return ft.Card(
                content=ft.Container(
                    content=ft.Column([
                        ft.Row([
                            ft.Text(nombre, size=18, weight="bold", color=ft.Colors.GREEN_900),
                            ft.Text(precio, size=18, weight="bold", color=ft.Colors.ORANGE_800),
                        ], alignment=ft.MainAxisAlignment.SPACE_BETWEEN),
                        ft.Container(height=4),
                        ft.Text(descripcion, size=14, color=ft.Colors.BLACK54),
                    ]),
                    padding=15,
                    width=340,
                    bgcolor=ft.Colors.WHITE,
                    border_radius=15,
                ),
                elevation=2
            )

        column_controls = [
            ft.Row([self.btn_volver, self.titulo], alignment=ft.MainAxisAlignment.START),
            ft.Container(height=15)
        ]

        # CORRECCIÓN: Lee de la base centralizada de main.py
        lista_items = self.page.productos.get(self.categoria, [])
        
        for item in lista_items:
            # FILTRO: Si el admin lo desactivó (disponible == False), el cliente no lo ve
            if item.get("disponible", True):
                card = crear_tarjeta_producto(item["nombre"], item["desc"], item["precio"])
                column_controls.append(card)
                column_controls.append(ft.Container(height=10))

        self.content = ft.Container(
            content=ft.Column(
                column_controls,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO,
                spacing=0
            ),
            expand=True,
            bgcolor="#FDF5E6",
            padding=20
        )