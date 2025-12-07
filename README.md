# CipherCat
CipherCat is a Python-based, cross-platform hash-cracking tool optimized for efficient computation, reduced memory usage, and configurable CPU utilization that allows for independent usage or seamless integration with Hashcat. The goal for CipherCat is to make password cracking simpler and easier. CipherCat currently only offers the MD5 hash cracking mode but may offer more in the future.


## License
CipherCat is licensed under the MIT license. More information can be found in [LICENSE](https://github.com/TrickySnoah/ciphercat/blob/main/LICENSE).


## Requirements
- Python **3.10.11**
- (Optional) Hashcat **v6.2.6**


## Installation
### Windows
Download the ZIP of the repository.

Move the ZIP file to the desired path.

Extract the contents.
### Linux
Clone the repository.
```
git clone https://github.com/TrickySnoah/ciphercat.git
```

### (Optional) Hashcat
Visit Hashcat's [releases page](https://hashcat.net/hashcat/) and install the binaries for Hashcat v6.2.6.

Once the 7z zip file is downloaded:
#### Windows
Extract the 7z zip file in any desired path.

Relocate the **OpenCL** and **modules** folders and **hashcat.hcstat2** file to the same folder as CipherCat's **main.py** file.

Add a new file in the same folder as the **main.py** file and completely rename the newly created file to **hashcat.potfile**

#### Linux
Extract the 7z zip file in a path that is accessible to CipherCat


## Usage
### Windows
Visit the **config.py** file for more instructions on how to set up the tool.

Once the tool has been configured to the desired cracking state, open the **main.py** file in an IDE and run the tool.
### Linux
Refer to the output of ```python3 main.py --help``` for usage information and general help with the tool. 


## Frequently Asked Questions
### Why is Hashcat is not working with Windows?
For Hashcat functionality with Windows, the **OpenCL** and **modules** folders and **hashcat.hcstat2** and **hashcat.potfile** files must be in the same path as the **main.py** file.

### Why is Hashcat is not working yet I have already moved all of the files?
First, double check that the folders and files are where they should be. Next, ensure that the given paths either in the **config.py** file or in the Linux command are accurate.

### What file should the hashcat_path variable in the config.py file or the ```--hashcat-path``` in my Linux command point towards?
The hashcat_path variable or the ```--hashcat-path``` flag should both point towards Hashcat's .exe file or ELF file. The elf file may look like a file named "hashcat" without any file extension.

### Does this tool work with WSL, or Windows Subsystem for Linux?
Yes! The tool works with WSL just as it would be used in any other distribution of Linux.

### Will more hashing modes come out in the future?
Depending on the popularity and usage of the tool, it may receive more hashing options in the future.
