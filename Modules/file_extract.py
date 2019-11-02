from Modules.common import *

def main(inp, out):

    for line in inp.readlines():

        try:
            file = re.search("^[\w,\s-]+\.[A-Za-z0-9]{3}$", line)
            print(file.group())

            if file not in Files:
                Files.append(file.group())
            else:
                print('Already in List')
        except AttributeError:
            pass

    out.write('\n#####FILES#####\n\n')
    for item in Files:
        out.write('"' + item + '", \n')