

filenames = ['/Users/Mario/Documents/Git/IOC-Parser/tests/files.txt', 'file2.txt', ...]
with open('path/to/output/file', 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                outfile.write(line)