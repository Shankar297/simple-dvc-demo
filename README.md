create env
```bash
conda create -n wineq python=3.7 -y
```

activate env
```bash
conda activate wineq
```
create a requirement.txt file

write in requirements.txt

dvc

dvc[gdrive]

sklearn

install the requirement.txt
```bash
pip install -r requirement.txt
```
run below command
```bash
git init
```
```bash
dvc init
```
```bash
dvc add data_given/winequality.csv
```
```bash
git add .
```
```bash
git commit -m "first commit"
```
```bash
git remote add origin https://github.com/Shankar297/simple-dvc-demo.git
```
```bash
git branch -M main
```
```bash
git push origin main
```
tox command - 
```bash
tox
```
for rebuilding - 
```bash
tox -r
```
pytest command -
```bash
pytest -v
```

setup command - 
```bash
pip install -e .
```

build your own package command - 
```bash
python setup.py sdist bdist weel
```