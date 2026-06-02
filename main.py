import flet as ft
from views.home_view import HomeView
from views.admin_login_view import AdminLoginView
from views.admin_panel_view import AdminPanelView

def navegar_a(page: ft.Page):
    page.title = "Sistema de Restaurante"
    page.padding = 0
    page.bgcolor = "#FDF5E6"
    
    if not hasattr(page, "productos"):
        page.productos = {
            "COMIDA": [
                {"nombre": "Asado con Puré", "desc": "Carne tierna con puré casero", "precio": "$6.50", "disponible": True},
                {"nombre": "Milanesa de Pollo", "desc": "Con papas fritas", "precio": "$5.00", "disponible": True}
            ],
            "BEBIDAS": [
                {"nombre": "Coca-Cola 500ml", "desc": "Bien fría", "precio": "$1.50", "disponible": True}
            ],
            "POSTRES": [
                {"nombre": "Flan Casero", "desc": "Con dulce de leche", "precio": "$2.50", "disponible": True}
            ]
        }

    def cambiar_ruta(ruta):
        page.controls.clear()
        page.update() 
        
        if ruta == "/home" or ruta == "/":
            vista = HomeView(page, cambiar_ruta)
            if hasattr(vista, "content"):
                vista.content.expand = True
                page.add(vista.content)
        elif ruta == "/admin_login":
            vista = AdminLoginView(page, cambiar_ruta)
            if hasattr(vista, "content"):
                vista.content.expand = True
                page.add(vista.content)
        elif ruta == "/admin_panel":
            vista = AdminPanelView(page, cambiar_ruta)
            if hasattr(vista, "content"):
                vista.content.expand = True
                page.add(vista.content)
                
        page.update()

    cambiar_ruta("/home")

ft.app(target=navegar_a, view=ft.AppView.WEB_BROWSER)