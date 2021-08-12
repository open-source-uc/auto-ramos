def extraer(s):
    return s[s.find('>') + 1 : s.find('</')]

def hay_errores(info):
    inicio = 0
    final = 0
    for i in range(len(info)):
        item = info[i]
        if '<TABLE  CLASS="datadisplaytable" SUMMARY="Esta tabla es usada para presentar Errores' in item:
            inicio = i
        if inicio and not final:
            if '</TABLE>' in item:
                final = i
    return inicio, final

def obtener_errores(info, inicio, final):
    output = list()
    first = 1
    for i in range(inicio, final):
        item = info[i]
        if '<TR>' in item:
            if not first:
                a, b = extraer(info[i + 1]), extraer(info[i + 2])
                output.append((a, b))
            first = 0
    return output

def obtener_errores_de(ruta):
    with open(ruta, 'r') as file:
        info = [i.strip() for i in file.readlines()]

    inicio, final = hay_errores(info)
    if inicio:
        return obtener_errores(info, inicio, final)

    return None       

if __name__ == '__main__':
    print(obtener_errores_de('pruebadetoma.html'))
