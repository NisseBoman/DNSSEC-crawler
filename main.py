
##########################################################################
##### Sample code to crawl DNS to if they have DNSSEC enabled or not #####
##### Not saying this is amazing code but it an example on how       #####
##### easy it is to figure it out                                    #####
##### This is my first python code ever written                      #####
##########################################################################

import subprocess


HOST = "api.fastly.com"

def main():

    domains = ["ikea.com", "ingka.com", "google.com", "boman.church"]
    for tld in domains:
        #print(tld)
        print("Checking: " + tld + " for DNSSEC")
        command = "whois " + tld + " | egrep -i 'DNSSEC|signed'"
        try:
            result = subprocess.check_output(command, shell = True, executable = "/bin/bash", stderr = subprocess.STDOUT)

        except subprocess.CalledProcessError as cpe:
            result = cpe.output

        finally:
            for line in result.splitlines():
                print(line.decode())
                


# This is the standard boilerplate that calls the main() function.
if __name__ == '__main__':
    main()






