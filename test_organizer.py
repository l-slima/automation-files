from pathlib import Path
import shutil
import pytest
from src.organizer import organize_files

def test_folder_creation(tmp_path):
    test_file = tmp_path / "teste.txt"
    test_file.write_text("arquivo de teste")

    organize_files(tmp_path)

    assert (tmp_path / "documentos" / "teste.txt").exists()
