import flet as ft

class SplashView:
    def __init__(self, page: ft.Page, navegar_fun):
        self.page = page
        self.navegar_fun = navegar_fun 
        
        # Botón que ahora apunta directamente al catálogo de comida
        self.btn_comenzar = ft.ElevatedButton(
            content=ft.Text("Ver Menú", color=ft.Colors.WHITE, weight="bold", size=16),
            style=ft.ButtonStyle(
                bgcolor="#2D5A27", 
                shape=ft.RoundedRectangleBorder(radius=15),
            ),
            width=280,
            height=50,
            on_click=self.comenzar_click
        )

        self.content = ft.Container(
            content=ft.Column(
                [
                    ft.Image(src="/logo.png", width=250),
                    ft.Container(height=10), 
                    ft.Text("BIENVENIDOS", size=20, weight="bold", color="#4A4A4A"),
                    ft.Text("VALLE ENCANTADO", size=32, weight="bold", color="#2D5A27"),
                    ft.Text("Sabor natural en cada plato", italic=True, color="#4A4A4A"),
                    ft.Container(height=40),
                    self.btn_comenzar
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            alignment=ft.Alignment(0, 0),
            expand=True,
            bgcolor="#FDF5E6"
        )

    def comenzar_click(self, e):
        # CAMBIO CLAVE: Viaja directo al Home (Menú de categorías) sin escalas
        self.navegar_fun("/home")