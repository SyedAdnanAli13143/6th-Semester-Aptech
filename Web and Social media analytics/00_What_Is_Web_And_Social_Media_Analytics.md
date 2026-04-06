# What Is Web & Social Media Analytics?

## A Simple Guide for Software Engineering Students

---

## 1. The Big Picture

Every time someone visits a website, clicks a button, posts a review, or likes a photo — **data is created**. Web & Social Media Analytics is about **collecting that data and turning it into useful answers** for businesses.

Think of it like this:

```
Millions of clicks, posts, likes, reviews
        ↓
   Collect & Organize
        ↓
   Find Patterns
        ↓
   Make Smart Decisions
```

---

## 2. Web Analytics — What Is It?

Web Analytics means **tracking what people do on a website** to answer questions like:

- How many people visited our site today?
- Which page do people leave from the most? (something is wrong there!)
- Did our new homepage design get more sales?
- Where do our visitors come from — Google? Instagram? Direct?

### Real-World Examples

| Company | Question | How Analytics Helps |
|---------|----------|-------------------|
| **Amazon** | Which products should we show on the homepage? | Track which products get the most clicks and purchases |
| **Netflix** | Is our new sign-up page working? | Compare old vs new page conversion rates (A/B testing) |
| **A local bakery website** | Should we invest in Google Ads? | Check if Google visitors actually place orders |

### Key Terms (Simple Definitions)

| Term | What It Means | Example |
|------|--------------|---------|
| **Page View** | Someone loaded a page | You opened amazon.com → that's 1 page view |
| **Visitor** | One unique person | You visited 10 pages → that's 1 visitor, 10 page views |
| **Bounce Rate** | % of people who leave after seeing only 1 page | 60% bounce = 60 out of 100 people left immediately |
| **Session Duration** | How long someone stayed | Average 3 minutes = people browse for 3 min |
| **Conversion Rate** | % of visitors who did what you wanted | 5% = 5 out of 100 visitors bought something |
| **Traffic Source** | Where visitors came from | Google, Instagram, typed the URL directly, etc. |

### How Is The Data Collected?

Most websites use a **small piece of JavaScript code** (called a tracking script) that runs in your browser whenever you visit a page. This script silently records everything and sends it to an analytics server.

**What does the tracking script record?**

- When a page is loaded and which page it is
- What the user clicks (buttons, links, images)
- How long they stay on each page
- What device (phone/laptop) and browser (Chrome/Safari) they use
- Screen size, language, country (from IP address)

**How does the website know WHERE you came from?**

Every time you click a link to visit a website, your browser sends a hidden piece of information called the **Referrer**. The website reads this to figure out your traffic source:

| How You Arrived | What The Website Sees | Classified As |
|---|---|---|
| Typed `stylehub.com` in the address bar | Referrer is empty | **Direct** |
| Clicked a Google search result | Referrer = `google.com` | **Organic Search** |
| Clicked a link on someone's Instagram story | Referrer = `instagram.com` | **Social Media** |
| Clicked a link in a marketing email | URL contains `?utm_source=email` | **Email Campaign** |
| Clicked a link on another blog | Referrer = `blogname.com` | **Referral** |

**What are UTM parameters?**

Marketers add special tags to URLs so they can track exactly which campaign brought a visitor. For example:

```
https://stylehub.com/sale?utm_source=instagram&utm_medium=story&utm_campaign=summer_sale
```

| Tag | Meaning | Example |
|-----|---------|---------|
| `utm_source` | Which platform? | `instagram`, `google`, `newsletter` |
| `utm_medium` | What type of link? | `story`, `post`, `email`, `cpc` (cost per click) |
| `utm_campaign` | Which campaign? | `summer_sale`, `black_friday`, `new_launch` |

When someone clicks this link, the analytics tool records: *"This visitor came from Instagram, via a story, as part of the summer_sale campaign."*

**How does it track clicks and actions on the page?**

The JavaScript tracking code listens for **events** — specific things a user does:

```
User clicks "Add to Cart" button  →  Event recorded: {action: "add_to_cart", product: "Shoes"}
User scrolls to bottom of page    →  Event recorded: {action: "scroll", depth: "100%"}
User fills in checkout form        →  Event recorded: {action: "begin_checkout", value: "$89"}
```

This is called **event tracking**. The website owner decides which events to track by adding code like:

```javascript
// Example: Google Analytics tracking code on a "Buy Now" button
document.getElementById('buy-button').addEventListener('click', function() {
    gtag('event', 'purchase', { value: 89.99, currency: 'USD' });
});
```

**Popular analytics tools (all have free tiers):**

| Tool | What It Does | Cost |
|------|-------------|------|
| **Google Analytics** | The industry standard — used by ~85% of websites | Free |
| **Plausible** | Privacy-friendly, simple, open source | Free (self-hosted) |
| **Mixpanel** | Focuses on user actions and funnels | Free tier |
| **Hotjar** | Records heatmaps of where users click | Free tier |

**Google Analytics** is the most popular free tool. But as software engineers, we can also build our own analysis using **Python**.

---

## 3. Social Media Analytics — What Is It?

Social Media Analytics means **analyzing what people say and do on social platforms** (Twitter/X, Reddit, YouTube, Instagram, Facebook) to answer questions like:

- Are people saying good or bad things about our brand?
- What topics are trending right now?
- Who are the most influential people talking about our product?
- Did our marketing campaign work?

### Real-World Examples

| Company | Question | How Analytics Helps |
|---------|----------|-------------------|
| **Samsung** | What do people think of our new phone? | Analyze thousands of reviews — are they positive or negative? |
| **A restaurant** | Why did our rating drop? | Read recent reviews, find the most common complaints |
| **Nike** | Which influencer should we sponsor? | Find who has the most engagement when talking about sports |

### Key Terms (Simple Definitions)

| Term | What It Means | Example |
|------|--------------|---------|
| **Sentiment** | Is the opinion positive, negative, or neutral? | "I love this phone!" = Positive |
| **Engagement** | How much people interact with a post | Likes + Comments + Shares |
| **Reach** | How many unique people saw something | Your post was seen by 5,000 people |
| **Impressions** | Total number of times something was shown | Shown 8,000 times (some people saw it twice) |
| **Trending** | A topic growing in popularity fast | "#WorldCup" suddenly gets millions of mentions |
| **Influencer** | A person with many followers who affects opinions | A YouTuber with 1M subscribers reviews your product |

### How Is The Data Collected?

- **APIs (Application Programming Interfaces):** Social platforms give developers a way to request data programmatically. Reddit and YouTube have **free** APIs.
- **Web Scraping:** When no API exists, we can read the webpage HTML and extract data using Python.

---

## 4. Google Analytics vs Python — What Does What?

A common question: *"If Google Analytics already tracks everything, why do we need Python?"*

**Short answer:** Google Analytics handles the basics automatically. Python handles everything it can't.

### What Google Analytics Does (No Coding Needed)

Google Analytics is a **free tool by Google**. You paste one small script into your website's HTML, and it automatically gives you a dashboard showing:

- How many visitors today / this week / this month
- Where they came from (Google, Instagram, Direct, etc.)
- Which pages are most popular
- Bounce rate, session duration, device type
- Which country/city visitors are from

**You don't write any code for this. It just works.**

### What Google Analytics CANNOT Do

| Task | Can Google Analytics Do It? | Can Python Do It? |
|------|:---:|:---:|
| Count visitors and page views | Yes | Not needed |
| Show traffic sources | Yes | Not needed |
| Basic bounce rate and session stats | Yes | Not needed |
| **Read customer reviews and detect if they're angry or happy** | No | Yes |
| **Predict next month's sales from past data** | No | Yes |
| **Scrape competitor websites** to compare prices | No | Yes |
| **Combine data from Reddit + YouTube + your website** into one report | No | Yes |
| **Find the most common complaints** in 10,000 reviews | No | Yes |
| **Create word clouds** and custom visualizations | No | Yes |
| **Build automated alerts** ("notify me if negative reviews spike") | No | Yes |
| **A/B test with full statistical analysis** | Basic only | Yes (full control) |
| **Analyze social media** (Reddit, YouTube comments, forums) | No | Yes |

### So When Do You Use What?

```
"How many people visited our website?"          → Google Analytics (automatic)
"Are people happy with our product?"            → Python (sentiment analysis)
"What are the top complaints this month?"       → Python (text mining)
"Which traffic source has the best customers?"  → Both (GA collects, Python digs deeper)
"Predict if sales will go up or down?"          → Python (machine learning)
```

### The Real World

In a real company, the workflow looks like this:

```
Google Analytics       →  Collects raw website data automatically
        ↓
Export data as CSV     →  Download the data file
        ↓
Python                 →  Deep analysis, predictions, custom reports
        ↓
Dashboard / Report     →  Present findings to the business team
```

**In this course**, we skip Google Analytics setup (it requires owning a website) and go straight to Python analysis using realistic simulated data. The skills you learn — pandas, matplotlib, sentiment analysis — are exactly what you'd use on real Google Analytics exports too.

---

## 5. Why Should Software Engineers Care?

As a software engineer, you will likely:

1. **Build products** — Analytics tells you which features users actually use
2. **Work with data teams** — You need to understand what they're measuring
3. **Make technical decisions** — "Should we optimize the checkout page?" → analytics data gives the answer
4. **Build dashboards** — Companies need tools to visualize their data
5. **Automate monitoring** — Write scripts that alert when something goes wrong (e.g., sudden spike in negative reviews)

---

## 5. Tools We Will Use (All Free)

| Tool | What It Does | Cost |
|------|-------------|------|
| **Python** | Programming language for everything | Free |
| **pandas** | Work with tables of data | Free |
| **matplotlib / seaborn** | Create charts and graphs | Free |
| **BeautifulSoup** | Scrape data from websites | Free |
| **TextBlob / VADER** | Analyze if text is positive or negative | Free |
| **Reddit API (PRAW)** | Get posts and comments from Reddit | Free |
| **wordcloud** | Create word cloud images | Free |
| **plotly** | Create interactive charts | Free |

### Install Everything (One Command)

Open your terminal/command prompt and run:

```
pip install pandas numpy matplotlib seaborn requests beautifulsoup4 textblob nltk wordcloud plotly praw scikit-learn
```

Then run this once in Python to download language data:

```python
import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
```

---

## 6. The Analytics Pipeline

Every analytics project follows the same 5 steps:

```
Step 1: COLLECT     →  Get the data (scrape, API, CSV file)
Step 2: CLEAN       →  Fix messy data (remove junk, handle missing values)
Step 3: ANALYZE     →  Find patterns (counts, averages, sentiment)
Step 4: VISUALIZE   →  Make charts so humans can understand
Step 5: DECIDE      →  Use the insights to take action
```

In our two lectures, we will go through this entire pipeline:
- **Lecture 1 (Web Analytics):** Analyze an online store's traffic data
- **Lecture 2 (Social Media Analytics):** Analyze what customers say about brands on Reddit

---

## 7. Ethics — Important Rules

- **Never collect personal data** (emails, names, addresses) without permission
- **Respect website rules** — always check `robots.txt` before scraping
- **Don't overload servers** — add delays between requests
- **Be transparent** — if you build a bot, say so in the User-Agent header
- **Use data responsibly** — analytics should help people, not manipulate them
