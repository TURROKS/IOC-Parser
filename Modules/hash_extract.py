from Modules.common import *


def main(inp, out):

    for line in inp.readlines():

        for hash in iocextract.extract_hashes(line):

            if hash not in Hashes:

                Hashes.append(hash)
                print(hash + ', ')
            else:
                print(hash + ' Already in List')

    out.write('\n#####HASHES#####\n\n')
    for item in Hashes:
        out.write('"' + item + '", \n')