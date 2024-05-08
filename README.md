# Link Cleaner Tool 🧹

A tool for managing and organizing big collections of URLs. It's perfect for pulling out and sorting links from megathreads or similar big lists.

## Requirements 📋

- Python 3.x
- pandas
- tkinter

## Installation 🛠️

You need Python 3 and Thonny, a simple IDE made for beginners. Install Thonny from the [official website](https://thonny.org).

To install additional libraries like `pandas`:
1. Open Thonny and go to `Tools` > `Manage packages...`.
2. Search for `pandas` and click `Install`.

tkinter is already part of Python's standard library, so you don't need to install it separately.

## Usage 🔍

Here’s how to use the Link Cleaner Tool:

1. **Start the Tool**: Open the script in Thonny and run it.
2. **Load Files**: Click `Choose Files` to load your CSV files that contain URLs.
3. **Apply Filters**:
   - You can enter a custom filter text to keep only URLs that include specific words. For example, if you only want URLs that have the word "tutorial", you type "tutorial" in the text box.
   - Check the boxes to filter out Reddit links and/or remove duplicate URLs.
4. **Clean and Save**: Click `Clean Links and Save` to process the URLs and save them to a text file.

## Features 🌟

- **CSV Input**: Load URLs from CSV files.
- **Filter Options**:
  - Custom text filtering for URLs.
  - Pre-set filters to exclude specific types of links, like Reddit.
  - Option to remove duplicate URLs.
- **Export**: The cleaned URLs are saved in a simple text file.

## GUI Components 🖥️

- **File Selection**: Choose CSV files with URLs to clean.
- **Filter Settings**: Text entry and checkboxes to set filters.
- **Save Button**: Process and save the cleaned list of URLs.

## Screenshots 📸

[![Jr6K80J.md.png](https://iili.io/Jr6K80J.md.png)](https://freeimage.host/i/Jr6K80J)

## Contributing 🤝

Contributions are welcome. Please fork the repository and submit pull requests with your suggested changes.

## License 📄

This project is open-sourced under the MIT License. See the LICENSE file for more details.
