# Usa una imagen base oficial de Python
FROM python:3.9-slim

# Instala cron, unixODBC, gnupg y curl
RUN apt-get update && apt-get install -y \
    cron \
    unixodbc-dev \
    gnupg \
    curl

# Instala el controlador ODBC para SQL Server
RUN curl https://packages.microsoft.com/keys/microsoft.asc | apt-key add - \
    && curl https://packages.microsoft.com/config/debian/10/prod.list > /etc/apt/sources.list.d/msprod.list \
    && apt-get update \
    && ACCEPT_EULA=Y apt-get install -y msodbcsql17

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos necesarios al contenedor
COPY . /app

# Instala las dependencias necesarias
RUN pip install --no-cache-dir -r requirements.txt

# Copia el archivo crontab y el script de inicialización
COPY crontab /etc/cron.d/mi-trabajo-programado
COPY entrypoint.sh /entrypoint.sh

# Da permisos de ejecución a los scripts
RUN chmod 0644 /etc/cron.d/mi-trabajo-programado
RUN chmod +x /entrypoint.sh

# Aplica la crontab
RUN crontab /etc/cron.d/mi-trabajo-programado

# Crear el archivo de log si no existe
RUN touch /var/log/cron.log

# Comando de inicio
CMD ["/entrypoint.sh"]
