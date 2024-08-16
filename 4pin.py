# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 15:58:09 2024

@author: IAN CARTER KULANI
"""

# Generate all 4-digit PINs and save them to pin.txt
with open('4pin.txt', 'w') as file:
    for pin in range(1000000):
        file.write(f"{pin:04}\n")  # Format PIN with leading zeros
