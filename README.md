# Automatic Downloads Organizer for MAC

The Automatic Downloads Organizer is a helpful script and folder action setup for macOS that automates the organization of files in your Downloads folder based on their file types.

## Description

This setup combines a Python script with a macOS folder action to automatically categorize and move files in your Downloads folder into specific subfolders based on their file extensions.

## Features

- **Automated Organization:** Files in your Downloads folder are automatically categorized and sorted into appropriate subfolders.
- **Customizable:** You can easily customize the script to add or modify file type categories and extensions.

## Requirements

- A macOS system with Python installed.

## Setup Instructions

### Step 1: Download the Script

1. Download the script file named `downloads.py`.

### Step 2: Open Automator

1. Search for "Automator" using Spotlight or find it in the Applications folder.

### Step 3: Create a New Folder Action

1. Choose "File" > "New Folder Action" in Automator.

### Step 4: Choose the Downloads Folder

1. In the top menu, select your Downloads folder from the "Folder Action receives files and folders added to" dropdown.

### Step 5: Add the Run Shell Script Action

1. In the left sidebar, search for "Run Shell Script" in the actions.
2. Drag the "Run Shell Script" action to the right-side pane.

### Step 6: Configure the Shell Script

1. In the "Run Shell Script" action, choose "as arguments" from the "Pass input:" dropdown.
2. Replace the default script with the path to your script, for example:
   
   ```bash
   /usr/bin/python3 /path/to/your/script.py "$@"
   ```

### Step 7: Save the Folder Action

1. Save the Automator workflow by clicking on "File" in the menu bar and selecting "Save."
2. Choose a location to save the workflow and give it a meaningful name, such as "Downloads Organizer."


## Additional Notes

- Always back up your important data before running scripts that modify your file structure.
- Folder actions are a powerful tool, so exercise caution and test on a smaller scale before deploying widely.
- Be mindful of macOS updates that might affect folder actions or script execution.


This README is provided under the [MIT License](LICENSE).


