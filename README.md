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

Once the files are downloaded, place the files in a path that is accessible to CipherCat.


## Usage
### Windows
Visit the **config.py** file for more instructions on how to set up the tool.

Once the tool has been configured to the desired cracking state, open the **main.py** file in an IDE and run the tool.
### Linux
Refer to the output of ```--help``` for usage information and general help with the tool. 


## Frequently Asked Questions
### Does this tool work with WSL, or Windows Subsystem for Linux?
Yes! The tool works with WSL just as it would be used in any other distribution of Linux.

### Will more hashing modes come out in the future?
Depending on the popularity and usage of the tool, it may receive more hashing options in the future.
