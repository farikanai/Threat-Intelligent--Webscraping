from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd

# Load the data
data = pd.read_csv('processed_results.csv')

# Combine all descriptions into one text
text = ' '.join(description for description in data.Description)

# Create a WordCloud object
wordcloud = WordCloud(background_color='white').generate(text)

# Display the generated image
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
