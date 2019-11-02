import modules.common as common
import iocextract


# function reads inp file, extracts URLs using a regex string
def main(inp, out):

    for line in inp.readlines():

        for url in iocextract.extract_urls(line, refang=True):

            if url not in common.URLs:

                common.URLs.append(url)
                print(url + ', ')
            else:
                print(url + ' Already in List')

    out.write('\n#####URLS#####\n\n')
    for item in common.URLs:
        out.write('"' + item + '", \n')