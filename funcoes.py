def verificarLink(conteudo):
    if conteudo[:8] == "https://":
        return True
    elif conteudo[:7] == "http://":
        return True
    elif conteudo[:3] == "www":
        return True
    elif conteudo[4:] == ".com":
        return True
    elif conteudo[3:] == ".br":
        return True
    else:
        return False

def verificarPrograma(conteudo):
    caminho_prog = status = False

    caminhos = [
        "C:/Users/guilh/AppData/Local/Programs/Microsoft VS Code/Code.exe",
        "C:/Program Files/HeidiSQL/heidisql.exe",
        "C:/Users/guilh/AppData/Local/Postman/Postman.exe",
        "C:/Program Files/Cryptomator/Cryptomator.exe"
    ]

    programas = [
        "VSCode",
        "Heidi",
        "Postman",
        "Cryptomator"
    ]

    for i in programas:
        if i.upper() == conteudo.upper():
            indice = programas.index(i)
            caminho_prog = caminhos[indice]
            status = True
            return status, caminho_prog
    
    return status, caminho_prog
