package set1

import (
	"bufio"
	"fmt"
	"os"
	"sort"
)

func Challenge4() {
	file, err := os.Open("./set1/inputs/challenge4.txt")
	if err != nil {
		panic(err)
	}

	defer file.Close()

	scanner := bufio.NewScanner(file)

	allScores := make([]KeyAndScore, 0)

	for scanner.Scan() {
		s := scanner.Text()

		scores := GetScores(s)
		allScores = append(allScores, scores...)
	}

	sort.Slice(allScores, func(i, j int) bool {
		return allScores[i].Score < allScores[j].Score
	})

	for i := 0; i < 10; i += 1 {
		fmt.Println(i, allScores[i])
	}
}
