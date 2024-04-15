set py_venv=venv

call "%py_venv%\Scripts\activate.bat"

py apps/test.py

echo finish!!!
pause