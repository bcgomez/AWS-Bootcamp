# AWS EC2 Python Automation – Prime Number Generator

## Overview
This project demonstrates how to connect to an AWS EC2 Linux instance through SSH and run a Python automation script.

The script generates prime numbers from 1 to 250 and saves them into a text file.

## Objectives
- Practice remote access to a Linux server using PuTTY
- Use AWS EC2 as a cloud environment
- Run Python scripts on a Linux instance
- Store results in an output file

## Technologies Used
- AWS EC2
- Amazon Linux
- PuTTY
- SSH
- Python 3
- Linux CLI

## Project Structure
```bash
aws-ec2-python-primes/
├── README.md
├── prime_generator.py
├── output/
│   └── results.txt
└── docs/
    └── screenshots/

## How to Run

1. Connect to the EC2 instance using SSH or PuTTY.

2. Navigate to the project directory.

3. Run the script:
python3 prime_generator.py

## Output Example

The script generates a file called `results.txt` that contains all prime numbers between 1 and 250.

## Lessons Learned

This project helped me practice:

- Working with AWS EC2 instances
- Connecting to a Linux server using SSH
- Running Python automation scripts
- Managing files in a Linux environment