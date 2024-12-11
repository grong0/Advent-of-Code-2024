package main

import (
	"fmt"
	"maps"
	"os"
	"slices"
	"strconv"
	"strings"
)

func check(err error) {
	if err != nil {
		panic(err)
	}
}

func parse(stones []int, memo map[[3]int][]int, blink_target int, blink_count int) []int {
	if blink_count == blink_target {
		return stones
	}

	new_stones := []int{}
	for i := 0; i < len(stones); i++ {
		if slices.Contains(slices.Collect(maps.Keys(memo)), [3]int{stones[i], blink_target, blink_count}) {
			// fmt.Println("memoziation was used to evaluate", stones[i], "as", memo[[3]int{stones[i], blink_target, blink_count}])
			new_stones = slices.Concat(memo[[3]int{stones[i], blink_target, blink_count}])
			continue
		}
		if stones[i] == 0 {
			parsed_val := parse([]int{1}, memo, blink_target, blink_count + 1)
			new_stones = slices.Concat(new_stones, parsed_val)
		} else if len(strconv.Itoa(stones[i]))%2 == 0 {
			length := len(strconv.Itoa(stones[i]))
			new_int_1, err_1 := strconv.Atoi(strconv.Itoa(stones[i])[:length/2])
			new_int_2, err_2 := strconv.Atoi(strconv.Itoa(stones[i])[length/2 : length])
			check(err_1)
			check(err_2)
			parsed_val_1 := parse([]int{new_int_1}, memo, blink_target, blink_count + 1)
			parsed_val_2 := parse([]int{new_int_2}, memo, blink_target, blink_count + 1)
			memo[[3]int{stones[i], blink_target, blink_count}] = slices.Concat(parsed_val_1, parsed_val_2)
			new_stones = slices.Concat(new_stones, parsed_val_1, parsed_val_2)
		} else {
			parsed_val := parse([]int{stones[i] * 2024}, memo, blink_target, blink_count + 1)
			memo[[3]int{stones[i], blink_target, blink_count}] = parsed_val
			new_stones = slices.Concat(new_stones, parsed_val)
		}
	}

	fmt.Println(len(slices.Collect(maps.Keys(memo))))

	return new_stones
}

func main() {
	data, err := os.ReadFile("./sample.txt")
	check(err)
	raw_stones := strings.Split(strings.TrimRight(strings.TrimRight(string(data), "\n"), "\r"), " ")
	stones := []int{}
	for i := 0; i < len(raw_stones); i++ {
		new_int, err := strconv.Atoi(raw_stones[i])
		check(err)
		stones = append(stones, new_int)
	}

	// memo := make(map[int][]int)
	// blinks := 25
	// for i := 0; i < blinks; i++ {
	// 	fmt.Println(i)

	// 	new_stones := []int{}
	// 	for j := 0; j < len(stones); j++ {
	// 		if slices.Contains(slices.Collect(maps.Keys(memo)), stones[j]) {
	// 			// fmt.Println("memoization was used to evaluate", stones[j], "as", memo[stones[j]])
	// 			new_stones = slices.Concat(new_stones, memo[stones[j]])
	// 			continue
	// 		}

	// 		if stones[j] == 0 {
	// 			memo[stones[j]] = []int{1}
	// 			new_stones = append(new_stones, 1)
	// 		} else if len(strconv.Itoa(stones[j]))%2 == 0 {
	// 			length := len(strconv.Itoa(stones[j]))
	// 			new_int_1, err_1 := strconv.Atoi(strconv.Itoa(stones[j])[:length/2])
	// 			new_int_2, err_2 := strconv.Atoi(strconv.Itoa(stones[j])[length/2 : length])
	// 			check(err_1)
	// 			check(err_2)
	// 			memo[stones[j]] = []int{new_int_1, new_int_2}
	// 			new_stones = append(new_stones, new_int_1)
	// 			new_stones = append(new_stones, new_int_2)
	// 		} else {
	// 			memo[stones[j]] = []int{stones[j] * 2024}
	// 			new_stones = append(new_stones, stones[j]*2024)
	// 		}
	// 	}
	// 	stones = new_stones
	// }

	stones = parse(stones, map[[3]int][]int{}, 75, 0)

	// fmt.Println(stones)
	fmt.Println(len(stones))
}
