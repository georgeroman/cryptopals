def solve(b: bytes):
    scores = []
    for i in range(0, 256):
        d = bytes(x ^ i for x in b)

        score = 0
        for x in d:
            # Valid ASCII characters are prioritized
            if (x >= 65 and x <= 90) or (x >= 97 and x <= 122) or x == 32:
                score += 1
            else:
                score -= 1
        scores.append((score, d, i))

    scores.sort(key=lambda x: x[0], reverse=True)
    return scores


def main():
    s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
    scores = solve(bytes.fromhex(s))

    print(scores[:5])


if __name__ == "__main__":
    main()
