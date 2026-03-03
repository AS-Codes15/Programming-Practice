from textblob import TextBlob

text = input("Enter a sentence or paragraph: ")

# Create analysis object
blob = TextBlob(text)

# Polarity ranges from -1 (negative) to +1 (positive)
# Subjectivity ranges from 0 (fact) to 1 (opinion)
print("Polarity:", blob.sentiment.polarity)
print("Subjectivity:", blob.sentiment.subjectivity)

# Basic interpretation
if blob.sentiment.polarity > 0:
    print("Sentiment: Positive")
elif blob.sentiment.polarity < 0:
    print("Sentiment: Negative")
else:
    print("Sentiment: Neutral")
