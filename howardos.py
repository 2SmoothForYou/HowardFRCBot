from howardinit import bcolors
from unicode import pipe
import sys
class app:
    framewidth = 100
    frameheight = 200
    
    
    def loop():
        

    sys.stdout.write('┏')
    for each in xrange(framewidth-2):
        sys.stdout.write('━')