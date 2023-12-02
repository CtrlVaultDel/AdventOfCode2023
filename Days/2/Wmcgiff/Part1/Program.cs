using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;

class Program
{
    static void Main(string[] args)
    {
        string filePath = "./Input/Input.txt";
        var gamesData = ReadGamesFromFile(filePath);

        int sumOfValidGameIds = CalculateSumOfValidGames(gamesData, 12, 13, 14);
        Console.WriteLine($"Sum of valid game IDs: {sumOfValidGameIds}");
    }

    private static List<string> ReadGamesFromFile(string filePath)
    {
        var gamesData = new List<string>();
        try
        {
            using (StreamReader sr = new StreamReader(filePath))
            {
                string line;
                while ((line = sr.ReadLine()) != null)
                {
                    gamesData.Add(line);
                }
            }
        }
        catch (Exception e)
        {
            Console.WriteLine($"Error reading the file: {e.Message}");
        }
        return gamesData;
    }

    private static int CalculateSumOfValidGames(List<string> gamesData, int redCubes, int greenCubes, int blueCubes)
    {
        int sum = 0;
        foreach (var game in gamesData)
        {
            if (IsGameValid(game, redCubes, greenCubes, blueCubes))
            {
                var gameId = int.Parse(Regex.Match(game, @"\d+").Value);
                sum += gameId;
            }
        }
        return sum;
    }

    private static bool IsGameValid(string gameData, int redCubes, int greenCubes, int blueCubes)
    {
        var sets = gameData.Split(';');
        foreach (var set in sets)
        {
            int red = CountCubes(set, "red");
            int green = CountCubes(set, "green");
            int blue = CountCubes(set, "blue");

            if (red > redCubes || green > greenCubes || blue > blueCubes)
                return false;
        }
        return true;
    }

    private static int CountCubes(string set, string color)
    {
        var match = Regex.Match(set, $@"(\d+) {color}");
        return match.Success ? int.Parse(match.Groups[1].Value) : 0;
    }
}
