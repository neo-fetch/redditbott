from telegram.ext import Updater, CommandHandler
import requests
import re
import praw
import telegram
api = ""
contents = requests.get('https://random.dog/woof.json').json()
image_url = contents['url']


reddit = praw.Reddit(client_id='x', \
                     client_secret='x', \
                     user_agent='x', \
                     username='x', \
                     password='x')


def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def reddit_scraper(submission):
    news_data = []
    subreddit = reddit.subreddit('india')
  #  new_subreddit = subreddit.new(limit=500)
    for submission in subreddit.new(limit=10):
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

def cov(bot, update):
    chat_id = update.message.chat_id
    subreddit = reddit.subreddit('india')
 #   new_subreddit = subreddit.new(limit=500)
    for submission in subreddit.new(limit=1):
        news_data = reddit_scraper(submission)
        if len(news_data) > 0:
            msg = get_msg(news_data)
            status = bot.send_message(chat_id= chat_id, text=msg, parse_mode=telegram.ParseMode.HTML)        
            if status:            
                print(status)
            else:
                print('No updates.')



def bop(bot, update):
    url = get_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def main():
    updater = Updater(api)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bop',bop))
    dp.add_handler(CommandHandler('cov',cov))
    updater.start_polling()
    updater.idle()
    
if __name__ == '__main__':
    main()





