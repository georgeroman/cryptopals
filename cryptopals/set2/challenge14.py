import base64
import random
import secrets

from cryptopals.set1.challenge7 import aes_ecb_encrypt
from cryptopals.set2.challenge9 import pcks7_pad

KEY = secrets.token_bytes(16)
PREFIX = secrets.token_bytes(random.randint(1, 100))


def consistent_ecb_encrypt(s: bytes) -> bytes:
    suffix = """
        Um9sbGluJyBpbiBteSA1LjAKV2l0aCBteSByYWctdG9wIGRvd24gc28gbXkg
        aGFpciBjYW4gYmxvdwpUaGUgZ2lybGllcyBvbiBzdGFuZGJ5IHdhdmluZyBq
        dXN0IHRvIHNheSBoaQpEaWQgeW91IHN0b3A/IE5vLCBJIGp1c3QgZHJvdmUg
        YnkK
    """
    suffix = base64.b64decode(
        "".join(map(lambda x: x.strip(), suffix.split("\n"))))
    s += suffix

    s = PREFIX + s

    return aes_ecb_encrypt(pcks7_pad(s, 16), KEY)


def main():
    # Detect block size by checking for two exact ciphertext sequences
    # while properly handling any random size the prefix might have
    block_size = 0
    for i in range(2, 128 + 1):
        result = consistent_ecb_encrypt(("a" * i * 3).encode())
        blocks = [result[j:j + i] for j in range(0, len(result), i)]
        for j in range(len(blocks) - 1):
            if blocks[j] == blocks[j + 1]:
                block_size = i
                break
        if block_size != 0:
            break

    # Detect the size of the random prefix by finding the shortest prefix
    # pad so that we still have two consecutive matching ECB blocks
    prefix_size = 0
    prefix_pad = 0
    for i in range(0, block_size + 1):
        result = consistent_ecb_encrypt(
            ("a" * i + "a" * block_size * 2).encode()
        )
        blocks = [
            result[j:j + block_size] for j in range(0, len(result), block_size)
        ]
        for j in range(len(blocks) - 1):
            if blocks[j] == blocks[j + 1]:
                prefix_size = j * block_size - i
                prefix_pad = i
                break
        if prefix_size != 0:
            break

    sbi = prefix_size + prefix_pad

    # Brute-force one byte at a time (also pad all plaintexts
    # so that the random prefix will not interfere)
    decrypted = bytearray()
    for block in range(1, 17):
        detected_bytes = bytearray()
        for i in range(block_size - 1, -1, -1):
            plaintext = ("a" * (i + prefix_pad)).encode()
            result = consistent_ecb_encrypt(plaintext)

            for x in range(256):
                guess = consistent_ecb_encrypt(
                    plaintext + decrypted + detected_bytes + bytes([x])
                )
                if result[sbi:sbi + block_size * block] == guess[sbi:sbi + block_size * block]:
                    detected_bytes.append(x)
                    break

        decrypted.extend(detected_bytes)

    print(decrypted)


if __name__ == "__main__":
    main()
