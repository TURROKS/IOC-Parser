import modules.common as common


def main(inp, out):

    for line in inp.readlines():

        for hash in common.iocextract.extract_hashes(line):

            if hash not in common.Hashes:

                common.Hashes.append(hash)
                print(hash + ', ')
            else:
                print(hash + ' Already in List')

    out.write('#####HASHES#####\n\n')
    for item in common.Hashes:
        out.write('"' + item + '", \n')