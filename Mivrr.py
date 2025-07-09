import requests
import json
import pandas as pd # Import Pandas
import ipaddress
import os
from dotenv import load_dotenv

load_dotenv()

ABUSEIPDB_API_KEY = os.getenv('ABUSEIPDB_API_KEY')

if not ABUSEIPDB_API_KEY:
     print("Error: No se encontro la API Key de AbuseIPDB.")
     exit()

def obtener_ip_publica():
    """
    Intenta obtener la IP pública del usuario a través de una API externa.
    """
    try:
        response = requests.get("https://api.ipify.org?format=json")
        response.raise_for_status() # Raises an HTTPError for bad responses (4xx or 5xx)
        ip_data = response.json()
        return ip_data["ip"]
    except requests.exceptions.RequestException as e:
        print(f"No se pudo obtener la IP pública automáticamente: {e}")
        return None

def analizar_ip(ip_address):
    """
    Consulta la API de ip-api.com para obtener información de una dirección IP.
    """
    base_url = "http://ip-api.com/json/"
    full_url = f"{base_url}{ip_address}"

    print(f"Consultando información para la IP: {ip_address}...")

    try:
        response = requests.get(full_url)
        response.raise_for_status()

        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error al conectar con la API de IP-API.com: {e}")
        return None

# --- Main program logic ---
# This line MUST NOT have any indentation.
if __name__ == "__main__":
    ips_a_analizar = []
    
    print("\n--- Analizador de informacion de IP ---")
    print("¿Cómo deseas proporcionar las direcciones IP?")
    print("1. Ingresar una sola IP por teclado")
    print("2. Leer IPs desde un rachivo de texto (.txt), una IP por linea")

    opcion = input("Elige una opción (1 o 2):").strip()

    if opcion == '1':
        ip_ingresada = input("Ingresa la direccion IP a analizar: ").strip()
        if ip_ingresada:
            try:
                ipaddress.ip_address(ip_ingresada)
                ips_a_analizar.append(ip_ingresada)
                print(f"IP '{ip_ingresada}' validada y añadida a la lista.") 
            except ValueError:
                          print(f"Error: '{ip_ingresada}' no es una direccion IP valida. Saliendo del programa.")
        else:
            print("No se ingresó ninguna IP. Saliendo del programa.")
            exit()
        if not ips_a_analizar:
             print("No se encontraron direcciones IP validad para analizar. Saliendo del programa") 
             exit()   

elif opcion == '2':
    nombre_archivo = input("Ingresa el nombre del archivo de texto (ej. ips.txt): ").strip()

    try:
         with open(nombre_archivo, 'r') as f:
             for line in f:
                 ip_limpia = line.strip()
                 if ip_limpia:
                    ips_a_analizar.append(ip_limpia)   
         if not ips_a_analizar:
             print("El archivo '{nombre_archivo}' no contiene IPs válidas o está vacío. Saliendo.")
             exit()
         print(f"IPs cargadas desde '{nombre_archivo}'")
    except FileNotFoundError:
        print(f"Ocurrio un error al leer el archivo: {e}. Saliendo del programa")
        exit()

else:
    print("Opcion no valida. Saliendo del programa.")
    exit()
             
     

resultados_analisis = []

    
for ip in ips_a_analizar:
        ip_info = analizar_ip(ip)

        
        if ip_info and ip_info.get('status') == 'success': 
            resultados_analisis.append({
                'IP': ip_info.get('query', 'N/A'),
                'Pais': ip_info.get('country', 'N/A'),
                'Codigo_Pais': ip_info.get('countryCode', 'N/A'),
                'Region': ip_info.get('regionName', 'N/A'),
                'Ciudad': ip_info.get('city', 'N/A'),
                'Zona_Horaria': ip_info.get('timezone', 'N/A'),
                'ISP': ip_info.get('isp', 'N/A'),
                'Organizacion': ip_info.get('org', 'N/A'),
                'Latitud': ip_info.get('lat', 'N/A'),
                'Longitud': ip_info.get('lon', 'N/A'),
                'Estatus_API': ip_info.get('status', 'N/A')
            })
            print(f"Información de {ip} procesada con éxito.")
        else:
            # Added a check for ip_info before trying to access its message
            error_message = ip_info.get('message', 'No message from API.') if ip_info else 'Error: No data received.'
            print(f"No se pudo obtener información exitosa para la IP: {ip}. Mensaje: {error_message}")

    # --- PANDAS AND CSV EXPORT LOGIC ---
    # This block MUST be outside the 'for' loop, but still inside the '__main__' block.
print("\nAnálisis de IPs completado.")
if resultados_analisis: # Only proceed if there are results to save
        df_resultados = pd.DataFrame(resultados_analisis)
        nombre_archivo_csv = "informacion_ip.csv"
        df_resultados.to_csv(nombre_archivo_csv, index=False)
        print(f"Resultados guardados exitosamente en '{nombre_archivo_csv}'")
        print("\nContenido del archivo CSV (primeras 5 filas):")
        print(df_resultados.head().to_string()) # Display first 5 rows in console
else:
        print("No se generaron resultados para guardar en CSV.")

