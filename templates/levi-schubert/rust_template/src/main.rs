use std::fs;
use std::error::Error;
use std::time::SystemTime;

fn main() -> Result<(), Box<dyn Error>>{
    let start_time = SystemTime::now();
    let mut answer = "";
    let input: String = fs::read_to_string("input/input.txt")?.parse()?;
    println!("{}", input);


    let end_time = SystemTime::now();
    let time_taken = end_time.duration_since(start_time).expect("Clock may have gone backwards");
    println!("answer: {} \ntime taken: {:?}", answer, time_taken);
    Ok(())
}
