import pandas as pd
from flask import Flask, render_template
from utils import get_project_root, get_latest_file

# Get paths
root_dir = get_project_root()
templates_dir = root_dir / 'templates'
csv_file = get_latest_file(root_dir / 'data' / 'cleaned')

app = Flask(__name__, template_folder=str(templates_dir))

@app.route('/')
def display_csv():
    # Read the CSV file
    df = pd.read_csv(csv_file)

    # Convert the dataframe to HTML table
    table_html = df.to_html(classes='table table-striped', index=False)
    return render_template('index.html', table=table_html)

if __name__ == '__main__':
    app.run(debug=True)