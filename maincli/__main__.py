import sys
import os
import getpass
from .encrypt_pdf import encrypt_pdf
def main():
    if len(sys.argv) < 2:
        os.system("echo please pass a file name")
        exit()
    if len(sys.argv) > 2:
        os.system("echo to many arguments")
        exit()
    file = sys.argv[1]
    file = file + ".pdf"
    if not os.path.exists(file):
        os.system(f"echo {file} does not exist")
        exit()
    password = getpass.getpass('Password:')
    encrypt_pdf(file,password)
    


if __name__ == '__main__':
    main()
