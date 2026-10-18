# launch the virtual environment
.\env\Scripts\Activate.ps1

# pause for a moment to ensure the virtual environment is activated
Start-Sleep -Seconds 2

# install the required packages from requirements.txt
python -m pip install --upgrade pip
python -m pip install -r requirements.txt