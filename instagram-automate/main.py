from instabot import Bot
bot=Bot()

bot.login(username="username",password="password")
bot.follow('username of account to follow')
bot.unfollow('username of account to unfollow')
bot.upload_photo('path to image',aption="caption for the post")
bot.send_message('message to send',['all acoount usernames to send'])
bot.like('username of account to like')

followers_list=bot.get_user_followers('username')
for follower in followers_list:
    print(follower)

following_list=bot.get_user_following('username')
for following in following_list:
    print(following)

