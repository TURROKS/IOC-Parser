from modules import email_extract,file_extract,hash_extract,ip_extract,url_extract


def main():

    with open('/Users/Mario/Documents/Git/IOC-Parser/tests/test.txt', 'r') as inp:
        with open('/Users/Mario/Documents/Git/IOC-Parser/tests/output.txt', 'w') as out:

            email_extract.main(inp,out)
            file_extract.main(inp,out)
            hash_extract.main(inp,out)
            ip_extract.main(inp,out)
            url_extract.main(inp,out)

if __name__ == '__main__':
    main()
