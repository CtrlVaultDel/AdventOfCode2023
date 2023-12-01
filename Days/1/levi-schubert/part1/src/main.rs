use std::fs;
use std::error::Error;


fn main() -> Result<(), Box<dyn Error>>{
    let input: String = fs::read_to_string("input/input.txt")?.parse()?;
    let lines: Vec<&str> = input.split("\r\n").collect();
    let mut sum = 0;

    let mut line_count = 1;

    for line in &lines {
        let mut num_index1 = 0;
        let mut num_one_set = false;
        let mut num_index2 = 0;
        let mut num_two_set = false;
        let mut count = 0;
        for c in line.chars(){
            if c.is_numeric() {
                if !num_one_set {
                    num_index1 = count;
                    num_one_set = true;
                }else{
                    num_index2 = count;
                    num_two_set = true;
                }
            }
            count += 1;
        }
        if !num_two_set{
            num_index2 = num_index1
        }
        let num = line.chars().nth(num_index1).unwrap().to_string() + &line.chars().nth(num_index2).unwrap().to_string();
        println!("line: {}, num: {:?}", line_count, num);
        sum += num.parse::<usize>().unwrap();
        line_count += 1;
    }

    println!("{}", sum);
    Ok(())
}


