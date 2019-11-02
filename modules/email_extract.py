import modules.common as common
import re


# function reads inp file, extracts email addresses using a regex string
def main(inp, out):

    for line in inp.readlines():

        try:
            mail = re.search(common.email_re, line)
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
