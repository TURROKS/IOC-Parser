from Modules.common import *

def main(inp, out):

    for line in inp.readlines():

        for url in iocextract.extract_urls(line, refang=True):

            if url not in URLs:

                URLs.append(url)
                print(url + ', ')
            else:
                print(url + ' Already in List')

    out.write('#####URLS#####\n\n')
    for item in URLs:
        out.write('"' + item + '", \n')