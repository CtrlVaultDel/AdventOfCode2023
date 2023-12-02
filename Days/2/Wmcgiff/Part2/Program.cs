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

        long totalPower = CalculateTotalPower(gamesData);
        Console.WriteLine($"Total power of the sets: {totalPower}");
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

    private static long CalculateTotalPower(List<string> gamesData)
    {
        long totalPower = 0;
        foreach (var game in gamesData)
        {
            var (minRed, minGreen, minBlue) = CalculateMinimumCubes(game);
            totalPower += (long)minRed * minGreen * minBlue;
        }
        return totalPower;
    }

    private static (int minRed, int minGreen, int minBlue) CalculateMinimumCubes(string gameData)
    {
        int minRed = 0, minGreen = 0, minBlue = 0;
        var sets = gameData.Split(';');
        foreach (var set in sets)
        {
            minRed = Math.Max(minRed, CountCubes(set, "red"));
            minGreen = Math.Max(minGreen, CountCubes(set, "green"));
            minBlue = Math.Max(minBlue, CountCubes(set, "blue"));
        }
        return (minRed, minGreen, minBlue);
    }

    private static int CountCubes(string set, string color)
    {
        var match = Regex.Match(set, $@"(\d+) {color}");
        return match.Success ? int.Parse(match.Groups[1].Value) : 0;
    }
}
