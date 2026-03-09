def install_or_remove_packages():
    iOrR = ""

    while iOrR != "I" and iOrR != "R":
        print("Would you like to install or remove packages? (I/R)")
        iOrR = input().upper()

    if iOrR == "I":
        iOrR = "install"
    elif iOrR == "R":
        iOrR = "remove"

    defaultPackages = "curl wget git"

    print("Enter a list of packages")
    print("The list should be separated by spaces, for example:")
    print("package1 package2 package3")
    print("Otherwise, input 'default' to " + iOrR + " the default packages listed in this program")

    packages = input().lower()

    if packages == "default":
        packages = defaultPackages

    if iOrR == "install":
        print("Se ejecutaría: sudo apt-get install " + packages)

    elif iOrR == "remove":
        while True:
            print("Purge files after removing? (Y/N)")
            choice = input().upper()

            if choice == "Y":
                print("Se ejecutaría: sudo apt-get --purge remove " + packages)
                break
            elif choice == "N":
                print("Se ejecutaría: sudo apt-get remove " + packages)
                break

        print("Se ejecutaría: sudo apt autoremove")


def clean_environment():
    print("Se ejecutaría: sudo apt-get autoremove")
    print("Se ejecutaría: sudo apt-get autoclean")


install_or_remove_packages()
clean_environment()