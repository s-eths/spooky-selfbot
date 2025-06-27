if not exist "data\.first_run_done" (
    pip install -r data/requirements.txt
    pip uninstall discord.py -y
    pip install discord.py-self
    echo done > data\.first_run_done
)

py main.py