from speach import speach
from random import randint, choice
import time

levels = {

    "easy": ["dairy", "mouse", "computer"],

    "medium": ["programming", "algorithm", "developer"],

    "hard": ["neural network", "machine learning", "artificial intelligence"]

}

def play_game (level):
    score = 0
    words = levels.get(level, []) # Выбираем слова в зависимости от уровня сложности

    for i in range(3):
        random_word = choice(words)
        print(f"Произнесите слово {random_word}") 
        recog_word = speach()
        print(recog_word)

    if random_word == recog_word:
        print("Абсолютно верно!") 
        score += 1
    else:
        print(f"Что-то не получилось. Правильное слово: {random_word}")
    time.sleep(2) # Пауза между словами
    print("Игра завершена! Ваш счет: {score}/{len(words)}")
# Выберите уровень сложности

selected_level = input("Bыберите уровень сложности (easy/medium/hard):").lower() 
play_game (selected_level)

