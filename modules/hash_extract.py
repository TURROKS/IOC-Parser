import modules.common as common
import iocextract


# function reads inp file, extracts hashes using a regex string
def main(inp, out):

    for line in inp.readlines():

        for new_hash in iocextract.extract_hashes(line):

            if new_hash not in common.Hashes:

                common.Hashes.append(new_hash)
                print(new_hash + ', ')
            else:
                print(new_hash + ' Already in List')

    out.write('#####HASHES#####\n\n')
    for item in common.Hashes:
        out.write('"' + item + '", \n')