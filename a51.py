import hashlib
import os
import sys
from pathlib import Path

print(r"""

            ________      ________      ________      ________ 
---------- |\_____  \    |\   __  \    |\   __  \    |\  _____\----------------
----------  \|___/  /|   \ \  \|\  \   \ \  \|\  \   \ \  \__/ ---------------
--------------  /  / /    \ \   __  \   \ \   _  _\   \ \   __\--------------
-------------- /  /_/__    \ \  \ \  \   \ \  \\  \|   \ \  \_|----------------
------------- |\________\   \ \__\ \__\   \ \__\\ _\    \ \__\ ----------------
-------------- \|_______|    \|__|\|__|    \|__|\|__|    \|__| -----------------

""")

print("Parche full español Área51 Xbox Clásico")

HASH = "38428086AC435F05FE57E17757C1C56F"
offset_1 = 0x198
bloque_1 = b"\x20\x00\x35\x00\x31"

offset_2 = 0x22b6c9
bloque_2 = b"\x75"
# -----------------------------------

def main():
    ruta_base = Path(sys.argv[0]).parent if getattr(sys, 'frozen', False) else Path(__file__).parent
    ruta_xbe = ruta_base / "default.xbe"

    if not ruta_xbe.exists():
        print("Error: No se encuentra el ejecutable default.xbe")
        print("Busca ayuda en https://www.youtube.com/@MODZARF")
        input("Presiona Enter para cerrar...")
        return

    with open(ruta_xbe, 'rb') as f:
        datos = f.read()
        md5_actual = hashlib.md5(datos).hexdigest()

    if md5_actual.lower()!= HASH.lower():
        print("¡ERROR! El default.xbe no pertenece al juego Área51.")
        print(f"Esperado: {HASH}")
        print(f"Actual: {md5_actual}")
        print("Busca ayuda en https://www.youtube.com/@MODZARF")
        input("Presiona Enter para cerrar...")
        return

    datos_mod = bytearray(datos)

    try:
        datos_mod[offset_1:offset_1 + len(bloque_1)] = bloque_1
        datos_mod[offset_2:offset_2 + len(bloque_2)] = bloque_2
    except Exception as e:
        print(f"Error al parchear: {e}")
        print("Busca ayuda en https://www.youtube.com/@MODZARF")
        input("Presiona Enter para cerrar...")
        return

    carpeta_mod = ruta_base / "MOD"
    carpeta_mod.mkdir(exist_ok=True)

    ruta_salida = carpeta_mod / "default.xbe"
    with open(ruta_salida, 'wb') as f:
        f.write(datos_mod)

    print("¡ÉXITO! revisa la carpeta MOD")
    input("Presiona Enter para cerrar...")

if __name__ == "__main__":
    main()