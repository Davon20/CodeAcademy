using System;
using System.IO;
using System.Text;

namespace cSharpFunctionality
{
    class cSharpFunctionality
    {
        static void Main(string[] args)
        {
            // variableTypes();
            // convertInput();
            // stringConcat();
        }

        private static void variableTypes()
        {
            string breed = "Golden Retriever";
            Console.WriteLine(breed);
            int age = 5;
            Console.WriteLine(age);
            double weight = 65.22;
            Console.WriteLine(weight);
            bool spayed = true;
            Console.WriteLine(spayed);
        }
        private static void convertInput()
        {
            Console.Write("Enter your favorite number: ");
            int favNum = Convert.ToInt32(Console.ReadLine());
            Console.Write($"Your favorite number is {favNum}");
            Console.Read();
        }
        private static void stringConcat()
        {
            string beginning = "Today";
            string middle = "I went for a run";
            string end = "It was nice";

            string story = beginning + ", " + middle + ". " + end + ".";

            Console.WriteLine(story);
        }
    }
}