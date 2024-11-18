from sentient import sentient
import os, dotenv
import asyncio
from colorama import Fore
from datetime import datetime

dotenv.load_dotenv()
base_url = os.environ.get("BASE_URL")
model_name = os.environ.get("MODEL_NAME")

print(f"{Fore.YELLOW}base_url: {Fore.GREEN}{base_url}")
print(f"{Fore.YELLOW}model_name: {Fore.GREEN}{model_name}")

if not os.path.exists("saves"):
    os.makedirs("saves")
timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
save_path = "saves/log_" + timestamp + ".txt"
print(f"{Fore.YELLOW}save_path: {Fore.GREEN}{save_path}")
with open(save_path, "w") as file:
    pass

# 添加python执可选行arguements -cnv(交互模式)
if "-cnv" in os.sys.argv:
    print(f"{Fore.YELLOW}Conversation mode enabled")
    while 1:
        prompt = input("请输入您的问题: ")
        result = asyncio.run(
            sentient.invoke(
                goal=prompt,
                provider="custom",
                model=model_name,
                custom_base_url=base_url,
            )
        )
        with open(save_path, "a") as f:
            f.write(f"问题: {prompt}\n")
            f.write(f"答案: {result}\n")

else:
    with open("input.txt", "r") as f:
        prompt = f.read()
    with open(save_path, "a") as f:
        result = asyncio.run(
            sentient.invoke(
                goal=prompt,
                provider="custom",
                model=model_name,
                custom_base_url=base_url,
            )
        )
        f.write(f"问题: {prompt}\n")
        f.write(f"答案: {result}\n")
