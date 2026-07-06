import socket


def lookup(host):

    print()
    print("MicroDNS")
    print("=" * 40)

    try:
        name, aliases, addresses = socket.gethostbyname_ex(host)

        print("Hostname :", name)

        if aliases:
            print("Aliases :")
            for alias in aliases:
                print("  -", alias)

        print("Addresses:")
        for ip in addresses:
            print("  -", ip)

    except Exception as e:
        print("Lookup failed.")
        print(e)
