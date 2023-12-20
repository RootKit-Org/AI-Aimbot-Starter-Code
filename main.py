import sys
import os
import requests
import json
from colorama import Fore, Back, Style
import time
import importlib
import sys

def prRed(skk): print(Fore.RED, skk, Style.RESET_ALL)
def prGreen(skk): print(Fore.GREEN + skk + Style.RESET_ALL)
def prYellow(skk): print(Fore.YELLOW + skk + Style.RESET_ALL)
def prBlue(skk): print(Fore.BLUE + skk + Style.RESET_ALL)
def prPurple(skk): print(Fore.MAGENTA, skk + Style.RESET_ALL)
def prCyan(skk): print(Fore.CYAN + skk + Style.RESET_ALL)
def prLightGray(skk): print(Fore.WHITE + skk + Style.RESET_ALL)
def prBlack(skk): print(Fore.BLACK + skk + Style.RESET_ALL)

appdataLocation = os.getenv("LOCALAPPDATA")
appdata = os.getenv("APPDATA")
currentDirectory = os.path.dirname(os.path.realpath(__file__))
os.environ['Path'] += f';{appdataLocation}\\Programs\\Python\\Python311\\Scripts'
os.environ['Path'] += f';{appdataLocation}\\Programs\\Python\\Python311\\'
os.environ['Path'] += ';C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.8'
os.environ['Path'] += ';C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.8\\bin'
os.environ['Path'] += ';C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.8\\libnvvp'
os.environ['Path'] += ';C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.8\\lib'
os.environ['CUDA_PATH'] = 'C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.8'
os.environ['CUDA_PATH_V11_8'] = 'C:\\Program Files\\NVIDIA GPU Computing Toolkit\\CUDA\\v11.8'

TEST = True

def main():
    customCode = None
    if len(sys.argv) > 3:
        settingsProfile = sys.argv[1]
        yoloVersion = int(sys.argv[2])
        modelFileName = sys.argv[3]
    else:
        print("That's not how you run this. Tsk, tsk, try again.")
        prRed("python main.py <settingsProfile> <yoloVersion> <modelFileName> <customCode>")
        return
    
    if len(sys.argv) > 4:
        try:
            sys.path.append(f"{currentDirectory}\\{sys.argv[4].split('.')[0]}\\")

            customCode = importlib.import_module(sys.argv[4])
        except Exception as err:
            raise Exception("Failed to import custom code")
        
        prBlue(f"Custom Code: {sys.argv[4]}")

    botVersion = 0

    if yoloVersion not in [5, 8]:
        prRed("Invalid YOLO version. Please use 5 or 8")
        return
    
    versionText = ""
    _, fileExtension = os.path.splitext(modelFileName)
    if fileExtension == ".pt":
        botVersion = 0
        versionText = "Fast (PyTorch)"
    elif fileExtension == ".onnx":
        botVersion = 1
        versionText = "Faster (ONNX)"
    elif fileExtension == ".engine":
        botVersion = 2
        versionText = "Fastest (TensorRT)"
    else:
        prRed("Invalid model file extension. Please use .pt, .onnx, or .engine")
        return
    
    prGreen(f"Version: {versionText} YOLOv{yoloVersion} from {modelFileName}")

    paidTier = 0

    if TEST:
        paidTier = 1

    prGreen(f"Settings Profile: {settingsProfile}")

    if customCode is not None:
        customCode.main(
            version=botVersion,
            settingsProfile=settingsProfile,
            paidTier=paidTier,
            yoloVersion=yoloVersion,
            modelFileName=modelFileName
        )
    else:
        prBlue("RUNNING MAIN BOT")

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        import traceback
        prRed(traceback.format_exc())
        prRed(e)
        prYellow("Ask @Wonder for help in our Discord: https://discord.gg/rootkitorg")
    
    for i in range(3, 0, -1):
        prYellow(f"Bot will close in {i} seconds")
        time.sleep(1)