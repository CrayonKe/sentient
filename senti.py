from sentient import sentient
import asyncio
import dotenv
import os

dotenv.load_dotenv()
base_url = os.environ.get("BASE_URL")
model_name = os.environ["MODEL_NAME"]

result = asyncio.run(
    sentient.invoke(
        goal="play shape of you on youtube",
        provider="custom",
        model=model_name,
        custom_base_url=base_url,
    )
)
