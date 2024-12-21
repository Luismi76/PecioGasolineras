# 🚀 Proyecto de Precios de Gasolineras en España 🚀

¡Bienvenido/a a este emocionante proyecto! Aquí rastreamos y analizamos los precios de los combustibles en las gasolineras de toda España utilizando datos proporcionados por el Ministerio de Industria. 🌍⛽️

## Descripción

Este proyecto recopila datos de los precios de los combustibles desde una API del Ministerio de Industria, los almacena en una base de datos SQL Server y los presenta de manera visual utilizando Power BI. Todo está desplegado en un contenedor Docker ejecutándose en un servidor local dentro de una máquina virtual gestionada por Proxmox.

## Características

- **Consulta y procesamiento de datos en tiempo real** 📊
- **Visualización de datos con Power BI** 📈
- **Automatización mediante scripts en Python** 🐍
- **Despliegue utilizando Docker** 🐳
- **Entorno seguro y eficiente con Proxmox** 🖥️

## Instalación

Sigue estos pasos para clonar el repositorio y poner en marcha el proyecto en tu máquina local:

1. Clona este repositorio:
   ```bash
   git clone https://github.com/tu-usuario/Gasolineras-Precios.git
   cd Gasolineras-Precios
   ```
2. Configura y ejecuta Docker:

    ```bash
    docker-compose up --build
    ```
## Uso
Una vez configurado, puedes ejecutar el script de Python para recopilar y almacenar los datos de los combustibles:

  
    python obtener_precios.py
  
    
Luego, abre Power BI y conecta a la base de datos SQL Server para visualizar los datos y crear tus propios informes interactivos.

## Contribución
  ¡Nos encantaría que contribuyas a este proyecto! Puedes hacerlo de las siguientes maneras:

  #### Reportar errores: Abre un issue en GitHub si encuentras algún problema.
  
  #### Mejoras y características: Realiza un fork del proyecto, crea una nueva rama con tus mejoras y envía un pull request.
  
  #### Ideas y sugerencias: Comparte tus ideas a través de los issues o en la sección de discusiones.

## Contacto
  Si tienes alguna pregunta o necesitas ayuda, no dudes en contactarme a través de LinkedIn o enviar un correo a princiapl@lmsc.es.
