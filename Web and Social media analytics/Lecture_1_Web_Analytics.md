# Lecture 1: Web Analytics — Understand Your Website With Python

## What Will We Do Today?

You are the **data analyst for an online clothing store** called "StyleHub". The CEO wants answers:

1. Which days make the most money?
2. Where do our best customers come from — Google, Instagram, or Direct?
3. Is our website getting better or worse over time?
4. Which products should we promote more?

We will answer ALL of these using Python. No paid tools. No signup required.

---

## Step 0: Setup (Run Once)

Open your terminal and install the libraries:

```
pip install pandas numpy matplotlib seaborn plotly
```

---

## Step 1: Load the Store's Data

In real life, this data comes from Google Analytics or your database.
Here, we **simulate realistic data** so you can run this right now without any account.

```python
# -------------------------------------------------------
# STEP 1: CREATE REALISTIC E-COMMERCE DATA
# We are pretending to be analysts at "StyleHub" online store
# -------------------------------------------------------

import pandas as pd       # pandas = the #1 tool for working with tables in Python
import numpy as np        # numpy = for generating random numbers
from datetime import datetime, timedelta  # for creating dates

# This makes the random numbers the same every time you run it
# So your charts will match your classmate's charts
np.random.seed(42)

# --- Create 180 days of website data (6 months) ---
num_days = 180
start_date = datetime(2025, 7, 1)

# Generate a list of 180 dates
dates = [start_date + timedelta(days=i) for i in range(num_days)]

# People shop MORE on weekdays and LESS on weekends (realistic pattern)
# Monday=0, Sunday=6
weekend_factor = []
for d in dates:
    if d.weekday() >= 5:   # Saturday or Sunday
        weekend_factor.append(0.6)  # 40% less traffic on weekends
    else:
        weekend_factor.append(1.0)  # Normal traffic on weekdays

# Build the dataset row by row
rows = []
for i in range(num_days):
    # Random daily visitors (800-2500), adjusted for weekends
    visitors = int(np.random.randint(800, 2500) * weekend_factor[i])
    
    # Each visitor sees about 3-5 pages on average
    page_views = int(visitors * np.random.uniform(3, 5))
    
    # About 2-6% of visitors actually buy something
    conversion_rate = np.random.uniform(0.02, 0.06)
    orders = int(visitors * conversion_rate)
    
    # Average order is $40-$120
    avg_order_value = round(np.random.uniform(40, 120), 2)
    revenue = round(orders * avg_order_value, 2)
    
    # Where did visitors come from?
    source = np.random.choice(
        ['Google Search', 'Instagram', 'Direct', 'Facebook', 'Email Campaign'],
        p=[0.35, 0.25, 0.20, 0.12, 0.08]  # Google is the biggest source (35%)
    )
    
    # Bounce rate: % who left after 1 page (30-70%)
    bounce_rate = round(np.random.uniform(30, 70), 1)
    
    rows.append({
        'date': dates[i],
        'visitors': visitors,
        'page_views': page_views,
        'orders': orders,
        'revenue': revenue,
        'avg_order_value': avg_order_value,
        'conversion_rate': round(conversion_rate * 100, 2),  # as percentage
        'bounce_rate': bounce_rate,
        'traffic_source': source
    })

# Turn the list of rows into a pandas DataFrame (a table)
df = pd.DataFrame(rows)

# Let's see what the data looks like
print("=== StyleHub Website Data (First 10 Days) ===\n")
print(df.head(10).to_string(index=False))
print(f"\nTotal rows: {len(df)}")
print(f"Date range: {df['date'].min().strftime('%Y-%m-%d')} to {df['date'].max().strftime('%Y-%m-%d')}")
```

---

## Step 2: Answer the CEO's Questions

### Question 1: "How is our business doing overall?"

```python
# -------------------------------------------------------
# QUESTION 1: BUSINESS OVERVIEW
# Calculate the key numbers the CEO cares about
# -------------------------------------------------------

print("=" * 50)
print("   STYLEHUB — 6 MONTH BUSINESS REPORT")
print("=" * 50)

# .sum() adds up all values in a column
total_revenue = df['revenue'].sum()
total_orders = df['orders'].sum()
total_visitors = df['visitors'].sum()

# .mean() calculates the average
avg_daily_revenue = df['revenue'].mean()
avg_conversion = df['conversion_rate'].mean()
avg_bounce = df['bounce_rate'].mean()

print(f"\n  Total Revenue:         ${total_revenue:,.2f}")     # :,.2f = commas + 2 decimals
print(f"  Total Orders:          {total_orders:,}")
print(f"  Total Visitors:        {total_visitors:,}")
print(f"  Avg Daily Revenue:     ${avg_daily_revenue:,.2f}")
print(f"  Avg Conversion Rate:   {avg_conversion:.2f}%")
print(f"  Avg Bounce Rate:       {avg_bounce:.1f}%")
print(f"\n  Revenue per Visitor:   ${total_revenue / total_visitors:.2f}")

print("\n" + "=" * 50)
```

### Question 2: "Which traffic source brings us the most money?"

```python
# -------------------------------------------------------
# QUESTION 2: WHICH TRAFFIC SOURCE IS THE BEST?
# Group the data by traffic source and compare
# -------------------------------------------------------

import matplotlib.pyplot as plt   # For creating charts
import seaborn as sns             # Makes charts look prettier

# Group rows by traffic_source, then calculate totals and averages for each group
source_stats = df.groupby('traffic_source').agg(
    total_revenue=('revenue', 'sum'),          # Total money from this source
    total_orders=('orders', 'sum'),            # Total orders from this source
    total_visitors=('visitors', 'sum'),        # Total visitors from this source
    avg_conversion=('conversion_rate', 'mean'), # Average conversion rate
    avg_order_value=('avg_order_value', 'mean') # Average order size
).round(2)

# Sort by revenue (highest first)
source_stats = source_stats.sort_values('total_revenue', ascending=False)

print("=== Revenue by Traffic Source ===\n")
print(source_stats.to_string())

# --- CREATE A BAR CHART ---
fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Chart 1: Total Revenue by Source
colors = ['#2196F3', '#4CAF50', '#FF9800', '#E91E63', '#9C27B0']
axes[0].bar(source_stats.index, source_stats['total_revenue'], color=colors)
axes[0].set_title('Total Revenue by Traffic Source', fontsize=14, fontweight='bold')
axes[0].set_ylabel('Revenue ($)')
# Rotate labels so they don't overlap
axes[0].tick_params(axis='x', rotation=20)
# Add dollar amounts on top of each bar
for i, val in enumerate(source_stats['total_revenue']):
    axes[0].text(i, val + 500, f'${val:,.0f}', ha='center', fontsize=9)

# Chart 2: Average Conversion Rate by Source
axes[1].bar(source_stats.index, source_stats['avg_conversion'], color=colors)
axes[1].set_title('Avg Conversion Rate by Traffic Source', fontsize=14, fontweight='bold')
axes[1].set_ylabel('Conversion Rate (%)')
axes[1].tick_params(axis='x', rotation=20)

plt.tight_layout()  # Prevent charts from overlapping
plt.savefig('traffic_sources.png', dpi=150, bbox_inches='tight')
plt.show()

print("\nChart saved as 'traffic_sources.png'")
```

### Question 3: "Is our website getting better or worse over time?"

```python
# -------------------------------------------------------
# QUESTION 3: TREND ANALYSIS — ARE WE GROWING?
# Look at how revenue and visitors change week by week
# -------------------------------------------------------

import matplotlib.pyplot as plt

# Add a 'week' column — group days into weeks for cleaner trends
# .dt accesses date properties; .isocalendar().week gives the week number
df['week_number'] = df['date'].dt.isocalendar().week.astype(int)
df['month'] = df['date'].dt.strftime('%Y-%m')  # "2025-07", "2025-08", etc.

# Calculate weekly totals
weekly = df.groupby('week_number').agg(
    revenue=('revenue', 'sum'),
    visitors=('visitors', 'sum'),
    orders=('orders', 'sum')
).reset_index()

# --- CREATE THE TREND CHART ---
fig, ax1 = plt.subplots(figsize=(14, 6))

# Left axis: Revenue as bars
color_bars = '#E3F2FD'
ax1.bar(weekly['week_number'], weekly['revenue'], color='#2196F3', alpha=0.3, label='Weekly Revenue')
ax1.set_xlabel('Week Number', fontsize=12)
ax1.set_ylabel('Revenue ($)', fontsize=12, color='#2196F3')
ax1.tick_params(axis='y', labelcolor='#2196F3')

# Right axis: Visitors as a line (second y-axis)
ax2 = ax1.twinx()  # Create a second y-axis that shares the same x-axis
ax2.plot(weekly['week_number'], weekly['visitors'], color='#E91E63', linewidth=2.5, 
         marker='o', markersize=5, label='Weekly Visitors')
ax2.set_ylabel('Visitors', fontsize=12, color='#E91E63')
ax2.tick_params(axis='y', labelcolor='#E91E63')

plt.title('StyleHub Weekly Performance — Revenue & Visitors', fontsize=15, fontweight='bold')
fig.legend(loc='upper left', bbox_to_anchor=(0.12, 0.95))
plt.tight_layout()
plt.savefig('weekly_trend.png', dpi=150, bbox_inches='tight')
plt.show()

# --- MONTH OVER MONTH COMPARISON ---
monthly = df.groupby('month').agg(
    revenue=('revenue', 'sum'),
    visitors=('visitors', 'sum'),
    orders=('orders', 'sum'),
    avg_conversion=('conversion_rate', 'mean')
).round(2)

print("\n=== Monthly Performance ===\n")
print(monthly.to_string())
```

### Question 4: "When should we run promotions?"

```python
# -------------------------------------------------------
# QUESTION 4: BEST AND WORST DAYS OF THE WEEK
# Find patterns in shopping behavior
# -------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Add day name column
df['day_name'] = df['date'].dt.day_name()  # "Monday", "Tuesday", etc.

# Calculate average revenue and visitors for each day of the week
day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
daily_avg = df.groupby('day_name').agg(
    avg_revenue=('revenue', 'mean'),
    avg_visitors=('visitors', 'mean'),
    avg_orders=('orders', 'mean'),
    avg_bounce=('bounce_rate', 'mean')
).reindex(day_order).round(2)  # reindex puts days in correct order

print("=== Average Performance by Day of Week ===\n")
print(daily_avg.to_string())

# --- HEATMAP-STYLE BAR CHART ---
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle('StyleHub — Day of Week Analysis', fontsize=16, fontweight='bold')

# Use different colors for weekdays vs weekends
day_colors = ['#2196F3'] * 5 + ['#FF9800'] * 2  # Blue=weekday, Orange=weekend

# Chart 1: Average Revenue
axes[0, 0].bar(range(7), daily_avg['avg_revenue'], color=day_colors)
axes[0, 0].set_xticks(range(7))
axes[0, 0].set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
axes[0, 0].set_title('Avg Revenue per Day')
axes[0, 0].set_ylabel('Revenue ($)')

# Chart 2: Average Visitors
axes[0, 1].bar(range(7), daily_avg['avg_visitors'], color=day_colors)
axes[0, 1].set_xticks(range(7))
axes[0, 1].set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
axes[0, 1].set_title('Avg Visitors per Day')
axes[0, 1].set_ylabel('Visitors')

# Chart 3: Average Orders
axes[1, 0].bar(range(7), daily_avg['avg_orders'], color=day_colors)
axes[1, 0].set_xticks(range(7))
axes[1, 0].set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
axes[1, 0].set_title('Avg Orders per Day')
axes[1, 0].set_ylabel('Orders')

# Chart 4: Bounce Rate (lower is better)
axes[1, 1].bar(range(7), daily_avg['avg_bounce'], color=day_colors)
axes[1, 1].set_xticks(range(7))
axes[1, 1].set_xticklabels(['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])
axes[1, 1].set_title('Avg Bounce Rate (lower = better)')
axes[1, 1].set_ylabel('Bounce Rate (%)')

plt.tight_layout()
plt.savefig('day_of_week_analysis.png', dpi=150, bbox_inches='tight')
plt.show()

# --- BUSINESS INSIGHT ---
best_day = daily_avg['avg_revenue'].idxmax()
worst_day = daily_avg['avg_revenue'].idxmin()
print(f"\n>>> INSIGHT: Best day for revenue is {best_day} (${daily_avg.loc[best_day, 'avg_revenue']:,.2f})")
print(f">>> INSIGHT: Worst day for revenue is {worst_day} (${daily_avg.loc[worst_day, 'avg_revenue']:,.2f})")
print(f">>> RECOMMENDATION: Run weekend promotions to boost Saturday/Sunday sales!")
```

---

## Step 3: A/B Testing — Did the New Homepage Work?

This is one of the most important analytics techniques in the industry.

```python
# -------------------------------------------------------
# A/B TEST: THE CEO CHANGED THE HOMEPAGE ON DAY 90
# Did the new design increase conversion rate?
# -------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np

# Split data into "before" (old design) and "after" (new design)
# First 90 days = old homepage, Last 90 days = new homepage
before = df.iloc[:90]   # .iloc[:90] = first 90 rows
after = df.iloc[90:]    # .iloc[90:] = remaining rows

# Compare key metrics
print("=" * 55)
print("   A/B TEST: OLD HOMEPAGE vs NEW HOMEPAGE")
print("=" * 55)
print(f"{'Metric':<25} {'Old Design':>12} {'New Design':>12} {'Change':>10}")
print("-" * 55)

metrics = {
    'Avg Conversion Rate': ('conversion_rate', 'mean', '%'),
    'Avg Revenue/Day': ('revenue', 'mean', '$'),
    'Avg Bounce Rate': ('bounce_rate', 'mean', '%'),
    'Avg Orders/Day': ('orders', 'mean', ''),
    'Avg Visitors/Day': ('visitors', 'mean', ''),
}

for label, (col, agg, unit) in metrics.items():
    old_val = before[col].mean()
    new_val = after[col].mean()
    change = ((new_val - old_val) / old_val) * 100  # Percentage change
    
    if unit == '$':
        print(f"{label:<25} {f'${old_val:,.2f}':>12} {f'${new_val:,.2f}':>12} {f'{change:+.1f}%':>10}")
    else:
        print(f"{label:<25} {f'{old_val:.2f}':>12} {f'{new_val:.2f}':>12} {f'{change:+.1f}%':>10}")

print("-" * 55)

# --- VISUAL COMPARISON ---
fig, axes = plt.subplots(1, 3, figsize=(16, 5))
fig.suptitle('A/B Test Results: Old vs New Homepage', fontsize=15, fontweight='bold')

# Revenue comparison
axes[0].bar(['Old Design', 'New Design'], 
            [before['revenue'].mean(), after['revenue'].mean()],
            color=['#EF5350', '#4CAF50'])
axes[0].set_title('Avg Daily Revenue')
axes[0].set_ylabel('Revenue ($)')

# Conversion rate comparison
axes[1].bar(['Old Design', 'New Design'], 
            [before['conversion_rate'].mean(), after['conversion_rate'].mean()],
            color=['#EF5350', '#4CAF50'])
axes[1].set_title('Avg Conversion Rate')
axes[1].set_ylabel('Conversion Rate (%)')

# Bounce rate comparison (lower is better)
axes[2].bar(['Old Design', 'New Design'], 
            [before['bounce_rate'].mean(), after['bounce_rate'].mean()],
            color=['#EF5350', '#4CAF50'])
axes[2].set_title('Avg Bounce Rate (lower = better)')
axes[2].set_ylabel('Bounce Rate (%)')

plt.tight_layout()
plt.savefig('ab_test_results.png', dpi=150, bbox_inches='tight')
plt.show()
```

---

## Step 4: Scrape a Real Website (Bonus — Live Demo)

Let's scrape **real data** from Hacker News (a popular tech news site).
**Requires internet connection.**

```python
# -------------------------------------------------------
# BONUS: SCRAPE REAL DATA FROM HACKER NEWS
# This pulls LIVE data from the internet right now
# -------------------------------------------------------

import requests                    # Makes HTTP requests (like a browser)
from bs4 import BeautifulSoup      # Reads HTML and extracts data
import pandas as pd
import time

def get_hacker_news_stories():
    """
    Scrape the top stories from Hacker News right now.
    Hacker News allows scraping (check: https://news.ycombinator.com/robots.txt)
    """
    print("Fetching stories from Hacker News...")
    
    all_stories = []
    
    # Scrape 3 pages (about 90 stories)
    for page_num in range(1, 4):
        # Build the URL for each page
        url = f'https://news.ycombinator.com/news?p={page_num}'
        
        # Download the page HTML (like opening it in a browser)
        response = requests.get(url, timeout=10)
        
        # Parse the HTML so we can search through it
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # Find all story title links
        title_links = soup.select('.titleline > a')
        # Find all score elements (e.g., "142 points")
        scores = soup.select('.score')
        
        for i, link in enumerate(title_links):
            story = {
                'rank': len(all_stories) + 1,
                'title': link.get_text(),              # The story headline
                'url': link.get('href', ''),           # The link URL
                'score': 0
            }
            
            # Get the score if available
            if i < len(scores):
                try:
                    story['score'] = int(scores[i].get_text().split()[0])
                except (ValueError, IndexError):
                    pass
            
            all_stories.append(story)
        
        # Wait 1 second between pages (be polite to the server)
        time.sleep(1)
    
    df = pd.DataFrame(all_stories)
    return df

# --- RUN THE SCRAPER ---
df_hn = get_hacker_news_stories()

print(f"\nCollected {len(df_hn)} stories!\n")
print("=== TOP 15 STORIES RIGHT NOW ===\n")
top15 = df_hn.nlargest(15, 'score')  # Sort by score, take top 15
for _, row in top15.iterrows():
    print(f"  [{row['score']:>4} pts] {row['title'][:80]}")

# Quick analysis
print(f"\n=== Quick Stats ===")
print(f"Average score: {df_hn['score'].mean():.1f} points")
print(f"Highest score: {df_hn['score'].max()} points")
print(f"Stories with 100+ points: {(df_hn['score'] >= 100).sum()}")
```

---

## Summary — What Did We Learn?

| Step | What We Did | Business Value |
|------|------------|---------------|
| **Step 1** | Created realistic e-commerce data | Understand what web data looks like |
| **Step 2** | Answered CEO's questions with charts | Data-driven decision making |
| **Step 3** | A/B test comparison | Measure if changes actually work |
| **Step 4** | Scraped real website data | Collect data from any website |

### Key Python Skills Used

- `pandas` — Working with tables (`DataFrame`, `groupby`, `agg`)
- `matplotlib` — Creating charts (`bar`, `plot`, `subplots`)
- `requests` + `BeautifulSoup` — Scraping websites
- Basic statistics — `mean()`, `sum()`, percentage change
