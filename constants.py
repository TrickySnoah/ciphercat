
import string, os



# os types

WINDOWS_SYSTEM_INDICATORS = ["windows", "win32", "nt", "win64"]

LINUX_SYSTEM_INDICATORS = ["linux" ,"linux2", "posix"]



# flags

ACCEPTABLE_FLAGS = ["-w","-m","--files-hashes","--files-h-output","-o","--files-input","-c","--hashcat-path","-p", "-v", "--hashcat-potfile-path"]

REQUIRED_FLAGS = ["word"]

DEFAULT_FLAGS = {"mode":"0", "file hashes":r"files/hashes.txt", "file hashes output":r"files/cracked.txt", "file input":r"files/wordlist.txt", "cores":"1", "permutations":"0", "version":"0"}

""" NOTES FOR REQUIRED / NON-REQUIRED STUFF

REQUIRED -
-w is for word. This shows the type of password format the cracker will be cracking for

NON REQUIRED -
-m is for mode. this will be the mode that Hashcat uses and is directly from their mode list. The default will be mode 0 (MD5)
--files-hashes is for the file that contains the hashes to crack. The default is "hashes.txt"
--files-h-output OR -o is for the results of cracking the hashes. The default is "cracked.txt"
--files-input is for the given word list. The defualt is "wordlist.txt"
-t is for the amount of threads being used. The default is going to be 1 ('0' or '1' to represent this)
-p is used for the types of permutations needed. The default is no changes, with numbers being used to represent the other types (caps, lowercase, capitalized, all, etc.)
-v is used to tell whether the program will integrate with Hashcat or be used on its own. The default is to auto detect based on the word format given

SITUATIONAL -
--hashcat-path is used to tell where the hashcat.exe file is at. This will be needed IF it is not specified in the config.py file

NO LONGER BEING USED
--files-w-output is for the files where the resulting word list will go. I have change my mind on 11/12/2025 11:00 PM to make this automatically create a certain amount
 of .txt files depending on the resulting size of all the possible passwords

"""

HELP_FLAGS = ["-help", "--help", "-h", "-man", "--man", "--manual"]

VERSION_FLAGS = ["--version"]

ACCEPTABLE_HASH_MODES = ["0"]



# masking related

ACCEPTABLE_MASKS = ["a","s","d","u","l","t"]

HASHFOX_UNIQUE_MASKS = ["t"]

SYMBOLS = """`~!@#$%^&*()_-+={[}]|\\;:'",<.>/?"""
NUMBERS = "0123456789"
ALPHA_UPPER = string.ascii_uppercase
ALPHA_LOWER = string.ascii_lowercase
ALL = SYMBOLS + NUMBERS + ALPHA_UPPER + ALPHA_LOWER
TOP = SYMBOLS + NUMBERS
MASK_DICTIONARY = {"s":SYMBOLS,"d":NUMBERS,"u":ALPHA_UPPER,"l":ALPHA_LOWER,"a":ALL,"t":TOP}



# arguments

ACCEPTABLE_PERMUTATIONS = ["0", "1", "2", "3", "4"]

""" PERMUTATIONS INFORMATION

0 for just taking the passwords as they are in the wordlist

1 for doing just lowercase

2 for doing just uppercase

3 for doing capitalizations

4 for doing all (excluding original)

"""

ACCEPTABLE_VERSIONS = ["0", "1", "2"]



# file related

HASHCAT_MODES_FILE = r"files/hashcat_modes.txt"

MANUAL_FILE = r"resources/man.info"

PASSWORDS_DEFAULT_FILE_PATH = r"files/password_files/passwordlist"



# other

MAX_THREADS = os.cpu_count()

EXIT_WAIT_TIME = 1

TOOL_VERSION = "1.0.0"

# MINIMUM_CHUNK_SIZE = 10000

MINIMUM_HASHCAT_WORDLIST_SIZE = 144384 # 144,384 is the minimum according to Hashcat
