# version 1.1

# have a graphic interface that allows the users to:
#  input the path to where they want to store the save files
#  input the time in seconds between each search
#  a button that both start and stop the program
#  a Text widget that's read-only that shows the last 10 outputs from the program
#    this text widget will be updated every time does a search, and it'll display the time and message

# this graphic interface will be made with tkinter

import os
import time
import tkinter as tk
import tkinter.filedialog as filedialog

import threading


# create a class for the gui
class MainProgramGUI(tk.Tk):
    def __init__(self):
        super().__init__()

        # lets define the window yes
        self.title("VRChat Idle home auto save made by fuzzyCute")

        # start the variables
        self.vrchat_path = os.environ['USERPROFILE'] + '\\AppData\\LocalLow\\VRChat\\VRChat'

        self.path = ""
        self.save_file_path = ""
        self.time = 0
        self.is_running = False

        # create the GUI elements or widgets or what's the name you give them

        # lets make it a grid system

        ######### path #########

        self.path_label = tk.Label(self, text="Path to the save file:")
        self.path_entry = tk.Entry(self, width=60)
        self.path_entry.config(state="disabled")
        self.path_button = tk.Button(self, text="Select path", command=self.select_path)

        # place the path on the grid

        self.path_label.grid(row=0, column=0, padx=5, pady=5, sticky="E")
        self.path_entry.grid(row=0, column=1, padx=5, pady=5, sticky="W")
        self.path_button.grid(row=0, column=2, padx=5, pady=5)

        ######### file_name #########

        self.name_label = tk.Label(self, text="Name of the file:")
        self.name_entry = tk.Entry(self, width=30)
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

        ######### start/stop button #########

        self.start_button = tk.Button(self, text="Start", command=self.start_stop)

        # place the button on the grid

        self.start_button.grid(row=3, column=0, padx=5, pady=5, columnspan=3)

        ######### last outputs #########

        self.last_outputs_label = tk.Label(self, text="Last outputs:")
        self.last_outputs_text = tk.Text(self, width=70, height=10)
        self.last_outputs_text.config(state="disabled")

        # place the last outputs on the grid

        self.last_outputs_label.grid(row=4, column=0, padx=5, pady=5, columnspan=3)
        self.last_outputs_text.grid(row=5, column=0, padx=5, pady=5, columnspan=3)

        # let's lock the size of the window
        self.resizable(False, False)

    def select_path(self):
        path = filedialog.askdirectory()
        if path:
            self.path_entry.config(state="normal")
            self.path = path
            self.path_entry.insert(tk.END, path)
            self.path_entry.config(state="disabled")

    def start_stop(self):

        #check if path is not empty
        if not self.path:
            self.update_last_outputs("Please select a path")
            return

        #now check if there's a file name
        if not self.name_entry.get():
            self.update_last_outputs("Please input a file name")
            return

        #now check if there's a time and its of the type int
        try:
            int(self.time_entry.get())
        except ValueError:
            self.update_last_outputs("Please input a number for the time")
            return

        #now check if the time is not 0
        if int(self.time_entry.get()) < 0 or int(self.time_entry.get()) == 0:
            self.update_last_outputs("Please input a number bigger than 0")
            return

        #start the saves

        if not self.is_running:
            #start the thread
            self.is_running = True
            self.start_button.config(text="Stop")
            self.time = int(self.time_entry.get())
            self.save_file_path = os.path.join(self.path, self.name_entry.get())

            #disable the widgets
            self.path_button.config(state="disabled")
            self.name_entry.config(state="disabled")
            self.time_entry.config(state="disabled")


            # check if the file exists, if not creates it
            if not os.path.exists(self.save_file_path):
                with open(self.save_file_path, 'w') as file:
                    file.write('')

            self.thread = threading.Thread(target=self.start_saves, daemon=True)
            self.thread.start()
        else:
            self.stop_saves()

    def update_last_outputs(self, text):
        self.last_outputs_text.config(state="normal")
        self.last_outputs_text.insert("1.0", text + "\n")
        self.last_outputs_text.config(state="disabled")

    def start_saves(self):
        self.update_last_outputs("Program started")
        while self.is_running:
            # first find the vrchat logs
            vrchat_logs = self.find_more_recent_txt_files(self.vrchat_path)

            # find the last save times
            last_save_time = self.find_last_saved_time(vrchat_logs)

            self.save_to_file(last_save_time)

            time.sleep(self.time)

        self.update_last_outputs("Program stopped")
        self.start_button.config(state="active")
        self.start_button.config(text="Start")

        # enable the widgets
        self.path_button.config(state="normal")
        self.name_entry.config(state="normal")
        self.time_entry.config(state="normal")

    def stop_saves(self):
        self.is_running = False
        self.start_button.config(state="disabled")

    def find_more_recent_txt_files(self, path):
        txt_files = []
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith('.txt'):
                    txt_files.append(os.path.join(root, file))
        return max(txt_files, key=os.path.getctime)

    def find_last_saved_time(self, txt_file):
        save_times = []
        with open(txt_file, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            last_lines = []
            for line in lines[-100:]:
                if line.strip():
                    last_lines.append(line.strip())
        for line in last_lines:
            if '[🦀 Idle Home 🦀] Saved' in line:
                line = line.split()
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
            self.update_last_outputs(f"{time.ctime()} ---> No new saves")
        else:
            self.update_last_outputs(f"{time.ctime()} ---> {len(final) - len(last_saves)} New save/s found")
            with open(self.save_file_path, 'w') as file:
                for line in final:
                    file.write(line + '\n')

if __name__ == "__main__":
    main = MainProgramGUI()
    main.mainloop()

