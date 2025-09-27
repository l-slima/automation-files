import os
import shutil
import argparse
from pathlib import Path

# Dicionário com extensões e pastas de destino
EXTENSIONS_MAP = {
    "imagens": [".jpg", ".jpeg", ".png", ".gif"],
    "documentos": [".pdf", ".docx", ".txt"],
    "planilhas": [".xlsx", ".csv"],
    "musicas": [".mp3", ".wav"],
    "videos": [".mp4", ".mkv"],
    "outros": []
}

def organize_files(folder_path: Path):
    if not folder_path.exists():
        print(f"❌ A pasta {folder_path} não existe.")
        return

    for file in folder_path.iterdir():
        if file.is_file():
            moved = False
            for folder, extensions in EXTENSIONS_MAP.items():
                if file.suffix.lower() in extensions:
                    target_dir = folder_path / folder
                    target_dir.mkdir(exist_ok=True)
                    shutil.move(str(file), target_dir / file.name)
                    print(f"📂 {file.name} -> {folder}/")
                    moved = True
                    break
            if not moved:
                target_dir = folder_path / "outros"
                target_dir.mkdir(exist_ok=True)
                shutil.move(str(file), target_dir / file.name)
                print(f"📂 {file.name} -> outros/")

def main():
    parser = argparse.ArgumentParser(description="Organizador de arquivos por extensão")
    parser.add_argument("--path", required=True, help="Caminho da pasta a ser organizada")
    args = parser.parse_args()

    organize_files(Path(args.path))

if __name__ == "__main__":
    main()
