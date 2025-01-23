import os
import shutil

# Ruta de origen
ruta_origen = r"C:\Users\User\Desktop\"

# Ruta  destino
ruta_destino = r"C:\Users\User\Desktop\SHN\RdelaPlata"

# Subcarpetas a copiar (las que voy a usar!)
subcarpetas = ['AUX_DATA', 'IMG_DATA', 'QI_DATA']

# Años con los que voy a procesar los datos (desde 2016 hasta 2024)
años= range(2016, 2025)

# Meses  con los que voy a procesar los datos (desde 2016 hasta 2024)
meses = [
    'enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio',
    'julio', 'agosto', 'septiembre', 'octubre', 'noviembre', 'diciembre'
]

# Iterar sobre los años y meses (bucles!)
for año in años:
    for mes in meses:
        # Construir la ruta base para el año y mes actual
       año_mes_dir = os.path.join(ruta_origen, str(year), mes)

        # Verificar si la carpeta del año y mes existe
        if os.path.exists(year_mes_dir):
            # Buscar carpetas que comienzan con "S2A_MSIL2A_" dentro del mes
            for folder_name in os.listdir(year_month_dir):
                folder_path = os.path.join(year_month_dir, folder_name)

                # Ignorar archivos (como .zip) y solo procesar carpetas
                if os.path.isdir(folder_path) and folder_name.startswith("S2A_MSIL2A_"):
                    # Construir la ruta de la segunda carpeta S2A_MSIL2A_
                    inner_folder_path = os.path.join(folder_path, folder_name)

                    # Verificar si la segunda carpeta existe
                    if os.path.exists(inner_folder_path):
                        # Construir la ruta de la carpeta GRANULE
                        granule_dir = os.path.join(inner_folder_path, "GRANULE")

                        # Verificar si la carpeta GRANULE existe
                        if os.path.exists(granule_dir):
                            # Construir la ruta de destino
                            destination_dir = os.path.join(ruta_destino, str(year), month, f"{folder_name}_nuevo")

                            # Crear la carpeta destino si no existe
                            os.makedirs(destination_dir, exist_ok=True)

                            # Copiar cada subcarpeta
                            for subfolder in subcarpetas:
                                source_subfolder = os.path.join(granule_dir, subfolder)
                                destination_subfolder = os.path.join(destination_dir, subfolder)

                                # Verificar si la subcarpeta existe
                                if os.path.exists(source_subfolder):
                                    # Crear la carpeta en el destino
                                    os.makedirs(destination_subfolder, exist_ok=True)
                                    print(f"Copiando {subfolder} desde {source_subfolder} a {destination_subfolder}...")

                                    # Copiar archivos de la subcarpeta
                                    for root, _, files in os.walk(source_subfolder):
                                        for file in files:
                                            source_file = os.path.join(root, file)
                                            relative_path = os.path.relpath(root, source_subfolder)
                                            destination_file = os.path.join(destination_subfolder, relative_path, file)

                                            # Crear carpetas intermedias si es necesario
                                            os.makedirs(os.path.dirname(destination_file), exist_ok=True)
                                            shutil.copy(source_file, destination_file)
                                            print(f"Archivo copiado: {source_file} -> {destination_file}")
                                else:
                                    print(f"La carpeta {subfolder} no existe en {source_subfolder}")
                        else:
                            print(f"La carpeta GRANULE no existe en {inner_folder_path}")
                    else:
                        print(f"La carpeta interna {inner_folder_path} no existe.")
                else:
                    print(f"Ignorando archivo o carpeta no válida: {folder_path}")
        else:
            print(f"La carpeta {year_month_dir} no existe.")

print("Copiado completado.")