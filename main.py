import flet as ft
# Asegúrate de importar tus vistas correctamente de tu carpeta views
from views.home_view import HomeView
from views.admin_login_view import AdminLoginView
from views.admin_panel_view import AdminPanelView

def navegar_a(page: ft.Page):
    # 1. Configuración inicial de la página para la Web
    page.title = "Sistema de Restaurante"
    page.padding = 0
    page.bgcolor = "#FDF5E6"
    
    # Datos globales compartidos de tu restaurante (tu base de datos simulada)
    if not hasattr(page, "productos"):
        page.productos = {
            "COMIDA": [
                {"nombre": "Asado con Puré", "desc": "Carne tierna con puré casero", "precio": "$6.50", "disponible": True},
                {"nombre": "Milanesa de Pollo", "desc": "Con papas fritas crujientes", "precio": "$5.00", "disponible": True}
            ],
            "BEBIDAS": [
                {"nombre": "Coca-Cola 500ml", "desc": "Bien fría", "precio": "$1.50", "disponible": True},
                {"nombre": "Jugo Natural", "desc": "Naranja o zanahoria", "precio": "$2.00", "disponible": True}
            ],
            "POSTRES": [
                {"nombre": "Flan Casero", "desc": "Con dulce de leche", "precio": "$2.50", "disponible": True}
            ]
        }

    # 2. Función interna para manejar el enrutamiento (cambio de vistas)
    def cambiar_ruta(ruta):
        page.controls.clear()
        
        if ruta == "/home" or ruta == "/":
            vista = HomeView(page, cambiar_ruta)
            page.add(vista.content)
        elif ruta == "/admin_login":
            vista = AdminLoginView(page, cambiar_ruta)
            page.add(vista.content)
        elif ruta == "/admin_panel":
            vista = AdminPanelView(page, cambiar_ruta)
            page.add(vista.content)
            
        page.update()

    # 3. Cargar la vista inicial por defecto
    cambiar_ruta("/home")

# ==============================================================================
# ¡LA LÍNEA CLAVE PARA RENDER!
# En lugar de ft.app(target=navegar_a), usamos esta firma estricta para web:
# ==============================================================================
ft.app(target=navegar_a, view=ft.AppView.WEB_BROWSER)