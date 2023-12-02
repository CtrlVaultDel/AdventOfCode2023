using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;

public class Program
{
    private static void Main(string[] args)
    {
        List<int> results = new List<int>();
        List<int> results2 = new List<int>();
        results = FirstPass();
        results2 = AlternativeWay();
        for (int i = 0; i < 1000; i++)
        {
            if (results[i] != results2[i])
            {
                Console.WriteLine("My results: {0} || Other results: {1} || Index: {2}", results[i], results2[i], i+1);
            }
        }
    }
    public static List<int> FirstPass(){
        Console.WriteLine("Advent of Code 2023 - Day 1");

        using (StreamReader file = new StreamReader("input/input.txt"))
        {
            List<string> valueList = new List<string>();
            string? inputLine;
            int sum = 0;
            List<string> answers = new List<string>();
            List<int> finalList = new List<int>();


            while ((inputLine = file.ReadLine()) != null)
            {
                Console.WriteLine(inputLine);
                string inputString = Conversion(inputLine);
                valueList.Add(inputString);
                Console.WriteLine(inputString);
            }
            foreach (string line in valueList){
                List<int> numList = new List<int>();
                Console.WriteLine(line);
                foreach (char c in line)
                {
                    if (int.TryParse(c.ToString(), out int number))
                    {
                        numList.Add(number);
                    }
                }
                if (numList.Count > 1)
                {
                    string firsDigit = numList[0].ToString();
                    string secondDigit = numList[numList.Count - 1].ToString();
                    answers.Add(firsDigit + secondDigit);
                    Console.WriteLine(firsDigit + secondDigit);
                }
                if (numList.Count == 1)
                {
                    string digit = numList[0].ToString();
                    answers.Add(digit + digit);
                    Console.WriteLine(digit + digit);
                }
            }

            finalList = answers.Select(int.Parse).ToList();
            sum = finalList.Sum();
            Console.WriteLine("Total Sum:{0}", sum);
            return finalList;
        };
    }
    static string Conversion(string input)
    {
        var numberWords = new Dictionary<string, string>
        {
            {"one", "1"},
            {"two", "2"},
            {"three", "3"},
            {"four", "4"},
            {"five", "5"},
            {"six", "6"},
            {"seven", "7"},
            {"eight", "8"},
            {"nine", "9"}
        };

        bool found;
        do
        {
            found = false;
            var firstMatch = numberWords
                .Select(pair => new { Word = pair.Key, Match = Regex.Match(input, pair.Key) })
                .Where(x => x.Match.Success)
                .OrderBy(x => x.Match.Index)
                .FirstOrDefault();
     
            if (firstMatch != null)
            {
                input = input
                    .Remove(firstMatch.Match.Index, firstMatch.Word.Length)
                    .Insert(firstMatch.Match.Index, numberWords[firstMatch.Word]);
                found = true;
            }
        }
        while (found);

        return input;
    }
    public static List<int> AlternativeWay()
    {
        Console.WriteLine("Advent of Code 2023 - Day 1");
        List<int> results = new List<int>();
        string[] numbers = { "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", };
        string[] numbers2 = { "one1one", "two2two", "three3three", "four4four", "five5five", "six6six", "seven7seven", "eight8eight", "nine9nine" };
        string filepath = "input/input.txt";
        StreamReader sr = new StreamReader(filepath);
        int sum = 0;
        while (!sr.EndOfStream)
        {
            string line = sr.ReadLine(); 
            string temp = "";
            Console.WriteLine(line);
            for (int i = 0; i < numbers.Length; i++)
            {
                line = line.Replace(numbers[i], numbers2[i]);
            }
            Console.WriteLine(line);

            char[] lineArray = line.ToCharArray();
            string first = "";
            string last = "";

            foreach (char c in lineArray)
            {
                if (Char.IsDigit(c))
                {
                    first = c.ToString();
                    break;
                }
            }

            char[] lineArrayBackwards = lineArray.Reverse().ToArray();

            foreach (char c in lineArrayBackwards)
            {
                if (Char.IsDigit(c))
                {
                    last = c.ToString();
                    break;
                }
            }

            string total = string.Concat(first, last);
            int rowResult = int.Parse(total);
            results.Add(rowResult);
            sum += rowResult;
        }
        Console.WriteLine(sum);
        return results;
    }
}