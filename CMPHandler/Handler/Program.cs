using System.Text.RegularExpressions;

STLib.Main.Init(@"C:\Users\gfgfhfvfvfhf41\source\repos\MVP\CMPHandler\model.json");
Console.WriteLine(Regex.Replace(Console.ReadLine().ToLower(), @"[^\w\s]", ""));
Console.WriteLine(STLib.Main.GetAnswer(Console.ReadLine()));
