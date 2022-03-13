def validate_pcks7_padding(s: bytes):
    if len(s) % 16 != 0:
        raise ValueError("Input has incorrect length")

    padding_size = s[-1]
    for x in s[-padding_size:]:
        if x != padding_size:
            raise ValueError("Invalid padding")

    return s[:-padding_size]


def main():
    print(validate_pcks7_padding(b'ICE ICE BABY\x04\x04\x04\x04'))


if __name__ == "__main__":
    main()
