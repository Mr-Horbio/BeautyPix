<h1 align="center">
  <img src="static/Beautypix-logo.png" alt="Beautypix" width="200px">
  <br>
</h1>

<h4 align="center">Fast capturing screenshots and merging files tool.</h4>
<p align="center">
  <a href="#features">Features</a> •
  <a href="#installation">Install</a> •
  <a href="#Usage">Usage</a> •
  <a href="#Library ">Library</a> •
  <a href="https://www.youtube.com/channel/UCBiIg0P8onz7EZgXNhjpR4A">Join Youtube</a>
</p>

---




# BeautyPix
BeautyPix is a versatile tool designed to enhance web security and data management by capturing screenshots of subdomains and merging files while eliminating duplicate entries. It streamlines the process of visual verification and data consolidation, making it an essential utility for web developers, security analysts, and data managers.

## Features
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

```
#for screenshot
python beautypix.py screenshot -p <subdomains.txt> 
```
```
#for merge files
python beautypix.py merge -f file1.txt file2.txt
```
# Examples (for Screenshot)
```
$ python beautypix.py screenshot -p domainlist.txt -t 2
```
### (Merge two file)
```
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

