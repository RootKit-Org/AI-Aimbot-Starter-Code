from .schema.settings import Settings
import json
import os

def main(
    version: int = 0,
    settingsProfile: str = "",
    paidTier: int = 0,
    yoloVersion: int = 0,
    modelFileName: str = ""
    ):

    # getting %appdata%
    appdataLocation = os.getenv("APPDATA")
    settingsPath = os.path.join(appdataLocation, "ai-aimbot-launcher", "aimbotSettings", f"{settingsProfile.lower()}.json")

    # loading settings
    with open(settingsPath, "r") as f:
        settings = json.load(f)
        settings = Settings(**settings)


    print("BASE CODE")

    # getting model path
    modelPath = os.path.join(appdataLocation, "ai-aimbot-launcher", "models", modelFileName)

