# Analizador de IPs Geográfico y de Reputación

---

##  Descripción del Proyecto

Este proyecto es una herramienta de línea de comandos escrita en Python que permite a los usuarios obtener información detallada sobre direcciones IP. Combina datos geográficos (país, ciudad, ISP, etc.) utilizando la API de **ip-api.com** con información de reputación y posibles reportes de abuso de **AbuseIPDB**.

Es una herramienta útil para análisis básico de inteligencia de amenazas, ciberseguridad, o simplemente para explorar la procedencia y el estado de una dirección IP.

---

##  Características

* **Análisis Geográfico:** Obtiene datos como país, ciudad, región, ISP, latitud y longitud.
* **Análisis de Reputación:** Consulta el score de confianza de abuso, el total de reportes y la última vez que una IP fue reportada por actividades maliciosas (spam, ataques, etc.).
* **Entrada Interactiva:** Permite al usuario ingresar una sola IP o cargar múltiples IPs desde un archivo de texto.
* **Validación Robusta de IPs:** Utiliza la librería `ipaddress` de Python para asegurar que solo las direcciones IP válidas sean procesadas.
* **Exportación a CSV:** Guarda todos los resultados del análisis en un archivo CSV (`informacion_ip_completa.csv`) para facilitar su posterior análisis en hojas de cálculo.
* **Manejo Seguro de API Keys:** Utiliza variables de entorno (`.env`) para mantener las claves de API fuera del código fuente, garantizando la seguridad al compartir el proyecto en repositorios públicos como GitHub.

---

##  Cómo Empezar

Sigue estos pasos para configurar y ejecutar el proyecto en tu máquina local.

### Prerrequisitos

Asegúrate de tener instalado Python 3.x. Puedes descargarlo desde [python.org](https://www.python.org/downloads/).

### Instalación

1.  **Clona el repositorio:**
    ```bash
    git clone [https://github.com/tu_usuario/tu_repositorio.git](https://github.com/tu_usuario/tu_repositorio.git)
    cd tu_repositorio
    ```
    *(Reemplaza `tu_usuario` y `tu_repositorio` con tu nombre de usuario de GitHub y el nombre de tu repositorio)*

2.  **Instala las dependencias:**
    ```bash
    pip install -r requirements.txt
    ```
    *(Si no tienes un `requirements.txt` aún, créalo con `pip freeze > requirements.txt` después de instalar las librerías `requests`, `pandas`, `python-dotenv`.)*

3.  **Obtén tu API Key de AbuseIPDB:**
    * Ve a [AbuseIPDB.com](https://www.abuseipdb.com/) y regístrate para una cuenta gratuita.
    * Inicia sesión y encuentra/genera tu API Key en la sección "API" o "My Account".

4.  **Configura tus variables de entorno:**
    * Crea un archivo llamado `.env` en la raíz de tu proyecto (al mismo nivel que `Mivrr.py`).
    * Dentro de `.env`, añade la siguiente línea, reemplazando `TU_API_KEY_AQUI` con tu clave real de AbuseIPDB:
        ```
        ABUSEIPDB_API_KEY=TU_API_KEY_AQUI
        ```
    * **¡Importante!** Este archivo `.env` está incluido en `.gitignore` y **no será subido a GitHub** para proteger tu clave.

---

##  Cómo Usar

1.  **Ejecuta el script:**
    ```bash
    python Mivrr.py
    ```

2.  **Elige una opción:** El programa te preguntará cómo deseas proporcionar las direcciones IP:
    * `1`: Para ingresar una sola IP por teclado.
    * `2`: Para leer IPs desde un archivo de texto (una IP por línea).

3.  **Proporciona la IP o el archivo:**
    * Si eliges `1`, ingresa la IP cuando se te solicite.
    * Si eliges `2`, ingresa el nombre de tu archivo de texto (ej. `ips.txt`). Asegúrate de que el archivo exista en el mismo directorio o proporciona la ruta completa.

4.  **Resultados:** El script procesará las IPs, mostrando el progreso en la consola. Una vez completado, generará un archivo CSV llamado `informacion_ip_completa.csv` en el mismo directorio, que contendrá todos los datos recolectados. También imprimirá las primeras filas del CSV en la consola.

---

##  Tecnologías Utilizadas

* **Python 3.x**
* **Requests:** Para realizar llamadas HTTP a las APIs.
* **Pandas:**
