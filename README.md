# Idle home Auto save

![init_gui_1_1_4](https://github.com/fuzzyCute/Idle_home_Auto_save/assets/22378193/57ba078e-2074-4ca5-b8ab-9af4943f510e)

An auto save program that allows you to save a game from the vrchat world [Idle Home](https://vrchat.com/home/world/wrld_c16e4dee-d149-4116-adbc-16bc30b664b0)
This works by going to vrchat's log file and getting the save string that you'd get when you click on the save button, or when it auto saves

## How to use the program
2 ways:

### Compiled executable
Download the ZIP file for the Windows build that exists on
the [releases page](https://github.com/Baplar/Idle_home_Auto_save/releases/latest).

Extract it, and just launch `auto_save.exe`!

The binary may be flagged as dangerous when starting it for the first time,
but Windows should allow you to execute it after a warning,
and will not show the warning again the next time you run it.

### Running the python code yourself

To run the script directly, you need to have a version of Python 3 installed on your computer.
You can fetch it from the [official website](https://www.python.org/downloads/).

Make sure to check the option to add it to PATH, this will make it easier to run scripts and tools.

#### Install the package and its dependencies (only once)
```
python -m pip install .
```

#### After installing locally, start the program with
```
pythonw -m idle_home_auto_save
```
Or just launch [`auto_save.bat`](./auto_save.bat) which does basically the same thing !

---

If you have installed the package outside of a virtual environment
(which should be the case unless you *really* know what you're doing),
you can also just run the script `idle_home_auto_save/auto_save.pyw` directly.

Just be wary that the config file will be created in the subfolder,
instead of the root folder for the previous methods.

## The GUI

![init_1_1_4](https://github.com/fuzzyCute/Idle_home_Auto_save/assets/22378193/7f69e507-bc0a-4e41-a9c9-81e703cf56f2)

Once you open the program this little window will show up
HEre's what you need to do on each step:
* 1 - When you click on the button another window will pop up, you'll have to choose where you want the file to be saved
* 2 - Give a name and an extension to your file, could be anything. The example I give is save.txt
* 3 - Give a number, this will represent the interval between log checks.
* 4 - Just start the program.

When you're done it'll start the program and you'll end up with a file with your save codes like in the image below

![imagem](https://github.com/fuzzyCute/Idle_home_Auto_save/assets/22378193/0c039f28-6101-4f3b-9252-32e105b7cd08)

If you want to just copy the last saved string to your clipboard just click on the button (5)

If you want you can open the file clicking on button (6) and it'll open a file like the one below

You can also ignore the line limite by checking the checkbox (7)

## Building the project for distribution
See [BUILD.md](./BUILD.md)

## Disclaimer
I did this tool because I'm a bit lazy, but I held no responsibility for what could happen if you run this

Have a good day!
