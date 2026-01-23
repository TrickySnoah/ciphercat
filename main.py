
# CipherCat tool created by Noah Jackson

import sys, utils
from time import time as start, sleep as wait
from constants import *


def main():
    # proud mark
    print("\nCipherCat tool created by: Noah Jackson")
    
    # start time for statistics
    start_time = start()
    
    # discover the os
    os = utils.discover_os()
    
    
    # Manual / IDE version
    if os == "Win":
        print("\nManual Version Detected. Working with Manual version now.\n")
        args = utils.manual_validate_and_parse(sys.argv, os)
    
    # CLI / Linux version
    elif os == "Linux":
        print("\nCLI Version Detected. Working with CLI version now.\n")
        
        if len(sys.argv) % 2 != 1 or len(sys.argv) == 1:
            if len(sys.argv) != 1:
                if sys.argv[1] in HELP_FLAGS:
                    utils.display_manual()
                    wait(EXIT_WAIT_TIME)
                    exit(0)
                elif sys.argv[1] in VERSION_FLAGS:
                    utils.display_version()
                    wait(EXIT_WAIT_TIME)
                    exit(0)
            utils.solutions(10)
            wait(EXIT_WAIT_TIME)
            exit(1)
        
        args = utils.cli_validate_and_parse(sys.argv, os)
        
        
        
    # universal functions
    utils.ensure_files() # ensures that default files are present    
    utils.validate_given_files(args, os)
    cracked_hashes, hashes, ignore_hashes_potfile, ignore_hashes_cracked = utils.crack_hashes(args, os)
    utils.save(args, cracked_hashes, ignore_hashes_potfile, ignore_hashes_cracked)
    utils.results(args, cracked_hashes, hashes, start_time, start())
    
    
    wait(EXIT_WAIT_TIME)
    return


if __name__ == "__main__":
  main()
  