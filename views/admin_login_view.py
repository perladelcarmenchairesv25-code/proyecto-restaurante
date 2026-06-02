import flet as ft

class AdminLoginView:
    def __init__(self, page: ft.Page, navegar_fun):
        self.page = page
        self.navegar_fun = navegar_fun

        # Título principal
        self.titulo = ft.Text(
            "Acceso Admin",
            size=28,
            weight=ft.FontWeight.BOLD,
            color=ft.Colors.GREEN_900
        )

        # Campo de texto para el Usuario
        self.txt_usuario = ft.TextField(
            label="Usuario",
            width=280,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
            hint_text="Ej: admin"
        )

        # Campo de texto para la contraseña
        self.txt_clave = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            width=280,
            bgcolor=ft.Colors.WHITE,
            color=ft.Colors.BLACK,
        )

        # Texto para mostrar mensajes de error
        self.txt_error = ft.Text(
            "",
            color=ft.Colors.RED_600,
            size=14,
            weight="bold"
        )

        # Botón para ingresar
        self.btn_ingresar = ft.ElevatedButton(
            content=ft.Text("Entrar al Panel", color=ft.Colors.WHITE, weight="bold"),
            style=ft.ButtonStyle(
                bgcolor="#2D5A27",
                shape=ft.RoundedRectangleBorder(radius=10),
            ),
            width=280,
            height=45,
            on_click=self.verificar_credenciales
        )

        # Botón para regresar al Home
        self.btn_cancelar = ft.TextButton(
            content=ft.Text("Volver al Menú", color=ft.Colors.GREEN_900, size=14),
            on_click=lambda _: self.navegar_fun("/home")
        )

        # Contenedor de la vista completa
        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="/logo.png", width=100),
                    ft.Container(height=10),
                    self.titulo,
                    ft.Text("Sistemas de control interno", color=ft.Colors.BLACK54, size=14),
                    ft.Container(height=20),
                    
                    self.txt_usuario,   # Caja de texto 1: Usuario
                    ft.Container(height=10),
                    self.txt_clave,     # Caja de texto 2: Contraseña
                    
                    self.txt_error,     # Alerta de error
                    ft.Container(height=10),
                    self.btn_ingresar,
                    ft.Container(height=15),
                    self.btn_cancelar
                ], # <- CORRECCIÓN: Aquí se cierra correctamente la lista de controles de la columna
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.Alignment(0, 0),
            expand=True,
            bgcolor="#FDF5E6",
            padding=20
        )

    # Lógica de validación
    def verificar_credenciales(self, e):
        if self.txt_usuario.value == "admin" and self.txt_clave.value == "1234":
            self.txt_error.value = ""
            self.page.update()
            self.navegar_fun("/admin_panel")
        else:
            self.txt_error.value = "Usuario o contraseña incorrectos."
            self.txt_usuario.value = ""
            self.txt_clave.value = ""
            self.page.update()