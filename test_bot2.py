
''' Built using PRAW(Python Reddit API Wrapper)'''

import praw
import wikipedia
#print(wikipedia.summary('Python (programming language)', sentences = 3))
import googlesearch

reddit = praw.Reddit(client_id = 'A7QCBFgdygrtJQ',
                     client_secret = 'cZeaPBgZQLoN3x_yeVJgnV3uhRM',
                     username = 'univ_bot1',
                     password = 'UCI_t3ch!',
                     user_agent='web:test_script2:1.0 (by /u/univ_bot1)')


''' Code for static comment reading '''
'''
subreddit = reddit.subreddit('test')
posts = subreddit.new(limit = 5)

for p in posts:
    p.comments.replace_more(limit=None)
    for comment in p.comments.list():
        if 'wikibot:' in comment.body:
            keyword = comment.body.split(':')[-1]
            print(keyword)
            comment.reply('**Here is a summary of this article:**' +
                          wikipedia.summary(keyword, sentences=3))
            print('Comment posted')
'''


''' Code for live comment responses '''
subreddit = reddit.subreddit('test')
posts = subreddit.new(limit = 10)
'''
for comment in subreddit.stream.comments():
    try:
        print(comment.body)
    except:
        pass
'''
''' if finds keyword 'wikibot' inside the comments, replies with a wiki summary of the word after wikibot
for comment in subreddit.stream.comments():
    if 'wikibot:' in comment.body:
        keyword = comment.body.split(':')[-1]
        print(keyword)
        comment.reply('**Here is a summary of this article: ' + '\n' 
                      + wikipedia.summary(keyword, sentences = 3))
        print('Comment posted')
'''
for comment in subreddit.stream.comments():
    if 'wikipedia.org' in comment.body:
        split_comment = comment.body.split()
        for word in split_comment:
            if 'wikipedia.org' in word:
                link = word
                keyword = link.split('/')[-1]
                try:
                    print(keyword)
                    print(wikipedia.summary(keyword, 3))
                except wikipedia.exceptions.DisambiguationError as e:
                    keyword = e.options[0]
                    print(keyword)
                    print(wikipedia.summary(keyword, 3))
                except:
                    pass
                

