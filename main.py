import sys
import os
import flet as ft

# TRUCO DEFINITIVO: Asegura que Python encuentre la carpeta 'views' sin importar cómo ejecutes el script
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from views.splash_view import SplashView
from views.home_view import HomeView
from views.menu_view import MenuView
from views.admin_login_view import AdminLoginView
from views.admin_panel_view import AdminPanelView 

def main(page: ft.Page):
    page.title = "Valle Encantado"
    page.window_width = 400
    page.window_height = 750
    page.window_resizable = False

    # BASE DE DATOS CENTRALIZADA
    if not hasattr(page, "productos"):
        page.productos = {
            "COMIDA": [
                {"nombre": "Hamburguesa Artesanal", "desc": "Carre de res, queso fundido y vegetales.", "precio": "$8.50", "disponible": True},
                {"nombre": "Asado Valle Encantado", "desc": "Corte premium con guarnición rústica.", "precio": "$12.00", "disponible": True},
                {"nombre": "Pasta Alfredo", "desc": "Salsa cremosa con pollo a la plancha.", "precio": "$9.50", "disponible": True},
            ],
            "BEBIDAS": [
                {"nombre": "Limonada Imperial", "desc": "Con un toque de menta y jengibre.", "precio": "$2.50", "disponible": True},
                {"nombre": "Café de la Finca", "desc": "Filtrado al momento, aroma intenso.", "precio": "$2.00", "disponible": True},
                {"nombre": "Jugo Natural", "desc": "Frutas de temporada 100% exprimidas.", "precio": "$3.00", "disponible": True},
            ],
            "POSTRES": [
                {"nombre": "Volcán de Chocolate", "desc": "Centro líquido con helado de vainilla.", "precio": "$4.50", "disponible": True},
                {"nombre": "Cheesecake de Frutos", "desc": "Base crujiente y mermelada artesanal.", "precio": "$4.00", "disponible": True},
                {"nombre": "Flan Casero", "desc": "Receta tradicional con caramelo.", "precio": "$3.50", "disponible": True},
            ]
        }

    def navegar_a(ruta):
        page.views.clear()
        
        if ruta == "/":
            splash = SplashView(page, navegar_a)
            page.views.append(ft.View(route="/", controls=[splash.content], padding=0))
            
        elif ruta == "/home":
            home = HomeView(page, navegar_a)
            page.views.append(ft.View(route="/home", controls=[home.content], padding=0))
            
        elif ruta.startswith("/menu_"):
            categoria = ruta.replace("/menu_", "")
            menu = MenuView(page, categoria, navegar_a)
            page.views.append(ft.View(route=ruta, controls=[menu.content], padding=0))
            
        elif ruta == "/admin_login":
            admin_login = AdminLoginView(page, navegar_a)
            page.views.append(ft.View(route="/admin_login", controls=[admin_login.content], padding=0))
            
        elif ruta == "/admin_panel":
            admin_panel = AdminPanelView(page, navegar_a)
            page.views.append(ft.View(route="/admin_panel", controls=[admin_panel.content], padding=0))
            
        page.update()

    navegar_a("/")

ft.run(main, assets_dir="assets")