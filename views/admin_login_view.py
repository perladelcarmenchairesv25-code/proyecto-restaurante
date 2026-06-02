import flet as ft

class AdminLoginView:
    def __init__(self, page: ft.Page, navegar_fun):
        self.page = page
        self.navegar_fun = navegar_fun

        self.txt_user = ft.TextField(label="Usuario", width=300, bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK)
        self.txt_pass = ft.TextField(label="Contraseña", password=True, can_reveal_password=True, width=300, bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK)
        self.lbl_error = ft.Text("", color=ft.Colors.RED_500, weight="bold")

        btn_ingresar = ft.ElevatedButton(
            content=ft.Text("Ingresar", color=ft.Colors.WHITE),
            style=ft.ButtonStyle(bgcolor="#2D5A27"),
            width=300,
            on_click=self.verificar_credenciales
        )
        
        btn_volver = ft.TextButton(
            "Volver al Menú", 
            on_click=lambda _: self.navegar_fun("/home")
        )

        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Text("Acceso Administrativo", size=24, weight="bold", color=ft.Colors.GREEN_900),
                    ft.Container(height=10),
                    self.txt_user,
                    self.txt_pass,
                    self.lbl_error,
                    ft.Container(height=10),
                    btn_ingresar,
                    btn_volver
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER
            ),
            expand=True,
            bgcolor="#FDF5E6"
        )

    def verificar_credenciales(self, e):
        if self.txt_user.value == "admin" and self.txt_pass.value == "1234":
            self.lbl_error.value = ""
            self.navegar_fun("/admin_panel")
        else:
            self.lbl_error.value = "Usuario o contraseña incorrectos"
            self.page.update()