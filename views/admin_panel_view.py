import flet as ft

class AdminPanelView:
    def __init__(self, page: ft.Page, navegar_fun):
        self.page = page
        self.navegar_fun = navegar_fun

        # Componentes para AGREGAR nuevo producto
        self.dd_categoria = ft.Dropdown(
            label="Categoría",
            options=[
                ft.dropdown.Option("COMIDA"),
                ft.dropdown.Option("BEBIDAS"),
                ft.dropdown.Option("POSTRES"),
            ],
            width=320, bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK
        )
        self.txt_nombre = ft.TextField(label="Nombre del Platillo", width=320, bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK)
        self.txt_desc = ft.TextField(label="Descripción breve", width=320, bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK)
        self.txt_precio = ft.TextField(label="Precio (Ej: $4.50)", width=320, bgcolor=ft.Colors.WHITE, color=ft.Colors.BLACK)

        # Contenedores dinámicos para las listas
        self.lista_eliminar = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, height=400)
        self.lista_disponibilidad = ft.Column(spacing=10, scroll=ft.ScrollMode.AUTO, height=500)

        # Cargar los datos iniciales
        self.actualizar_listas_admin()

        # PESTAÑA 1: Formulario Agregar + Lista Eliminar
        pestana_gestion = ft.Column(
            [
                ft.Text("Añadir Producto", size=18, weight="bold", color=ft.Colors.GREEN_900),
                self.dd_categoria,
                self.txt_nombre,
                self.txt_desc,
                self.txt_precio,
                ft.ElevatedButton(
                    content=ft.Text("Guardar Producto", color=ft.Colors.WHITE, weight="bold"),
                    style=ft.ButtonStyle(bgcolor="#2D5A27", shape=ft.RoundedRectangleBorder(radius=10)),
                    width=320, height=40, on_click=self.agregar_producto
                ),
                ft.Divider(height=30, color=ft.Colors.GREY_400),
                ft.Text("Eliminar Productos Definitivamente", size=16, weight="bold", color=ft.Colors.RED_700),
                self.lista_eliminar
            ],
            scroll=ft.ScrollMode.AUTO
        )

        # PESTAÑA 2: Control de disponibilidad (Menú del día)
        pestana_disponibilidad = ft.Column(
            [
                ft.Text("Disponibilidad del Día", size=18, weight="bold", color=ft.Colors.GREEN_900),
                ft.Text("Desactiva los platos agotados temporalmente:", size=13, color=ft.Colors.BLACK54),
                ft.Container(height=10),
                self.lista_disponibilidad
            ]
        )

        # Diseño de la barra superior
        header = ft.Row(
            [
                ft.Text("Panel Admin", size=24, weight="bold", color=ft.Colors.GREEN_900),
                ft.IconButton(icon=ft.Icons.LOGOUT, icon_color=ft.Colors.RED_600, on_click=lambda _: self.navegar_fun("/home"))
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )

        # 1. Creamos las pestañas vacías primero
        tab1 = ft.Tab()
        tab1.label = "Gestión Base" # ¡CORREGIDO! Usamos estrictamente '.label'

        tab2 = ft.Tab()
        tab2.label = "Menú del Día" # ¡CORREGIDO! Usamos estrictamente '.label'

        # 2. Configuración de la barra de pestañas (TabBar)
        barra_pestanas = ft.TabBar(
            tabs=[tab1, tab2]
        )

        # 3. Contenedor de las vistas (TabBarView)
        vista_pestanas = ft.TabBarView(
            controls=[
                pestana_gestion,
                pestana_disponibilidad
            ]
        )

        # 4. Inicialización de las Tabs principales de la página
        self.tabs = ft.Tabs(
            length=2,
            content=ft.Column([
                barra_pestanas,
                ft.Container(content=vista_pestanas, expand=True)
            ], expand=True),
            expand=1
        )

        # Contenedor padre de la vista
        self.content = ft.Container(
            content=ft.Column([header, ft.Container(height=10), self.tabs], expand=True),
            expand=True,
            bgcolor="#FDF5E6",
            padding=20
        )

    def actualizar_listas_admin(self):
        self.lista_eliminar.controls.clear()
        self.lista_disponibilidad.controls.clear()

        for cat, items in self.page.productos.items():
            self.lista_eliminar.controls.append(ft.Text(f"--- {cat} ---", weight="bold", color=ft.Colors.GREEN_700))
            self.lista_disponibilidad.controls.append(ft.Text(f"--- {cat} ---", weight="bold", color=ft.Colors.GREEN_700))

            for index, item in enumerate(items):
                # Fila Eliminar
                fila_del = ft.Row(
                    [
                        ft.Text(f"{item['nombre']} ({item['precio']})", size=14, color=ft.Colors.BLACK, expand=True),
                        ft.IconButton(
                            icon=ft.Icons.DELETE_FOREVER,
                            icon_color=ft.Colors.RED_500,
                            on_click=lambda _, c=cat, i=index: self.eliminar_producto(c, i)
                        )
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
                self.lista_eliminar.controls.append(fila_del)

                # Fila Disponibilidad
                switch_disp = ft.Switch(
                    label=item['nombre'],
                    value=item['disponible'],
                    on_change=lambda e, c=cat, i=index: self.cambiar_disponibilidad(c, i, e.control.value)
                )
                self.lista_disponibilidad.controls.append(switch_disp)

    def agregar_producto(self, e):
        if not self.dd_categoria.value or not self.txt_nombre.value or not self.txt_precio.value:
            return

        nuevo = {
            "nombre": self.txt_nombre.value,
            "desc": self.txt_desc.value,
            "precio": self.txt_precio.value if "$" in self.txt_precio.value else f"${self.txt_precio.value}",
            "disponible": True
        }

        self.page.productos[self.dd_categoria.value].append(nuevo)
        
        self.txt_nombre.value = ""
        self.txt_desc.value = ""
        self.txt_precio.value = ""
        
        self.actualizar_listas_admin()
        self.page.update()

    def eliminar_producto(self, categoria, index):
        self.page.productos[categoria].pop(index)
        self.actualizar_listas_admin()
        self.page.update()

    def cambiar_disponibilidad(self, categoria, index, valor_switch):
        self.page.productos[categoria][index]["disponible"] = valor_switch
        self.page.update()