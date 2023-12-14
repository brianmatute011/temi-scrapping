Extracción de Tablas desde PDF con pdftables_api
Descripción

Esta aplicación utiliza la librería pdftables_api para facilitar la extracción de tablas con datos desde archivos PDF. La librería pdftables_api permite convertir las tablas en un formato fácilmente manejable, como CSV o Excel, para su posterior análisis.
Requisitos Previos

Antes de utilizar esta aplicación, asegúrate de tener instaladas las siguientes dependencias:

    Python 3.x
    pdftables_api (puedes instalarlo utilizando pip install pdftables-api)

Configuración

    Registra una cuenta en pdftables.com y obtén tu clave de API.
    Copia la clave de API en el archivo de configuración config.json:

json

{
  "api_key": "tu_clave_de_api_aqui"
}

Uso

bash

python extract_tables.py input.pdf

Reemplaza input.pdf con la ruta de tu archivo PDF de origen. El resultado se guardará en un archivo CSV en el mismo directorio.
Ejemplo

bash

python extract_tables.py ejemplo.pdf

Contribuciones

¡Contribuciones son bienvenidas! Si encuentras algún problema o tienes sugerencias de mejora, no dudes en abrir un problema o enviar una solicitud de extracción.
Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para obtener más detalles.

 
