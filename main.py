# modules
import getpass

# imports
from shapes import *
from interactive import interactive

# global variables
bg_color = ''
world = []

def satisfies_condition(shape, x, y):
    '''
    Returns whether a given point is within the bounds of the given shape

    shape: shape to check
    x,y: coords of point
    '''
    data = shape['data']
    if shape['name'] == 'rect_filled':
        return rect_filled(x, y, data['h'], data['k'], data['l'], data['b'])
    elif shape['name'] == 'circle_filled':
        return circle_filled(x, y, data['h'], data['k'], data['r'])
    elif shape['name'] == 'rect':
        return rect(x, y, data['h'], data['k'], data['l'],data['b'],data['t'])
    elif shape['name'] == 'circle':
        return circle(x, y, data['h'], data['k'], data['r'], data['t'])
    elif shape['name'] == 'ellipse_filled':
        return ellipse_filled(x, y, data['h'], data['k'], data['width'], data['height'])

def pixel(x, y):
    '''
    Returns the character to be displayed a particular coordinate

    x,y: cartesian coordinate to check
    '''
    global world
    global bg_color
    for shape in world[::-1]:
        if satisfies_condition(shape, x, y):
            return shape['color']
    else:
        return bg_color

def render_frame(x1, y1, w, h, zoom):
    '''
    Returns a string containing the rendered ASCII art of the scene.

    x1,y1: coords of bottom left of frame
    w,h: length and breadth of frame in characters
    zoom: distance in space covered by one character
    '''
    result = ""
    # iterate over each pixel
    for j in range(h):
        for i in range(w):
            # apply zoom
            x = x1 + i / zoom
            y = (h-j + y1) / zoom
            # double the pixel since each character is a rectangle,
            # but a pixel needs to roughly be a square
            result += pixel(x, y)*2
        result += '\n'
    return result
    
def render(scene):
    global world
    global bg_color

    world = scene['world']
    bg_color = scene['bg_color']
    frame = scene['renderframe']
    x, y = frame['corner']
    w, h = frame['size']
    zoom = frame['zoom']
    return render_frame(x, y, w, h, zoom)

def importScene(path):
    '''
    Read a file and return the scene stored in it
    '''
    with open(path, 'r') as file:
        content = file.read()
        dictionary = eval(content)
    return dictionary

def writeToFile(img):
    path = input("Enter path to write to: ")
    with open(path, 'w') as f:
        f.write(img)

def load_from_file(path):
    try:
        scene = importScene(path)
    except:
        print("Error reading file.")
        main()
        return
    try:
        image = render(scene)
    except:
        print("Error while rendering. Ensure the file is in proper format.")
        main()
        return
    print("Image rendered successfully.")
    print("Menu:")
    print("1. Display image")
    print("2. Write image to file")
    print("3. Edit image")
    print("Leave blank to return to main menu")
    option = input(">> ")
    if not option:
        main()
        return
    if option == '1':
        print(image)
    elif option == '2':
        writeToFile(image)
    elif option == '3':
        interactive(render, scenedata = scene)
    load_from_file(path)

MENU = '''
Main menu:
1. Load scene from file
2. Interactively create scene
Leave blank to exit
'''

def main():
    '''
    Command line front-end
    '''
    print(MENU)
    op = input("> ")
    if not op:
        return
    if op == '1':
        path = input("Enter file path to read from: ")
        load_from_file(path)
    elif op == '2':
        interactive(render)
    else:
        print("Invalid option.")
        main()

def login():
    with open("pass.txt") as f: PASSWD = f.read()
    while True:
        p=getpass.getpass(prompt='Enter password: ')
        if p==PASSWD:
            main()
            break
        else:
            print('Password is incorrect, please try again!')

if __name__ == '__main__':
    login()
