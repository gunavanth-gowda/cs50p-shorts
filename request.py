from week6_libraries.museum.artists import get_artists


def main():
    artist = input("Artist: ")
    artists_response = get_artists(query=artist, limit=6)
    for artist in artists_response:
        print(f"* {artist}")


if __name__ == "__main__":
    main()
