def repeating_key_xor(b: bytes, key: bytes) -> bytearray:
    result = bytearray()
    for i in range(len(b)):
        result.append(b[i] ^ key[i % len(key)])
    return result


def main():
    s = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
    print(repeating_key_xor(bytes(s, "ascii"), bytes("ICE", "ascii")).hex())


if __name__ == "__main__":
    main()
