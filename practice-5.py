from random import randrange

def get_jokes(n):
    joke_list = []
    for joke in range(n):
        joke = ' '.join([nouns[randrange(len(nouns))], adv[randrange(len(adv))], adj[randrange(len(adj))]])
        joke_list.append(joke)
    print(joke_list)

nouns = ["автомобиль", "лес", "огонь", "город", "дом", "кровать", "яблоко"]
adv = ["сегодня", "вчера", "завтра", "позавчера", "ночью", "днём", "послезавтра"]
adj = ["веселый", "яркий", "зеленый", "утопичный", "мягкий", "светлый", "грустный"]

get_jokes(3)
print = (int(2), 'times')