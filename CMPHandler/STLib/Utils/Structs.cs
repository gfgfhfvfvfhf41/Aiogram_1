using SQLite;
using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Threading.Tasks;
using STLib.Utils;

namespace STLib.Utils
{
	/// <summary>
	/// Структура вопросов в материале
	/// </summary>
	public struct LContentMaterial
	{
		/// <summary>
		/// Вопрос на который будет дан ответ пользователем
		/// </summary>
		public string answer { get; set; }
		/// <summary>
		/// Предлагаемый выбор ответов
		/// </summary>
		public string[] questions { get; set; }
	}

	/// <summary>
	/// Подготовленный материал для обучения пользователя
	/// </summary>
	public class LMaterial
	{
		/// <summary>
		/// Загаловок материала
		/// </summary>
		public string title {get; set; }
		/// <summary>
		/// Контент задания
		/// </summary>
		public List<LContentMaterial> content { get; set; }
	}
}