# Changelog

## 1.1.5
### Updates
- Stop scanning loop as soon as the "stop" button is clicked,
  instead of waiting for the next loop.
- Iterate on all lines on the fly without storing them to improve performance
- Due to the aforementioned reading performance improvement,
  the checkbox to set a a line limit has been removed.
- Scan all files once in the beginning, then only re-scan the latest one.
- Added changelog document
- Added docs for building the Windows exe from the script

## 1.1.4
### Updates
- The limit of lines that the program search for in the logs went from 100 to 1000
- Added a checkbox to ignore this limit

## 1.1.3
### Bug Fixes
- The program now looks at all log files on the folder
- The Information window is wider

## 1.1.2
### Bug Fixes
- Save file now has the saves sorted by date
- Users can now copy the last save to the clipboard while the program is running

## 1.1.1
### Changes
- added button to clipboard last save from save file (if exists)
- added button to open save file with notepad, Thanks to M1XZG
- Added the creation of a config file that'll be created on the same folder as the program
    - it'll store the previous options made the last time the program was run
    - if the config file didn't exist it'll create a new one
- added more informational text

**IMPORTANT:** Some antivirus will flag this as a virus, unfortunately this is an known issue. 
If you think this is an issue you can always use version 1.0

## 1.1
### Changes
- Added GUI for the project
- you can now save the file anywhere
- you can give your save file a different custom extension, instead of the .log extension
- some custom error prevention.
- Hamburger

**IMPORTANT:** Some antivirus will flag this as a virus, unfortunately this is an known issue.
If you think this is an issue you can always use version 1.0

## 1.0
### Initial release
