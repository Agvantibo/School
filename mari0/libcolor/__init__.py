class color:
    """"Contains 3 rgb integers"""
    r = 0
    g = 0
    b = 0

    def __init__(self, r, g, b):
        self.r = r
        self.g = g
        self.b = b

    def to_hex(self):
        """"returns a hex color string"""
        return '#'+code(abs(int(self.r)))+code(abs(int(self.g)))+code(abs(int(self.b)))

    def to_tuple(self):
        """returns a tuple with 3 rgb channels"""
        return (int(self.r), int(self.g), int(self.b))

def rect_mid(x, y, h, w):
    return (x - w // 2, y - h // 2, x + w // 2, y + h // 2)


def digit(x):
    if x <= 9:
        return str(x)
    elif x == 10:
        return 'a'
    elif x == 11:
        return 'b'
    elif x == 12:
        return 'c'
    elif x == 13:
        return 'd'
    elif x == 14:
        return 'e'
    elif x == 15:
        return 'f'
    else:
        return 'f'


def real_color(r, g, b):
    minimal = min([r, g, b])
    return r - minimal, g - minimal, b - minimal,minimal


def code(x):
    a = x // 16
    b = x % 16
    return digit(int(a)) + digit(int(b))


def color_code(r, g, b):
    return '#'+code(r)+code(g)+code(b)

def lingrad_mono(init, stop, length):
    for i in range(length - 1):
        yield int(init-i*(init-stop)/(length-1))

def lingrad_triple(init, stop, length):
    for i in range(length - 1):
        yield color(int(init.r-i*(init.r-stop.r)/(length-1)),
        int(init.g-i*(init.g-stop.g)/(length-1)), int(init.b-i*(init.b-stop.b)/(length-1)))

def pointgrad(init, stop, point, length):
    return int(init-point*(init-stop)/(length-1))

def pointgrad_triple(init, stop, point, length):
    return color(int(init.r-point*(init.r-stop.r)/(length-1)),
    int(init.g-point*(init.g-stop.g)/(length-1)), int(init.b-point*(init.b-stop.b)/(length-1)))

def animate():
    global frame_num
    cnv.delete(ALL)
    r1, g1, b1
