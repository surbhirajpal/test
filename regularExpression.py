import re
#Q1
email=["zuck26@facebook.com","page33@google.com","jeff42@amazon.com"]
ls=[]
for i in email:

    x=re.findall("[\w]+",i)
    x=tuple(x)
    ls.append(x)
print(ls)


#Q2
text = "Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
x=re.findall("[Bb][\w]+",text)
print(x)

#Q3
sentence = "A,very very;irregular_sentence"
x=re.compile("[,;_]")
y=x.sub(" ",sentence)
print(y)

#Q optional
tweet = "Good advice! RT @TheNextWeb:What I would do differently if I was learning to code today http://t.co/lbwej0pxOd cc: @garybernhardt #rstats"
tweet = re.sub('http\S+\s*', '', tweet)
tweet = re.sub('RT|cc', '', tweet)
tweet = re.sub('#\S+', '', tweet)
tweet = re.sub('@\S+', '', tweet)
tweet = re.sub('[%s]' % re.escape(""":!"""), '', tweet)
tweet = re.sub('\s+', ' ', tweet)

print(tweet)
