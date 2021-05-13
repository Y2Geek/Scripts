"""Lists file in given location with given extension"""
import os

# Get location to look
location = input("Where would you like to look?\nPlease enter full path: ")

try:
    # Try get list of files
    files = os.listdir(location)
except FileNotFoundError:
    print(f"\nSorry that {location} was not found\n")
else:
    # Get file extension to look for
    extension = input("What file extensions would you like to look for? ").lower()
    
    # Check if there are any files
    if files:
        files_found = []
        
        for entry in files:
            if entry.lower().endswith(extension):
                files_found.append(entry)
                
        if files_found:
            # List  the files ending in given extension
            for entry in sorted(files_found):
                print(entry)
