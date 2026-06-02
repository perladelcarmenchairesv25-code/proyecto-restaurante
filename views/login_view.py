import flet as ft

class LoginView:
    # CLAVE AQUÍ TAMBIÉN: self, page y navegar_fun
    def __init__(self, page: ft.Page, navegar_fun):
        self.page = page
        self.navegar_fun = navegar_fun
        
        self.titulo = ft.Text(
            "Bienvenido de nuevo", 
            size=32, 
            weight=ft.FontWeight.BOLD, 
            color=ft.Colors.GREEN_900
        )
        
        self.subtitulo = ft.Text(
            "Ingresa tus credenciales para continuar",
            color=ft.Colors.BLACK54
        )

        self.txt_user = ft.TextField(
            label="Correo electrónico o Usuario",
            border_radius=15,
            border_color=ft.Colors.GREEN_900,
            width=320
        )

        self.txt_pass = ft.TextField(
            label="Contraseña",
            password=True,
            can_reveal_password=True,
            border_radius=15,
            border_color=ft.Colors.GREEN_900,
            width=320
        )

        self.btn_entrar = ft.ElevatedButton(
            content=ft.Text("Iniciar Sesión", color=ft.Colors.WHITE, weight="bold"),
            style=ft.ButtonStyle(
                bgcolor=ft.Colors.GREEN_800,
                shape=ft.RoundedRectangleBorder(radius=15),
            ),
            width=320,
            height=50,
            on_click=self.login_click
        )

        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="/logo.png", width=120),
                    self.titulo,
                    self.subtitulo,
                    ft.Container(height=20),
                    self.txt_user,
                    self.txt_pass,
                    ft.Text("¿Olvidaste tu contraseña?", color=ft.Colors.GREEN_900, size=12, weight="bold"),
                    ft.Container(height=10),
                    self.btn_entrar,
                    ft.Row(
                        [
                            ft.Text("¿No tienes cuenta?"),
                            ft.TextButton(
                                content=ft.Text("Regístrate", color=ft.Colors.GREEN_900, weight="bold")
                            )
                        ],
                        alignment=ft.MainAxisAlignment.CENTER
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.Alignment(0, 0),
            expand=True,
            bgcolor="#FDF5E6"
        )

    def login_click(self, e):
        # Nos movemos directo al Home
        self.navegar_fun("/home")