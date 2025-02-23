from flask import Flask, render_template, request
from forms import BlogForm
import re
from pytrends.request import TrendReq
import time
from requests.exceptions import RequestException

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Replace with a secure key in production

def analyze_seo(text):
    """
    Advanced SEO analysis using Google Trends API with stopword filtering and error handling.
    """
    # Calculate word count from full text
    word_count = len(text.split())

    # Define common stopwords to exclude from analysis
    stopwords = set([
        "and", "the", "is", "in", "to", "of", "a", "for", "that", "on", "with",
        "as", "at", "by", "an", "be", "this", "it", "or"
    ])

    # Extract words and filter out stopwords
    all_words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in all_words if word not in stopwords]

    # Calculate frequency of filtered words
    word_freq = {word: filtered_words.count(word) for word in set(filtered_words)}
    sorted_keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    top_keywords = [word for word, freq in sorted_keywords[:5]]

    trends_score = {}
    max_retries = 3
    retry_delay = 2  # seconds

    def fetch_trends(keywords):
        pytrends = TrendReq(hl='en-US', tz=360, timeout=(10,25), 
                           retries=2, backoff_factor=0.1)
        
        # Split keywords into smaller chunks to avoid API limits
        chunk_size = 2
        keyword_chunks = [keywords[i:i + chunk_size] 
                        for i in range(0, len(keywords), chunk_size)]
        
        all_trends = {}
        for chunk in keyword_chunks:
            try:
                pytrends.build_payload(chunk, cat=0, 
                                     timeframe='today 1-m', 
                                     geo='US', gprop='')
                trends_data = pytrends.interest_over_time()
                
                if not trends_data.empty:
                    for keyword in chunk:
                        if keyword in trends_data.columns:
                            # Get average interest over time instead of just last value
                            all_trends[keyword] = int(trends_data[keyword].mean())
                        else:
                            all_trends[keyword] = 0
                
                # Add delay between chunks to avoid rate limiting
                time.sleep(1)
                
            except Exception as e:
                print(f"Error fetching trends for chunk {chunk}: {str(e)}")
                for keyword in chunk:
                    all_trends[keyword] = 0
                
        return all_trends

    # Try to fetch trends with retries
    for attempt in range(max_retries):
        try:
            trends_score = fetch_trends(top_keywords)
            break
        except RequestException as e:
            if attempt == max_retries - 1:
                print(f"Failed to fetch trends after {max_retries} attempts: {str(e)}")
                trends_score = {keyword: 0 for keyword in top_keywords}
            else:
                time.sleep(retry_delay * (attempt + 1))

    # Generate SEO recommendations
    recommendations = []
    if word_count < 300:
        recommendations.append("Your blog post is too short. Aim for at least 300 words.")
    elif word_count < 600:
        recommendations.append("Consider expanding your content to 600+ words for better SEO performance.")
    
    # Check keyword density
    for keyword, freq in sorted_keywords[:5]:
        density = (freq / word_count) * 100
        if density > 3:
            recommendations.append(f"Keyword '{keyword}' appears too frequently ({density:.1f}%). Try reducing it.")
    
    # Check the first line (assuming title) length
    first_line = text.split('\n')[0]
    if len(first_line) > 60:
        recommendations.append("Your title is too long. Try to keep it under 60 characters.")
    elif len(first_line) < 20:
        recommendations.append("Your title might be too short. Consider making it more descriptive.")

    return word_count, sorted_keywords[:5], trends_score, recommendations

@app.route("/", methods=["GET", "POST"])
def index():
    form = BlogForm()
    if form.validate_on_submit():
        text = form.content.data
        word_count, top_keywords, trends_score, recommendations = analyze_seo(text)
        return render_template("result.html", 
                             word_count=word_count, 
                             keywords=top_keywords, 
                             trends=trends_score, 
                             recommendations=recommendations)
    return render_template("index.html", form=form)

if __name__ == "__main__":
    app.run(debug=True)