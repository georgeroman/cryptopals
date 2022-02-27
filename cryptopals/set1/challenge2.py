def xor(b1: bytes, b2: bytes) -> bytes:
    return bytes(x ^ y for (x, y) in zip(b1, b2))


def main():
    s1 = "1c0111001f010100061a024b53535009181c"
    s2 = "686974207468652062756c6c277320657965"

    b1 = bytes.fromhex(s1)
    b2 = bytes.fromhex(s2)

    print(xor(b1, b2).hex())


if __name__ == "__main__":
    main()
