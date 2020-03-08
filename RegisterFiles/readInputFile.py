import re

# fileActions = {
#     1: {
#         'command': '',
#         'action': ''
#     },
# }

# fileActions = {}

# for action in fileActions:
#     if (action['command'] == 'click'):
#         splitAction = action['action'].split(",")
#         pytautogui.click(splitAction[0], splitAction[1]) # need to validate this is accurate
        

def scanLine(line):
    result = re.search("^#", line)
    if result:
        return False
    else:
        return line

def parseLine(line):
    # Click parse
    # returns two captures - Click literally and any number, any number
    clicking = re.search(r"^(click) \((\d+,\d+)\)$", line)    
    # type parse
    typing = re.search(r"^(type) \((.*)\)$", line)

    if (line == False):
        return
    elif (clicking != None):
        # Add click to queue
        return clicking
    elif (typing != None):
        return typing





with open('./input.txt') as file:
    print(file)

