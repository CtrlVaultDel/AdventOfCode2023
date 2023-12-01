use std::cmp::Ordering;
use std::fs;
use std::error::Error;


fn main() -> Result<(), Box<dyn Error>>{
    let input: String = fs::read_to_string("input/input.txt")?.parse()?;
    let lines: Vec<&str> = input.split("\r\n").collect();
    let mut sum = 0;

    let mut line_count = 1;

    for line in &lines {
        let _num_index1 = 0;
        let _num_one_set = false;
        let _num_index2 = 0;
        let _num_two_set = false;
        let mut count = 0;
        let mut nums = get_word_nums(line);
        println!("{:?}", line);
        for c in line.chars(){
            if c.is_numeric() {
                let num_index = NumIndex{
                    num: c.to_string(),
                    index: count
                };
                nums.push(num_index);
            }
            count += 1;
        }
        nums.sort_by(|one, two| one.cmp(two));
        let letter1 = nums[0].num.to_string();
        let letter2 = nums[nums.len()-1].num.to_string();
        println!("nums: {:?}", nums);

        let num = letter1.to_string() + &letter2.to_string();
        println!("line: {}, num: {:?}", line_count, num);
        sum += num.parse::<usize>().unwrap();
        line_count += 1;
    }

    println!("sum: {}", sum);
    Ok(())
}

#[derive(Debug, Eq, Clone)]
struct NumIndex{
    num: String,
    index: usize,
}

impl Ord for NumIndex{
    fn cmp(&self, other: &Self) -> Ordering {
        self.index.cmp(&other.index)
    }
}

impl PartialOrd for NumIndex{
    fn partial_cmp(&self, other: &Self) -> Option<Ordering>{
        Some(self.cmp(other))
    }
}

impl PartialEq for NumIndex{
    fn eq(&self, other: &Self) -> bool {
        self.index == other.index
    }
}


fn get_word_nums(line: &str) -> Vec<NumIndex>{
    let mut nums = Vec::<NumIndex>::new();
    let mut contains_index: Vec<_> = line.match_indices("one").collect();
    if contains_index != [] {
        for item in contains_index{
            let one_num_index = NumIndex{
                num: "1".to_string(),
                index: item.0 
            };
            nums.push(one_num_index);
        }
    }
    contains_index = line.match_indices("two").collect();
    if contains_index != [] {
        for item in contains_index{
            let num_index = NumIndex{
                num: "2".to_string(),
                index: item.0 
            };
            nums.push(num_index);
        }
    }
    contains_index = line.match_indices("three").collect();
    if contains_index != [] {
        for item in contains_index{
            let num_index = NumIndex{
                num: "3".to_string(),
                index: item.0 
            };
            nums.push(num_index);
        }
    }
    contains_index = line.match_indices("four").collect();
    if contains_index != [] {
        for item in contains_index{
            let num_index = NumIndex{
                num: "4".to_string(),
                index: item.0 
            };
            nums.push(num_index);
        }
    }
    contains_index = line.match_indices("five").collect();
    if contains_index != [] {
        for item in contains_index{
            let num_index = NumIndex{
                num: "5".to_string(),
                index: item.0 
            };
            nums.push(num_index);
        }
    }
    contains_index = line.match_indices("six").collect();
    if contains_index != [] {
        for item in contains_index{
            let num_index = NumIndex{
                num: "6".to_string(),
                index: item.0 
            };
            nums.push(num_index);
        }
    }
    contains_index = line.match_indices("seven").collect();
    if contains_index != [] {
        for item in contains_index{
            let num_index = NumIndex{
                num: "7".to_string(),
                index: item.0 
            };
            nums.push(num_index);
        }
    }
    contains_index = line.match_indices("eight").collect();
    if contains_index != [] {
        for item in contains_index{
            let num_index = NumIndex{
                num: "8".to_string(),
                index: item.0 
            };
            nums.push(num_index);
        }
    }
    contains_index = line.match_indices("nine").collect();
    if contains_index != [] {
        for item in contains_index{
            let num_index = NumIndex{
                num: "9".to_string(),
                index: item.0 
            };
            nums.push(num_index);
        }
    }

    return nums;
}

