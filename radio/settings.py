# settings.py
from dotenv import load_dotenv
load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to 'radio.env'
from pathlib import Path  # Python 3.6+ only
env_path = Path('..') / 'radio.env'
load_dotenv(dotenv_path=env_path)