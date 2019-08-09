pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org pyinstaller 
pyinstaller --onefile --icon="icon.ico" --name VoicePlay main.py --hidden-import="icon.ico"
move "dist\\VoicePlay.exe" "."
@RD /S /Q "dist"
@RD /S /Q "build"