import os
from open.text.embeddings.openai import OpenAIEmbeddings
from dotenv import load_dotenv

HERE = os.path.dirname(__file__)
ENV_PATH = os.path.join(HERE, '.env')

load_dotenv(
    dotenv_path=ENV_PATH,
    verbose=True,
)

ADDRESS = os.getenv('V_ADDRESS')
KEY = os.getenv('V_API_KEY')
TEXT = os.getenv('V_TEST_TEXT')

embeddings = OpenAIEmbeddings(
    openai_api_base=ADDRESS,
    openai_api_key=KEY
)