from random import randint, random
from typing import Tuple
from secrets import token_bytes

from cryptopals.set1.challenge7 import aes_ecb_encrypt
from cryptopals.set2.challenge1 import pcks7_pad
from cryptopals.set2.challenge2 import aes_cbc_encrypt


def encryption_oracle(msg: bytes) -> Tuple[bytearray, int]:
    prefix_len = randint(5, 10)
    msg = token_bytes(prefix_len) + msg

    suffix_len = randint(5, 10)
    msg = msg + token_bytes(suffix_len)

    key = token_bytes(16)
    if random() < 0.5:
        # Use AES ECB mode
        return (aes_ecb_encrypt(pcks7_pad(msg, 16), key), 0)
    else:
        # Use AES CBC mode
        iv = token_bytes(16)
        return (aes_cbc_encrypt(pcks7_pad(msg, 16), key, iv), 1)


def main():
    p = "".join(["X" for _ in range(128)]).encode("utf-8")
    for _ in range(20):
        (e, mode) = encryption_oracle(p)
        # Detect matching sequences which hint to AES ECB
        guessed_mode = 1
        for i in range(0, len(e) - 16):
            if e[i+16:].find(e[i:i+16]) != -1:
                guessed_mode = 0
                break
        print(mode, guessed_mode)


if __name__ == "__main__":
    main()
