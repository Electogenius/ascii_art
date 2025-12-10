# Implementation of shapes

def rect_filled(x, y, h, k, l, b):
    if h <= x <= h+l and k <= y <= k+b:
        return True
    else:
        return False

def circle_filled(x, y, h, k, r):
    if (x - h)**2 + (y - k)**2 <= r**2:
        return True
    else:
        return False

def rect(x,y,h,k,l,b,t):
    lg=rect_filled(x, y, h-t, k-t, l+2*t, b+2*t)
    sm=rect_filled(x, y, h+t, k+t, l-2*t, b-2*t)
    if lg and not sm:
        return True
    else:
        return False

def circle(x,y,h,k,r,t):
    d=((h-x)**2+(k-y)**2)**0.5
    if r-t <= d <= r+t:
        return True
    else:
        return False