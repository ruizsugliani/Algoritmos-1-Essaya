def cp(archivo_origen, archivo_destino):
    '''
    Copia todo el contenido del archivo_origen (sea de texto o binario) a otro
    llamado archivo_destino de modo que quede exactamente igual.
    '''
    with open(archivo_origen, "r", encoding="utf8") as file_o:
        lineas = file_o.readlines()
        with open(archivo_destino, "w", encoding="utf8") as file_d:
            file_d.writelines(lineas)
    return

cp("materias.txt", "destino.txt")
