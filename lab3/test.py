#!/usr/bin/python
import sys
from optparse import OptionParser



def writeline(option, file_1, file_2, both, context):
    space = "        "
    if option == 1:
        if file_1 != True:
            return
    elif option == 2:
        if file_2 != True:
            return
        if file_1 == True:
            sys.stdout.write(space)
    elif option == 3:
        if both != True:
            return
        if file_1 == True:
            sys.stdout.write(space)
        if file_2 == True:
            sys.stdout.write(space)
    else:
        return
    sys.stdout.write(context)


def comp(content1,content2,fusort,file_1, file_2, both):
    if fusort == True:
            i = 0
            j = 0
            while i<len(content1) or j<len(content2):
                    line1= ""
                    line2 =""
                    if i <len(content1):
                        line1 = content1[i]
                    if j< len(content2):
                        line2 = content2[j]
                    if (line1>line2 and line2!=0) or (line1=="" and line2!=""):
                        writeline(2,file_1,file_2,both,line2)
                        j+=1
                        continue
                    elif (line1<line2 and line1!=0) or line2 ==0:
                        writeline(1, file_1, file_2, both, line1)
                        i+=1
                        continue
                    elif line1==line2 and (line1!="" and line2!=""):
                        writeline(3,file_1,file_2,both,line2)
                        j+=1
                        i+=1
                        continue
            return
    else:
        temp = content2
        within=False
        for x in content1:
            for y in content2:
                if x==y:
                    writeline(3,file_1,file_2,both,x)
                    temp.remove(y)
                    within=True
                    break
            if(within):
                writeline(1,file_1,file_2,both,x)
                within =False

        for z in temp:
            writeline(2,file_1,file_2,both,z)

def main():
    version_msg = "%prog 2.0"
    usage_msg = """%prog [OPTION]... FILE1 FILE2                                                                                                      
    Compare files FILE1 and FILE2 line by line.                                                                                                       
    When FILE1 or FILE2 (not both) is -, read standard input.                                                                                         
    """
    parser = OptionParser(version=version_msg,usage=usage_msg)
    parser.add_option("-u",action="store_false", dest="sort_u", default=True, help="sort file before compare")
    parser.add_option("-1",action="store_false",dest="file_1",default=True,help="suppress column 1 (lines unique to FILE1)")
    parser.add_option("-2",action="store_false",dest="file_2",default=True,help="suppress colum  2 (lines unique to FILE2)")
    parser.add_option("-3",action="store_false",dest="both",default=True,help="suppress column 3 (lines that appear in both files)")


    options, args = parser.parse_args(sys.argv[1:])

    try:
        file_1 = bool(options.file_1)

    except:
        parser.error("invalid options: {0}".
             format(options.file_1))
    try:
        file_2 = bool(options.file_2)
    except:
        parser.error("invalid options: {0}".
                 format(options.file_2))
    try:
        both = bool(options.both)
    except:
        parser.error("invalid options: {0}".
        format(options.both))
    try:
        sort_u = bool(options.sort_u)
    except:
        parser.error("invalid options: {0}".
                     format(options.usort))




    if len(args) > 2:
        parser.error("extra operand\n")
    elif len(args) < 2:
        parser.error("missing operand\n")
    if args[0] != "-":
            f1 = open(args[0], 'r')
            content1 = f1.readlines()
            content1 = list(content1)
            f1.close()
    else:
            content1 = sys.stdin.readlines()

    if args[1] != "-":
            f2 = open(args[1], 'r')
            content2 = f2.readlines()
            content2 = list(content2)
            f2.close()
    else:
            content2 = sys.stdin.readlines()

    comp(content1, content2, sort_u, file_1, file_2, both)

if __name__ == "__main__":
        main()
