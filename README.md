# Idle home Auto save

![init_gui_1_1_4](https://github.com/fuzzyCute/Idle_home_Auto_save/assets/22378193/57ba078e-2074-4ca5-b8ab-9af4943f510e)

An auto save program that allows you to save a game from the vrchat world [Idle Home](https://vrchat.com/home/world/wrld_c16e4dee-d149-4116-adbc-16bc30b664b0)
This works by going to vrchat's log file and getting the save string that you'd get when you click on the save button, or when it auto saves

## How to use the program
2 ways:
* Downloading python and running the program yourself
* Just run the executable that exists on the [releases page](https://github.com/fuzzyCute/Idle_home_Auto_save/releases/tag/version_1_1_4) - If you get a false virus warning [read this](#installation-note)

### If you want to run the python code yourself
Don't forget to install the dependencies, which are included in the requirements.txt file

## The GUI

![init_1_1_4](https://github.com/fuzzyCute/Idle_home_Auto_save/assets/22378193/7f69e507-bc0a-4e41-a9c9-81e703cf56f2)

Once you open the program this little window will show up
Here's what you need to do on each step:
* 1 - When you click on the button another window will pop up, you'll have to choose where you want the file to be saved
* 2 - Give a name and an extension to your file, could be anything. The example I give (in the screenshot) is `dinner.txt`
* 3 - Give a number, this will represent the interval between log checks.
* 4 - Just start the program.

When you're done it'll start the program and you'll end up with a file with your save codes like in the image below

![imagem](https://github.com/fuzzyCute/Idle_home_Auto_save/assets/22378193/0c039f28-6101-4f3b-9252-32e105b7cd08)

If you want to just copy the last saved string to your clipboard just click on the button (5)

If you want you can open the file clicking on button (6) and it'll open a file like the one below

You can also ignore the line limit by checking the checkbox (7)

## Disclaimer
I did this tool because I'm a bit lazy, but I hold no responsibility for what could happen if you run this.

<a name="install-note"></a>
## Installation Note

You may get a warning from your anti-virus that this may contain a virus, it does not. This is a known issue with `unsigned exe's` that have been compiled from python scripts using pyintaller. You can read more about this [by clicking here](https://plainenglish.io/blog/pyinstaller-exe-false-positive-trojan-virus-resolved-b33842bd3184).

Have a good day!
