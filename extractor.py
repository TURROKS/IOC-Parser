from modules import email_extract,file_extract,hash_extract,ip_extract,url_extract,domain_extract

def main():

    with open('output.txt', 'w') as out:

        # Calls hash extract function
        with open('input.txt', 'r') as inp:
            hash_extract.main(inp, out)

        # Calls ip extract function
        with open('input.txt', 'r') as inp:
            ip_extract.main(inp, out)

        # Calls url extract function
        with open('input.txt', 'r') as inp:
            url_extract.main(inp, out)

        # Calls domain extract function
        domain_extract.main(out)

        # Calls email extract function
        with open('input.txt', 'r') as inp:
            email_extract.main(inp, out)

        # Calls file extract function
        with open('input.txt', 'r') as inp:
            file_extract.main(inp, out)

if __name__ == '__main__':

    main()