def reloj():
    horas = 0
    while(horas < 24):
        minutos = 0
        while(minutos < 60):
            segundos = 0
            while(segundos < 60):
                print(f"{horas}:{minutos}:{segundos}")
                segundos += 1
            minutos += 1
        horas += 1
        
        