import flet as ft

class HomeView:
    def __init__(self, page: ft.Page, navegar_fun):
        self.page = page
        self.navegar_fun = navegar_fun

        titulo = ft.Text("¡Bienvenidos al Restaurante!", size=28, weight="bold", color=ft.Colors.GREEN_900)
        subtitulo = ft.Text("Selecciona tus platillos favoritos del menú del día", size=14, color=ft.Colors.BLACK54)

        self.categoria_actual = list(self.page.productos.keys())[0] if self.page.productos else None
        self.menu_clientes = ft.Column(spacing=15, scroll=ft.ScrollMode.AUTO, expand=True)
        self.botones_categoria = ft.Row(spacing=10, wrap=True, alignment=ft.MainAxisAlignment.CENTER)
        self.cargar_menu_publico()
        self._crear_botones_categorias()

        btn_admin = ft.ElevatedButton(
            content=ft.Text("Panel Administrador", color=ft.Colors.WHITE),
            style=ft.ButtonStyle(bgcolor="#2D5A27"),
            on_click=lambda _: self.navegar_fun("/admin_login")
        )

        self.content = ft.Container(
            content=ft.Column(
                [
                    titulo,
                    subtitulo,
                    ft.Container(height=12),
                    self.botones_categoria,
                    ft.Divider(height=20),
                    self.menu_clientes,
                    ft.Container(height=20),
                    ft.Row(
                        [btn_admin],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                expand=True
            ),
            expand=True,
            bgcolor="#FDF5E6",
            padding=20
        )

    def cargar_menu_publico(self):
        self.menu_clientes.controls.clear()
        
        if not self.categoria_actual:
            return

        categoria_items = self.page.productos.get(self.categoria_actual, [])
        self.menu_clientes.controls.append(
            ft.Text(f"--- {self.categoria_actual} ---", size=18, weight="bold", color=ft.Colors.GREEN_700)
        )

        for item in categoria_items:
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

        if not any(item["disponible"] for item in categoria_items):
            self.menu_clientes.controls.append(
                ft.Text("No hay productos disponibles en esta categoría.", size=14, color=ft.Colors.BLACK54)
            )

    def _crear_botones_categorias(self):
        self.botones_categoria.controls.clear()
        for categoria in self.page.productos.keys():
            seleccionado = categoria == self.categoria_actual
            self.botones_categoria.controls.append(
                ft.ElevatedButton(
                    content=ft.Text(categoria, weight="bold"),
                    style=ft.ButtonStyle(
                        bgcolor=ft.Colors.GREEN_900 if seleccionado else ft.Colors.WHITE,
                        color=ft.Colors.WHITE if seleccionado else ft.Colors.BLACK,
                        shape=ft.RoundedRectangleBorder(radius=12),
                        side=ft.BorderSide(1, ft.Colors.GREEN_900 if seleccionado else ft.Colors.GREY_300)
                    ),
                    height=40,
                    on_click=lambda e, cat=categoria: self.cambiar_categoria(cat)
                )
            )

    def cambiar_categoria(self, categoria):
        self.categoria_actual = categoria
        self.cargar_menu_publico()
        self._crear_botones_categorias()
        self.page.update()