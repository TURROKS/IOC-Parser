import iocextract, re

#Variables

IPs = []
Hashes = []
URLs = []
Files = []
Emails = []

#Open the files that will be modified by the script


def extract_email(test,output):

    for line in test.readlines():

        try:
            mail = re.search(
                "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",
                line)
            print(mail.group())

            if mail not in Emails:
                Emails.append(mail.group())
            else:
                print('Already in List')
        except AttributeError:
            pass

    output.write('\n#####EMAILS#####\n\n')
    for item in Emails:
        output.write('"' + item + '", \n')

def extract_files(test,output):

    for line in test.readlines():

        try:
            file=re.search("^[\w,\s-]+\.[A-Za-z0-9]{3}$",line)
            print(file.group())

            if file not in Files:
                Files.append(file.group())
            else:
                print('Already in List')
        except AttributeError:
            pass

    output.write('\n#####FILES#####\n\n')
    for item in Files:
        output.write('"' + item + '", \n')

def extract_url(test,output):

    for line in test.readlines():

        for url in iocextract.extract_urls(line, refang=True):

            if url not in URLs:

                URLs.append(url)
                print(url + ', ')
            else:
                print(url+' Already in List')

    output.write('#####URLS#####\n\n')
    for item in URLs:
        output.write('"'+item+'", \n')

def extract_ip(test,output):

    for line in test.readlines():

        for ip in iocextract.extract_ipv4s(line, refang=True):

            if ip not in IPs:

                IPs.append(ip)
                print(ip+', ')
            else:
                print(ip+' Already in List')

    output.write('\n#####IPs#####\n\n')
    for item in IPs:
        output.write('"' + item + '", \n')

def extract_hash(test,output):

    for line in test.readlines():

        for hash in iocextract.extract_hashes(line):

            if hash not in Hashes:

                Hashes.append(hash)
                print(hash + ', ')
            else:
                print(hash+' Already in List')

    output.write('\n#####HASHES#####\n\n')
    for item in Hashes:
        output.write('"' + item + '", \n')


def main():

    with open('/Users/Mario/Documents/Git/IOC-Parser/Tests/test.txt', 'r') as test:
        with open('/Users/Mario/Documents/Git/IOC-Parser/Tests/output.txt', 'w') as output:

            extract_email(test,output)
            extract_files(test,output)
            extract_hash(test,output)
            extract_ip(test,output)
            extract_url(test,output)

if __name__ == '__main__':

    main()
