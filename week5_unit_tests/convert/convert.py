def main():
    while True:
        au = input("AU: ")
        try:
            au = float(au)
            break
        except ValueError:
            continue

    print(f"{au} AU is {convert(au)} m.")


def convert(au):
    if not isinstance(au, (float, int)):
        raise TypeError("au must be a float or an int")
    return au * 149597870700
