RESP=$(rm app.zip)
if [ -z "$RESP" ]; then
  echo "removing old zip file."
else
  echo "no old zip file found."
fi
zip -r app.zip . -x *.idea* *.git* *.vscode* *.DS_Store* *.pyc __pycache__/**\* *.md test/**\* venv/* venv/**\* @
