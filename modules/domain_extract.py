import modules.common as common
import re


# function reads inp file, extracts file names using a regex string
def main(out):

    for url in common.URLs:

        try:
            domain = re.search(common.domain_re, url)
            print(domain.group())

            if domain not in common.Domains:
                common.Domains.append(domain.group())
            else:
                print('Already in List')
        except AttributeError:
            pass

    out.write('\n#####Domain#####\n\n')
    for item in common.Domains:
        out.write('"' + item + '", \n')