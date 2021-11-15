create env
```bash
conda create -n wineq python=3.7 -y
```

activate env
```bash
conda activate wineq
```
create a requirement.txt file

install the requirement.txt
```bash
pip install -r requirement.txt
```

```bash
git init

dvc init

dvc add data_given/winequality.csv

git add .
 
git commit -m "first commit"

git remote add origin https://github.com/Shankar297/simple-dvc-demo.git

git branch -M main

git push origin main
```