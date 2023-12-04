use std::fs;
use std::error::Error;
use std::time::SystemTime;
use substring::Substring;
use std::collections::VecDeque;

fn main() -> Result<(), Box<dyn Error>>{
    let start_time = SystemTime::now();
    let mut total_cards = 0;
    let input: String = fs::read_to_string("input/input.txt")?.parse()?;
    let lines: Vec<&str> = input.split("\r\n").collect();

    let mut extra_cards = ExtraCards{
        extras: VecDeque::<i32>::new()
    };

    for line in &lines{
            let matches = process_card_from_str(line);
            let mut extra = 0;
            if let Some(next) = extra_cards.get_next_extra_cards(){
                extra += next;
            }
            total_cards += extra + 1;
            extra_cards.add_extra_cards(matches, extra);
        }

    let end_time = SystemTime::now();
    let time_taken = end_time.duration_since(start_time).expect("Clock may have gone backwards");
    println!("answer: {} \ntime taken: {:?}", total_cards, time_taken);
    Ok(())
}

fn process_card_from_str(line: &str) -> i32 {
    parse_card(line).matches()

}

fn parse_card(line: &str) -> Card {
    //remove double spaces on pass in
    let local_line = &line.replace("  ", " ");

    //get card id
    let colon_index = local_line.chars().position(|c| c == ':').unwrap();
    let game_id = local_line.substring(4, colon_index).trim().parse::<i32>().unwrap();
    
    //get winning numbers
    let pipe_index = local_line.chars().position(|c| c == '|').unwrap();
    let winning_numbers: Vec<i32> = local_line.substring(colon_index + 2, pipe_index -1).split(" ").collect::<Vec<_>>().iter().map(|i| i.trim().parse::<i32>().unwrap()).collect();
    
    //get scoring numbers
    let scoring_numbers: Vec<i32> = local_line.substring(pipe_index + 2, local_line.len()).split(" ").collect::<Vec<_>>().iter().map(|i| i.trim().parse::<i32>().unwrap()).collect();

    //create and return card
    Card{
        id: game_id,
        winning_numbers: winning_numbers.clone(),
        scoring_numbers: scoring_numbers.clone()
    }
}

#[derive(Debug, Clone)]
struct Card{
    id: i32,
    winning_numbers: Vec<i32>,
    scoring_numbers: Vec<i32>
}

impl Card{
    fn matches(&self) -> i32{
        let matches: Vec<_> = self.scoring_numbers.iter().filter(|sn| {self.winning_numbers.contains(sn)}).collect();
        if matches.len() == 0 {
            0
        }else{
            matches.len() as i32
        }
    }

    fn to_string(&self) -> String{
        return format!("id: {}, winning_numbers: {:?}, scoring_numbers: {:?}", self.id, self.winning_numbers, self.scoring_numbers)
    }
}

#[derive(Debug, Clone, Default)]
struct ExtraCards{
    extras: VecDeque<i32>
}

impl ExtraCards{
    fn add_extra_cards(&mut self, card_matches: i32, current_extra: i32){
        let additional = current_extra + 1;
        for i in 0..card_matches{
            if self.extras.len() > i as usize {
                self.extras[i as usize] += additional;
            }else{
                self.extras.push_back(additional);
            }
        }
    }

    fn get_next_extra_cards(&mut self) -> Option<i32>{
        self.extras.pop_front()
    }
}


#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_parse_card_one(){
        let result = parse_card("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53");
        assert_eq!(result.to_string(), "id: 1, winning_numbers: [41, 48, 83, 86, 17], scoring_numbers: [83, 86, 6, 31, 17, 9, 48, 53]");
    }

    #[test]
    fn test_parse_card_two(){
        let result = parse_card("Card 20: 41 48 83 86 17 | 83 86 6 31 22 9 48 53");
        assert_eq!(result.to_string(), "id: 20, winning_numbers: [41, 48, 83, 86, 17], scoring_numbers: [83, 86, 6, 31, 22, 9, 48, 53]");
    }

    #[test]
    fn test_card_one(){
        let result = process_card_from_str("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53");
        assert_eq!(result, 4);
    }

    #[test]
    fn test_card_two(){
        let result = process_card_from_str("Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19");
        assert_eq!(result, 2);
    }

    #[test]
    fn test_card_three(){
        let result = process_card_from_str("Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1");
        assert_eq!(result, 2);
    }

    #[test]
    fn test_card_four(){
        let result = process_card_from_str("Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83");
        assert_eq!(result, 1);
    }

    #[test]
    fn test_card_five(){
        let result = process_card_from_str("Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36");
        assert_eq!(result, 0);
    }

    #[test]
    fn test_card_six(){
        let result = process_card_from_str("Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11");
        assert_eq!(result, 0);
    }

    #[test]
    fn test_extra_cards(){
        let input = "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53\r\nCard 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19\r\nCard 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1\r\nCard 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83\r\nCard 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36\r\nCard 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11";
        let lines: Vec<&str> = input.split("\r\n").collect();
        let mut result = 0;

        let mut extra_cards = ExtraCards{
            extras: VecDeque::<i32>::new()
        };

        for line in &lines{
            let matches = process_card_from_str(line);
            let mut extra = 0;
            if let Some(next) = extra_cards.get_next_extra_cards(){
                extra += next;
            }
            result += extra + 1;
            extra_cards.add_extra_cards(matches, extra);
        }

        assert_eq!(result, 30);
    }
} 