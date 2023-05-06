# first find the only txt file on a folder
# if there more than one, pick the one thats more recent
# open the file and search the last 100 lines
# remove the white spaces 'empty' or '\n'
# if the line has '[🦀 Idle Home 🦀] Saved' then save those lines to a list
# after do a for loop for the list and then break the lines

import os
import time

path = os.environ['USERPROFILE'] + '\\AppData\\LocalLow\\VRChat\\VRChat'

last_save_path = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') + f'\\save_times.log'

tm = int(input("Enter time in seconds between each search: "))

if not os.path.exists(last_save_path):
    with open(last_save_path, 'w') as file:
        file.write('')


def find_more_recent_txt_files(path):
    txt_files = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if file.endswith('.txt'):
                txt_files.append(os.path.join(root, file))
    return max(txt_files, key=os.path.getctime)


def find_last_saved_time(txt_file):
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


def save_to_file(save_times):
    last_saves = []
    with open(last_save_path, 'r') as file:
        for line in file.readlines():
            last_saves.append(line[:-1:])
    # combine the two lists into one without repetitive lines

    final = list(set(save_times + last_saves))
    if len(last_saves) == len(final):
        print("No new saves")
    else:
        print(f"{len(final) - len(last_saves)} New save/s found")
        with open(last_save_path, 'w') as file:
            for line in final:
                file.write(line + '\n')


def main():
    txt_file = find_more_recent_txt_files(path)
    save_times = find_last_saved_time(txt_file)
    save_to_file(save_times)


if __name__ == "__main__":

    while True:
        main()
        time.sleep(tm)
