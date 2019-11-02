import modules.common as common


def main(inp, out):
    for line in inp.readlines():

        for ip in common.iocextract.extract_ipv4s(line, refang=True):

            if ip not in common.IPs:

                common.IPs.append(ip)
                print(ip + ', ')
            else:
                print(ip + ' Already in List')

    out.write('#####IPs#####\n\n')
    for item in common.IPs:
        out.write('"' + item + '", \n')