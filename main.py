#Import da biblioteca utilizada
import tweepy

#Informações obtidas na API do Twitter
API_KEY = ''
API_SECRET_KEY = ''
BEARER_TOKEN = ''
ACCESS_TOKEN = ''
ACCESS_TOKEN_SECRET = ''

#Inicialização para facilicar a navegação
client = tweepy.Client(BEARER_TOKEN,API_KEY,API_SECRET_KEY,ACCESS_TOKEN,ACCESS_TOKEN_SECRET)

#Cria um tweet
client.create_tweet(text='Testo do Tweet')

#Deleta um tweet
client.delete_tweet(id='Id do tweet no navegador')   