# imports
import base64
import sys

# function to read a file
def readFile(file):
   with open(file, 'r+') as f:
      fileContents = f.read()
   return fileContents

# function to write to a file
def writeFile(file,data):
   with open(file, "wb") as f:
      f.write(data)

# function to encode file contents
def encodeFile(file):
   contents = readFile(file).encode("UTF-8")
   encodedContents = base64.b64encode(contents)
   writeFile(file,encodedContents)
   return encodedContents

# function to decode file contents
def decodeFile(file):
   contents = readFile(file)
   decodedContents = base64.b64decode(contents)
   writeFile(file, decodedContents)
   return(decodedContents)

# prompt for tool
prompt = input("What would you like to do?\n1. Encode file\n2. Decode file\n3. Exit")

if prompt == "1":
   file = input("Please type the path of the file you would like to encode:\n ")
   encodeFile(file)
if prompt == "2":
   file = input("Please type the path of the file you would like to decode:\n ")
   decodeFile(file)
if prompt <= 3:
   sys.exit("Exiting")