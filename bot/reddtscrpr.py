import telegram
import telebot
import praw
import config
bot_token = 'x'
bot_chatID = 'x'
bot = telebot.TeleBot(bot_token)
bot.config['api_key'] = bot_token
reddit = praw.Reddit(client_id='x', \
                     client_secret='x', \
                     user_agent='x', \
                     username='x ', \
                     password='x')

def reddit_scraper(submission):
    news_data = []
    subreddit = reddit.subreddit('Coronavirus')
    new_subreddit = subreddit.new(limit=500)
    for submission in subreddit.new(limit=5):
        data = {}
        data['title'] = submission.title
        data['link'] = submission.url
        news_data.append(data)
    return news_data

def get_msg(news_data):
    msg = '\n\n\n'
    for news_item in news_data:
        title = news_item['title']
        link = news_item['link']
        msg += title+'\n[<a href="'+link+'">Read the full article --></a>]'
        msg += '\n\n'

    return msg

subreddit = reddit.subreddit('Coronavirus')
new_subreddit = subreddit.new(limit=500)
for submission in subreddit.new(limit=1):
    news_data = reddit_scraper(submission)
    if len(news_data) > 0:
        msg = get_msg(news_data)
        status = bot.send_message(chat_id='@monsterKing_bot', text=msg)        
        if status:            
            print(status)
else:
    print('No updates.')
