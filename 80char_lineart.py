import sys
import argparse

def create_line(str_in,length,decorate="-"):
    line_length = len(str_in)
    if(line_length > length):
        print "error:"
        print "line is %s characters  too long. ( length=%s )" % (line_length - length, line_length)
        return
    wiggle_room = length - line_length
    out = ""
    decoration = ""
    for i in range((wiggle_room/2)-1):
        decoration += decorate

    out= decoration +" "+ str_in+" " + decoration
    if(len(out) < length):
        for i in range( length-len(out)):
            out+=decorate

    print out


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("-i","--input", help="text you want to decorate", required=True)
    parser.add_argument("--char", help="the character that will decorate the text")
    parser.add_argument("--max_length",help="how big the line should be", required=False)
    args = parser.parse_args()

    length = 80
    if(args.max_length):
        length=int(args.max_length)
    if(args.char):
        create_line(args.input,length,args.char)
    else:
        create_line(args.input,length)
    
    


    
