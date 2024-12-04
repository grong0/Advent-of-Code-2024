package main

import (
	"fmt"
	// "math"
	"os"
	"regexp"
	"strings"
)

func check(er error) {
	if er != nil {
		panic(er)
	}
}

func parseDiagnallyLeft(file []byte) {
	array := strings.Split(string(file), "\n")
	array = array[:len(array)-1]

	// for i := 0; i < len(array); i++ {
	// 	for z := i; z >= 0; z-- {
	// 		fmt.Print(string(array[z][i-z]))
	// 	}
	// 	fmt.Println("")
	// }
	for i := len(array) - 1; i > 0; i-- {
		// fmt.Println(i)
		// fmt.Print(" ")
		for z := i; z < len(array[i])-i; z++ {
			// fmt.Print(z)
			fmt.Print(string(array[z][len(array[i])-z-1]))
			// fmt.Println(z, len(array[i])-z-1)
			// fmt.Print(" ")
		}
		fmt.Println("")
	}
	// for i := 0; i < len(array); i++ {
	// 	for z := 0; z < len(array[0]); z++ {
	// 		fmt.Print(string(array[i+z][z]))
	// 	}
	// 	fmt.Println("")
	// }
}

// func getRotate(file []byte) string {
// 	str := string(file)

// 	strings.Split(str, "\n")

// 	newArr := new([]string)
// }

func main() {
	fmt.Println("starting...")

	file, err := os.ReadFile("./input.txt")
	check(err)

	spl := strings.Split(string(file), "\n")
	spl = spl[:len(spl)-1]
	modFile := ""
	for i := 0; i < len(spl); i++ {
		for z := 0; z < len(spl[i]); z++ {
			modFile += string(spl[z][i])
		}
		modFile += "\n"
	}
	println(modFile)

	tot := 0
	rx, _ := regexp.Compile("XMAS")
	rs, _ := regexp.Compile("SAMX")
	// horizontal
	horFor := len(rx.FindAllString(string(file), -1))
	horBac := len(rs.FindAllString(string(file), -1))
	tot += horFor + horBac
	println("hor\t", horFor + horBac)
	// vertical
	verFor := len(rx.FindAllString(modFile, -1))
	verBack := len(rs.FindAllString(modFile, -1))
	tot += verFor + verBack
	println("ver\t", verFor + verBack)
	// diagnal
	nwCount := 0
	neCount := 0
	swCount := 0
	seCount := 0
	for i := 0; i < len(spl); i++ {
		for z := 0; z < len(spl[i]); z++ {
			if string(spl[i][z]) == "X" {
				// north west
				if i-3 >= 0 && z-3 >= 0 && (string(spl[i][z]) + string(spl[i-1][z-1]) + string(spl[i-2][z-2]) + string(spl[i-3][z-3])) == "XMAS" {
					tot += 1
					nwCount += 1
				}
				// north east
				if i-3 >= 0 && z+3 < len(spl[0]) && (string(spl[i][z]) + string(spl[i-1][z+1]) + string(spl[i-2][z+2]) + string(spl[i-3][z+3])) == "XMAS" {
					tot += 1
					neCount += 1
				}
				// south west
				if i+3 < len(spl) && z-3 >= 0 && (string(spl[i][z]) + string(spl[i+1][z-1]) + string(spl[i+2][z-2]) + string(spl[i+3][z-3])) == "XMAS" {
					tot += 1
					swCount += 1
				}
				// south east
				if i+3 < len(spl) && z+3 < len(spl[0]) && (string(spl[i][z]) + string(spl[i+1][z+1]) + string(spl[i+2][z+2]) + string(spl[i+3][z+3])) == "XMAS" {
					tot += 1
					seCount += 1
				}
			}
		}
	}
	println("nw\t", nwCount)
	println("ne\t", neCount)
	println("sw\t", swCount)
	println("se\t", seCount)
	fmt.Println("tot\t", tot)
}
