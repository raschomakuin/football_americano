import flet as ft
from supabase import create_client

# Reemplazá con tu URL y API KEY de Supabase
SUPABASE_URL = "https://zfvfbynsfljtrcqawefs.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InpmdmZieW5zZmxqdHJjcWF3ZWZzIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NTIxMTIwNDksImV4cCI6MjA2NzY4ODA0OX0.oJaevKWnn-24JPObgmx0btUFQpO7dp953FZETnEfeyE"

supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

def main(page: ft.Page):
    page.title = "Liga Football Americano"
    page.scroll = "auto"
    page.add(ft.Text("¡Bienvenido a Football Americano en Córdoba!", size=24, weight="bold"))

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
            ft.Text(f"🏈 {e['NOMBRE_EQUIPO']}", size=20)
            for e in equipos_data
        ]
    )

    # Jugadores
    jugadores_data = cargar_tabla("JUGADORES")
    jugadores_column = ft.Column(
        controls=[
            ft.Text(f"{j['NOMBRE']} - DNI: {j['DNI']} - Nac: {j['FECHA_NACIMIENTO']}")
            for j in jugadores_data
        ]
    )

    # Socios
    socios_data = cargar_tabla("TIPO_SOCIO")
    socios_column = ft.Column(
        controls=[
            ft.Text(f"👤 {s['socio_DESCRIPCION']}", size=18)
            for s in socios_data
        ]
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
