public class Program
{
    private static void Main(string[] args)
    {
        Console.WriteLine("Advent of Code 2023 - Day 1");
        using (StreamReader file = new StreamReader("input/Input.txt"))
        {
            string? line;
            int sum = 0;
            List<string> answers = new List<string>();
            List<int> finalList = new List<int>();

            while ((line = file.ReadLine()) != null)
            {
                List<int> numList = new List<int>();
                Console.WriteLine(line);
                foreach (char c in line)
                {
                    int number;
                    if (int.TryParse(c.ToString(), out number))
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
                if (numList.Count <= 1)
                {
                    string digit = numList[0].ToString();
                    answers.Add(digit + digit);
                    Console.WriteLine(digit + digit);
                }
            }
            finalList = answers.Select(int.Parse).ToList();
            sum = finalList.Sum();
            Console.WriteLine("Total Sum:{0}", sum);
        };
    }
}