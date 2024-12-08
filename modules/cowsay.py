import sys

def main(message):
    cow = r"""
     ______________
    < {msg} >
     --------------
            \   ^__^
             \  (oo)\_______
                (__)\       )\/\
                    ||----w |
                    ||     ||
    """

    max_length = 14
    if len(message) > max_length:
        message = message[:max_length-3] + "..."
    print(cow.format(msg=message))

if __name__ == "__main__":
    import sys
    if len(sys.argv) != 2:
        print("Usage: python cowsay.py <message>")
    else:
        main(sys.argv[1])