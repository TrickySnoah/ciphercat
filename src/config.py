
""" Current version: v1.0.0 """



""" The 'Instructions and Help' section can be found further below """



# PASSWORD FORMAT (separate password formats by commas)
password_format = ""

# HASH MODE
hash_mode = 0

# CORE AMOUNT HERE
cores = 1

# PERMUATIONS TYPE
permutations = 0

# VERSION (tool)
version = 1

# HASHES FILE FILENAME
hashes_file = "files/hashes.txt"

# OUTPUT FILENAME
h_output_file = "files/cracked.txt"

# RAW INPUT PASSWORDS FILE FILENAME
input_file = "files/wordlist.txt"

# HASHCAT FILE PATH HERE (default for CLI version)
hashcat_path = ""

# HASHCAT POTFILE FILE PATH HERE (default for CLI version)
hashcat_potfile_path = ""


""" Instructions and Help """

"""

The 'config.py' file will be used to set up cracking settings for Windows usage and sometimes Linux usage. Windows will rely completely on
this file whilst Linux will have the option of relying on this file for ease of use.


- [ Purposes of Variables ] -

  Variable             | Purpose                                                  | Example
 ======================+==========================================================+=================
  password_format      | Used to define the intended password format(s). This can | password_format = "word?a?a,word?d"
                       | be formatted for one single password format or multiple  |
                       | password formats, each separated with a comma. Password  |
                       | formats will also include masking as desired.            |
                       |                                                          |
  hash_mode            | Determines the hashing mode.                             | hash_mode = 0
                       |                                                          |
  cores                | Determines the amount of cores on the CPU to use. Cores  | cores = 6
                       | are used to divide the work in the tool to optimize      |
                       | cracking time.                                           |
                       |                                                          |
  permutations         | Determines the capitalization permutations used in the   | permutations = 4
                       | cracking. For example, all of the permutations for the   |
                       | following "Hello world" would be: "hello world", "Hello  |
                       | world", "hello World", "Hello World".                    |
                       |                                                          |
  hashes_file          | Defines the file that contains the hashes to be cracked. | hashes_file = r"examples/example-03_hashes.txt"
                       |                                                          |
  h_output_file        | Defines the file that will contain the results of the    | h_output_file = r"examples/example-03_cracked.txt"
                       | cracking session.                                        |
                       |                                                          |
  input_file           | Defines the wordlist                                     | _file = r"examples/example-03_wordlist.txt"
                       |                                                          |
  hashcat_path         | Defines the path of the hashcat .exe or elf file         | hashcat_path = r"../../../../../hashcat-6.2.6/hashcat-6.2.6/hashcat.exe"
                       |                                                          |
  hashcat_potfile_path | Defines the potfile file path used by hashcat. For       | (Windows) hashcat_potfile_path = r"hashcat.potfile"
                       | Windows users, the potfile path will have to remain      | (Linux) hashcat_potfile_path = r"../../.local/share/hashcat/hashcat.potfile"
                       | within the same folder as this file, config.py. For      |
                       | Linux users, the potfile path will be wherever it is     |
                       | initially placed by Hashcat upon installation            |
 ===================================================================================================
 
 - [ Cores (-c) ] -

                  # | Description
 ===================+=============
                  0 | Total amount of cores on current CPU
  0 < # < MAX CORES | Number of cores below the max

- [ Built-in Charsets (-w) ] -

  ? | Charset
 ===+=========
  l | abcdefghijklmnopqrstuvwxyz [a-z]
  u | ABCDEFGHIJKLMNOPQRSTUVWXYZ [A-Z]
  d | 0123456789                 [0-9]
  s | !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
  t | ?s?d
  a | ?l?u?d?s

- [ Hash Modes (-m) ] -

  # | Name
 ===+======
  0 | MD5

- [ Permutations (-p) ] -

  # | Letter Casing
 ===+===============
  0 | Uses words directly as they are typed in the provided word list
  1 | Uses lowercase versions only of words in the provided word list
  2 | Uses uppercase versions only of words in the provided word list
  3 | Uses all capitalization possibilities of words / phrases in provided word list
  4 | Uses all capitalizations, lowercase, and uppercase versions of words in the provided word list

- [ Versions / Tools (-v) ] -

  # | Tool
 ===+==============
  0 | Both - defaults to Hashcat but opts to use HashFox when needed
  1 | HashFox
  2 | HashCat

- [ Working Example ] -

# PASSWORD FORMAT (separate password formats by commas)
password_format = "?a?a?aword,word?a?a?a,?a?aword?a,?aword?a?a"

# HASH MODE
hash_mode = 0

# CORE AMOUNT HERE
cores = 0

# PERMUATIONS TYPE
permutations = 4

# VERSION
version = 1

# HASHES FILE FILENAME
hashes_file = "examples/example-02_hashes.txt"

# OUTPUT FILENAME
h_output_file = "examples/example-02_cracked.txt"

# RAW INPUT PASSWORDS FILE FILENAME
input_file = "examples/example-02_wordlist.txt"

# HASHCAT FILE PATH HERE (default for CLI version)
hashcat_path = ""

# HASHCAT POTFILE FILE PATH HERE (default for CLI version)
hashcat_potfile_path = ""

"""

