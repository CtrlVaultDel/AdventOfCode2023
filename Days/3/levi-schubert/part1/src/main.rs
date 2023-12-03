use std::fs;
use std::error::Error;
use std::time::SystemTime;
use substring::Substring;

fn main() -> Result<(), Box<dyn Error>>{
    let start_time = SystemTime::now();
    let input: String = fs::read_to_string("input/input.txt")?.parse()?;
    let lines: Vec<&str> = input.split("\r\n").collect();

    let (nums, symbols) = parse_lines_to_nums_and_symbols(lines);

    

    let answer = sum_nums_adjacent_to_symbol(nums, symbols);

    let end_time = SystemTime::now();
    let time_taken = end_time.duration_since(start_time).expect("Clock may have gone backwards");
    println!("answer: {} \ntime taken: {:?}", answer, time_taken);
    Ok(())
}

fn parse_lines_to_nums_and_symbols(lines: Vec<&str>) -> (Vec<Num>, Vec<Point>){
    let mut nums: Vec<Num> = Vec::<Num>::new();
    let mut symbols: Vec<Point> = Vec::<Point>::new();

    let mut y_counter = 0;
    for line in &lines{
        println!("checking line {}", y_counter);
        let mut number = String::new();
        let mut counter = 0;
        for ch in line.chars(){
            if ch.is_numeric() {
                number = String::new() + &number + &ch.to_string();
                let max_size = (line.len() - 1) as i32;
                if counter == max_size{
                    nums.push(Num{
                            x_min: counter - number.len() as i32 + 1,
                            x_max: counter - 1,
                            y: y_counter.clone(),
                            value: number.parse::<i32>().unwrap()
                        });
                }
            }else{
                if number != "" {
                    nums.push(Num{
                        x_min: counter - number.len() as i32,
                        x_max: counter - 1,
                        y: y_counter.clone(),
                        value: number.parse::<i32>().unwrap()
                    });
                    number = String::new();
                }
                if ch != '.' {
                    symbols.push(Point{
                        x: counter,
                        y: y_counter.clone(),
                        symbol: ch
                    });
                }
            }
            counter += 1;
        }
        y_counter += 1;
    }

    (nums, symbols)
}

fn sum_nums_adjacent_to_symbol(nums: Vec<Num>, symbols: Vec<Point>) -> i32 {
    let mut sum = 0;
    for number in &nums{
        for symbol in &symbols{
            if symbol.y > number.y + 1 || symbol.y < number.y - 1 {
                continue;
            }
            if symbol.y == number.y{
                if symbol.x == number.x_min-1 || symbol.x == number.x_max+1{
                    sum += number.value;
                    println!("is_adjacent: {:?}, {:?}", number, symbol);
                    continue;
                } 
            }else{
                if symbol.y == number.y + 1 || symbol.y == number.y - 1{
                    if symbol.x >= number.x_min - 1 && symbol.x <= number.x_max + 1{
                        sum += number.value;
                        continue;
                    }
                }
            }
        }
    }

    sum
}

#[derive(Debug, Clone)]
struct Point{
    x: i32,
    y: i32,
    symbol: char
}

#[derive(Debug, Clone)]
struct Num{
    x_min: i32,
    x_max: i32,
    y: i32,
    value: i32
}

impl ToString for Num{
    fn to_string(&self) -> String{
        format!("value: {}, x: {}, y: {}", self.value, self.x_min, self.y)
    }
}

impl ToString for Point{
    fn to_string(&self) -> String{
        format!("symbol: {}, x: {}, y: {}", self.symbol, self.x, self.y)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_points(){
        let inp = vec!["..511.............*.."];
        let (nums, syms) = parse_lines_to_nums_and_symbols(inp);
        assert_eq!(format!("{} | {}",nums.get(0).unwrap().to_string(), syms.get(0).unwrap().to_string()), "value: 511, x: 2, y: 0 | symbol: *, x: 18, y: 0");
    }

    #[test]
    fn test_parse_points_end_num(){
        let inp = vec!["..511.............*..611"];
        let (nums, syms) = parse_lines_to_nums_and_symbols(inp);
        assert_eq!(format!("{} | {}",nums.get(1).unwrap().to_string(), syms.get(0).unwrap().to_string()), "value: 611, x: 21, y: 0 | symbol: *, x: 18, y: 0");
    }
}