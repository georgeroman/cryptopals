package set1

import (
	"encoding/hex"
	"fmt"
)

func Challenge2() {
	str := "1c0111001f010100061a024b53535009181c"
	key := "686974207468652062756c6c277320657965"

	var err error

	strByteArr, err := hex.DecodeString(str)
	if err != nil {
		fmt.Println("Error decoding hex string")
	}

	keyByteArr, err := hex.DecodeString(key)
	if err != nil {
		fmt.Println("Error decoding hex string")
	}

	xorByteArr := make([]byte, len(strByteArr))
	for i, b := range strByteArr {
		xorByteArr[i] = b ^ keyByteArr[i]
	}

	xor := hex.EncodeToString(xorByteArr)
	fmt.Println(xor)
}
