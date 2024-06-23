# Introduction
This program allows you to take any image and create the code needed to display it on the [CC: Tweaked](https://www.curseforge.com/minecraft/mc-mods/cc-tweaked) monitors. The program will copy it to your clipboard, as well as save it to a file. Then you can put the code into [pastebin](https://pastebin.com/) and get it in-game with the `pastebin get` command.

## Installation
1. Clone the repository
```bash
git clone https://github.com/ThatOneShortGuy/CCTweakedImageMaker.git
```
2. Install the required packages
```bash
pip install -r requirements.txt
```
3. Run the program
```bash
python main.py <image_path> <num_monitors_wide> <num_monitors_tall>
```
4. Paste the code into [pastebin](https://pastebin.com/)
5. Run the command `pastebin get <code> <filename>` in Minecraft
ex. `pastebin get 123456789 image`
6. Run the program on the computer.
ex. `image`