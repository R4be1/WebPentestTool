import os

def ExtractTLD(domain):
    file_path = os.path.join( os.path.dirname(os.path.abspath(__file__)), "effective_tld_names.dat" )
    with open(file_path, errors='ignore') as effective_tld_names_file:
        effective_tld_names=[line.strip() for line in effective_tld_names_file.readlines()]
        effective_tld_names=sorted(effective_tld_names, key=lambda x: len(x.split(".")), reverse=True)
        for line in effective_tld_names:
            if line.startswith('//') or line.startswith('!') or line == '':
                continue
            if line.startswith("*") and domain.endswith(line[1:]):
                return domain
            elif domain.endswith(line):
                return ".".join( domain.split(".")[-1*len(line.split("."))-1:] )

