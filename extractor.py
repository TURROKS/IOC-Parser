from modules import email_extract,file_extract,hash_extract,ip_extract,url_extract

def main():

    with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/emails.txt', 'w') as out:

            email_extract.main(inp,out)

    with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/files.txt', 'w') as out:

            file_extract.main(inp,out)

    with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/hashes.txt', 'w') as out:
            hash_extract.main(inp,out)

    with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/ips.txt', 'w') as out:
            ip_extract.main(inp,out)

    with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/urls.txt', 'w') as out:
            url_extract.main(inp,out)

if __name__ == '__main__':

    main()

