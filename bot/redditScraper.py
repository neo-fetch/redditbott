import telegram
import telebot
import praw
import config
bot_token = '1114772756:AAF55QU6q5dVP2bi81i5HKFilYMPcmZVrXs'
bot_chatID = '@monsterKing_bot'
bot = telebot.TeleBot(bot_token)

reddit = praw.Reddit(client_id='XXXXXXXXXXXXXX', \
                     client_secret='XXXXXXXXXXXXXXXXXXXXXXXX', \
                     user_agent='your_bot_name', \
                     username='your_reddit_username', \
                     password='XXXXXXXXXXXXXX')

def reddit_scraper(submission):
    news_data = []
    subreddit = reddit.subreddit('r/coronavirus')
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

subreddit = reddit.subreddit('r/coronavirus')
new_subreddit = subreddit.new(limit=500)
for submission in subreddit.new(limit=1):
    news_data = reddit_scraper(submission)
    if len(news_data) > 0:
        msg = get_msg(news_data)
        status = bot.send_message(chat_id='@monsterKing_bot', text=msg, parse_mode=telegram.ParseMode.HTML)        
        if status:            
            print(status)
else:
    print('No updates.')
