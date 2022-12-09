import runpy
import os
from os import path


def test_run_download_script_gets_datafile():
    datapath = 'data/raw/titanic.csv'
    if path.exists(datapath):
        os.remove(datapath)
    assert not path.exists(datapath)
    runpy.run_path('scripts/download_data.py')
    assert path.exists(datapath)

