import iocextract, re


with open('test.txt','r') as test:

    with open('output.txt','w') as output:

        IPs = []
        Hashes = []
        URLs = []
        Files = []
        Emails = []

        for line in test.readlines():



            try:
                mail=re.search("^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$",line)
                print(mail.group())

                if mail not in Emails:
                    Emails.append(mail.group())
                else:
                    print('Already in List')
            except AttributeError:
                pass

            try:
                file=re.search("^[\w,\s-]+\.[A-Za-z0-9]{3}$",line)
                print(file.group())

                if file not in Files:
                    Files.append(file.group())
                else:
                    print('Already in List')
            except AttributeError:
                pass

            for url in iocextract.extract_urls(line, refang=True):

                if url not in URLs:

                    URLs.append(url)
                    print(url + ', ')
                else:
                    print(url+' Already in List')

            for ip in iocextract.extract_ipv4s(line, refang=True):

                if ip not in IPs:

                    IPs.append(ip)
                    print(ip+', ')
                else:
                    print(ip+' Already in List')

            for hash in iocextract.extract_hashes(line):

                if hash not in Hashes:

                    Hashes.append(hash)
                    print(hash + ', ')
                else:
                    print(hash+' Already in List')

        output.write('#####URLS#####\n\n')
        for item in URLs:
            output.write('"'+item+'", \n')

        output.write('\n#####IPs#####\n\n')
        for item in IPs:
            output.write('"'+item+'", \n')

        output.write('\n#####HASHES#####\n\n')
        for item in Hashes:
            output.write('"'+item+'", \n')

        output.write('\n#####FILES#####\n\n')
        for item in Files:
            output.write('"' + item + '", \n')

        output.write('\n#####EMAILS#####\n\n')
        for item in Emails:
            output.write('"' + item + '", \n')