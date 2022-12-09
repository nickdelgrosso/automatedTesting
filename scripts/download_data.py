import requests
from pathlib import Path


url = 'https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv'
r = requests.get(url)
csv = r.text

filepath = Path('data/raw/titanic.csv')
filepath.parent.mkdir(parents=True, exist_ok=True)
filepath.write_text(csv)