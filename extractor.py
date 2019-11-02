from modules import email_extract,file_extract,hash_extract,ip_extract,url_extract


def main():

    with open('/Users/Mario/Documents/Git/IOC-Parser/tests/output.txt', 'w') as out:

        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
            hash_extract.main(inp,out)

        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
            ip_extract.main(inp,out)

        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
            url_extract.main(inp,out)

        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
            email_extract.main(inp,out)

        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
            file_extract.main(inp,out)


if __name__ == '__main__':

    main()