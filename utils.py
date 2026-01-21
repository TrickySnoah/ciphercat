
import itertools # iteration tool used for permutations
import os # total core amount
import sys # os discovery
import subprocess # used to run hashcat
import hashlib # generates MD5 hashes
from time import time as time, sleep as wait # for output and IDE purposes. Thonny was performing too quick and the processed the "exit(0)" statements and ended the program too early sometimes.
from concurrent.futures import ProcessPoolExecutor # multiprocessing / using all cores of CPU. Not threads because of the GIL?
from constants import *
from config import *



##############################################################################################################################
#-------------------------------------------------- CAUSES AND SOLUTIONS ----------------------------------------------------#
##############################################################################################################################

def solutions(error_code, args=None, os=None):
    
    print("ERROR. See causes and solutions below.\n\n" + "-"*15)
    
    # 001 - Missing Hashcat file paths
    if error_code == 1:
        print("Error code 001: Missing Hashcat file paths while trying to use Hashcat.\n")
        print("""If Hashcat is not wanted, then this error is typically due to the version being "0" or "2".""")
        print("If Hashcat usage is desired:")
        if os == "Linux":
            print("  No argument was given. Ensure the Hashcat variables within the config.py file hold accurate paths. If")
            print("   arguments are wanting to be given, refer to the output of 'python3 main.py --help'.")
        elif os == "Win":
            print("  Ensure the Hashcat variables within the config.py file hold accurate paths.")
        print("  For more help, refer to: https://github.com/TrickySnoah/ciphercat/blob/main/README.md#optional-hashcat")
        return
    
    # 002 - Incorrect Hashcat potfile path
    if error_code == 2:
        print("Error code 002: Incorrect Hashcat potfile path.\n")
        if os == "Linux":
            print("If an argument was given in the command, ensure that the path was spelled correctly and is accurate.")
            print("If no argument was given in the command, ensure that the hashcat_potfile_path variable in the config.py file is accurate.")
        elif os == "Win":
            print("Ensure that the hashcat_potfile_path variable in the config.py file is accurate.")
            print("""The file "hashcat.potfile" should be located in the same directory as main.py file. If not, create a new file and completely rename it to "hashcat.potfile".""")
        print("For more help, refer to:")
        print("  Hashcat installation: https://github.com/TrickySnoah/ciphercat/blob/main/README.md#optional-hashcat")
        print("  Hashcat Q/A: https://github.com/TrickySnoah/ciphercat/blob/main/README.md#why-is-hashcat-is-not-working-yet-i-have-already-moved-all-of-the-files")
        return
    
    # 003 - Incorrect Hashcat path
    if error_code == 3:
        print("Error code 003: Incorrect Hashcat path.\n")
        if os == "Linux":
            print("If an argument was given in the command, ensure that the path was spelled correctly and is accurate.")
            print("If no argument was given in the command, ensure that the hashcat_path variable in the config.py file is accurate.")
        elif os == "Win":
            print("Ensure that the hashcat_path variable in the config.py file is accurate.")
            print("The path given to the hashcat_path variable in the config.py file should point towards Hashcat's .exe file")
        print("For more help, refer to:")
        print("  Hashcat installation: https://github.com/TrickySnoah/ciphercat/blob/main/README.md#optional-hashcat")
        print("  Hashcat path Q/A: https://github.com/TrickySnoah/ciphercat/blob/main/README.md#what-file-should-the-hashcat_path-variable-in-the-configpy-file-or-the---hashcat-path-in-my-linux-command-point-towards")
        return
    
    # 004 - Could Not Open Wordlist
    if error_code == 4:
        print("Error code 004: Could Not Open Wordlist.\n")
        if os == "Linux":
            print("Ensure that the provided argument for '--files-input' is accurate.")
        elif os == "Win":
            print("Ensure that the value for the 'input_file' variable in the config.py file is accurate.")
        return
    
    # 005 - Could Not Open Hashes File
    if error_code == 5:
        print("Error code 005: Could Not Open Hashes File.\n")
        if os == "Linux":
            print("Ensure that the provided argument for '--files-hashes' is accurate.")
        elif os == "Win":
            print("Ensure that the value for the 'hashes_file' variable in the config.py file is accurate.")
        return
    
    # 006 - Error With Provided Password Format(s)
    if error_code == 6:
        print("Error code 006: Error With Provided Password Format(s).\n")
        if os == "Linux":
            print("The argument for every '-w' flag:")
            print("  should have all characters be lowercase.")
            print("  should have a question mark (?) before every single mask.")
            print("""  should have "word" somewhere in the argument that represents where the base word is in each password format.""")
            print("For more help, refer to the output of 'python3 main.py --help'.")
        elif os == "Win":
            print("The provided value for the 'password_format' in the config.py file:")
            print("  should have a comma separating each password format if multiple are given.")
            print("  should have no spaces anywhere.")
            print("""  should have "word" somewhere in he value that represents where the base word is in each password format.""")
            print("For more help, refer to the 'Instructions and Help' section at the bottom of the config.py file.")
        return
    
    # 007 - Error With Provided Hash Mode
    if error_code == 7:
        print("Error code 007: Error With Provided Hash Mode.\n")
        if os == "Linux":
            print("Ensure that the argument provided for the '-m' flag is accurate.")
            print("Refer to the output of 'python3 main.py --help' to find all of the arguments for hash modes.")
        elif os == "Win":
            print("Ensure that the value given to the hashcat_mode variable in the config.py file is accurate.")
            print("Refer to the 'Instructions and Help' section at the bottom of the config.py file to find all of the available values for the hashcat_mode variable.")
        print("To find all currently supported hash functions, refer to https://github.com/TrickySnoah/ciphercat/blob/main/README.md#supported-hash-functions")
        return
    
    # 008 - Error With Provided Permutations
    if error_code == 8:
        print("Error code 008: Error With Provided Permutations.\n")
        print("Perumations, in this case, refers to all of the capitalization possibilities of a provided password base.")
        print(""" For example, all permutations of "Hello World" would be "hello world", "Hello world", "hello World", and "Hello World".""")
        if os == "Linux":
            print("Ensure that the argument provided for the '-p' flag is accurate.")
            print("Refer to the output of 'python3 main.py --help' to find all of the arguments for permutations.")
        elif os == "Win":
            print("Ensure that the value given to the permutations variable in the config.py file is accurate.")
            print("Refer to the 'Instructions and Help' section at the bottom of the config.py file to find all of the available values for the permutations variable.")
        return
    
    # 009 - Error With Provided Version
    if error_code == 9:
        print("Error code 009: Error With Provided Verison.\n")
        print("Version, in this case, refers to the tool that CipherCat is using as CipherCat has the option of either")
        print(" being independent or integrating with Hashcat for more password cracking capability.")
        if os == "Linux":
            print("Refer to the output of 'python3 main.py --help' to find all of the arguments for version.")
        elif os == "Win":
            print("Refer to the 'Instructions and Help' section at the bottom of the config.py file to find all of the available values for the version variable.")
        print("For more help, refer to https://github.com/TrickySnoah/ciphercat/blob/main/README.md#what-does-version-mean-to-ciphercat")
        return
    
    # 010 - Error With Flags and Arguments
    if error_code == 10:
        print("Error code 010: Error With Flags and Arguments.\n")
        print("For all of the available flags, refer to the output of 'python3 main.py --help'.")
        return
    
    # 011 - Error With Required Flags/Variables
    if error_code == 11:
        print("Error code 011: Error With Required Flags/Variables.\n")
        if os == "Linux":
            print("Ensure that the '-w' flag is used with a valid argument.")
            print("For more help, refer to the output of 'python3 main.py --help'.")
        elif os == "Win":
            print("Ensure that the password_format variable in the config.py file has a valid value given to it.")
            print("For more help, refer to the 'Instructions and Help' section at the bottom of the config.py file.")
        return
            
            
        


##############################################################################################################################
#------------------------------------------------ DISCOVER OPERATING SYSTEM -------------------------------------------------#
##############################################################################################################################

def discover_os():
    
    result = ""
    for name in WINDOWS_SYSTEM_INDICATORS:
        if sys.platform.lower() == name:
            result = "Win"
            break
    
    if result == "":
        for name in LINUX_SYSTEM_INDICATORS:
            if sys.platform.lower() == name:
                result = "Linux"
                
    if result == "":
        print("Working with unknown OS. Defaulting to Manual version. (the version that Windows machines use).")
        result = "Win"
    
    return result

##############################################################################################################################
#--------------------------------------------------- HELP / MANUAL PAGE -----------------------------------------------------#
##############################################################################################################################

def display_manual():
    with open(MANUAL_FILE, "r", encoding="utf-8") as file:
        for line in file:
            print(line.rstrip())


##############################################################################################################################
#---------------------------------------------------- VALIDATING FILES ------------------------------------------------------#
##############################################################################################################################

def ensure_files():
    
    print("Validating the existance of the default files... ", end="")
    
    for flag in DEFAULT_FLAGS:
        if "file" in flag:
            try:
                with open(DEFAULT_FLAGS[flag], "r", encoding="utf-8"):
                    pass
            except:
                with open(DEFAULT_FLAGS[flag], "w", encoding="utf-8"):
                    pass
                
    for core in range(os.cpu_count()):
        try:
            with open(f"{PASSWORDS_DEFAULT_FILE_PATH}{core}.txt", "r", encoding="utf-8"):
                pass
        except:
            with open(f"{PASSWORDS_DEFAULT_FILE_PATH}{core}.txt", "w", encoding="utf-8"):
                pass
                
    print("Finished.")
                

##############################################################################################################################
#------------------------------------------------- MANUAL VALIDATE & PARSE --------------------------------------------------#
##############################################################################################################################

def manual_validate_and_parse(args, os_name):
    
    print("Validating and parsing information from within config.py file... ", end="")

    info = {"word":[], "mode":"", "file hashes":"", "file hashes output":"", "file input":"", "cores":"", "hashcat path":"", "permutations":"", "versions":"", "hashcat potfile path":""}
    
    # password format
    word_amount = 0
    for current_word in password_format.split(","):
        sub_target = "flag"
        previous = ""
        central_word_satisfied = False
        info["word"].append("")
        for char in current_word:
            if char == "?" and sub_target == "flag":
                sub_target = "input"
                continue
            elif char in ACCEPTABLE_MASKS and sub_target == "input":
                sub_target = "flag"
                info["word"][word_amount] += char
                continue
            elif char == "w" and sub_target == "flag" and previous == "":
                previous = "w"
                continue
            elif char == "o" and sub_target == "flag" and previous == "w":
                previous += "o"
                continue
            elif char == "r" and sub_target == "flag" and previous == "wo":
                previous += "r"
                continue
            elif char == "d" and sub_target == "flag" and previous == "wor":
                previous += "d"
                central_word_satisfied = True
                info["word"][word_amount] += "w"
                continue
            else:
                solutions(6, os=os_name)
                wait(EXIT_WAIT_TIME)
                exit(1)
        if not central_word_satisfied:
            solutions(6, os=os_name)
            wait(EXIT_WAIT_TIME)
            exit(1)
        word_amount += 1
        
    # hashcat mode
    if str(hashcat_mode) not in ACCEPTABLE_HASH_MODES:
        solutions(7, os=os_name)
        wait(EXIT_WAIT_TIME)
        exit(1)
    info["mode"] = str(hashcat_mode)
    
    # cores
    if str(cores).isdigit():
        if int(cores) <= MAX_THREADS and int(cores) > 0:
            info["cores"] = str(cores)
        elif str(cores) == "0":
            info["cores"] = os.cpu_count()
        else:
            print("Error with given cores. It is likely that too many were given.")
            wait(EXIT_WAIT_TIME)
            exit(1)
    else:
        print("Error with given cores.")
        wait(EXIT_WAIT_TIME)
        exit(1)
        
    # permutations
    if str(permutations) in ACCEPTABLE_PERMUTATIONS:
        info["permutations"] = str(permutations)
    else:
        solutions(8, os=os_name)
        wait(EXIT_WAIT_TIME)
        exit(1)
        
    # version
    if str(version) in ACCEPTABLE_VERSIONS:
        info["version"] = str(version)
    else:
        solutions(9, os=os_name)
        wait(EXIT_WAIT_TIME)
        exit(1)
        
    # all files
    info["file hashes"] = hashes_file

    # HASHCAT OUTPUT FILENAME
    info["file hashes output"] = h_output_file

    # RAW INPUT PASSWORDS FILE FILENAME
    info["file input"] = input_file

    # HASHCAT FILE PATH HERE (default for CLI version)
    info["hashcat path"] = hashcat_path
    
    # HASHCAT POTFILE PATH HERE (default for CLI version)
    info["hashcat potfile path"] = hashcat_potfile_path
    
    print("Finished.")
    
    return info
                
                
##############################################################################################################################
#-------------------------------------------------- CLI VALIDATE & PARSE ----------------------------------------------------#
##############################################################################################################################

def cli_validate_and_parse(args, os_name):
    
    print("Validating and parsing CLI command... ", end="")
    
    info = {"word":[], "mode":"", "file hashes":"", "file hashes output":"", "file input":"", "cores":"", "hashcat path":"", "permutations":"", "version":"", "hashcat potfile path":""}
    target = "flag"
    word_amount = 0
    
    for arg_org in args:
        if arg_org == "main.py":
            continue
        arg = str(arg_org)
        
        if target == "flag":
            
            if arg not in ACCEPTABLE_FLAGS:
                solutions(10)
                wait(EXIT_WAIT_TIME)
                exit(1)
            flag = arg
            target = "input"
            continue
        
        elif target == "input":
            if flag == "-w":
                sub_target = "flag"
                previous = ""
                central_word_satisfied = False
                info["word"].append("")
                for char in arg:
                    if char == "?" and sub_target == "flag":
                        sub_target = "input"
                        continue
                    elif char in ACCEPTABLE_MASKS and sub_target == "input":
                        sub_target = "flag"
                        info["word"][word_amount] += char
                        continue
                    elif char == "w" and sub_target == "flag" and previous == "":
                        previous = "w"
                        continue
                    elif char == "o" and sub_target == "flag" and previous == "w":
                        previous += "o"
                        continue
                    elif char == "r" and sub_target == "flag" and previous == "wo":
                        previous += "r"
                        continue
                    elif char == "d" and sub_target == "flag" and previous == "wor":
                        previous += "d"
                        central_word_satisfied = True
                        info["word"][word_amount] += "w"
                        continue
                    else:
                        solutions(6, os=os_name)
                        wait(EXIT_WAIT_TIME)
                        exit(1)
                if not central_word_satisfied:
                    solutions(6, os=os_name)
                    wait(EXIT_WAIT_TIME)
                    exit(1)
                word_amount += 1
                        
            elif flag == "-m":
                if arg not in ACCEPTABLE_HASH_MODES:
                    solutions(7, os=os_name)
                    wait(EXIT_WAIT_TIME)
                    exit(1)
                info["mode"] = arg
                    
            elif flag == "--files-hashes":
                info["file hashes"] = arg
            
            elif flag in ["--files-h-output", "-o"]:
                info["file hashes output"] = arg
                
            elif flag == "--files-input":
                info["file input"] = arg
                
            elif flag == "--hashcat-path":
                info["hashcat path"] = arg
                
            elif flag == "-c":
                if arg.isdigit():
                    if int(arg) <= MAX_THREADS and int(arg) > 0:
                        info["cores"] = arg
                    elif arg == "0":
                        info["cores"] = os.cpu_count()
                    else:
                        print("Error with given cores. It is likely that too many were given.")
                        wait(EXIT_WAIT_TIME)
                        exit(1)
                else:
                    print("Error with given cores.")
                    wait(EXIT_WAIT_TIME)
                    exit(1)
                    
            elif flag == "-p":
                if arg in ACCEPTABLE_PERMUTATIONS:
                    info["permutations"] = arg
                else:
                    solutions(8, os=os_name)
                    wait(EXIT_WAIT_TIME)
                    exit(1)
                    
            elif flag == "-v":
                if arg in ACCEPTABLE_VERSIONS:
                    info["version"] = arg
                else:
                    solutions(9, os=os_name)
                    wait(EXIT_WAIT_TIME)
                    exit(1)
            
            target = "flag"
    
    # check for required flags
    for flag in REQUIRED_FLAGS:
        if info[flag] == "" or info[flag] == []:
            solutions(11, os=os_name)
            wait(EXIT_WAIT_TIME)
            exit(1)
            
    # fill in for information that is not given. Defaulted hashcat path will be from within the config.py file. The rest from the constants file.
    for part in info:
        if info[part] == "" and part != "hashcat path" and part != "hashcat potfile path":
            info[part] = DEFAULT_FLAGS[part]
    if info["hashcat path"] == "":
        info["hashcat path"] = hashcat_path
    if info["hashcat potfile path"] == "":
        info["hashcat potfile path"] = hashcat_potfile_path
    
    print("Finished.")
    
    return info


##############################################################################################################################
#--------------------------------------------------- VALIDATE GIVEN FILES ---------------------------------------------------#
##############################################################################################################################

def validate_given_files(args, os_name):
    
    print("Validating given files... ", end="")
    
    if args["version"] in ["0", "2"] and (args["hashcat potfile path"] == "" or args["hashcat path"] == ""):
        solutions(1, os=os_name)
        wait(EXIT_WAIT_TIME)
        exit(1)
                
    for flag in args:
        if (("file" in flag and "hashcat potfile path" not in flag) or ("hashcat path" == flag and args["version"] in ["0", "2"]) or ("hashcat potfile path" == flag and args["version"] in ["0", "2"])) and flag != "file hashes output":
            try:
                with open(args[flag], "r", encoding="utf-8"):
                    pass
            except:
                if flag == "file hashes":
                    solutions(5, os=os_name)
                elif flag == "file input":
                    solutions(4, os=os_name)
                elif flag == "hashcat path":
                    solutions(3, os=os_name)
                elif flag == "hashcat potfile path":
                    solutions(2, os=os_name)
                else:
                    print("Error with unknown file.")
                wait(EXIT_WAIT_TIME)
                exit(1)
    
    print("Finished.")

##############################################################################################################################
#------------------------------------------------------ CRACK HASHES --------------------------------------------------------#
##############################################################################################################################    

# general functions
def get_word_combos(word_org):
    
    indexes = {} # keys are integers that stand for indexes of each hyphen and elements are integers that stand for how many spaces led up to each hyphen
    spaces = 0
    possible = False
    
    for char_index in range(len(word_org)):
        if word_org[char_index] == " ":
            spaces += 1
        if word_org[char_index] != "-":
            continue
        
        possible = True
        
        if char_index not in [0, len(word_org)-1]:
            if word_org[char_index-1].isalpha() and word_org[char_index+1].isalpha():
                indexes[char_index] = spaces
            else:
                possible = False
                break
        else:
            possible = False
            break
        
    if not possible:
        word_combos = ["".join(func(current_word) for func, current_word in zip(pattern, word_org.split())) for pattern in itertools.product([str.lower, str.capitalize], repeat=len(word_org.split()))]
        return word_combos
        
    word_combos = ["".join(func(current_word) for func, current_word in zip(pattern, word_org.replace("-", " ").split())) for pattern in itertools.product([str.lower, str.capitalize], repeat=len(word_org.replace("-", " ").split()))]
    
    for index in indexes:
        for temp_word_index in range(len(word_combos)):
            word_combos[temp_word_index] = word_combos[temp_word_index][:index-indexes[index]] + "-" + word_combos[temp_word_index][index-indexes[index]:]
            
    return word_combos

# PassCat functions
def hash_generator(pre_word_list, iterations, word_format, word_index, increase_points):
    
    for word in pre_word_list:
        for iteration in range(iterations):
                candidate = ""
                for index in range(len(word_format)):
                    if index != word_index:
                        candidate += f"""{MASK_DICTIONARY[word_format[index]][(iteration // increase_points[index]) % len(MASK_DICTIONARY[word_format[index]])]}"""
                    else:
                        candidate += f"{word}"
                
                md5_hash = hashlib.md5()
                md5_hash.update(candidate.encode())
                
                yield md5_hash.hexdigest(), candidate

def pc_chunk_processor(chunk, iterations, word_format, word_index, increase_points, hashes):
        
    solves = []
    for result, password in hash_generator(chunk, iterations, word_format, word_index, increase_points):
        if result in hashes:
            print(f"  PassCat discovered: {result} : {password}")
            solves.append([result, password])
            
    return solves



def crack_hashes(args, os_name):
    
    # grab all of the words from the file
    all_org_words = []
    try: # already validated. Here for just in case.
        with open(args["file input"], "r", encoding="utf-8", errors="ignore") as file:
            for word in file:
                all_org_words.append(word.rstrip())
    except:
        solutions(4, os=os_name)
        wait(EXIT_WAIT_TIME)
        exit(1)
    
    # get the hashes
    hashes = []
    with open(args["file hashes"], "r", encoding="utf-8") as file:
        for item in file:
            hashes.append(item.rstrip())
    
    # get the starting point in the cracked list. This is for Hashcat usage
    cracked_file_starting_point = 0
    with open(args["file hashes output"], "r", encoding="utf-8") as file:
        for line in file:
            cracked_file_starting_point += 1
    
    
    # grab already cracked hashes from the potfile and cracked file.
    if args["hashcat potfile path"] != "":
        print("\nAttempting to find hashes in Hashcat potfile and chosen hash output files now...\n---")
    else:
        print("\nAttempting to find hashes in chosen hash output file now...\n---")
     
    ignore_hashes_cracked = []
    ignore_hashes_potfile = []
    cracked_hashes = []
    with open(args["file hashes output"], "r", encoding="utf-8") as file:
        for line in file:
            if line[:line.index(":")] in hashes:
                ignore_hashes_cracked.append([line[:line.index(":")], line[line.index(":")+1:].rstrip()])
    for result in ignore_hashes_cracked:
        cracked_hashes.append(result)
        print(f"Disovered {result[0]}:{result[1]}")
    if args["hashcat potfile path"] != "":          
        with open(args["hashcat potfile path"], "r", encoding="utf-8") as file:
            for line in file:
                if line[:line.index(":")] in hashes:
                    ignore_hashes_potfile.append([line[:line.index(":")], line[line.index(":")+1:].rstrip()])
        for result in ignore_hashes_potfile:
            if result not in cracked_hashes:
                cracked_hashes.append(result)
                print(f"Disovered {result[0]}:{result[1]}")

    print(f"---\nAlready found {len(cracked_hashes)}/{len(hashes)} hashes from potfile and/or cracked file.")
    
    # ensure that the potfile and cracked files are in sync
    save(args, cracked_hashes, ignore_hashes_potfile, ignore_hashes_cracked)
    
    # end premature if all hashes are already cracked
    if len(cracked_hashes) >= len(hashes):
        if args["hashcat potfile path"] != "":
            print(f"""\nAll hashes already found. Check '{args["hashcat potfile path"]}' and/or '{args["file hashes output"]}' for hashes.""")
        else:
            print(f"""\nAll hashes already found. Check the Hashcat potfile if used and/or '{args["file hashes output"]}' for hashes.""")
        wait(EXIT_WAIT_TIME)
        exit(0)
    
    print("\nAttempting to crack remaining unsolved hashes now...\n")
    
    # loop for every word format
    for password_format_index in range(len(args["word"])):
        
        if password_format_index == 0:
            print("Starting cracking...")
        else:
            print("Starting next cracking...")

        # determine whether to integrate Hashcat or not
        if args["version"] == "1":
            tool = "PassCat"
        elif args["version"] == "2":
            tool = "Hashcat"
        elif args["version"] == "0":
            tool = "Hashcat"
            for char in args["word"][password_format_index]:
                if char in PASSCAT_UNIQUE_MASKS:
                    tool = "PassCat"
                    break
            if ((args["word"][password_format_index].index("w") == 0) == (args["word"][password_format_index].index("w") == len(args["word"][password_format_index])-1)) and len(args["word"][password_format_index]) != 1:
                tool = "PassCat"

        # calculate the amount of iterations per word when looping
        iterations = 1
        for char in args["word"][password_format_index]:
            if char != "w":
                iterations *= len(MASK_DICTIONARY[char])
        
        # calculate the points in the iterations in which an index per element of the product will increase
        increase_points = {} # keys will be integers that represen the indexes of the masks
        word_index = args["word"][password_format_index].index("w")
        for index in range(len(args["word"][password_format_index])):
            if index != word_index:
                current_increase_point = 1
                for sub_index in range(index+1, len(args["word"][password_format_index])):
                    if sub_index != word_index:
                        current_increase_point *= len(MASK_DICTIONARY[args["word"][password_format_index][sub_index]])
                increase_points[index] = current_increase_point # elements will be increase point. example math equation for adding to candidates: ((iterations // increase_point) % len(current_item))
      
        # loop through every word in the word list
        pre_word_set = set()
        for word_org in all_org_words:
            # get permutations of word based on given args
            word_combos = []
            if args["permutations"] == "0": # normal
                word_combos.append(word_org)
            elif args["permutations"] == "1": # lower
                word_combos.append(word_org.lower())
            elif args["permutations"] == "2": # upper
                word_combos.append(word_org.upper())
            elif args["permutations"] == "3": # capitalizations
                word_combos = get_word_combos(word_org)
            elif args["permutations"] == "4": # all
                word_combos = get_word_combos(word_org)
                word_combos.append(word_org.upper().replace(" ", ""))
                word_combos.append(word_org.replace(" ", ""))
                
                
            # remove spaces as needed
            if args["permutations"] != "4":
                for word in range(len(word_combos)):
                    if " " in word_combos[word]:
                        word_combos[word] = word_combos[word].replace(" ","")
            
            # create the pre word list that will be fed into multiprocessing
            for word in word_combos:
                    pre_word_set.add(word)
                    
        pre_word_list = list(pre_word_set)

        # based on how many total words there are after everything, determine the final choice of tool
        if len(pre_word_list) <= MINIMUM_HASHCAT_WORDLIST_SIZE and tool == "Hashcat":
            print("* Wordlist too small - changing tool to PassCat")
            tool = "PassCat"
            
        # if the tool is Hashcat, then determine the attack mode
        attack_mode = "N/A"
        if tool == "Hashcat":
            attack_mode = "0"
            if len(args["word"][password_format_index]) > 1:
                if args["word"][password_format_index].index("w") == 0:
                    attack_mode = "6"
                elif args["word"][password_format_index].index("w") == len(args["word"][password_format_index])-1:
                    attack_mode = "7"
                else:
                    print("Error with determining Hashcat's attack mode. Hashcat does not support: Mask + Wordlist + Mask.")
                    wait(EXIT_WAIT_TIME)
                    exit(1)

        # create chunks based on the amount of cores being used
        current_cores = args["cores"]
        if len(pre_word_list) <= int(args["cores"]):
            print("""* changing cores to "1" due to a tiny word list.""")
            current_cores = "1"
        chunks = []
        total_words = len(pre_word_list)
        base_chunk_size = total_words // int(current_cores) # base size of chunks
        larger_chunks = total_words % int(current_cores) # chunks with +1 size for
        start_index = 0
        for index in range(int(current_cores)):
            if index < larger_chunks:
                current_chunk_size = base_chunk_size + 1
            else:
                current_chunk_size = base_chunk_size
            chunks.append(pre_word_list[start_index:start_index + current_chunk_size])
            start_index += current_chunk_size

        # get the start time for every word format
        start_time = time()
        
        # give info per iteration
        print(f"""  Current password format: {args["word"][password_format_index]}\n  Cores: {current_cores}\n  Tool: {tool}\n  Attack mode: {attack_mode}""")
        
        
        # using either tool
        if tool == "PassCat":
            
            print("Using PassCat to crack hashes now... ")
            
            # use multiprocessing to get the word list
            with ProcessPoolExecutor(max_workers=int(args["cores"])) as executor:
                processes = []
                for chunk in chunks:
                    processes.append(executor.submit(pc_chunk_processor, chunk, iterations, args["word"][password_format_index], word_index, increase_points, hashes))
                    
            for sub_result in processes:
                if len(sub_result.result()) > 0:
                    for result in sub_result.result():
                        if result not in cracked_hashes:
                            cracked_hashes.append(result)
        
        elif tool == "Hashcat":
            
            print("Using Hashcat to crack hashes now... ")
            
            # write the sub_results to their respective passwordlist.txt files
            current_core = 0
            for chunk in chunks:
                with open(f"{PASSWORDS_DEFAULT_FILE_PATH}{current_core}.txt", "w", encoding="utf-8") as file:
                    for password in chunk:
                        file.write(password + "\n")
                current_core += 1
            
            # crack with Hashcat
            hashcat(args, args["word"][password_format_index], attack_mode, current_cores, len(cracked_hashes))
            
            # update the cracked list
            current_line = -1
            with open(args["file hashes output"], "r", encoding="utf-8") as file:
                for line in file:
                    current_line += 1
                    if current_line >= cracked_file_starting_point:
                        part_0 = line[:line.index(":")]
                        part_1 = line[line.index(":")+1:].rstrip() # change this later to work with SHA1 and SHA256
                        if "HEX" in part_1:
                            part_1 = bytes.fromhex(part_1[5:-1]).decode("utf-8")
                        if [part_0, part_1] not in cracked_hashes:
                            print(f"  Hashcat discovered: {part_0} : {part_1}")
                            cracked_hashes.append([part_0, part_1])


        # give a status update
        print(f"""Tool finished.\n  Tool's elapsed time: {int((time() - start_time)//60//60)} hours {int((time() - start_time)//60%60)} mins {(time() - start_time)%60:.2f} secs""")
        print(f"Current results: {len(cracked_hashes)}/{len(hashes)}\n")
        
        # pause to ensure cap speed
        wait(EXIT_WAIT_TIME)
        
        # check for premature finishes
        if len(cracked_hashes) >= len(hashes) and password_format_index != len(args["word"])-1:
            print("\nAll passwords found. Ending prematurely.")
            return cracked_hashes, hashes, ignore_hashes_potfile, ignore_hashes_cracked
        
    print("\nFinished cracking.")
    return cracked_hashes, hashes, ignore_hashes_potfile, ignore_hashes_cracked
        

##############################################################################################################################
#--------------------------------------------------------- HASHCAT ----------------------------------------------------------#
##############################################################################################################################

def hashcat(args, current_password_format, attack_mode, current_cores, cracked_hashes):
    
    # generate the arguments that will be given to hashcat
    hashcat_arguments = [args["hashcat path"], "-m", args["mode"], "-a", attack_mode, args["file hashes"], "PASSWORD FILE HERE", "-o", args["file hashes output"]]
    
    # insert the attack mode into the arguments list as needed
    mask_insertion_index = -1
    if attack_mode != "0":
        mask = ""
        if attack_mode == "6":
            for char in current_password_format[1:]:
                mask += f"?{char}"
            mask_insertion_index = 7
        elif attack_mode == "7":
            for char in current_password_format[:-1]:
                mask += f"?{char}"
            mask_insertion_index = 6
        hashcat_arguments.insert(mask_insertion_index, mask)
    
    # get the total amount of hashes in the hash file
    total_hashes = 0
    with open(args["file hashes"], "r", encoding="utf-8") as file:
        for line in file:
            total_hashes += 1
    
    # newly ingested hashes for output information
    total_ingested_hashes = 0
    
    # loop through the lists and run hashcat
    for core in range(int(current_cores)):
        if mask_insertion_index in [-1, 7]:
            hashcat_arguments[6] = f"{PASSWORDS_DEFAULT_FILE_PATH}{core}.txt"
        elif mask_insertion_index == 6:
            hashcat_arguments[7] = f"{PASSWORDS_DEFAULT_FILE_PATH}{core}.txt"
            
        results = subprocess.Popen(hashcat_arguments, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        for line in results.stdout:

            if "Token length exception" in line:
                print("Error with specified hash type.")
                wait(EXIT_WAIT_TIME)
                exit(1)

            if "All hashes found as potfile" in line:
                print("All hashes already cracked. Please check Hashcat's potfile to see found passwords.")
                wait(EXIT_WAIT_TIME)
                exit(1)

            if "Recovered......" in line:
                start_index = line.index(",")+2
                offset = 0
                for char in line[start_index:]:
                    if char == "/":
                        break
                    offset += 1
                end_index = start_index+offset
                total_ingested_hashes += int(line[start_index:end_index])
                print(f"""Password File {core} | Cracked {cracked_hashes+total_ingested_hashes}/{total_hashes}""")
        
        for line in results.stderr:
            if "No such file or directory" in line:
                print(f"""Error occurred with finding file/directory: {line[2:line.index(":")]}""")
                wait(EXIT_WAIT_TIME)
                exit(1)
        
        if cracked_hashes+total_ingested_hashes == total_hashes and core != int(args["cores"])-1:
            print("All hashes found. Ending prematurely.")
            break
  
  
##############################################################################################################################
#--------------------------------------------------- SAVE AND SYNC FILES ----------------------------------------------------#
##############################################################################################################################

def save(args, cracked_hashes, ignore_hashes_potfile, ignore_hashes_cracked):
    
    print("\nEnsuring results are saved and readable... ", end="")
    
    # save results
    for result in cracked_hashes:
        # ensure end up in files hashes output file
        if result not in ignore_hashes_cracked:
            found = False
            with open(args["file hashes output"], "r", encoding="utf-8") as file:
                for line in file:
                    if [line[:len(result[0])],line[len(result[0])+1:].rstrip()] == result:
                        found = True
                        break
            if not found:
                with open(args["file hashes output"], "a") as file:
                    file.write(f"{result[0]}:{result[1]}\n")

    
    # ensure results are readable
    cracked_txt_hex_results = []
    
    with open(args["file hashes output"], "r", encoding="utf-8") as file:
        for line in file:
            if line.rstrip() not in cracked_txt_hex_results:
                cracked_txt_hex_results.append(line.rstrip())
    
    for result_index in range(len(cracked_txt_hex_results)):
        if cracked_txt_hex_results[result_index][cracked_txt_hex_results[result_index].index(":")+2:cracked_txt_hex_results[result_index].index(":")+5] == "HEX":
            cracked_txt_hex_results[result_index] = f"""{cracked_txt_hex_results[result_index][:cracked_txt_hex_results[result_index].index(":")]}:{bytes.fromhex(cracked_txt_hex_results[result_index][cracked_txt_hex_results[result_index].index("[")+1:-1]).decode("utf-8")}"""
            
    
    with open(args["file hashes output"], "w", encoding="utf-8") as file:
        for result in cracked_txt_hex_results:
            file.write(f"{result}\n")
    
    # work with hashcat's potfile if needed
    if args["hashcat potfile path"] != "":
            
        # ensure end up in hashcat potfile file
        for result in cracked_hashes:
            if args["hashcat potfile path"] != "":
                if result not in ignore_hashes_potfile:
                    found = False
                    with open(args["hashcat potfile path"], "r", encoding="utf-8") as file:
                        for line in file:
                            if [line[:len(result[0])],line[len(result[0])+1:].rstrip()] == result:
                                found = True
                                break
                    if not found:
                        with open(args["hashcat potfile path"], "a") as file:
                            file.write(f"{result[0]}:{result[1]}\n")
        
        # ensure results are readable
        hashcat_potfile_hex_results = []
            
        with open(args["hashcat potfile path"], "r", encoding="utf-8") as file:
            for line in file:
                if line.rstrip() not in hashcat_potfile_hex_results:
                    hashcat_potfile_hex_results.append(line.rstrip())
                    
        for result_index in range(len(hashcat_potfile_hex_results)):
            if hashcat_potfile_hex_results[result_index][hashcat_potfile_hex_results[result_index].index(":")+2:hashcat_potfile_hex_results[result_index].index(":")+5] == "HEX":
                hashcat_potfile_hex_results[result_index] = f"""{hashcat_potfile_hex_results[result_index][:hashcat_potfile_hex_results[result_index].index(":")]}:{bytes.fromhex(hashcat_potfile_hex_results[result_index][hashcat_potfile_hex_results[result_index].index("[")+1:-1]).decode("utf-8")}"""
        
        with open(args["hashcat potfile path"], "w", encoding="utf-8") as file:
            for result in hashcat_potfile_hex_results:
                file.write(f"{result}\n")
        
    
    print("Finished.")

##############################################################################################################################
#--------------------------------------------------------- RESULTS ----------------------------------------------------------#
##############################################################################################################################

def results(args, cracked_hashes, hashes, start_time, current_time):
    
    print("\n"*3 + "-"*70, "\nResults of cracking found below.\n")
    print(f"""Hashing mode: {args["mode"]}\nPermutations: {args["permutations"]}\nCores: {args["cores"]}\nWordlist: {args["file input"]}""")
    print(f"""Hash file: {args["file hashes"]}\nOutput file: {args["file hashes output"]}""")
    if args["hashcat potfile path"] != "":
        print(f"""Hashcat file path: {args["hashcat path"]}\nHashcat potfile file path: {args["hashcat potfile path"]}\n""")
    else:
        print("Hashcat file path: N/A\nHashcat potfile file path: N/A\n")
    print(f"""Cracked hashes: {len(cracked_hashes)}/{len(hashes)}""")
    print(f"""Total elapsed time: {int((current_time - start_time)//60//60)} hours {int((current_time - start_time)//60%60)} mins {(current_time - start_time)%60:.2f} secs""")
    
    if len(cracked_hashes) > 0:
        print("\nCracked hashes\n" + "-"*15)
        for cracked_hash in cracked_hashes:
            print(f"{cracked_hash[0]} : {cracked_hash[1]}")
        
        if len(cracked_hashes) != len(hashes):
            print("\nUnsolved hashes\n" + "-"*15)
            for potential_hash in hashes:
                found = False
                for cracked_hash in cracked_hashes:
                    if potential_hash == cracked_hash[0]:
                        found = True
                        break
                if not found:
                    print(f"{potential_hash}")
    print("-"*70)
        
    
        
        
        
        
            
        
        

