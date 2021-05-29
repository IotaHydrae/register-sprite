cd  %~dp0
pyinstaller --clean -s -w -F main.py  -i ./assets/chip.ico --name RegisterSprite  --distpath ./bin -y --uac-admin