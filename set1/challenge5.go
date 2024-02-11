package set1

import (
	"encoding/hex"
	"fmt"
)

func Challenge5() {
	str := "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
	key := "ICE"

	encoded := make([]byte, len(str))
	for i := 0; i < len(str); i += 1 {
		encoded[i] = str[i] ^ key[(i%len(key))]
	}

	fmt.Println(hex.EncodeToString(encoded))
}
