use std::fs;
use std::error::Error;


fn main() -> Result<(), Box<dyn Error>>{
    let input: String = fs::read_to_string("input/input.txt")?.parse()?;
    println!("{}", input);
    Ok(())
}
