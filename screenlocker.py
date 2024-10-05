# Copyright 2023-2024 C14147.

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at:
#   http://www.apache.org/licenses/LICENSE-2.0
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.

# See the License for the specific language governing permissions and
# limitations under the License.

import os
import time
import argparse
from tkinter import *


parse = argparse.ArgumentParser(description="Lock Your PC when the countdown done.")
parse.add_argument(
    "-s", type=int, default=10, metavar="second", help="Lock screen's time(s)"
)
parse.add_argument(
    "-bg",
    type=str,
    default="black",
    metavar="colour",
    help="Screen's Background Colour",
)
parse.add_argument(
    "-fg", type=str, default="white", metavar="colour", help="Screen's Text Colour"
)
parse.add_argument(
    "-font",
    type=str,
    default="Microsoft YaHei",
    metavar="Font",
    help="Screen's Text's Font Style",
)
parse.add_argument(
    "-lang", type=int, default=0, metavar="lang", help="App's Language(0:en, 1:cn)"
)
args = parse.parse_args()
lang = args.lang
times = int(args.s) * 1000
if times < 10000:
    print("Times too short.")
    exit()
wtimes = 1

# Create Window
lock = Tk()
wintime = IntVar()

lock.title("ScreenLocker")
lock.attributes("-topmost", "true")
lock.attributes("-fullscreen", "true")
try:
    lock.config(bg=args.bg)

    lock.overrideredirect(1)
    Label(
        lock,
        text=("Your PC is locked." if lang == 0 else "你的电脑已被上锁"),
        font=(args.font, 20),
        fg=args.fg,
        bg=args.bg,
    ).pack()
    Label(
        lock,
        text=(
            "We'll unlock it When The Countdown Ends."
            if lang == 0
            else "我们将在倒计时结束后给您的电脑解锁"
        ),
        font=(args.font, 15),
        fg=args.fg,
        bg=args.bg,
    ).pack()
    Label(
        lock, textvariable=wintime, font=(args.font, 20), fg=args.fg, bg=args.bg
    ).pack()  # Show time
except TclError as e:
    print("Error:", end="")
    print(e)
    exit()
except Exception as e:
    print("UnkownError:", end="")
    print(e)
    exit()

# Loop the window
os.system("start taskkill /F /IM explorer.exe")
while wtimes <= times:
    wintime.set(times // 1000 - wtimes // 1000)
    lock.update()
    if wtimes == times - 5000:
        os.system("start explorer.exe")
    time.sleep(0.001)
    wtimes += 1

lock.destroy()
