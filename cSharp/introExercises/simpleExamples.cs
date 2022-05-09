using System;
using System.IO;
using System.Text;

namespace cSharpFunctionality
{
    class cSharpFunctionality
    {
        static void Main(string[] args)
        {
            //compOps();
            //booleanValues();
            // variableTypes();
            // convertInput();
            // stringConcat();
            // conditionalLogic();
            usingSwitch();
        }

        private static void compOps()
        {
            double timeToDinner = 4;
            double distance = 95;
            double rate = 30;
            double tripDuration = distance / rate;
            bool answer = tripDuration <= timeToDinner;
            Console.WriteLine(answer);
        }

        private static void booleanValues()
        {
            bool beach = true;
            bool hiking = false;
            bool city = true;
            bool yourNeeds = beach && city;
            bool friendNeeds = beach || hiking;
            bool tripDecision = yourNeeds && friendNeeds;
            Console.WriteLine(tripDecision);
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
        private static void conditionalLogic()
        {
            string intro = ("Enter the number of guests you have coming to your party. A game will be recommended based on your input: ");
            Console.Write(intro);
            int guests = Convert.ToInt32(Console.ReadLine());
            if (guests > 6)
            {
                Console.WriteLine("Catan");
            }
            else if (guests >= 3)
            {
                Console.WriteLine("Innovation");
            }
            else
            {
                Console.WriteLine("Solitaire");
            }
        }
        private static void usingSwitch()
        {
            Console.WriteLine("Select a genre: ");
            string genre = Console.ReadLine();
            switch (genre)
            {
                case "Drama":
                    Console.WriteLine("Citizen Kane");
                    break;

                case "Comedy":
                    Console.WriteLine("Duck Soup");
                    break;

                case "Adventure":
                    Console.WriteLine("King Kong");
                    break;

                case "Horror":
                    Console.WriteLine("Psycho");
                    break;

                case "Science Fiction":
                    Console.WriteLine("2001: A Space Odyssey");
                    break;

                default:
                    Console.WriteLine("No movie found");
                    break;
            }
        }
    }
}