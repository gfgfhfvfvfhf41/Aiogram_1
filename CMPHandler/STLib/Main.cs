using STLib.Utils;
using System;
using System.Threading.Tasks;
using SQLite;
using System.Reflection;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;

namespace STLib
{
    public static class Main
    {
        private static LMaterial _material = new LMaterial();

        /// <summary>
        /// Инициализация системы
        /// </summary>
        public static void Init(string PathToModel)
        {
            InstallResolveHandler();

            if (!File.Exists(PathToModel))
                throw new Exception("Path to model not found :(");

            _material = File.ReadAllText(PathToModel).FromJson<LMaterial>();
        }

        public static string GetAnswer(string[] question)
        {
            var highCorrectAnswer = new List<LContentMaterial>();

            var words = question.Select(word => word.ToLower()).ToArray();//Regex.Replace(question.ToLower(), @"[^\w\s]", "").Split(' ');
                                                                          //стоимость обучения
            foreach (var word in words)
            {
                while (true)
                {
                    var content = Find(word, highCorrectAnswer.ToArray());
                    if (!content.Equals(default(LContentMaterial)))
                        highCorrectAnswer.Add(content);
                    else
                        break;
                }
            }

            var (correctAnswer, count) = (default(LContentMaterial), 0);

            foreach (var answer in highCorrectAnswer)
            {
                var _count = words.Sum(word =>
                    answer.questions.Count(answerQuestion => answerQuestion.ToLower().Contains(word.ToLower())));

                if (count > _count)
                    continue;

                count = _count;
                correctAnswer = answer;
            }

            return correctAnswer.answer;
        }

        private static LContentMaterial Find(string word, LContentMaterial[] without)
        {
            foreach (var content in _material.content.Where(content => !without.Contains(content)).Where(content => content.questions.Any(question => question.ToLower().Contains(word))))
                return content;

            return default(LContentMaterial);
        }

        public static void InstallResolveHandler()
        {
            AppDomain.CurrentDomain.AssemblyResolve += ResolveHandler;
            AppDomain.CurrentDomain.ReflectionOnlyAssemblyResolve +=
                ResolveHandler;
        }

        public static void RemoveResolveHandler()
        {
            AppDomain.CurrentDomain.AssemblyResolve -= ResolveHandler;
            AppDomain.CurrentDomain.ReflectionOnlyAssemblyResolve -=
                ResolveHandler;
        }

        static IDictionary<string, Assembly> _cache =
            new Dictionary<string, Assembly>();

        private static Assembly ResolveHandler(
            object sender, ResolveEventArgs args)
        {
            var name = new AssemblyName(args.Name).Name;
            Assembly result = null;

            if (!_cache.TryGetValue(name, out result))
            {
                var current = Assembly.GetAssembly(typeof(Main));
                var path = Path.GetDirectoryName(current.Location);
                var dllPath = Path.Combine(path, name + ".dll");

                if (File.Exists(dllPath))
                {
                    result = Assembly.LoadFrom(dllPath);
                }

                _cache[name] = result;
            }

            return result;
        }
    }
}