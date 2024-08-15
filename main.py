with open('C:/your route', 'r', encoding='utf-8') as f:
    texto_completo = f.read()
    
max_longitud = 14500
segmentos = []
for i in range(0, len(texto_completo), max_longitud):
    segmentos.append(texto_completo[i:i+max_longitud])

# Bucle para escribir cada segmento en un archivo diferente
for i, segmento in enumerate(segmentos):
    nombre_archivo = f"segmento_{i+1}.txt"  # Genera un nombre de archivo único para cada segmento
    with open(nombre_archivo, 'w', encoding='utf-8') as f:
        f.write(segmento)
