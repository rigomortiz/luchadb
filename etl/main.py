import os
import shutil

PATH = "/mnt/c/Users/rcansecol/Documents/repositorios/luchadb"
TO = PATH + "/data/input"

def mov_files(path: str, to: str):
    """
    Mueve archivos .txt a otro directorio
    """
    if os.path.isdir(path):
        # Crear el directorio de destino si no existe
        if not os.path.exists(to):
            os.makedirs(to)

        # Listar solo los archivos .txt en el directorio de destino
        txt_files = [f for f in os.listdir(path) if f.endswith("luchadb.txt")]

        # Mover los archivos .txt al directorio de destino
        for txt_file in txt_files:
            src_file = os.path.join(path, txt_file)
            dest_file = os.path.join(to, txt_file)
            shutil.move(src_file, dest_file)

        print(f"Se movieron {len(txt_files)} archivos .txt al directorio {to}.")
    else:
        print(f"El directorio {dir} no existe.")


if __name__ == "__main__":
    mov_files(PATH, TO)