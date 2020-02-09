import pyautogui

# file 1
def calculateCoords(regNum):
    _reg = regNum

    _y = 1
    _x = 1

    _cdX = 235
    _cdY = 75
    _cdOffsetX = 150
    _cdOffsetY = 80

    if(_reg == 1):
        _x = _cdOffsetX
        _y = _cdOffsetY
        return (_x, _y)
    else:
        for i in range(1, _reg):
            if(_x % 4 == 0 and _x != 0):
                _y += 1
                _x = 0
            if(i % 4 == 0):
                _x += 1
            else:
                if(_reg != 1):
                    _x += 1

    # multiply X and Y by button width and height to get screen coords
    # _x *= 233 
    # _y *= 68
    if(_x == 2):
        print((_x * _cdX) + _cdOffsetX)

    _x = ((_x-1) * _cdX) + _cdOffsetX
    _y = ((_y-1) * _cdY) + _cdOffsetY
    
    return (_x, _y)


for f in range(1, 30):
    print(f"COORDS: {calculateCoords(f)}\nF: {f}\n------------")

# Button Dimensions
# Width: 233
# Height: 68

# 10 Columns
# 4 rows

# When X > 10, add 1 to Y
# When Y = 4 and X = 10 you hit the max.

# So Register 13 would be 



