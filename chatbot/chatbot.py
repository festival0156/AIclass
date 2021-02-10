print('\nFetching dependencies ...', end = '')
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
import sys

name = '{name}'
l = ['chatterbot.logic.BestMatch', # logic adapters
     'chatterbot.logic.MathematicalEvaluation',]
c = ['chatterbot.corpus.english'] # corpora

print('\rInitialising Bot Engine ...', end = '')
bot = ChatBot(name = name, logic_adapters = l)
print('\rTraining Bot. Please Wait.', end = '')
out = sys.stdout
sys.stdout = open('..\\fuck.txt', 'w')
ctr = ChatterBotCorpusTrainer(bot)
for i in c:
    ctr.train(i)

sys.stdout = out
print('\n[<] ', end = '')
while True:
    i = input()
    if i == '%exit%':
        break
    else:
        print('[>] ' + bot.get_response(i).text + '\n[<] ', end = '')
