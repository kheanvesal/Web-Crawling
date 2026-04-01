For the small project Guideline:

A minimal, real-time web search CLI that searches the internet for you. Enter a query and get search results as JSON (title, url, published_date), sorted by recency.

<img width="2012" height="1390" alt="image" src="https://github.com/user-attachments/assets/ea19d81c-df6a-467c-8e94-4a778c841aa4" />

Setup

Prerequisites: Python 3.12+ and uv installation

# Clone the repository

git clone https://github.com

# Navigate into the project root:

cd chapter-3-small-project

# How to Run

# From the repo root, run:
First type command => pip install uv, uv sync, then uv run chapter3-small-project

When prompted, enter your search (e.g., "Apple latest earnings").
Results print as JSON. Enter another query to continue.
Quit with q, quit, exit, or press Ctrl+C.

# Features

We currently have two features:

+ Search (see /src/search)
+ Parse (see /src/parse)


=> Search
Given a query (e.g. "Apple latest earnings"), search the internet for pages related to the query.

=> Parse
Given a URL, parse and extract the text content from the URL.
