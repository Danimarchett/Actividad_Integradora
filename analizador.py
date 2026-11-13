import string
import matplotlib.pyplot as plt

def contar_frecuencias(texto):
    """Cuenta la frecuencia de cada palabra en un texto, ignorando mayúsculas y puntuación."""
    frecuencias = {}
    
    # Limpiamos los signos de puntuación básicos del texto
    for signo in string.punctuation:
        texto = texto.replace(signo, "")
    
    # Pasamos todo a minúsculas y separamos por palabras
    palabras = texto.lower().split()
    
    # Contamos las frecuencias usando un diccionario
    for palabra in palabras:
        frecuencias[palabra] = frecuencias.get(palabra, 0) + 1
        
    return frecuencias

def main():
    nombre_archivo = "texto_integradora.txt"
    
    # 1. Lectura del archivo manejando errores con try/except (Clase 2)
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{nombre_archivo}'.")
        return

    # 2. Conteo de frecuencias
    frecuencias = contar_frecuencias(contenido)
    
    if not frecuencias:
        print("El archivo está vacío.")
        return

    # 3. Ordenar las palabras de mayor a menor y seleccionar las 10 más frecuentes
    palabras_ordenadas = sorted(frecuencias.items(), key=lambda x: x[1], reverse=True)
    top_10 = palabras_ordenadas[:10]
    
    palabras = [item[0] for item in top_10]
    conteos = [item[1] for item in top_10]

    # 4. Generar y guardar el gráfico de barras con matplotlib (Clase 3)
    plt.figure(figsize=(10, 6))
    plt.bar(palabras, conteos, color='skyblue')
    plt.xlabel('Palabras')
    plt.ylabel('Frecuencia')
    plt.title('Top 10 - Palabras más frecuentes')
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    plt.savefig('grafico_frecuencias.png')
    print("Gráfico guardado exitosamente como 'grafico_frecuencias.png'.")
    plt.close()

if __name__ == "__main__":
    main()
