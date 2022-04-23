import os
from dotenv import load_dotenv

# Load env
# -----------------------------------------------------------------------------
ROOT_PATH = os.path.abspath('')
ENV = os.path.join(ROOT_PATH, '.env')
load_dotenv(ENV)

API_KEY = os.environ.get('API_KEY')
