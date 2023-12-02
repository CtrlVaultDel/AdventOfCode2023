use std::fs;
use substring::Substring;
use std::error::Error;
use std::time::SystemTime;

fn main() -> Result<(), Box<dyn Error>>{
    let start_time = SystemTime::now();
    let input: String = fs::read_to_string("input/input.txt")?.parse()?;
    let lines: Vec<&str> = input.split("\r\n").collect();

    let solution = Game{
        id: -1,
        max_red: 12,
        max_green: 13,
        max_blue: 14
    };

    let mut id_sum = 0;

    for line in &lines {
        let game = parse_game(&line);
        id_sum += game_possible(&solution, &game);
    }


    let end_time = SystemTime::now();
    let time_taken = end_time.duration_since(start_time).expect("Clock may have gone backwards");
    println!("answer: {} \ntime taken: {:?}", id_sum, time_taken);
    Ok(())
}

fn _process_line(_line: &str) -> String {
    return "to-do".to_string();
}

fn game_possible(solution: &Game, game: &Game) -> i32{
    if  game.max_red <= solution.max_red &&
        game.max_green <= solution.max_green &&
        game.max_blue <= solution.max_blue {
            return game.id.clone();
    }

    return 0;
}

fn parse_game(line: &str) -> Game {
    let colon_index = line.chars().position(|c| c == ':').unwrap();
    let id = line.substring(5, colon_index).to_string().parse::<i32>().unwrap();



    let reds: Vec<_> = line.match_indices("red").collect();
    let greens: Vec<_> =line.match_indices("green").collect();
    let blues: Vec<_> = line.match_indices("blue").collect();

    let mut red = ColorCount{
        count: 0
    };
    let mut green = ColorCount{
        count: 0
    };
    let mut blue = ColorCount{
        count: 0
    };

    for item in reds{
        let number = line.substring(item.0 - 3, item.0 - 1).trim().to_string().parse::<i32>().unwrap();
        if number > red.count {
            red.count = number.clone();
        }
    }

    for item in greens{
        let number = line.substring(item.0 - 3, item.0 - 1).trim().to_string().parse::<i32>().unwrap();
        if number > green.count {
            green.count = number.clone();
        }
    }

    for item in blues{
        let number = line.substring(item.0 - 3, item.0 - 1).trim().to_string().parse::<i32>().unwrap();
        if number > blue.count {
            blue.count = number.clone();
        }
    }

    Game{
        id: id,
        max_red: red.count,
        max_blue: blue.count,
        max_green: green.count
    }
}

#[derive(Debug, Clone)]
struct ColorCount{
    count: i32
}

#[derive(Debug, Clone)]
struct Game{
    id: i32,
    max_red: i32,
    max_blue: i32,
    max_green: i32
}

impl ToString for Game{
    fn to_string(&self) -> String{
        format!("id: {}, red: {}, green: {}, blue: {}", self.id, self.max_red, self.max_green, self.max_blue)
    }
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn test_one(){
        let result = parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green");
        assert_eq!(result.to_string(), "id: 1, red: 4, green: 2, blue: 6");
    }

    #[test]
    fn test_two(){
        let result = parse_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue");
        assert_eq!(result.to_string(), "id: 2, red: 1, green: 3, blue: 4");
    }

    #[test]
    fn test_three(){
        let result = parse_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red");
        assert_eq!(result.to_string(), "id: 3, red: 20, green: 13, blue: 6");
    }

    #[test]
    fn test_four(){
        let result = parse_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red");
        assert_eq!(result.to_string(), "id: 4, red: 14, green: 3, blue: 15");
    }

    #[test]
    fn test_five(){
        let result = parse_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green");
        assert_eq!(result.to_string(), "id: 5, red: 6, green: 3, blue: 2");
    }

    #[test]
    fn test_six(){
        let solution = Game{
            id: -1,
            max_red: 12,
            max_green: 13,
            max_blue: 14
        };

        let mut games: Vec<Game> = Vec::<Game>::new(); 
        games.push(parse_game("Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green"));
        games.push(parse_game("Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue"));
        games.push(parse_game("Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red"));
        games.push(parse_game("Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red"));
        games.push(parse_game("Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"));

        let mut id_sum = 0;

        for game in games{
            id_sum += game_possible(&solution, &game);
        }

        assert_eq!(id_sum, 8);
    }

    #[test]
    fn test_seven(){
        let result = parse_game("Game 12: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green");
        assert_eq!(result.to_string(), "id: 12, red: 6, green: 3, blue: 2");
    }

    #[test]
    fn test_eight(){
        let result = parse_game("Game 100: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green");
        assert_eq!(result.to_string(), "id: 100, red: 6, green: 3, blue: 2");
    }

}