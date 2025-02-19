pip install -r requirement.txt
pyinstaller --icon icon.ico --onefile --add-data "updates/7z.exe;updates" --add-data "updates/7z.dll;updates" --add-data "updates/7-zip.dll;updates" --add-data "updates/7-zip32.dll;updates" pyupdate.py
move /Y dist\pyupdate.exe codecore.exe
rmdir dist
del /Q pyupdate.spec
rmdir /S /Q build
