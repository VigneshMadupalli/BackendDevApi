from flask import Flask, request, jsonify
import requests
from datetime import datetime

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/search', methods=['GET'])
def search_comments():
    # Extract query parameters
    search_author = request.args.get('search_author', default='')
    at_from = request.args.get('at_from', default='')
    at_to = request.args.get('at_to', default='')
    like_from = request.args.get('like_from', default=0, type=int)
    like_to = request.args.get('like_to', default=0, type=int)
    reply_from = request.args.get('reply_from', default=0, type=int)
    reply_to = request.args.get('reply_to', default=0, type=int)
    search_text = request.args.get('seach_text', default='')

    # Fetch data from the existing API
    response = requests.get('https://app.ylytic.com/ylytic/test')
    data = response.json()

    # Access comments from the nested structure
    comments = data['comments'] if 'comments' in data else []

    # Function to safely parse date
    def safe_parse_date(date_str):
        try:
            return datetime.strptime(date_str, '%a, %d %b %Y %H:%M:%S GMT')
        except ValueError:
            return None

    # Filter comments based on query parameters
    filtered_comments = []
    for comment in comments:
        # Safely parse dates
        comment_date = safe_parse_date(comment['at'])
        from_date = safe_parse_date(at_from)
        to_date = safe_parse_date(at_to)

        # Check each condition
        if search_author and search_author.lower() not in comment['author'].lower():
            continue
        if from_date and (comment_date is None or comment_date < from_date):
            continue
        if to_date and (comment_date is None or comment_date > to_date):
            continue
        if comment['like'] < like_from or comment['like'] > like_to:
            continue
        if comment['reply'] < reply_from or comment['reply'] > reply_to:
            continue
        if search_text and search_text.lower() not in comment['text'].lower():
            continue

        # Add comment to filtered list if all conditions are met
        filtered_comments.append(comment)

    # Return the filtered comments
    return jsonify(filtered_comments)


if __name__ == '__main__':
    app.run(debug=True)
