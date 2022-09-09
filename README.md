# Location Finder 

Find Location And Bypass Browser Want To Know Your Location Permission.

## Usage

### Run Tool

```python
  python find_location.py
```

### Convert To EXE

- Use Script In File Organizer EXE Folder
```python
  # Using Pyinstaller
  Pyinstaller --noconfirm --onefile find_location.py

  # Using Nuitka
  py -m nuitka --mingw64 .\find_location.py --standalone --onefile 
 ```


## Tutorial

You need to use chromedriver.exe to make this tool work and put into same directory with script/exe. chromedriver must have the same version with Chrome. 
Also findlocation can't work in headless mode but i set the chrome location to "window-position=-2000,0" so there's nothing shows on the screen. Only in taskbar.

## Download chronmedriver.exe

 - [chromedriver.exe](https://chromedriver.chromium.org/downloads)
 
## Demo
<img src="https://github.com/katakkentut/LocationFinderPython/blob/master/Tutorial/Tutorial.gif" width="700" height="600">
 
 
