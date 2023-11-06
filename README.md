# nmap-extract

A python3 script to parse NMAP output files (*.nmap) and quickly extract the unique IPv4 address.

Allows for output of results to a file, copying results to clipboard, and performing DNS lookup on extracted IP addresses.

## Usage
`python3 nmap-extract.py example.nmap`

## Options
**-h** or **--help**: Show help menu

**-o** or **--output**: Output results to file

**-c** or **--clipboard**: Copy results to clipboard

**-d** or **--dns**: Perform DNS lookup on extracted IPv4 addresses

## Requirements
`pyperclip==1.8.2`

## To-do
- [ ] Add the ability to extract hostnames from output as well
