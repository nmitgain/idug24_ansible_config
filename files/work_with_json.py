#!/usr/bin/python3

import sys
import json
import socket

hostname = socket.gethostname()

input = sys.stdin.read()
parsed_data = json.loads(input)
tgt_db = parsed_data['TGT_DB']
src_db = parsed_data['SRC_DB'] 
version = parsed_data['VERSION']

print(f"This is { hostname }")
print(f"My configuration Data")
print(f"=====================")
print(f"Target-Database: { tgt_db }")
print(f"Source-Database: {src_db }")
print(f"Version to be used { version }")