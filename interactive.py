# Interactive interface for creating and modifying scenes

MENU = """
Menu:
1. Add shape
2. Remove last shape
3. Modify frame data (image size, zoom, etc)
4. Display rendered image
5. Write rendered image (ASCII art) to file
6. Write scene data (information about the scene) to file
Leave blank to exit
"""

data = {
    'renderframe': {},
    'world': []
}

def add_shape():
    global data
    parameterdata = {
        'circle_filled': ['h','k','r'],
        'rect_filled': ['h','k','l','b'],
        'rect': ['h','k','l','b','t'],
        'circle': ['h','k','r','t']
    }
    parameternames = {
        'circle_filled':
            ['X coordinate of center of circle', 'Y coordinate of center of circle', 'radius'],
        'rect_filled':
            ['X coordinate of top-left corner', 'Y coordinate of top-left corner', 'width', 'height'],
        'rect':
            ['X coordinate of top-left corner', 'Y coordinate of top-left corner', 'width', 'height', 'thickness'],
        'circle':
            ['X coordinate of center of circle', 'Y coordinate of center of circle', 'radius', 'thickness']
    }
    shapes = list(parameterdata.keys())
    print("Enter shape type:")
    for i in range(len(shapes)):
        print("{}. {}".format(i+1, shapes[i]))
    op = int(input(">>> ")) - 1
    chosen = shapes[op]
    shape = {
        "name": chosen,
        "data": {},
    }
    shape['color'] = input("Enter color of shape: ")
    for i in range(len(parameterdata[chosen])):
        parameter = parameterdata[chosen][i]
        displayname = parameternames[chosen][i]
        prompt = 'Enter {}: '.format(displayname)
        shape['data'][parameter] = float(input(prompt))
    data['world'].append(shape)

def ask_scenedata():
    global data
    try:
        buffer = dict(data) # copy
        buffer['renderframe']['corner'] = eval(input("Enter coordinate of image corner (x,y): "))
        buffer['renderframe']['zoom'] = float(input("Enter zoom level: "))
        buffer['renderframe']['size'] = eval(input("Enter image size in characters (width, height): "))
        buffer['bg_color'] = input("Enter background character: ")
        buffer
        data = buffer
    except:
        print("Invalid input, try again.")
        ask_scenedata() # again

def interactive(render, scenedata = None):
    global data
    # load in case scene data is already given, else initialize
    if scenedata != None:
        data = scenedata
    else:
        ask_scenedata()
    
    while True:
        print(MENU)
        op = input(">> ")
        if not op:
            break
        if op == '1':
            add_shape()
        elif op == '2':
            if len(data['world']) > 0:
                data['world'].pop()
        elif op == '3':
            ask_scenedata()
        elif op == '4':
            print(render(data))
        elif op == '5':
            path = input("Enter path to write to: ")
            with open(path, 'w') as f:
                f.write(render(data))
        elif op == '6':
            path = input("Enter path to write to: ")
            with open(path, 'w') as f:
                f.write(str(data))

        