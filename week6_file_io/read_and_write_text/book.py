def main():
    with open("alice.txt") as file:
        contents = file.readlines()
    chapter1 = contents[9:244]

    with open("chapter1.txt", "w") as file:
        file.write("".join(chapter1))


if __name__ == "__main__":
    main()
