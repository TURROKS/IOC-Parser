import modules.common as common


def main(inp, out):

    for line in inp.readlines():

        try:
            mail = common.re.search(
                "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
                line)
            print(mail.group())

            if mail not in common.Emails:
                common.Emails.append(mail.group())
            else:
                print('Already in List')
        except AttributeError:
            pass

    out.write('\n#####EMAILS#####\n\n')
    for item in common.Emails:
        out.write('"' + item + '", \n')
