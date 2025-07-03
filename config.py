import time


START_ASCII = """                                                            
 .d8888b.   .d8888b.  8888888b.   .d8888b.  8888888b.  Y88b   d88P              d8888 888     888 88888888888  .d88888b.  
d88P  Y88b d88P  Y88b 888   Y88b d88P  Y88b 888   Y88b  Y88b d88P              d88888 888     888     888     d88P" "Y88b 
Y88b.      888    888 888    888 888    888 888    888   Y88o88P              d88P888 888     888     888     888     888 
 "Y888b.   888        888   d88P 888        888   d88P    Y888P              d88P 888 888     888     888     888     888 
    "Y88b. 888        8888888P"  888        8888888P"      888              d88P  888 888     888     888     888     888 
      "888 888    888 888 T88b   888    888 888            888             d88P   888 888     888     888     888     888 
Y88b  d88P Y88b  d88P 888  T88b  Y88b  d88P 888            888            d8888888888 Y88b. .d88P     888     Y88b. .d88P 
 "Y8888P"   "Y8888P"  888   T88b  "Y8888P"  888            888           d88P     888  "Y88888P"      888      "Y88888P"  
"""

END_MSG = "TO CANCEL PROGRAM PRESS CTRL+C"

COMMAND_DICT = {
    0: {"command": "user command", 
        "desc": "Your command"},
    1: {"command": "--video-codec=h265 -m1920 --max-fps=60 -K ",
        "desc": "Capture the screen in H.256(better quality) | 1920x1080 60fps | control | no audio"},
    2: {"command": "--video-codec=h264 -m1920 --max-fps=60  -K ", 
        "desc": "Capture the screen in H.254(better compatibility) | 1920x1080 60fps | control | no audio "},
    3: {"command": "--video-source=camera --video-codec=h265 --camera-size=1920x1080 --record=./Videos/CameraCast.mp4", 
        "desc": "Record the device camera in H.265(Better quality) at 1920x1080 and microphone to Videos/CameraCast.mp4"},
    4: {"command": "--video-source=camera --video-codec=h264 --camera-size=1920x1080 --record=./Videos/CameraCast.mp4", 
        "desc": "Record the device camera in H.264(Better compatibility) at 1920x1080 and microphone to Videos/CameraCast.mp4"},
    5: {"command": "--new-display=1920x1080 --start-app=org.videolan.vlc", 
        "desc": "Start VLC in a new virtual display (separate from the device display)"},
    6: {"command": "--otg", 
        "desc": "Control the device without mirroring by simulating a physical keyboard and mouse "},
    7: {"command": "--G", 
        "desc": "Control the device using gamepad controllers plugged into the computer"},
    8: {"command": "--video-source=camera --camera-size=1920x1080 --camera-facing=front --v4l2-sink=/dev/video2 --no-playback", 
        "desc": "Use the front camera as a video source and send the output to a virtual video device"},
    9: {"command": "--tcpip", 
        "desc": "Enable TCP/IP mode, allowing for wireless connections. After run this mode you can use another mode"},
    10: {"command": "scrcpy --no-video --no-audio --keyboard=aoa --mouse=aoa", 
        "desc": "Use the device as a keyboard and mouse input"},
    11: {"command": "", 
        "desc": ""},
    12: {"command": "", 
        "desc": ""},
    13: {"command": "", 
        "desc": ""},
    14: {"command": "", 
        "desc": ""},
    15: {"command": "", 
        "desc": ""},
    16: {"command": "", 
        "desc": ""},
    17: {"command": "", 
        "desc": ""},
    18: {"command": "--list-encoders", 
        "desc": "List all available video encoders"},
    19: {"command": "--help", 
        "desc": "Show help information"},
    20: {"command": "--version", 
         "desc": "Show version scrcpy"},
}

