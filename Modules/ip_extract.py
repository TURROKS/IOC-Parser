from Modules.common import *


def main(inp, out):
    for line in inp.readlines():

        for ip in iocextract.extract_ipv4s(line, refang=True):

            if ip not in IPs:

                IPs.append(ip)
                print(ip + ', ')
            else:
                print(ip + ' Already in List')

    out.write('\n#####IPs#####\n\n')
    for item in IPs:
        out.write('"' + item + '", \n')