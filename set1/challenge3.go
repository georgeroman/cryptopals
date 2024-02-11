package set1

import (
	"encoding/hex"
	"fmt"
	"sort"
)

type KeyAndScore struct {
	Original string
	Decoded  string
	Key      int
	Score    int
}

func GetScores(str string) []KeyAndScore {
	byteArr, err := hex.DecodeString(str)
	if err != nil {
		panic(err)
	}

	decodeAttempts := make([]string, 256)
	for k := 0; k < 256; k += 1 {
		decodedByteArr := make([]byte, len(byteArr))
		for i, b := range byteArr {
			decodedByteArr[i] = b ^ uint8(k)
		}

		decodeAttempts[k] = string(decodedByteArr)
	}

	englishCharacterFrequency := map[rune]uint{
		'e': 12,
		't': 9,
		'a': 8,
		'o': 8,
		'i': 8,
		'n': 8,
		's': 8,
		'h': 6,
		'r': 6,
		'd': 4,
		'l': 4,
		'u': 3,
	}

	scores := make([]KeyAndScore, len(decodeAttempts))
	for k, s := range decodeAttempts {
		characterCounts := make(map[rune]uint)
		for _, c := range s {
			characterCounts[c] += 1
		}

		score := 0
		for c, v := range englishCharacterFrequency {
			score += int(v) - int(characterCounts[c])
		}

		scores[k] = KeyAndScore{
			Original: str,
			Decoded:  decodeAttempts[k],
			Key:      k,
			Score:    score,
		}
	}

	sort.Slice(scores, func(i, j int) bool {
		return scores[i].Score < scores[j].Score
	})

	return scores
}

func Challenge3() {
	scores := GetScores("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")

	for i := 0; i < 10; i += 1 {
		fmt.Println(i, scores[i])
	}
}
