rm -r "dist/"
LD_LIBRARY_PATH=~/.pyenv/versions/3.7.0/lib python -m PyInstaller --name makodedit -F makodedit/main.py
cp -v "makodedit/makodedit.kv" "dist/"
cp -v -r "makodedit/images/" "dist/images/"
cp -v -r "makodedit/fonts/" "dist/fonts/"
