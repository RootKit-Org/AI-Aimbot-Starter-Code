![World's Best AI Aimbot Banner](imgs/banner.png)

[![Pull Requests Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat)](http://makeapullrequest.com)

# ✨Make sure you have the Launcher before starting✨
Download the [RootKit Launcher](https://github.com/RootKit-Org/Launcher). It is FREE. **No coding required.**

Over 2,100 users use the launcher

## Pros
Using the starter kit is the best way to make your own bot. This is the way you have to submit code to us for competitions to start with. here are more reasons.
- Offical Competitive Standard
- Access to models in Store
- Models will be auto converted for you
- Setting profiles can be used in your code
- You can publish your code on our store
- Everyone has the launcher (Over 1,700 users)

## Cons
- You have to learn how to use an API/SDK

## What's in the box?
We included 2 different examples for you.

- A bare example which has the bare minimum for most projects you would want to start.

- An example using the Open Source Aimbot

## Running
Place main.py anywhere. To run it, the syntax is 
`python main.py <settingsProfile> <yoloVersion> <modelFileName> <customCode>`

Treat it as if you were gonna import your code. Here is an example of what it would look like.
`python main.py Default 5 v5_base_s.pt example_bare.main`

## Deploying
Move your custom code folder into `%APPDATA%\ai-aimbot-launcher\customCode`.

If you want to post it on the store, `@Techincal Champions` in the discord.

## Starter Function
### What the Launcher Sends you
```python
version: int # 0-2 (pytorch, onnx, engine)
settingsProfile: str # file name of settings located in %APPDATA%\ai-aimbot-launcher\aimbotSettings
paidTier: int # 0-3 (free, supporter t1, t2, t3)
yoloVersion: int # 5 or 8 (yolov5 or yolov8)
modelfileName: str # file name of model located in %APPDATA%\ai-aimbot-launcher\models
```

### Example 1
```python
def main(**argv):
    print("My custom bot")
    print(argv)
```

### Example 2
```python
def main(
    version,
    settingsProfile,
    paidTier,
    yoloVersion,
    modelFileName
    ):
    print("My custom bot")
```

### Example 3
```python
from .schema.settings import Settings # Include the schema folder
import json
import os

def main(
    version: int = 0,
    settingsProfile: str = "",
    paidTier: int = 0,
    yoloVersion: int = 0,
    modelFileName: str = ""
    ):

    appdataLocation = os.getenv("APPDATA")
    settingsPath = os.path.join(appdataLocation, "ai-aimbot-launcher", "aimbotSettings", f"{settingsProfile.lower()}.json")

    # loading settings
    with open(settingsPath, "r") as f:
        settings = json.load(f)
        settings = Settings(**settings)

    # getting model path
    modelPath = os.path.join(appdataLocation, "ai-aimbot-launcher", "models", modelFileName)
```
