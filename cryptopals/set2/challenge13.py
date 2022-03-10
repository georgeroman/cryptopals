from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
import secrets

from cryptopals.set2.challenge9 import pcks7_pad

KEY = secrets.token_bytes(16)


def parse(s: str) -> object:
    result = {}
    kv = map(lambda x: x.split("=")[:2], s.split("&"))
    for [k, v] in kv:
        result[k] = v
    return result


def urlify(email: str) -> str:
    email = email.replace("=", "%3D").replace("&", "%26")
    return f"email={email}&uid=10&role=user"


def encrypt(encoded: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(KEY), modes.ECB())
    encryptor = cipher.encryptor()
    return encryptor.update(pcks7_pad(encoded, 16)) + encryptor.finalize()


def decrypt(encrypted: bytes) -> bytes:
    cipher = Cipher(algorithms.AES(KEY), modes.ECB())
    decryptor = cipher.decryptor()
    return decryptor.update(encrypted) + decryptor.finalize()


def main():
    # Second 16 bytes of 'email=xxxxxxxxxxxxx&uid=10&role=user'
    # will result in a valid ciphertext for 'xxx&uid=10&role='
    c1 = encrypt(urlify("xxxxxxxxxxxxx").encode())[16:32]

    # Second 16 bytes of 'email=xxxxxxxxxxadminPCKS7PAD&uid=10&role=user'
    # will result in a valid ciphertext for 'admin' (pcks7 padded)
    c2 = encrypt(urlify(
        "xxxxxxxxxx" +
        pcks7_pad("admin".encode(), 16).decode()
    ).encode())[16:32]

    # Generate the missing part of c1
    c0 = encrypt(urlify("xxxxxxxxxx").encode())[:16]

    # Concatenate everything and get the admin role
    print(parse(decrypt(c0 + c1 + c2)[:-11].decode()))


if __name__ == "__main__":
    main()
