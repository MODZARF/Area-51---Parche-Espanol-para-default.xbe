# Area-51---Parche-Espanol-para-default.xbe
Script en Python que edita el `default.xbe` del juego Area 51 de Xbox Clásico para forzar la carga del idioma español, tanto textos como voces.
Este es el código fuente del parche que había compartido en YouTube. YouTube eliminó el .exe por considerarlo un archivo peligroso, por eso ahora se comparte directamente el código aquí en GitHub.

### ¿Qué hace?
Modifica los bytes necesarios dentro del `default.xbe` para que el juego, aun siendo la versión NTSC (USA), cargue los archivos de idioma en español en lugar del inglés.

No necesitas re-empaquetar nada, solo reemplazar el .xbe.

### Requisitos
- Tener el `default.xbe` ORIGINAL del juego Area 51 región NTSC.

### Cómo usarlo

**Opción 1: Usando el script de Python**
1. Descarga el archivo `a52.py` de este repositorio.
2. Pon tu `default.xbe` original en la misma carpeta que `a52.py`.
3. Ejecuta `a52.py` con Python.

**Opción 2: Usando el .exe compilado**
1. Ve a la pestaña `Releases` de este repositorio.
2. Descarga el `a52.exe`.
3. Pon tu `default.xbe` original al lado del `a52.exe`.
4. Ejecuta el .exe.

En ambos casos, el script creará automáticamente una carpeta con el nombre del mod en la misma ruta, y dentro estará el `default.xbe` ya parcheado, listo para usar en tu Xbox.

### Créditos y Agradecimientos
- **Stagman**

### Aviso
Este proyecto no incluye ningún archivo del juego. Necesitas tu propia copia legal del juego para obtener el `default.xbe` original.
