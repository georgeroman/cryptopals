def pcks7_pad(b: bytes, block_size: int) -> bytearray:
    pad_size = 0
    while (len(b) + pad_size) % block_size != 0:
        pad_size += 1

    result = bytearray(b)
    result.extend([pad_size for _ in range(pad_size)])
    return result


def main():
    print(pcks7_pad("YELLOW SUBMARINE".encode("utf-8"), 20))


if __name__ == "__main__":
    main()
