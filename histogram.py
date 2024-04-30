import pandas as pd
import matplotlib.pyplot as plt

# Load the data
data = pd.read_csv('processed_results.csv')

# Plot a histogram of the 'Sentiment' column
plt.hist(data['Sentiment'], bins=10, edgecolor='black')

# Add title and labels
plt.title('Sentiment Analysis')
plt.xlabel('Sentiment')
plt.ylabel('Count')

# Show the plot
plt.show()
