from textblob import TextBlob
a=TextBlob('I lik to play fotball in my garden and i also play criket')
a=a.correct()
print(a)