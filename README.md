# Overview

My take on a technical assessment from a popular company.

# Instructions

Debian uses *deb packages to deploy and upgrade software. The packages are stored in repositories and each repository contains the so-called "Contents index". The format of that file is well described here:

https://wiki.debian.org/RepositoryFormat#A.22Contents.22_indices.

Your task is to develop a python command line tool that takes the architecture (amd64, arm64, mips etc.) as an argument and downloads the compressed Contents file associated with it from a Debian mirror. The program should parse the file and output the statistics of the top 10 packages that have the most files associated with them.

Example output:
```
$ ./package_statistics.py amd64
1. <package name 1> <number of files>
2. <package name 2> <number of files>
......
10. <package name 10> <number of files>
```

You can use the following Debian mirror http://ftp.uk.debian.org/debian/dists/stable/main/.


# Directions

### Create virtual environment and install dependencies
```
python3 -m venv venv
source venv/bin/activate
pip3 install -r requirements.txt
```

### Run script
```
python3 package_stats.py <arch>
```
