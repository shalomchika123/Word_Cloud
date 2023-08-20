import wikipediaapi
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Initialize Wikipedia API
wiki_wiki = wikipediaapi.Wikipedia('en')
page = wiki_wiki.page('Data_science')  # Replace with the title of the Wikipedia page you want
article_text = page.text

# Tokenize and clean text
words = word_tokenize(article_text)
words = [word.lower() for word in words if word.isalpha()]
words = [word for word in words if word not in stopwords.words('english')]

# Count word frequencies
word_freq = Counter(words)

# Create and display word cloud
wordcloud = WordCloud(width=800, height=800,
                      background_color='white',
                      min_font_size=10).generate_from_frequencies(word_freq)

plt.figure(figsize=(8, 8), facecolor=None)
plt.imshow(wordcloud)
plt.axis("off")
plt.tight_layout(pad=0)

plt.show()