YouTube Comments Search API# 

This Flask application provides a REST API to search and filter YouTube comments based on various criteria. It's built on top of an existing API that fetches comments from a YouTube video. Users can search comments by author name, date range, like and reply count range, and text content.

Features:
Search comments by author name.
Filter comments within a specific date range.
Filter by the number of likes and replies.
Search for specific text within comment content.
Combine all these search and filter capabilities in a single request.
Setup
Clone the Repository
Install Dependencies

Ensure Python 3.x is installed on your system.
Install required packages:
pip install -r requirements.txt
Running the Application

Navigate to the project directory and run:
python app.py

Usage
After running the application, you can access the API at http://127.0.0.1:5000/.

Example API Endpoints:

Search by author:

http://127.0.0.1:5000/search?search_author=JohnDoe
Search with date range and text:

http://127.0.0.1:5000/search?at_from=01-01-2023&at_to=01-02-2023&search_te
