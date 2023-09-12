# Hasher

## Overview

The Hasher is a powerful cybersecurity tool, created for educational purposes, aiming to illustrate the ease with which weak passwords can be cracked when stored as unsalted cryptographic hashes. It serves as a tool to educate users about password security practices and should not be employed for any unauthorized, unethical, or malicious purposes.

## Features

- Hasher can crack the following cryptographic hash algorithms:
  - MD5
  - SHA-1
  - SHA-256

## Installation

1. Clone the repository to your local machine:

   ```shell
   git clone https://github.com/Facelift2376/hasher.git
   ```

2. Change to the project directory:

   ```shell
   cd hasher
   ```

## Usage

### Basic Usage

To start a basic web crawl, use the following command:

```shell
python3 hasher.py  -c <HASH> -tp <Hash_Type> -t <THREAD> -f <wordlists>
```

Replace the following:
 -     <Hash> -   hash_to_crack
 -     <Hash_Type> - {md5,sha1,sha256}
 -     <THREAD> - thread Count 
 -     <wordlists> - path to wordlists



## Credit

This project is made by Shaikh Abdullah.

## Contributions

Contributions to this project are welcome. Feel free to open issues or submit pull requests to help improve this tool.

## Disclaimer

This tool is intended for educational and cybersecurity research purposes only. Ensure you have proper authorization before using it .

## Contact

For questions or inquiries, you can contact the project maintainer at abdullah13112004@gmail.com.

Happy cracking! 
