# Tableau — Data Visualization & Business Intelligence

## What is Tableau?

Tableau is a **data visualization and business intelligence (BI) tool** that lets you turn raw data into interactive, visual dashboards — charts, graphs, maps, and reports — without writing a single line of code. You connect it to your data (Excel files, databases, CSVs, cloud data), drag and drop fields, and it creates beautiful visualizations for you.

Think of it this way: Excel can make charts, but Tableau makes **dashboards**. The difference is like comparing a single photo to an entire interactive gallery where you can click, filter, and explore.

### Why Tableau Matters

In the real world, nobody reads through 1,470 rows of HR data in a spreadsheet to find patterns. That's inhuman. Instead, you load that data into Tableau and within minutes you can see things like:
- Which department has the highest employee attrition?
- Is there a relationship between overtime and people leaving?
- What's the average monthly income by job role?
- How does distance from home affect work-life balance?

**Data without visualization is just numbers. Visualization turns numbers into stories.**

### How Tableau Works (The Basics)

1. **Connect** — You connect Tableau to your data source (Excel file, SQL database, Google Sheets, CSV, etc.)
2. **Drag & Drop** — You drag columns (fields) onto rows, columns, colors, and filters to build charts
3. **Visualize** — Tableau automatically picks the best chart type, or you can choose your own (bar chart, line chart, scatter plot, heatmap, map, etc.)
4. **Dashboard** — You combine multiple charts into a single interactive dashboard
5. **Share** — You publish your dashboard so others can view and interact with it

### Key Tableau Terminology

- **Dimensions** — Categorical/descriptive fields (Department, Gender, Job Role, Marital Status). These are the things you group by.
- **Measures** — Numerical fields (Monthly Income, Age, Years at Company, Daily Rate). These are the things you count, sum, or average.
- **Worksheet** — A single chart or visualization
- **Dashboard** — Multiple worksheets combined on one page for a complete view
- **Story** — A sequence of dashboards that walk the viewer through a narrative
- **Filters** — Let you narrow down the data (show only Sales department, show only employees aged 30-40)
- **Marks** — The visual elements on your chart (bars, dots, lines, areas)

---

## Tableau Public vs Tableau Private (Desktop/Server/Cloud)

This is an important distinction you should understand:

### Tableau Public (Free)

**What it is:** A **free version** of Tableau where you can create visualizations and publish them to the internet for anyone to see.

**Key characteristics:**
- Completely **free to download and use**
- You can connect to limited data sources (Excel, CSV, Google Sheets, text files — but NOT databases like SQL Server or PostgreSQL)
- Every workbook you save **must be published to the Tableau Public website** — there is no option to save locally/privately
- Your data and dashboards are **visible to everyone on the internet**
- Great for learning, building a portfolio, and sharing public datasets
- Has a **data size limit** (up to 15 million rows, but file uploads limited to 1GB)
- You can embed your public dashboards on websites and blogs

**Website:** [public.tableau.com](https://public.tableau.com)

**When to use it:**
- You're a student learning Tableau (this is you right now!)
- You want to practice and build a portfolio of visualizations
- You're working with publicly available data (government data, sports stats, etc.)
- You want to share your work with the world

**When NOT to use it:**
- You're working with sensitive, private, or confidential data (company HR data, financial records, customer data)
- You need to keep your dashboards private

### Tableau Desktop (Paid / Private)

**What it is:** The **full, paid version** of Tableau that you install on your computer. This is what companies and professionals use.

**Key characteristics:**
- Paid license (expensive — around $70/month per user for Creator license)
- Can connect to **any data source** — SQL databases, cloud data warehouses, APIs, Hadoop, Salesforce, and many more
- You can **save workbooks locally** on your computer — nothing is forced to be public
- Your data stays **private and secure**
- No data size limits (handles millions of rows easily)
- Includes advanced features like calculated fields, parameters, LOD expressions, and data blending

### Tableau Server & Tableau Cloud (Enterprise / Private Sharing)

**What they are:** These are platforms for **sharing dashboards privately within an organization**.

- **Tableau Server** — You install it on your company's own servers. Only people inside your organization (or those you give access to) can see the dashboards. The company controls everything — security, access, data.
- **Tableau Cloud** — Same idea but hosted by Tableau/Salesforce in the cloud. You don't manage any servers — Tableau handles the infrastructure. You just upload dashboards and control who can view them.

**When companies use these:**
- HR team creates an employee attrition dashboard — only HR managers and executives should see it (not the whole internet)
- Finance team creates revenue reports — this is confidential data
- Sales team tracks pipeline — this data is competitive and sensitive

### Quick Comparison Table

| Feature | Tableau Public | Tableau Desktop | Tableau Server/Cloud |
|---------|---------------|----------------|---------------------|
| **Cost** | Free | ~$70/month | ~$35-70/user/month |
| **Data Privacy** | Everything is public | Private (local files) | Private (shared within org) |
| **Data Sources** | Excel, CSV, Google Sheets only | All sources (SQL, APIs, cloud, etc.) | All sources |
| **Save Locally** | No — must publish online | Yes | Publishes to private server |
| **Best For** | Learning, portfolios, public data | Professional analysis | Team collaboration |
| **Data Size** | Limited (1GB upload) | No practical limit | No practical limit |

### For This Class

You'll be using **Tableau Public** since it's free. Just remember — **do not upload any real sensitive data** to Tableau Public because it will be visible to everyone. The HR dataset provided for practice is a sample/dummy dataset, so it's safe to use.

---

---

# About the Data — HR Data.xlsx Explained

Along with this assignment, you have an Excel file called **`HR Data.xlsx`**. This is a **Human Resources (HR) dataset** that contains information about 1,470 employees at a fictional company. It's a classic dataset used for learning data analysis and visualization.

This data is the kind of data that HR departments in real companies collect to understand their workforce — who's leaving, who's staying, why, and what factors might predict employee behavior.

## What's in the Data?

The dataset has **1,470 rows** (each row is one employee) and **39 columns** (each column is a piece of information about that employee). Here's what every column means:

### Employee Identity & Demographics

| Column | What It Means | Example Values |
|--------|--------------|----------------|
| **emp no** | A unique staff ID for each employee | STAFF-1, STAFF-2, STAFF-4 |
| **Employee Number** | A numeric ID for each employee | 1, 2, 4 |
| **Gender** | Male or Female | Male, Female |
| **Age** | The employee's age in years | 41, 49, 37 |
| **CF_age band** | Age grouped into ranges for easier analysis | 25 - 34, 35 - 44, 45 - 54, Over 55 |
| **Marital Status** | Single, Married, or Divorced | Single, Married, Divorced |
| **Over18** | Whether the employee is over 18 (always "Y" in this dataset) | Y |
| **Education** | Education level as a number (1 = Below College, 2 = College, 3 = Bachelor, 4 = Master, 5 = Doctor) | 1, 2, 3, 4, 5 |
| **Education Field** | What field they studied | Life Sciences, Medical, Marketing, Technical, Human Resources, Other |

### Job & Company Information

| Column | What It Means | Example Values |
|--------|--------------|----------------|
| **Department** | Which department they work in | Sales, R&D (Research & Development), Human Resources |
| **Job Role** | Their specific job title | Sales Executive, Research Scientist, Laboratory Technician, Manager, etc. |
| **Job Level** | Seniority level (1 = entry level, 5 = senior/executive) | 1, 2, 3, 4, 5 |
| **Business Travel** | How often they travel for work | Non-Travel, Travel_Rarely, Travel_Frequently |
| **Standard Hours** | Standard working hours per week (always 80 in this dataset — likely biweekly) | 80 |
| **Over Time** | Whether they work overtime | Yes, No |

### Compensation & Financials

| Column | What It Means | Example Values |
|--------|--------------|----------------|
| **Monthly Income** | Monthly salary in dollars | 5993, 5130, 2090 |
| **Daily Rate** | Daily pay rate | 1102, 279, 1373 |
| **Hourly Rate** | Hourly pay rate | 94, 61, 92 |
| **Monthly Rate** | Another monthly rate metric | 19479, 24907, 2396 |
| **Percent Salary Hike** | Percentage of last salary increase | 11, 23, 15 |
| **Stock Option Level** | Level of stock options received (0 = none, 3 = highest) | 0, 1, 2, 3 |

### Experience & Tenure

| Column | What It Means | Example Values |
|--------|--------------|----------------|
| **Total Working Years** | Total career experience in years | 8, 10, 7 |
| **Years At Company** | How many years at this specific company | 6, 10, 0 |
| **Years In Current Role** | How many years in their current role | 4, 7, 0 |
| **Years Since Last Promotion** | How many years since they were last promoted | 0, 1, 0 |
| **Years With Curr Manager** | How many years with their current manager | 5, 7, 0 |
| **Num Companies Worked** | Number of companies they've worked at before | 8, 1, 6 |
| **Training Times Last Year** | Number of training sessions attended last year | 0, 3, 3 |

### Satisfaction & Performance

| Column | What It Means | Example Values |
|--------|--------------|----------------|
| **Job Satisfaction** | How satisfied with their job (1 = Low, 2 = Medium, 3 = High, 4 = Very High) | 1, 2, 3, 4 |
| **Environment Satisfaction** | How satisfied with work environment (1-4 scale, same as above) | 1, 2, 3, 4 |
| **Relationship Satisfaction** | How satisfied with work relationships (1-4 scale) | 1, 2, 3, 4 |
| **Job Involvement** | How involved/engaged they are in their job (1-4 scale) | 1, 2, 3, 4 |
| **Work Life Balance** | How they rate their work-life balance (1-4 scale) | 1, 2, 3, 4 |
| **Performance Rating** | Annual performance rating (typically 3 = Excellent, 4 = Outstanding) | 3, 4 |

### Attrition (The Key Column!)

| Column | What It Means | Example Values |
|--------|--------------|----------------|
| **Attrition** | **Did the employee leave the company?** This is the most important column. | Yes, No |
| **CF_attrition label** | A descriptive label for attrition status | Current Employees, Ex-Employees |
| **CF_current Employee** | A flag: 1 = still works here, 0 = left | 0, 1 |
| **Employee Count** | Always 1 — used for counting in visualizations | 1 |
| **Distance From Home** | How far they live from the office (in miles/km) | 1, 8, 2 |

## What Questions Can You Answer With This Data?

This dataset is perfect for exploring questions like:

- **What's the overall attrition rate?** (What percentage of employees have left?)
- **Which department loses the most people?** (Sales vs R&D vs HR)
- **Does overtime cause people to leave?** (Compare attrition for overtime vs non-overtime employees)
- **Does salary matter?** (Is monthly income lower for people who left?)
- **Does distance from home affect attrition?** (Do people who live far away leave more?)
- **Which age group is most likely to leave?** (Young employees vs senior employees)
- **Does job satisfaction predict attrition?** (Do unhappy employees leave more? Obviously yes — but by how much?)
- **What's the relationship between years at company and attrition?** (Do people leave early or after many years?)
- **Does education level affect salary?** (Do PhDs earn more than high school graduates?)
- **Which job role has the highest turnover?** (Sales Reps vs Research Scientists vs Managers)

## How to Use This Data

You can use this dataset to:

1. **Practice in Tableau** — Load the Excel file into Tableau Public and create dashboards answering the questions above
2. **Practice in Python** — Load it with Pandas (`pd.read_excel('HR Data.xlsx')`) and do exploratory data analysis
3. **Build ML models** — Try to predict which employees will leave (this is a classic classification problem — the target variable is "Attrition")

---

Good luck with your work!
