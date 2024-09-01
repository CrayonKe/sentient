# sentient - browser controlling agents in 3 lines of code

### setup

1. install sentient `pip install sentient`


2. start chrome in dev mode - in a seaparate terminal, use the command to start a chrome instance and do necesssary logins if needed

for mac, use command -

```bash
sudo /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
```

for linux -

```bash
google-chrome --remote-debugging-port=9222
```

for windows -

```bash
"C:\Program Files\Google\Chrome\Application\chrome.exe" --remote-debugging-port=9222
```

4. setup open ai api key in a .env file `OPENAI_API_KEY="sk-proj-"`

5. run the agent

```python
from sentient import sentient
import asyncio

result = asyncio.run(sentient.invoke("play shape of you on youtube"))
```