import flet as ft
from supabase import create_client

# Reemplazá con tu URL y API KEY de Supabase
SUPABASE_URL = "https://tu-proyecto.supabase.co"
SUPABASE_KEY = "tu-clave-api"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def main(page: ft.Page):
    page.title = "Liga Football Americano"
    page.scroll = "auto"

    def cargar_tabla(nombre_tabla):
        return supabase.table(nombre_tabla).select("*").execute().data

    # Equipos
    equipos_data = cargar_tabla("equipos")
    equipos_column = ft.Column(
        controls=[ft.Text(f"🏈 {e['nombre_equipo']}", size=20) for e in equipos_data]
    )

    # Jugadores
    jugadores_data = cargar_tabla("jugadores")
    jugadores_column = ft.Column(
        controls=[
            ft.Text(f"{j['nombre']} - DNI: {j['dni']} - Nac: {j['fecha_nacimiento']}")
            for j in jugadores_data
        ]
    )

    # Socios
    socios_data = cargar_tabla("socios")
    socios_column = ft.Column(
        controls=[ft.Text(f"👤 {s['nombre_socio']}", size=18) for s in socios_data]
    )

    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        tabs=[
            ft.Tab(text="Equipos", content=equipos_column),
            ft.Tab(text="Jugadores", content=jugadores_column),
            ft.Tab(text="Socios", content=socios_column),
        ],
    )

    page.add(tabs)

ft.app(target=main, view=ft.WEB_BROWSER)
