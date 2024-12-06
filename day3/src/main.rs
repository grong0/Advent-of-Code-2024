use std::fs;
use regex::Regex;

fn input() -> String {
	return fs::read_to_string("./input.txt").unwrap();
}

fn parse_mul(mul: &str) -> i32 {
	let spl: Vec<&str> = mul.split(",").collect();
	let re = Regex::new("\\d+").unwrap();
	
	let Some(val1) = re.captures(spl[0]) else { return -1; };
	let Some(val2) = re.captures(spl[1]) else { return -1; };
	
	let val1: i32 = (&val1[0]).parse().unwrap();
	let val2: i32 = (&val2[0]).parse().unwrap();
	
	return val1 * val2;
}

fn part1() {
	let input = input();
	let lines = input.split("\n");
	let re = Regex::new("mul\\(\\d+,\\d+\\)").unwrap();
	let mut muls: Vec<&str> = vec![];
	for line in lines {
		let values: Vec<&str> = re.captures_iter(line).map(|x| {
			return x.get(0).unwrap().as_str();
		}).collect();
		muls.extend(values);
	}
	
	let mut tot = 0;
	for mul in muls {
		tot += parse_mul(mul);
	}
	
	println!("{}", tot);
}

fn part2() {
	
	let input = input();
	let lines = input.split("\n");
	let re = Regex::new("mul\\(\\d+,\\d+\\)|do\\(\\)|don't\\(\\)").unwrap();
	let mut funcs: Vec<&str> = vec![];
	for line in lines {
		let values: Vec<&str> = re.captures_iter(line).map(|x| {
			return x.get(0).unwrap().as_str();
		}).collect();
		funcs.extend(values);
	}
	
	let mut tot = 0;
	let mut current_mod = "do()";
	for func in funcs {
		println!("{}", func);
		if !func.contains("mul") {
			current_mod = func;
			continue;
		}
		
		if current_mod.eq("don't()") {
			continue;
		}
		
		tot += parse_mul(func);
	}
	
	println!("{}", tot);
}

fn main() {
    part2();
}
