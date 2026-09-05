# 🇧🇩 Bangladesh Multi-Tool AI Agent

A LangChain-based AI agent for Bangladesh that answers questions from three structured datasets and uses web search when the required information is not available locally.

The project uses **Mistral AI** as the LLM, **SQLite** for structured data, **Tavily** for web search, and **Streamlit** for the user interface.

## ✨ Features

- 🏛️ Query Bangladesh institutional information
- 🏥 Query Bangladesh hospitals and health facilities
- 🍽️ Query Bangladesh restaurant data
- 🌐 Use web search for general/current information
- 🤖 Automatic tool selection with Mistral AI
- 🧠 Natural-language questions converted into SQL
- 🔒 Read-only SQL execution
- 💬 Streamlit chat interface
- 🔎 Web-search fallback when a requested field is missing from a local dataset

## 🧠 Architecture

```text
User Question
      |
      v
+--------------------+
|    Mistral AI      |
|   LangChain Agent  |
+---------+----------+
          |
          | Selects tool
          |
   +------+------+----------------+
   |             |                |
   v             v                v
Institutions   Hospitals      Restaurants
DB Tool        DB Tool         DB Tool
   |             |                |
   v             v                v
SQLite        SQLite           SQLite

          OR

          v
     Web Search
       Tavily
          |
          v
Natural-Language Answer
```

## 🛠️ Technology Stack

- Python
- LangChain
- Mistral AI
- SQLite
- Hugging Face Datasets
- Tavily Search
- Streamlit
- Pandas
- python-dotenv

## 📁 Project Structure

```text
Multi-Tool AI Agent/
│
├── data/
│   ├── hospitals.db
│   ├── institutions.db
│   └── restaurants.db
│
├── .env
├── .gitignore
├── agent.py
├── build_databases.py
├── db_tools.py
├── db_utils.py
├── main.py
├── README.md
├── requirements.txt
├── streamlit_app.py
├── test_agent.py
└── web_search_tool.py
```

## 📚 Datasets

### 1. Institutional Information of Bangladesh

Source:  
https://huggingface.co/datasets/Mahadih534/Institutional-Information-of-Bangladesh

Database:

```text
data/institutions.db
```

Table:

```text
institutions
```

Example fields:

- Institution name
- EIIN
- Institution type
- Division
- District
- Thana
- Address
- Management type
- Education level
- Affiliation
- MPO status

### 2. All Bangladeshi Hospitals

Source:  
https://huggingface.co/datasets/Mahadih534/all-bangladeshi-hospitals

Database:

```text
data/hospitals.db
```

Table:

```text
hospitals
```

Example fields:

- Facility name
- Agency
- Type
- Division
- District
- City corporation
- Upazila
- Paurasava
- Union
- Private status

> **Limitation:** This dataset does not contain bed counts, doctor counts, treatment prices, or detailed facilities.

### 3. Bangladeshi Restaurant Data

Source:  
https://huggingface.co/datasets/Mahadih534/Bangladeshi-Restaurant-Data

Database:

```text
data/restaurants.db
```

Table:

```text
restaurants
```

Example fields:

- Restaurant name
- Rating
- Number of reviews
- Address
- Latitude
- Longitude
- Affluence

> **Limitation:** This dataset does not contain cuisine, menus, food prices, or opening hours.

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <YOUR_REPOSITORY_URL>
cd "Multi-Tool AI Agent"
```

### 2. Create a virtual environment

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

## 🔑 Environment Variables

Create a `.env` file in the project root:

```env
MISTRAL_API_KEY=your_mistral_api_key
TAVILY_API_KEY=your_tavily_api_key
```

Never commit your real API keys.

Recommended `.gitignore` entries:

```gitignore
.env
venv/
__pycache__/
data/*.db
```

## 🗄️ Build the Databases

Run:

```bash
python build_databases.py
```

This creates:

```text
data/institutions.db
data/hospitals.db
data/restaurants.db
```

## 🤖 Mistral Model

Example configuration:

```python
from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(
    model="ministral-8b-2512",
    temperature=0,
    max_retries=2
)
```

Use any tool-calling-capable Mistral model available to your account.

## 🧰 Agent Tools

### Institutions DB Tool
Used for schools, colleges, institutions, EIIN, MPO status, education level, location, management type, and affiliation.

### Hospitals DB Tool
Used for hospitals, health facilities, agency, type, division, district, upazila, and private/public status.

### Restaurants DB Tool
Used for restaurant names, ratings, reviews, addresses, and coordinates.

### Web Search Tool
Used for policies, definitions, current information, and information unavailable in the local databases.

## 🧪 Testing

Run:

```bash
python test_agent.py
```

Suggested test questions:

```text
How many institutions are in Dhaka district?
Show me 5 institutions in Chattogram.
How many health facilities are in Dhaka district?
Show me 5 Medical College Hospitals in Bangladesh.
Show me 5 highly rated restaurants with addresses containing Dhaka.
Which 5 restaurants have the highest number of reviews?
What is the role of DGHS in Bangladesh?
What does MPO mean in the Bangladesh education system?
How many beds does Dhaka Medical College Hospital have?
```

## 💻 Run the CLI

```bash
python main.py
```

## 🌐 Run the Streamlit App

```bash
streamlit run streamlit_app.py
```

The local app normally opens at:

```text
http://localhost:8501
```

## 📸 Screenshots

<img width="2559" height="1272" alt="image" src="https://github.com/user-attachments/assets/0b80f424-5919-4d2a-91b5-3ab837cafde8" />
<img width="2559" height="1280" alt="image" src="https://github.com/user-attachments/assets/8de610ed-eaf5-4eba-b6e1-93e2ad29be12" />


## 🔐 SQL Safety

Only read-only SQL queries are allowed.

Allowed:

```sql
SELECT *
FROM hospitals
LIMIT 5;
```

Blocked:

```sql
DELETE FROM hospitals;
DROP TABLE institutions;
UPDATE restaurants SET rating = 5;
```

## ❓ Why SQLite Instead of a Vector Database?

The three local datasets are structured/tabular data, so SQL is ideal for:

- Exact counts
- Filtering
- Sorting
- Grouping
- Aggregation
- Statistical queries

Example:

```text
How many hospitals are in Dhaka?
```

```sql
SELECT COUNT(*)
FROM hospitals
WHERE LOWER(district) = 'dhaka';
```

A vector database would be useful later for unstructured data such as PDFs, government reports, policies, circulars, and long documents.

## 🚀 Possible Future Improvements

- Add vector database + RAG for PDFs
- Add persistent chat history
- Add user authentication
- Add charts and analytics
- Add hospital/restaurant map visualization
- Show tool/source badges
- Show generated SQL
- Add streaming responses
- Add Bangla language support
- Add FastAPI backend
- Deploy Streamlit publicly

## 👨‍💻 Author

Asiful Alam Sami

Project: **Bangladesh Multi-Tool AI Agent**

## 📄 License

This project is intended for educational and demonstration purposes.
