<h1 align="center">
  <img src="static/BeautyPix-logo.png" alt="Beautypix" width="500px">
  <br>
</h1>

<h4 align="center">Fast capturing screenshots and merging files tool.</h4>
<p align="center">
  <a href="https://www.youtube.com/channel/UCBiIg0P8onz7EZgXNhjpR4A" ><img src = "https://img.shields.io/badge/Join-Youtube-blue"></a>
</p>

<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Install</a> •
  <a href="#Usage">Usage</a> •
  <a href="#Library ">Library</a> •
  <a href="https://www.youtube.com/channel/UCBiIg0P8onz7EZgXNhjpR4A">Join Youtube</a> •
  <a href="#Report">Bug Report </a> 
</p>

---




# BeautyPix
BeautyPix is a versatile tool designed to enhance web security and data management by capturing screenshots of subdomains and merging files while eliminating duplicate entries. It streamlines the process of visual verification and data consolidation, making it an essential utility for web developers, security analysts, and data managers.

## Features
<h1 align="left">
  <img src="static/Beautypix-run.png" alt="Beautypix" width="700px"></a>
  <br>
</h1>

1. **Screenshot Capture:**
Automatically takes screenshots of specified subdomains, allowing users to visually verify the content and appearance of multiple web pages. The screenshots are saved in a designated directory with a clear, organized naming convention.

2. **File Merging**: 
Merges two input files, ensuring that duplicate entries are removed. This feature is particularly useful for consolidating lists of URLs, IP addresses, or any other data that might contain redundant information.

3. **Error Handling**: 
Robust error handling mechanisms ensure that the tool can handle various exceptions, such as network issues, file not found errors, and WebDriver exceptions, providing clear feedback to the user.

## Installation
Clone the repository and install the required dependencies:
```
git clone https://github.com/yourusername/BeautyPix.git
cd BeautyPix
pip install -r requirements.txt

```
# Usage
```sh
python beautypix.py -h

```

This will display help for the tool. Here are all the switches it supports.

```yaml
usage: beautypix.py [-h] [-V] {screenshot,merge} ...

Usages of Beautypix

positional arguments:
  {screenshot,merge}
    screenshot        Take screenshots of subdomains
    merge             Merge two files and remove duplicates

options:
  -h, --help          show this help message and exit
  -V                  Print version
```

```sh
#for screenshot
$ python beautypix.py screenshot -h
$ python beautypix.py screenshot -p <subdomains.txt> 
```
```sh
#for merge files
$ python beautypix.py merge -h
$ python beautypix.py merge -f file1.txt file2.txt
```
# Examples (for Screenshot)
```sh
$ python beautypix.py screenshot -p domainlist.txt -t 2
```
### (Merge two file)
```yaml
$ cat file1.txt
  1
  2
  3
  4
  5
$ cat file2.txt
  1
  2
  7
  8
  9

$ python beautypix.py merge -f file1.txt file2.txt
$ cat merged.txt
  1
  2
  3
  4
  5
  7
  8
  9
```
# Library 
Beautypix use python libraries:
- Selenium
- requests
- pyfiglet
- argparser
- sys
- os
- re
- time

# Report
Report Bug on horbio222@gmail.com
