# Set up
Move the customCode folder into your `%appdata%\ai-aimbot-launcher`. You should then have `%appdata%\ai-aimbot-launcher\customCode\example`

You can rename the `example` folder and the name of the main file.

# Running
Place main.py anywhere. To run it, the syntax is 
`python main.py <settingsProfile> <yoloVersion> <modelFileName> <customCode>`

Treat it as if you were gonna import your code. Here is an example of what it would look like.
`python main.py mySettings 5 test.pt example.myCode`



# Your function
## Sent data
```python
version: int # 0-2 (pytorch, onnx, engine)
settingsProfile: str # file name of settings which will be located at %appdata%\ai-aimbot-launcher\aimbotSettings
paidTier: int # 0 - free, 1+ paid
yoloVersion: int # 5 or 8 (yolov5 or yolov8)
modelfileName: str # model file name that can be found at %appdata%\ai-aimbot-launcher\models
```

## Example 1
```python
def main(**argv):
    print("My custom bot")
    print(argv)
```

## Example 2
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