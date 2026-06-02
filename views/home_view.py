import flet as ft

class HomeView:
    # Recibe 'navegar_fun' desde main.py para gestionar los cambios de ventana
    def __init__(self, page: ft.Page, navegar_fun):
        self.page = page
        self.navegar_fun = navegar_fun

        # Título de la sección
        self.header = ft.Text(
            "Selecciona una categoría",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.GREEN_900
        )

        # Función auxiliar para maquetar de forma idéntica las tres categorías principales
        def crear_opcion_menu(titulo, ruta_imagen):
            return ft.Container(
                content=ft.Stack(
                    [
                        # 1. Imagen de fondo de la categoría
                        ft.Image(
                            src=ruta_imagen,
                            fit="cover",
                            expand=True,
                            border_radius=20
                        ),
                        # 2. Capa oscura semitransparente para asegurar el contraste del texto
                        ft.Container(
                            bgcolor=ft.Colors.with_opacity(0.4, ft.Colors.BLACK),
                            border_radius=20
                        ),
                        # 3. Texto con el nombre de la categoría completamente centrado
                        ft.Container(
                            content=ft.Text(
                                titulo, 
                                size=24, 
                                weight="bold", 
                                color=ft.Colors.WHITE
                            ),
                            alignment=ft.Alignment(0, 0)
                        )
                    ]
                ),
                width=320,
                height=140,
                border_radius=20,
                # Al hacer clic, envía la ruta con el nombre de la categoría seleccionada
                on_click=lambda _: self.navegar_fun(f"/menu_{titulo}")
            )

        # Creación de las tarjetas conectadas a las imágenes en la carpeta assets
        self.card_comida = crear_opcion_menu("COMIDA", "/comida.png")
        self.card_bebidas = crear_opcion_menu("BEBIDAS", "/bebidas.png")
        self.card_postres = crear_opcion_menu("POSTRES", "/postres.png")

        # Botón alargado, discreto y minimalista para acceder al sector de administración
        self.btn_admin = ft.TextButton(
            content=ft.Text(
                "Panel de Administración", 
                color=ft.Colors.GREEN_900, 
                size=14,
                weight="bold"
            ),
            style=ft.ButtonStyle(
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            on_click=self.admin_click
        )

        # Construcción de la interfaz de la pantalla completa
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="/logo.png", width=80),
                    self.header,
                    ft.Container(height=15),
                    self.card_comida,
                    self.card_bebidas,
                    self.card_postres,
                    
                    # Espacio de separación antes del botón de administración
                    ft.Container(height=30), 
                    
                    # El botón del Administrador
                    self.btn_admin,
                    
                    # Contenedor de separación inferior que eleva el botón de forma segura
                    ft.Container(height=20)
                ], # <- CORRECCIÓN: Aquí cerramos correctamente el corchete de la lista de controles
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                scroll=ft.ScrollMode.AUTO
            ),
            alignment=ft.Alignment(0, 0),
            expand=True,
            bgcolor="#FDF5E6",
            padding=20
        )

    # Función encargada de redirigir al Login de Administración al pulsar el botón inferior
    def admin_click(self, e):
        self.navegar_fun("/admin_login")