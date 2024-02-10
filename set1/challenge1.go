package set1

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
)

func Challenge1() {
	hexStr := "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
	byteArr, err := hex.DecodeString(hexStr)
	if err != nil {
		fmt.Println("Error decoding hex string")
		return
	}

	base64Str := base64.StdEncoding.EncodeToString((byteArr))
	fmt.Println(base64Str)
}
