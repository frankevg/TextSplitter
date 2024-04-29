# TextSplitter
TextSplitter is a lightweight Python tool crafted for efficiently segmenting input text into smaller, digestible units. Ideal for preparing input data for language model tasks, it intelligently breaks down text into chunks

## How to Use

### 1. Input File
- Make sure the text file you want to split is located at `C:/route/archivoS.txt`.

### 2. Running the Script
- Open the Python script (`text_splitter.py`) in your preferred editor or IDE.
- Set the `max_longitud` variable to your desired maximum segment length.
- Run the script.

### 3. Output
- After running the script, the input file will be split into segments of the specified maximum length.
- Each segment will be saved as a separate text file in the same directory as the input file.

## Example

Suppose you have a file named `archivoS.txt` containing a large body of text. After running the script, the text will be split into segments, and files named `segment_1.txt`, `segment_2.txt`, etc., will be generated, each containing a portion of the original text.

## Script

```python
with open('C:/route/archivoS.txt', 'r', encoding='utf-8') as f:
    texto_completo = f.read()

max_longitud = 14500
segmentos = []
for i in range(0, len(texto_completo), max_longitud):
    segmentos.append(texto_completo[i:i+max_longitud])

# Loop to write each segment into a separate file
for i, segmento in enumerate(segmentos):
    file_name = f"segment_{i+1}.txt"  # Generates a unique file name for each segment
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(segmento)
