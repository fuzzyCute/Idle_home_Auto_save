# version 1.1.5

import os
import fnmatch
import tkinter as tk
import tkinter.filedialog as filedialog
from datetime import datetime

import pyperclip

import threading

# create a class for the gui
class MainProgramGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # lets define the window yes
        self.title("VRChat Idle home auto save made by fuzzyCute")

        # start the variables
        self.vrchat_path = os.environ['USERPROFILE'] + '\\AppData\\LocalLow\\VRChat\\VRChat'

        self.folder_path = ""
        self.save_file_path = ""
        self.time = 0
        self.is_running = False

        # to store the number of save files found (it'll be changed everytime the program finds a save file)
        self.found_save_files = []

        # get the current working directory, this is going to be used for a config file
        self.current_exec_file_path = os.path.abspath(os.getcwd())

        # create the GUI elements or widgets or what's the name you give them

        # lets make it a grid system

        ######### folder_path #########

        self.path_label = tk.Label(self, text="Path to the save file:")
        self.path_entry = tk.Entry(self, width=60)
        self.path_entry.config(state="disabled")
        self.path_button = tk.Button(self, text="Select folder_path", command=self.select_path)

        # place the folder_path on the grid

        self.path_label.grid(row=0, column=0, padx=5, pady=5, sticky="E")
        self.path_entry.grid(row=0, column=1, padx=5, pady=5, sticky="W")
        self.path_button.grid(row=0, column=2, padx=5, pady=5)

        ######### file_name #########

        self.name_label = tk.Label(self, text="Name of the file:")
        self.name_entry = tk.Entry(self, width=30)
        self.name_entry.bind("<KeyRelease>", self.update_path)
        self.name_explain = tk.Label(self, text="name + extension (ex: save.txt)")

        # place the name on the grid
        self.name_label.grid(row=1, column=0, padx=5, pady=5, sticky="E")
        self.name_entry.grid(row=1, column=1, padx=5, pady=5, sticky="W")
        self.name_explain.grid(row=1, column=2, padx=5, pady=5, sticky="W")

        ######### time #########

        self.time_label = tk.Label(self, text="Time in seconds between each search:")
        self.time_entry = tk.Entry(self, width=10)
        self.time_explain = tk.Label(self, text="time in seconds bigger than 0")

        # place the time on the grid

        self.time_label.grid(row=2, column=0, padx=5, pady=5, sticky="E")
        self.time_entry.grid(row=2, column=1, padx=5, pady=5, sticky="W")
        self.time_explain.grid(row=2, column=2, padx=5, pady=5, sticky="W")

        ######### add a button to open self.save_file_path using notepad.exe to see the saves #########
        self.open_button = tk.Button(self, text="Open Save file", command=self.open_save_file)

        # place the button on the grid

        self.open_button.grid(row=3, column=2, padx=5, pady=5)

        ######### copy last save to clipboard  #########

        self.copy_button = tk.Button(self, text="Copy last save to clipboard", command=self.copy_to_clipboard)

        # place the button on the grid

        self.copy_button.grid(row=3, column=0, padx=5, pady=5)

        ######### start/stop button #########

        self.start_button = tk.Button(self, text="Start", command=self.start_stop)

        # place the button on the grid

        self.start_button.grid(row=4, column=0, padx=5, pady=5, columnspan=3)

        ######### last outputs #########

        self.last_outputs_label = tk.Label(self, text="Last outputs:")
        self.last_outputs_text = tk.Text(self, width=110, height=10)
        self.last_outputs_text.config(state="disabled")

        # place the last outputs on the grid

        self.last_outputs_label.grid(row=5, column=0, padx=5, pady=5, columnspan=3)
        self.last_outputs_text.grid(row=6, column=0, padx=5, pady=5, columnspan=3)

        # let's lock the size of the window
        self.resizable(False, False)

        self.loadConfig()

    def loadConfig(self):
        if os.path.exists(os.path.join(self.current_exec_file_path, "config.ini")):
            try:
                with open(os.path.join(self.current_exec_file_path, "config.ini"), "r") as f:
                    lines = f.readlines()
                    self.folder_path = lines[0].split(" : ")[1].strip()
                    self.save_file_path = lines[1].split(" : ")[1].strip()
                    self.time = int(lines[2].split(" : ")[1].strip())
                    self.name_entry.insert(tk.END, lines[3].split(" : ")[1].strip())
                    self.path_entry.config(state="normal")
                    self.path_entry.insert(tk.END, self.folder_path)
                    self.path_entry.config(state="disabled")
                    self.time_entry.insert(tk.END, f"{self.time}")
                    self.save_file_path = os.path.join(self.folder_path, self.name_entry.get())
                self.update_last_outputs("Config file loaded")
            except:
                self.update_last_outputs("Error while loading config file")
                self.update_last_outputs("Delete the old one and Re-open the program")
        else:
            self.update_last_outputs("Config file doesn't exist")
            self.update_last_outputs("Creating a new one")

            with open(os.path.join(self.current_exec_file_path, "config.ini"), "w") as f:
                f.write("folder_path : \n")
                f.write("save_file_path : \n")
                f.write("time : \n")
                f.write("name : \n")

            self.update_last_outputs("Config file created at : " + os.path.join(self.current_exec_file_path, "config.ini"))

    def select_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_entry.config(state="normal")
            self.folder_path = path
            self.path_entry.insert(tk.END, path)
            self.path_entry.config(state="disabled")

    def update_path(self, event):
        self.save_file_path = os.path.join(self.folder_path, self.name_entry.get())

    def open_save_file(self):
        if self.save_file_path:
            if os.path.exists(self.save_file_path):
                os.system("notepad.exe " + self.save_file_path)
            else:
                self.update_last_outputs("File doesn't exist")
        else:
            self.update_last_outputs("Please select a folder_path")

    def start_stop(self):

        # check if folder_path is not empty
        if not self.folder_path:
            self.update_last_outputs("Please select a folder_path")
            return

        # now check if there's a file name
        if not self.name_entry.get():
            self.update_last_outputs("Please input a file name")
            return

        # now check if there's a time and its of the type int
        try:
            int(self.time_entry.get())
        except ValueError:
            self.update_last_outputs("Please input a number for the time")
            return

        # now check if the time is not 0
        if int(self.time_entry.get()) < 0 or int(self.time_entry.get()) == 0:
            self.update_last_outputs("Please input a number bigger than 0")
            return

        # start the saves

        if not self.is_running:
            # start the thread
            self.is_running = True
            self.start_button.config(text="Stop")
            self.time = int(self.time_entry.get())
            self.save_file_path = os.path.join(self.folder_path, self.name_entry.get())

            # disable the widgets
            self.path_button.config(state="disabled")
            self.name_entry.config(state="disabled")
            self.time_entry.config(state="disabled")

            #disable the open buttons
            self.open_button.config(state="disabled")

            # check if the file exists, if not creates it
            if not os.path.exists(self.save_file_path):
                with open(self.save_file_path, 'w') as file:
                    file.write('')
                self.update_last_outputs("No save file found, creating a new one")
                self.update_last_outputs(f"Save file created")
            else:
                self.update_last_outputs("Save file found")

            self.thread = threading.Thread(target=self.start_saves, daemon=True)
            self.thread.start()
        else:
            self.stop_saves()

    def copy_to_clipboard(self):
        if self.save_file_path and os.path.exists(self.save_file_path):
            try:
                # open the save file and get the lines
                with open(self.save_file_path, 'r') as file:
                    the_list = file.readlines()
                # get the dates
                dates = []
                for line in the_list:
                    dates.append(line.split(' -> ')[0])
                # get the most recent date
                most_recent = max(dates)
                # get the index of the most recent date
                index = dates.index(most_recent)
                # return the most recent line
                pyperclip.copy(the_list[index].split()[-1])
                self.update_last_outputs("Last save copied to clipboard")
            except:
                self.update_last_outputs("No save found")
        else:
            self.update_last_outputs("No save file found")

    def update_last_outputs(self, text):
        self.last_outputs_text.config(state="normal")
        self.last_outputs_text.insert("1.0", text + "\n")
        self.last_outputs_text.config(state="disabled")

    def start_saves(self):
        self.update_last_outputs("Program started")

        with open(os.path.join(self.current_exec_file_path, "config.ini"), "w") as f:
            f.write(f"folder_path : {self.folder_path}\n")
            f.write(f"save_file_path : {self.save_file_path}\n")
            f.write(f"time : {self.time}\n")
            f.write(f"name : {self.name_entry.get()}\n")
        while self.is_running:
            # first find the vrchat logs
            vrchat_logs = self.find_latest_txt_files(self.vrchat_path)

            # find the last save times
            last_save_time = self.find_last_saved_time(vrchat_logs)

            self.save_to_file(last_save_time)

            self.scan_loop_event = threading.Event()
            self.scan_loop_event.wait(self.time)

        self.update_last_outputs("Program stopped")
        self.start_button.config(state="active")
        self.start_button.config(text="Start")

        # enable the widgets
        self.path_button.config(state="normal")
        self.name_entry.config(state="normal")
        self.time_entry.config(state="normal")

        #enable the open buttons

        self.open_button.config(state="normal")

    def stop_saves(self):
        self.is_running = False
        self.start_button.config(state="disabled")
        if self.scan_loop_event is not None:
            self.scan_loop_event.set()

    def find_latest_txt_files(self, path):
        nb_files_before = len(self.found_save_files)
        txt_files = self.find_all_txt_files(path)
        if nb_files_before == 0:
            # 1st scan, return everything
            return txt_files
        # Otherwise, return all new files + the last one before that,
        # in case multiple were created at once since the last scan
        nb_new_files = len(self.found_save_files) - nb_files_before
        # File names are timestamped in ISO-8601, they will be sorted in ascending date
        return sorted(txt_files)[-(nb_new_files + 1):]

    def find_all_txt_files(self, path):
        txt_files = []
        for root, dirs, files in os.walk(path):
            for file in fnmatch.filter(files, 'output_log_*.txt'):
                txt_files.append(os.path.join(root, file))

        for i in txt_files:
            if i not in self.found_save_files:
                self.update_last_outputs(f"Log file found: {i}")
                self.found_save_files.append(i)
        return txt_files

    def find_last_saved_time(self, txt_files):
        save_times = []
        for filename in txt_files:
            self.update_last_outputs(f"Scanning file {filename} ...")
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    if '[🦀 Idle Home 🦀] Saved' in line:
                        line = line.strip().split()
                        text_to_save = f"{line[0]} - {line[1]} -> {line[-1]}"
                        save_times.append(text_to_save)
        return save_times

    def save_to_file(self, save_times):
        last_saves = []

        with open(self.save_file_path, 'r') as file:
            for line in file.readlines():
                last_saves.append(line[:-1:])

        # combine the two lists into one without repetitive lines

        final = list(set(save_times + last_saves))
        if len(last_saves) == len(final):
            self.update_last_outputs(f"{datetime.now().isoformat()} ---> No new saves")
        else:
            self.update_last_outputs(f"{datetime.now().isoformat()} ---> {len(final) - len(last_saves)} New save/s found")
            #first sorte the list by date
            final.sort(key=lambda x: datetime.strptime(x.split(' -> ')[0], '%Y.%m.%d - %H:%M:%S'))
            with open(self.save_file_path, 'w') as file:
                for line in final:
                    file.write(line + '\n')

def run():
    main = MainProgramGUI()
    main.mainloop()

if __name__ == "__main__":
    run()
