from runpy import run_path
import os

def test_download_data():

    run_path("scripts/download_data.py")

    assert os.path.exists("data/raw/titanic.csv")
