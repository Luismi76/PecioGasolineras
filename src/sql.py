import requests
import pyodbc
from datetime import datetime

# Configuración
API_URL = "https://sedeaplicaciones.minetur.gob.es/ServiciosRESTCarburantes/PreciosCarburantes/EstacionesTerrestres/"

# Configuración de la conexión a la base de datos
conn_str = (
    r"DRIVER={ODBC Driver 17 for SQL Server};"
    r"SERVER=192.168.0.196,32768;"
    r"DATABASE=GasolinerasDB;"
    r"UID=SA;"
    r"PWD=@Habita76;"
)
conn = pyodbc.connect(conn_str)
cursor = conn.cursor()

def obtener_datos_desde_api():
    """
    Realiza la consulta a la API y devuelve los datos en formato JSON.
    """
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Verifica errores HTTP
        return response.json()  # Retorna los datos en formato JSON
    except requests.exceptions.RequestException as e:
        print(f"Error al consultar la API: {e}")
        return []

def convertir_a_float(valor):
    """
    Convierte una cadena de texto a float, manejando valores vacíos y con comas.
    """
    try:
        return float(valor.replace(',', '.'))
    except (ValueError, AttributeError):
        return 0.0

def guardar_datos_en_sql(nuevos_datos):
    """
    Guarda los nuevos datos en la base de datos SQL.
    """
    fecha_consulta = datetime.now()

    for gasolinera in nuevos_datos["ListaEESSPrecio"]:
        cursor.execute("""
            IF NOT EXISTS (SELECT * FROM Gasolineras WHERE IDEESS = ?)
            BEGIN
                INSERT INTO Gasolineras (IDEESS, Rótulo, Dirección, Municipio, Provincia, Latitud, Longitud, EnServicio)
                VALUES (?, ?, ?, ?, ?, ?, ?, 1)
            END
            ELSE
            BEGIN
                UPDATE Gasolineras
                SET EnServicio = 1
                WHERE IDEESS = ?
            END
        """, (
            gasolinera["IDEESS"],
            gasolinera["IDEESS"],
            gasolinera["Rótulo"],
            gasolinera["Dirección"],
            gasolinera["Municipio"],
            gasolinera["Provincia"],
            convertir_a_float(gasolinera["Latitud"]),
            convertir_a_float(gasolinera["Longitud (WGS84)"]),
            gasolinera["IDEESS"]
        ))

        cursor.execute("""
            INSERT INTO Precios (IDEESS, FechaConsulta, PrecioBiodiesel, PrecioGasoleoA, PrecioGasoleoB, PrecioGasolina95E5, PrecioGasolina98E5)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, (
            gasolinera["IDEESS"],
            fecha_consulta,
            convertir_a_float(gasolinera["Precio Biodiesel"]),
            convertir_a_float(gasolinera["Precio Gasoleo A"]),
            convertir_a_float(gasolinera["Precio Gasoleo B"]),
            convertir_a_float(gasolinera["Precio Gasolina 95 E5"]),
            convertir_a_float(gasolinera["Precio Gasolina 98 E5"])
        ))

    conn.commit()

def main():
    # Obtener los datos nuevos desde la API
    nuevos_datos = obtener_datos_desde_api()
    if not nuevos_datos:
        print("No se obtuvieron nuevos datos.")
        return

    # Guardar los datos en la base de datos SQL
    guardar_datos_en_sql(nuevos_datos)

if __name__ == "__main__":
    main()

# Cerrar la conexión
conn.close()
