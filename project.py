from simple_blogger import Journalist
from simple_blogger.generators.OpenAIGenerator import OpenAITextGenerator
from datetime import datetime

class Project(Journalist):
    def __init__(self, **kwargs):
        super().__init__(            
            review_chat_id=-1002374309134,
            first_post_date=datetime(2025, 3, 4),
            text_generator=OpenAITextGenerator(),
            **kwargs)

    def _task_converter(self, item):
        return { 
                "topic": f"{item['topic']}",
                "category": f"{item['category']}",
                "topic_image": f"Нарисуй картинку, вдохновлённую темой '{item['topic']}' из области '{item['category']}'",
                "topic_prompt": f"Выбери рандомно актуальную проблему по теме '{item['topic']}' из области '{item['category']}', опиши проблему, выбери рандомно метод решения, опиши метод решения, используй смайлики, используй менее {self.topic_word_limit} слов",
            }
    
    def _system_prompt(self, task):
        return "Ты - проектный менеджер, лидер проекта со 100% харизмой, всегда оптимистично настроенный и с отличным чувством юмора"
    
   