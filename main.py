import flet as ft
from supabase import create_client

# Reemplazá con tu URL y API KEY de Supabase
SUPABASE_URL = "https://zfvfbynsfljtrcqawefs.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpmdmZieW5zZmxqdHJjcWF3ZWZzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTIxMTIwNDksImV4cCI6MjA2NzY4ODA0OX0.oJaevKWnn-24JPObgmx[...]"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def main(page: ft.Page):
    page.title = "Liga Football Americano"
    page.bgcolor = "#ECEFF1" 
    page.scroll = "auto"
    page.padding = 20
    page.spacing = 10

    # Título principal centrado y destacado
    page.add(
        ft.Container(
            ft.Text(
                "🏈 ¡Bienvenido a Football Americano en Córdoba! 🏈",
                size=32,
                weight="bold",
                color="#BBDEFB",
                text_align=ft.TextAlign.CENTER,
                expand=True,
            ),
            margin=ft.margin.only(bottom=20),
        )
    )

    def cargar_tabla(nombre_tabla):
        try:
            resultado = supabase.table(nombre_tabla).select("*").execute()
            return resultado.data
        except Exception as e:
            print(f"Error cargando {nombre_tabla}: {e}")
            return []

    # Equipos
    equipos_data = cargar_tabla("EQUIPOS")
    equipos_column = ft.Column(
        controls=[
            ft.Card(
                content=ft.Container(
                    ft.Row([
                        ft.Icon(ft.icons.SPORTS_FOOTBALL, color="#FF9800"),
                        ft.Text(e['NOMBRE_EQUIPO'], size=20, weight="bold"),
                    ]),
                    padding=10,
                ),
                elevation=4,
                margin=5,
                bgcolor="#0D47A1",
                border_radius=12,
            )
            for e in equipos_data
        ],
        scroll="auto",
        spacing=8,
    )

    # Jugadores
    jugadores_data = cargar_tabla("JUGADORES")
    jugadores_column = ft.Column(
        controls=[
            ft.Card(
                content=ft.Container(
                    ft.Column([
                        ft.Text(j['NOMBRE'], size=18, weight="bold", color="#0D47A1" ),
                        ft.Text(f"DNI: {j['DNI']}"),
                        ft.Text(f"Fecha Nac: {j['FECHA_NACIMIENTO']}"),
                    ]),
                    padding=10,
                ),
                elevation=3,
                margin=5,
                bgcolor="#BBDEFB",
                border_radius=10,
            )
            for j in jugadores_data
        ],
        scroll="auto",
        spacing=8,
    )

    # Socios
    socios_data = cargar_tabla("TIPO_SOCIO")
    socios_column = ft.Column(
        controls=[
            ft.Card(
                content=ft.Container(
                    ft.Row([
                        ft.Icon(ft.icons.PERSON, color="#BBDEFB"),
                        ft.Text(s['socio_DESCRIPCION'], size=18),
                    ]),
                    padding=10,
                ),
                elevation=2,
                margin=5,
                bgcolor="#BBDEFB",
                border_radius=10,
            )
            for s in socios_data
        ],
        scroll="auto",
        spacing=8,
    )

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Equipos", content=equipos_column),
            ft.Tab(text="Jugadores", content=jugadores_column),
            ft.Tab(text="Socios", content=socios_column),
        ],
        expand=True,
    )

    page.add(tabs)

ft.app(target=main, view=ft.WEB_BROWSER)

