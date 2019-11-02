import modules.common as common


def main(inp, out):

    for line in inp.readlines():

        try:
            file = common.re.search("^[\w,\s-]+\.[A-Za-z0-9]{3}$", line)
            print(file.group())

            if file not in common.Files:
                common.Files.append(file.group())
            else:
                print('Already in List')
        except AttributeError:
            pass

    out.write('#####FILES#####\n\n')
    for item in common.Files:
        out.write('"' + item + '", \n')