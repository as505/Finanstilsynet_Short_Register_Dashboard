Set-Location $PSScriptRoot
.venv\Scripts\Activate.ps1
Set-Location backend
fastapi dev main.py
