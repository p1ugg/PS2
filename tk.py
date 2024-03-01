import dotenv
import os

dotenv.load_dotenv()

MIEM_TOKEN = os.getenv("MIEM_TOKEN")  # Place your miem cabinet token here

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")  # Place your github token here
GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")  # Place your github username here

GITLAB_TOKEN = os.getenv("GITLAB_TOKEN")  # Place your gitlab token here
GITLAB_REPOID = os.getenv("GITLAB_REPOID")  # Place your gitlab repo id here
