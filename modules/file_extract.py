import modules.common as common
import re


# function reads inp file, extracts file names using a regex string
def main(inp, out):

    for line in inp.readlines():

        try:
            file = re.search(common.file_re, line)
            print(file.group())

            if file not in common.Files:
                common.Files.append(file.group())
            else:
                print('Already in List')
        except AttributeError:
            pass

    out.write('\n#####FILES#####\n\n')
    for item in common.Files:
        out.write('"' + item + '", \n')