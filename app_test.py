from flask import Flask, request, render_template
import pandas as pd

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_term = request.form.get('search_term')

        # Load the data from the CSV file
        df = pd.read_csv('link.csv')

        # Search the DataFrame for the user's term
        results = df[df.apply(lambda row: row.astype(str).str.contains(search_term).any(), axis=1)]

        # Convert the results to HTML
        results_html = results.to_html()

        return render_template('results.html', table=results_html)

    return render_template('index_1.html')

if __name__ == '__main__':
    app.run(debug=True)
