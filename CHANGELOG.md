
# [v1.0.0]

## Description

This is the initial release for HashFox! HashFox, as of now, is a Python-based hash-cracking
tool that optionally integrates with Hashcat.

## IMPORTANT DISCLOSURE

HashFox is a tool on its own that optionally integrates with Hashcat but is not affiliated with or
endorsed by the Hashcat project.

## Added

- core hash-cracking functionality
- multi-core CPU processing
- dictionary attack
- hybrid wordlist + mask attack
- case permutations
- cross-platform support for Windows and Linux
- Windows manual page under resources folder
- Linux manual page
- causes and Solutions messages
- example files
- optional Hashcat integration

## Supported Algorithms

- Added MD5 with hash-mode 0

## Permutation Types

- Original case (no modification)
- Lowercase only
- Uppercase only
- Full case permutations
- Common + full case variants

## Charsets

- Lowercase letters
- Uppercase letters
- Digits
- Symbols and punctuation
- Digits + symbols
- All character types

## Future Plans

- MD4 algorithm
- SHA1 algorithm
- SHA256 algorithm
- NTLM algorithm
- C-based / Ruby-based hash-cracking functions
- GUI option for Windows users
