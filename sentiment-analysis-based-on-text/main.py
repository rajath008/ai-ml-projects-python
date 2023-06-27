from textblob import TextBlob
from newspaper import Article


choice=int(input("Enter your choice \n1.Use text from an article\n2.Read text from user\n3.Read text from a file\n"))

if choice==1:

    url="https://en.wikipedia.org/wiki/Mathematics"
    article=Article(url)

    article.download()
    article.parse()
    article.nlp()

    #install punkt for this section of the code to work
    text=article.summary
    print(text)
    blob=TextBlob(text)
    sentiment=blob.sentiment.polarity # -1 to 1
    print(text)
    print(sentiment)
    if sentiment>= -1 and sentiment< -0.5:
        print("Very Negative")
    elif sentiment>= -0.5 and sentiment< 0:
        print("Negative")
    elif sentiment>= 0 and sentiment< 0.5:
        print("Positive")
    else:
        print("Very Positive")




elif choice==2:
    text= input("Enter the text : \n")
    blob=TextBlob(text)
    sentiment=blob.sentiment.polarity # -1 to 1
    print(text)
    print(sentiment)
    if sentiment>= -1 and sentiment< -0.5:
        print("Very Negative")
    elif sentiment>= -0.5 and sentiment< 0:
        print("Negative")
    elif sentiment>= 0 and sentiment< 0.5:
        print("Positive")
    else:
        print("Very Positive")

elif choice==3:
    f=open('text.txt','r')
    text=f.read()
    print(text)
    blob=TextBlob(text)
    sentiment=blob.sentiment.polarity # -1 to 1
    print(text)
    print(sentiment)
    if sentiment>= -1 and sentiment< -0.5:
        print("Very Negative")
    elif sentiment>= -0.5 and sentiment< 0:
        print("Negative")
    elif sentiment>= 0 and sentiment< 0.5:
        print("Positive")
    else:
        print("Very Positive")


