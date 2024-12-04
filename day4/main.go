package main

import (
	"os"
	"regexp"
	"strings"
)

func check(er error) {
	if er != nil {
		panic(er)
	}
}

func day1() {
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
	println("hor\t", horFor+horBac)
	// vertical
	verFor := len(rx.FindAllString(modFile, -1))
	verBack := len(rs.FindAllString(modFile, -1))
	tot += verFor + verBack
	println("ver\t", verFor+verBack)
	// diagnal
	nwCount := 0
	neCount := 0
	swCount := 0
	seCount := 0
	for i := 0; i < len(spl); i++ {
		for z := 0; z < len(spl[i]); z++ {
			if string(spl[i][z]) == "X" {
				// north west
				if i-3 >= 0 && z-3 >= 0 && (string(spl[i][z])+string(spl[i-1][z-1])+string(spl[i-2][z-2])+string(spl[i-3][z-3])) == "XMAS" {
					tot += 1
					nwCount += 1
				}
				// north east
				if i-3 >= 0 && z+3 < len(spl[0]) && (string(spl[i][z])+string(spl[i-1][z+1])+string(spl[i-2][z+2])+string(spl[i-3][z+3])) == "XMAS" {
					tot += 1
					neCount += 1
				}
				// south west
				if i+3 < len(spl) && z-3 >= 0 && (string(spl[i][z])+string(spl[i+1][z-1])+string(spl[i+2][z-2])+string(spl[i+3][z-3])) == "XMAS" {
					tot += 1
					swCount += 1
				}
				// south east
				if i+3 < len(spl) && z+3 < len(spl[0]) && (string(spl[i][z])+string(spl[i+1][z+1])+string(spl[i+2][z+2])+string(spl[i+3][z+3])) == "XMAS" {
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
	println("tot\t", tot)
}

func day2() {
	file, err := os.ReadFile("./input.txt")
	check(err)
	spl := strings.Split(string(file), "\n")
	spl = spl[:len(spl)-1]

	tot := 0
	for i := 0; i < len(spl); i++ {
		for z := 0; z < len(spl[i]); z++ {
			if string(spl[i][z]) == "A" && (i-1 >= 0 && i+1 < len(spl) && z-1 >= 0 && z+1 < len(spl[0])) {
				nw := string(spl[i-1][z-1])
				ne := string(spl[i-1][z+1])
				sw := string(spl[i+1][z-1])
				se := string(spl[i+1][z+1])
				comb := nw + ne + sw + se
				
				if comb == "MSMS" || comb == "MMSS" || comb == "SMSM" || comb == "SSMM" {
					tot += 1
				}
			}
		}
	}
	println("tot\t", tot)
}

func main() {
	println("starting...")

	// day1()
	day2()
}
