import time

zig = True
increment = 1
while True:
    try:
        if increment >= 20:
            zig = False
        elif increment <= 1:
            zig = True
        print(f"{" " * increment}*******")
        if zig == True:
            increment += 1
        elif zig == False:
            increment -= 1
        time.sleep(0.1)
    except:
        exit()
