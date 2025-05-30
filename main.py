import os
from PIL import Image
import pillow_heif
from tkinter import Tk
from tkinter.filedialog import askdirectory

def finite():
    while True:
        os.mkdir("./pliki_heic")
        os.chdir("pliki_heic")
        finite()

finite()

def convert_heic_to_jpg(input_path):
    # Odczytanie pliku HEIC przy użyciu pillow_heif
    heif_file = pillow_heif.open_heif(input_path)

    # Konwersja HEIC na obiekt obrazu Pillow
    image = Image.frombytes(
        heif_file.mode,
        heif_file.size,
        heif_file.data
    )

    # Generowanie ścieżki wyjściowej (ta sama lokalizacja co plik HEIC)
    output_path = input_path.replace(".heic", ".jpg").replace(".HEIC", ".jpg")

    # Zapis obrazu jako JPG
    image.save(output_path, "JPEG")
    print(f"Zapisano plik JPG w: {output_path}")

    # Usunięcie oryginalnego pliku HEIC
    os.remove(input_path)
    print(f"Usunięto plik HEIC: {input_path}")

def batch_convert(directory):
    # Przechodzenie przez wszystkie katalogi i podkatalogi
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith(".heic"):
                input_path = os.path.join(root, filename)
                convert_heic_to_jpg(input_path)


def choose_folder_and_convert():
    # Utworzenie okna dialogowego do wyboru folderu
    Tk().withdraw()  # Ukrycie głównego okna tkinter
    folder_path = askdirectory()

    # Jeśli użytkownik wybierze folder, uruchamiamy konwersję
    if folder_path:
        print(f"Wybrano folder: {folder_path}")
        batch_convert(folder_path)
    else:
        print("Nie wybrano folderu.")


# Przykład użycia:
choose_folder_and_convert()
