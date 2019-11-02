import modules.common as common
import iocextract


# function reads inp file, extracts IP Addresses using a regex string
def main(inp, out):
    for line in inp.readlines():

        for ip in iocextract.extract_ipv4s(line, refang=True):

            if ip not in common.IPs:

                common.IPs.append(ip)
                print(ip + ', ')
            else:
                print(ip + ' Already in List')

    out.write('\n#####IPs#####\n\n')
    for item in common.IPs:
        out.write('"' + item + '", \n')