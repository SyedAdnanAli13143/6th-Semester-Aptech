# Lecture 2: Social Media Analytics — What Are People Saying About Your Brand?

## What Will We Do Today?

You work for **"TechGadget"**, a company that sells phones, laptops, and headphones. The marketing team wants answers:

1. Are customers happy or angry? (Sentiment Analysis)
2. What do people complain about the most? (Topic Detection)
3. Which product gets the best reviews? (Product Comparison)
4. Can we see the big picture at a glance? (Word Clouds & Dashboard)

We will analyze **real-style customer reviews** using Python. Everything is **free**, no signups needed.

---

## Step 0: Setup (Run Once)

```
pip install pandas numpy matplotlib seaborn textblob nltk wordcloud plotly
```

Then run this once in Python:

```python
import nltk
nltk.download('vader_lexicon')   # Sentiment dictionary
nltk.download('punkt')           # Word splitter
nltk.download('punkt_tab')       # Updated word splitter data
nltk.download('stopwords')       # Common words list ("the", "is", "a")
nltk.download('wordnet')         # Word dictionary for lemmatization
```

---

## Step 1: Create Realistic Customer Review Data

In real life, this data would come from Reddit, Amazon reviews, or app store reviews.
We create it here so **everyone can run the code immediately**.

```python
# -------------------------------------------------------
# STEP 1: CREATE 500 REALISTIC CUSTOMER REVIEWS
# These simulate real reviews for TechGadget's 3 products
# -------------------------------------------------------

import pandas as pd
import numpy as np
from datetime import datetime, timedelta

np.random.seed(42)

# --- Define realistic review templates ---
# Positive reviews (customers are happy)
positive_reviews = [
    "Absolutely love this {product}! Best purchase I've made this year.",
    "The {product} exceeded my expectations. Amazing quality for the price.",
    "Five stars! The {product} is fast, reliable, and looks great.",
    "Super happy with my new {product}. Battery life is incredible!",
    "Great value for money. The {product} works perfectly right out of the box.",
    "The {product} has amazing sound quality. Highly recommend to everyone!",
    "Best {product} I've ever owned. The screen is beautiful and sharp.",
    "Impressed by the build quality of this {product}. Feels premium.",
    "My whole family loves the {product}. Easy to use and very intuitive.",
    "The {product} arrived quickly and works flawlessly. Very satisfied!",
    "Outstanding performance from this {product}. No lag at all.",
    "I've tried many brands but this {product} is by far the best one.",
]

# Negative reviews (customers are unhappy)
negative_reviews = [
    "Terrible {product}. Broke after just 2 weeks of use. Very disappointed.",
    "The {product} overheats constantly. Worst purchase I've made.",
    "Do NOT buy this {product}. The quality is awful and customer service is rude.",
    "Extremely slow {product}. Takes forever to load anything. Want my money back.",
    "The {product} battery dies within 3 hours. Completely useless.",
    "Cheap materials on this {product}. Feels like it will break any moment.",
    "Returned the {product} immediately. The screen had dead pixels.",
    "The {product} stopped working after one month. No warranty support either.",
    "Wasted my money on this {product}. The camera quality is horrible.",
    "Buggy software on this {product}. Crashes every hour. So frustrating!",
]

# Neutral reviews (mixed feelings)
neutral_reviews = [
    "The {product} is okay. Nothing special but gets the job done.",
    "Average {product}. Some features are good, others need improvement.",
    "It's a decent {product} for the price. Not the best, not the worst.",
    "The {product} works fine for basic use. Don't expect anything fancy.",
    "Mixed feelings about this {product}. Camera is good but battery is mediocre.",
    "The {product} is alright. Looks nice but performance could be better.",
]

# --- Generate 500 reviews ---
products = ['SmartPhone X1', 'Laptop Pro 15', 'Headphones Z3']

# Set probabilities: 45% positive, 30% negative, 25% neutral
review_types = ['positive'] * 45 + ['negative'] * 30 + ['neutral'] * 25

rows = []
for i in range(500):
    # Pick a random product
    product = np.random.choice(products)
    
    # Pick a random review type
    review_type = np.random.choice(review_types)
    
    # Pick a random review template and fill in the product name
    if review_type == 'positive':
        text = np.random.choice(positive_reviews).format(product=product)
        stars = np.random.choice([4, 5])          # Happy customers give 4-5 stars
    elif review_type == 'negative':
        text = np.random.choice(negative_reviews).format(product=product)
        stars = np.random.choice([1, 2])          # Angry customers give 1-2 stars
    else:
        text = np.random.choice(neutral_reviews).format(product=product)
        stars = 3                                  # Neutral = 3 stars
    
    # Random date in the last 90 days
    days_ago = np.random.randint(0, 90)
    review_date = datetime(2026, 1, 1) + timedelta(days=90 - days_ago)
    
    rows.append({
        'review_id': i + 1,
        'product': product,
        'review_text': text,
        'star_rating': stars,
        'date': review_date,
        'helpful_votes': np.random.randint(0, 50)  # How many people found this review useful
    })

df = pd.DataFrame(rows)

# Show sample data
print("=== TechGadget Customer Reviews (First 10) ===\n")
print(df[['product', 'star_rating', 'review_text']].head(10).to_string(index=False))
print(f"\nTotal reviews: {len(df)}")
print(f"\nReviews per product:")
print(df['product'].value_counts().to_string())
```

---

## Step 2: Sentiment Analysis — Are Customers Happy or Angry?

```python
# -------------------------------------------------------
# STEP 2: DETECT SENTIMENT IN EVERY REVIEW
# We use VADER — a free tool designed for social media text
# It can understand things like "AMAZING!!!" (very positive)
# and "worst. ever." (very negative)
# -------------------------------------------------------

from nltk.sentiment import SentimentIntensityAnalyzer

# Create the sentiment analyzer (it uses a built-in dictionary of 7,500+ words)
sia = SentimentIntensityAnalyzer()

# --- Let's first understand how VADER works with simple examples ---
print("=== How Sentiment Analysis Works ===\n")

demo_sentences = [
    "I love this phone!",
    "This is the worst product ever.",
    "It's okay, nothing special.",
    "AMAZING quality!!! So happy!!!",
    "Terrible. Just terrible. Never again."
]

for sentence in demo_sentences:
    # polarity_scores returns 4 numbers:
    # 'pos': how positive (0 to 1)
    # 'neg': how negative (0 to 1)
    # 'neu': how neutral (0 to 1)
    # 'compound': overall score (-1 = very bad, +1 = very good)
    scores = sia.polarity_scores(sentence)
    compound = scores['compound']
    
    # Simple classification based on compound score
    if compound >= 0.05:
        label = "POSITIVE"
    elif compound <= -0.05:
        label = "NEGATIVE"
    else:
        label = "NEUTRAL"
    
    print(f'  "{sentence}"')
    print(f'    Score: {compound:+.3f}  →  {label}\n')

# --- Now apply sentiment analysis to ALL 500 reviews ---
print("Analyzing all 500 reviews...")

def get_sentiment(text):
    """Analyze one review and return the compound score."""
    scores = sia.polarity_scores(text)
    return scores['compound']

def get_sentiment_label(score):
    """Convert a score into a human-readable label."""
    if score >= 0.05:
        return 'Positive'
    elif score <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# .apply() runs a function on every row in the column
df['sentiment_score'] = df['review_text'].apply(get_sentiment)
df['sentiment_label'] = df['sentiment_score'].apply(get_sentiment_label)

# Show results
print("\n=== Sentiment Results (First 10) ===\n")
print(df[['product', 'star_rating', 'sentiment_label', 'sentiment_score', 'review_text']].head(10).to_string(index=False))

# Overall sentiment breakdown
print("\n=== Overall Sentiment Distribution ===\n")
sentiment_counts = df['sentiment_label'].value_counts()
total = len(df)
for label, count in sentiment_counts.items():
    pct = count / total * 100
    bar = '█' * int(pct / 2)   # Simple text bar chart
    print(f"  {label:>8}: {count:>4} ({pct:5.1f}%) {bar}")
```

---

## Step 3: Which Product Is Loved Most? Which Is Hated?

```python
# -------------------------------------------------------
# STEP 3: COMPARE SENTIMENT ACROSS PRODUCTS
# This tells marketing which product needs attention
# -------------------------------------------------------

import matplotlib.pyplot as plt
import seaborn as sns

# Group reviews by product and calculate averages
product_sentiment = df.groupby('product').agg(
    avg_sentiment=('sentiment_score', 'mean'),    # Average sentiment score
    avg_stars=('star_rating', 'mean'),             # Average star rating
    total_reviews=('review_id', 'count'),          # Number of reviews
    positive_pct=('sentiment_label', lambda x: (x == 'Positive').mean() * 100),
    negative_pct=('sentiment_label', lambda x: (x == 'Negative').mean() * 100),
).round(2)

print("=== Product Comparison ===\n")
print(product_sentiment.to_string())

# --- VISUAL COMPARISON ---
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('TechGadget — Product Sentiment Comparison', fontsize=15, fontweight='bold')

products_list = product_sentiment.index.tolist()
colors = ['#2196F3', '#4CAF50', '#FF9800']

# Chart 1: Average Sentiment Score
bars1 = axes[0].bar(products_list, product_sentiment['avg_sentiment'], color=colors)
axes[0].set_title('Average Sentiment Score', fontsize=13)
axes[0].set_ylabel('Score (-1 = Bad, +1 = Good)')
axes[0].axhline(y=0, color='gray', linestyle='--', alpha=0.5)  # Zero line
# Add score labels on bars
for bar, val in zip(bars1, product_sentiment['avg_sentiment']):
    axes[0].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.02,
                f'{val:.2f}', ha='center', fontsize=11, fontweight='bold')

# Chart 2: Average Star Rating
bars2 = axes[1].bar(products_list, product_sentiment['avg_stars'], color=colors)
axes[1].set_title('Average Star Rating', fontsize=13)
axes[1].set_ylabel('Stars (out of 5)')
axes[1].set_ylim(0, 5.5)
for bar, val in zip(bars2, product_sentiment['avg_stars']):
    axes[1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                f'{val:.1f} ★', ha='center', fontsize=11, fontweight='bold')

# Chart 3: Positive vs Negative Percentage (Stacked)
x = range(len(products_list))
width = 0.35
axes[2].bar(x, product_sentiment['positive_pct'], width, label='Positive %', color='#4CAF50')
axes[2].bar([i + width for i in x], product_sentiment['negative_pct'], width, 
            label='Negative %', color='#F44336')
axes[2].set_xticks([i + width/2 for i in x])
axes[2].set_xticklabels(products_list)
axes[2].set_title('Positive vs Negative Reviews', fontsize=13)
axes[2].set_ylabel('Percentage (%)')
axes[2].legend()

plt.tight_layout()
plt.savefig('product_sentiment.png', dpi=150, bbox_inches='tight')
plt.show()

# --- BUSINESS INSIGHT ---
best = product_sentiment['avg_sentiment'].idxmax()
worst = product_sentiment['avg_sentiment'].idxmin()
print(f"\n>>> BEST reviewed product:  {best} (score: {product_sentiment.loc[best, 'avg_sentiment']:.2f})")
print(f">>> WORST reviewed product: {worst} (score: {product_sentiment.loc[worst, 'avg_sentiment']:.2f})")
print(f">>> RECOMMENDATION: Focus on fixing {worst} issues to reduce negative reviews!")
```

---

## Step 4: What Are People Complaining About? (Word Cloud)

```python
# -------------------------------------------------------
# STEP 4: WORD CLOUDS — SEE THE MOST COMMON WORDS
# Big word = appears more often in reviews
# We make separate clouds for positive and negative reviews
# -------------------------------------------------------

from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Separate positive and negative reviews
positive_text = ' '.join(df[df['sentiment_label'] == 'Positive']['review_text'].tolist())
negative_text = ' '.join(df[df['sentiment_label'] == 'Negative']['review_text'].tolist())

# Create word clouds
fig, axes = plt.subplots(1, 2, figsize=(16, 7))
fig.suptitle('What Are Customers Saying?', fontsize=18, fontweight='bold')

# Left: Positive reviews word cloud (green theme)
wc_positive = WordCloud(
    width=800, height=400,
    background_color='white',
    colormap='Greens',        # Green = positive
    max_words=60,
    random_state=42
).generate(positive_text)

axes[0].imshow(wc_positive, interpolation='bilinear')
axes[0].set_title('HAPPY Customers Say...', fontsize=14, color='green', fontweight='bold')
axes[0].axis('off')  # Hide axes — not meaningful for word clouds

# Right: Negative reviews word cloud (red theme)
wc_negative = WordCloud(
    width=800, height=400,
    background_color='white',
    colormap='Reds',          # Red = negative
    max_words=60,
    random_state=42
).generate(negative_text)

axes[1].imshow(wc_negative, interpolation='bilinear')
axes[1].set_title('ANGRY Customers Say...', fontsize=14, color='red', fontweight='bold')
axes[1].axis('off')

plt.tight_layout()
plt.savefig('sentiment_wordclouds.png', dpi=150, bbox_inches='tight')
plt.show()

print("Word clouds saved as 'sentiment_wordclouds.png'")
```

---

## Step 5: Find the Most Common Complaints

```python
# -------------------------------------------------------
# STEP 5: TOP COMPLAINTS — WHAT SHOULD WE FIX?
# Extract the most common words in negative reviews
# -------------------------------------------------------

import re
from collections import Counter
from nltk.corpus import stopwords
import matplotlib.pyplot as plt

# Get English stopwords (words like "the", "is", "a" that don't tell us anything)
stop_words = set(stopwords.words('english'))

# Add custom stopwords specific to our domain
stop_words.update(['product', 'buy', 'bought', 'would', 'one', 'use', 'also', 'get', 'got'])

def extract_keywords(texts, top_n=15):
    """
    Find the most common meaningful words in a list of texts.
    Removes stopwords and short words.
    """
    # Combine all texts into one big string, make lowercase
    all_text = ' '.join(texts).lower()
    
    # Keep only letters and spaces (remove punctuation, numbers)
    all_text = re.sub(r'[^a-z\s]', '', all_text)
    
    # Split into individual words
    words = all_text.split()
    
    # Keep only words that are NOT stopwords and have 3+ characters
    meaningful_words = [w for w in words if w not in stop_words and len(w) >= 3]
    
    # Count how many times each word appears
    word_counts = Counter(meaningful_words)
    
    return word_counts.most_common(top_n)

# Get top keywords for negative reviews
negative_reviews_text = df[df['sentiment_label'] == 'Negative']['review_text'].tolist()
top_complaints = extract_keywords(negative_reviews_text, top_n=15)

print("=== TOP 15 WORDS IN NEGATIVE REVIEWS ===\n")
for word, count in top_complaints:
    bar = '█' * (count // 2)  # Simple text bar
    print(f"  {word:<15} {count:>4}  {bar}")

# --- BAR CHART OF TOP COMPLAINTS ---
words = [w for w, c in top_complaints]
counts = [c for w, c in top_complaints]

plt.figure(figsize=(10, 6))
plt.barh(words[::-1], counts[::-1], color='#F44336')  # Reverse for top at top
plt.title('Most Common Words in Negative Reviews', fontsize=14, fontweight='bold')
plt.xlabel('Frequency')
plt.tight_layout()
plt.savefig('top_complaints.png', dpi=150, bbox_inches='tight')
plt.show()

# --- Also do positive keywords ---
positive_reviews_text = df[df['sentiment_label'] == 'Positive']['review_text'].tolist()
top_praise = extract_keywords(positive_reviews_text, top_n=10)

print("\n=== TOP 10 WORDS IN POSITIVE REVIEWS ===\n")
for word, count in top_praise:
    bar = '█' * (count // 2)
    print(f"  {word:<15} {count:>4}  {bar}")
```

---

## Step 6: Sentiment Over Time — Is It Getting Better or Worse?

```python
# -------------------------------------------------------
# STEP 6: TRACK SENTIMENT OVER TIME
# Are customers getting happier or angrier?
# This helps detect problems early
# -------------------------------------------------------

import matplotlib.pyplot as plt

# Calculate daily average sentiment
daily_sentiment = df.groupby('date').agg(
    avg_score=('sentiment_score', 'mean'),
    num_reviews=('review_id', 'count'),
    positive_count=('sentiment_label', lambda x: (x == 'Positive').sum()),
    negative_count=('sentiment_label', lambda x: (x == 'Negative').sum())
).reset_index()

# Calculate 7-day moving average (smooths out daily noise)
daily_sentiment['rolling_avg'] = daily_sentiment['avg_score'].rolling(7, min_periods=1).mean()

# --- TREND CHART ---
fig, axes = plt.subplots(2, 1, figsize=(14, 10))
fig.suptitle('TechGadget — Sentiment Trend Over 90 Days', fontsize=16, fontweight='bold')

# Top chart: Sentiment score over time
axes[0].scatter(daily_sentiment['date'], daily_sentiment['avg_score'], 
               alpha=0.4, s=30, color='gray', label='Daily Score')
axes[0].plot(daily_sentiment['date'], daily_sentiment['rolling_avg'], 
            color='#2196F3', linewidth=3, label='7-Day Moving Average')
axes[0].axhline(y=0, color='red', linestyle='--', alpha=0.5, label='Neutral Line')
axes[0].set_title('Average Sentiment Score Over Time')
axes[0].set_ylabel('Sentiment Score')
axes[0].legend()
axes[0].grid(True, alpha=0.3)

# Bottom chart: Number of positive vs negative reviews per day
axes[1].bar(daily_sentiment['date'], daily_sentiment['positive_count'], 
           color='#4CAF50', alpha=0.7, label='Positive Reviews')
axes[1].bar(daily_sentiment['date'], -daily_sentiment['negative_count'], 
           color='#F44336', alpha=0.7, label='Negative Reviews')
axes[1].set_title('Positive vs Negative Reviews Per Day')
axes[1].set_ylabel('Count')
axes[1].legend()
axes[1].grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('sentiment_trend.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## Step 7: The Final Dashboard (Interactive!)

```python
# -------------------------------------------------------
# STEP 7: INTERACTIVE DASHBOARD WITH PLOTLY
# Hover over charts to see details. Click legend to filter.
# Opens in your browser automatically!
# -------------------------------------------------------

import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

# --- Chart 1: Sentiment Distribution by Product (Interactive) ---
fig1 = px.histogram(
    df, 
    x='sentiment_score', 
    color='product',
    nbins=30,
    title='Sentiment Score Distribution by Product',
    labels={'sentiment_score': 'Sentiment Score', 'count': 'Number of Reviews'},
    color_discrete_sequence=['#2196F3', '#4CAF50', '#FF9800'],
    barmode='overlay',   # Overlay bars instead of stacking
    opacity=0.7
)
fig1.add_vline(x=0, line_dash="dash", line_color="red", annotation_text="Neutral")
fig1.write_html('interactive_sentiment.html')
fig1.show()

# --- Chart 2: Star Rating vs Sentiment (Interactive Scatter) ---
fig2 = px.scatter(
    df,
    x='star_rating',
    y='sentiment_score',
    color='product',
    size='helpful_votes',             # Bigger dot = more helpful votes
    hover_data=['review_text'],       # Show review text on hover!
    title='Star Rating vs Sentiment Score — Hover to Read Reviews!',
    labels={
        'star_rating': 'Star Rating (1-5)',
        'sentiment_score': 'Sentiment Score (-1 to +1)',
        'helpful_votes': 'Helpful Votes'
    },
    color_discrete_sequence=['#2196F3', '#4CAF50', '#FF9800'],
    opacity=0.6
)
fig2.write_html('interactive_scatter.html')
fig2.show()

# --- Chart 3: Sentiment by Product (Interactive Box Plot) ---
fig3 = px.box(
    df,
    x='product',
    y='sentiment_score',
    color='product',
    points='all',                     # Show every data point
    title='Sentiment Distribution by Product — Click a Product to Filter',
    labels={'sentiment_score': 'Sentiment Score', 'product': 'Product'},
    color_discrete_sequence=['#2196F3', '#4CAF50', '#FF9800']
)
fig3.write_html('interactive_boxplot.html')
fig3.show()

print("\nInteractive charts saved as HTML files!")
print("Open them in your browser to explore the data.")
```

---

## Bonus: Analyze Your Own Text (Try It!)

```python
# -------------------------------------------------------
# BONUS: TYPE ANY TEXT AND SEE ITS SENTIMENT
# Great for live demo in class!
# -------------------------------------------------------

from nltk.sentiment import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

# --- Try these examples or type your own ---
test_texts = [
    "I absolutely love this course! The professor is amazing!",
    "The cafeteria food is terrible and overpriced.",
    "The exam was fair but I wish we had more time.",
    "This is the best university in the country!",
    "The WiFi is so slow it's basically unusable.",
    "Pretty average experience, nothing to complain about.",
]

print("=" * 60)
print("   LIVE SENTIMENT ANALYZER — Type any text!")
print("=" * 60)

for text in test_texts:
    scores = sia.polarity_scores(text)
    compound = scores['compound']
    
    # Create a simple visual meter
    if compound >= 0.05:
        emoji = "😊"
        label = "POSITIVE"
    elif compound <= -0.05:
        emoji = "😠"
        label = "NEGATIVE"
    else:
        emoji = "😐"
        label = "NEUTRAL"
    
    # Visual score bar: ████████░░░░
    bar_length = 20
    filled = int((compound + 1) / 2 * bar_length)  # Map -1..+1 to 0..20
    bar = '█' * filled + '░' * (bar_length - filled)
    
    print(f'\n{emoji} [{label:>8}] Score: {compound:+.3f}  [{bar}]')
    print(f'   "{text}"')

print("\n" + "=" * 60)
```

---

## Summary — What Did We Learn?

| Step | What We Did | Business Value |
|------|------------|---------------|
| **Step 1** | Created 500 realistic reviews | Understand social media data format |
| **Step 2** | Sentiment analysis with VADER | Know if customers are happy or angry |
| **Step 3** | Compared products | Find which product needs fixing |
| **Step 4** | Word clouds | Visual snapshot of what people say |
| **Step 5** | Top complaints extraction | Find specific problems to fix |
| **Step 6** | Sentiment over time | Detect problems early |
| **Step 7** | Interactive dashboard | Explore data hands-on |

### Key Python Skills Used

- `nltk.sentiment` (VADER) — Sentiment analysis for social media text
- `wordcloud` — Visual word frequency maps
- `Counter` + regex — Extract meaningful keywords
- `plotly` — Interactive charts you can hover, click, and filter
- `pandas groupby` — Compare metrics across products

### What a Business Would Do Next

1. **Fix the worst-reviewed product** based on top complaints
2. **Promote the best-reviewed product** in marketing campaigns
3. **Set up alerts** — if negative sentiment spikes, investigate immediately
4. **Track sentiment weekly** — are improvements working?
