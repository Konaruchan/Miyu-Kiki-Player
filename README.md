# MiyuKikiPlayer

¡Bienvenido a MiyuKikiPlayer! Este es un software sencillo y humilde creado para permitir la experiencia de juego de **Miyu-Kiki Chaos Club!**, una novela gráfica spin-off del manga **"Miyubo!"** creado por **Konaru** y publicado en **"Shikashi Monthly Friday"**.

## Características Principales

- **Interfaz Amigable**: Interfaz gráfica sencilla y fácil de usar.
- **Reproducción de Música**: Reproduce música de fondo mientras juegas.
- **Compatibilidad**: Requiere Microsoft PowerPoint (recomendado 2021 o superior) para funcionar.

## Instalación

### Paso 1: Descargar el Cliente

1. Dirígete a la sección de [Releases](https://github.com/Konaruchan/Miyu-Kiki-Player/releases).
2. Descarga el archivo `Miyu-kiki_Client.zip`.

### Paso 2: Descomprimir el Archivo

1. Una vez descargado, descomprime `Miyu-kiki_Client.zip` en una carpeta de tu elección.
2. Dentro de la carpeta descomprimida, encontrarás varios archivos y carpetas necesarias para el juego.

### Paso 3: Instalación

1. Ejecuta el archivo `MiyuKikiPlayer_Installer.exe`.
2. Sigue las instrucciones del instalador para completar la instalación del juego.

### Paso 4: Mover Carpetas Necesarias

**Nota Importante**: Después de la instalación, debes realizar el siguiente paso manualmente:
1. Navega a la carpeta donde se ha instalado el juego (por ejemplo, `C:\Program Files (x86)\MiyuKikiPlayer\`).
2. Dentro de esta carpeta, crea una nueva carpeta llamada `GameFiles`.
3. Mueve las carpetas `BGM`, `Definitions` y `Shika` a la nueva carpeta `GameFiles` que acabas de crear.

### Paso 5: Ejecutar el Juego

1. Abre **MiyuKikiPlayer** desde el menú de inicio o el acceso directo en tu escritorio.
2. Si tu antivirus marca el archivo como una amenaza potencial, desactiva temporalmente la protección en tiempo real del antivirus. Esto es debido a que el ejecutable es de reciente creación y no tiene un certificado digital oficial.
3. Una vez iniciado el juego, vuelve a activar el antivirus.

## Cómo Funciona el Programa

### Estructura del Proyecto

- **main.py**: Punto de entrada principal del programa. Inicia la interfaz gráfica y el juego.
- **player.py**: Contiene la clase `MiyuKikiPlayer` que maneja la lógica del juego.
- **music_manager.py**: Maneja la reproducción de música de fondo.
- **defi_parser.py**: Analiza y maneja los archivos de definición del juego.
- **GameFiles/**: Carpeta que contiene los archivos del juego:
  - **BGM/**: Archivos de música (mp3).
  - **Definitions/**: Archivos de definición del juego (defi).
  - **Shika/**: Archivos de la novela gráfica (shika).

### Uso del Programa

1. **Iniciar Juego**: Al ejecutar `MiyuKikiPlayer`, se carga el archivo `miyu_kiki.shika` y la música de fondo correspondiente.
2. **Reproducción de Diapositivas**: Utiliza PowerPoint para mostrar las diapositivas del juego.
3. **Controles**:
   - **Quick Save**: Guarda el estado actual del juego.
   - **Quick Load**: Carga el estado guardado del juego.
   - **Check for Updates**: Comprueba si hay actualizaciones disponibles para el juego.
   - **Show Changelog**: Muestra el historial de cambios del juego.

### Actualizaciones

- **Actualización del Juego**: El juego se puede actualizar directamente desde el programa.
- **Actualización del Cliente**: El cliente debe actualizarse manualmente. Visita la sección de [Releases](https://github.com/Konaruchan/Miyu-Kiki-Player/releases) para descargar la última versión.

## Nota Importante

El contenido dentro del juego, como música, sprites y demás, pertenecen al autor, Konaru, y no se pueden distribuir sin permiso.

Para cualquier pregunta o soporte, no dudes en abrir un [issue](https://github.com/Konaruchan/Miyu-Kiki-Player/issues) en el repositorio.

¡Gracias por jugar Miyu-Kiki Chaos Club! ¡Disfruta del juego!

