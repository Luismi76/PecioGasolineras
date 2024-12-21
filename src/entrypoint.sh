#!/bin/bash

# Crear el archivo de log si no existe
touch /var/log/cron.log

# Iniciar cron
service cron start

# Mantener el contenedor en ejecución
tail -f /var/log/cron.log
