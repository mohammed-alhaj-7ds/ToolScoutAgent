# 🚀 ToolScoutAgent

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![GitHub Repo](https://img.shields.io/badge/GitHub-Repo-blueviolet)](https://github.com/mohammed-alhaj-7ds/ToolScoutAgent)
[![Open Issues](https://img.shields.io/github/issues/mohammed-alhaj-7ds/ToolScoutAgent)](https://github.com/mohammed-alhaj-7ds/ToolScoutAgent/issues)

**An AI-powered agent that discovers, analyzes, and recommends developer tools.**  
🔍 Helps developers quickly find, analyze, and choose the best tools and technologies.

---

## 📁 Project Structure

```

ToolScoutAgent/
├── main.py              # Entry point to run the program
├── pyproject.toml       # Project configuration and dependencies
├── README.md            # This file
├── src/                 # Main source code
│   ├── firecrawl.py     # Firecrawl interface for searching and scraping 🕵️‍♂️
│   ├── **init**.py      # Makes src a Python package 📦
│   ├── models.py        # Data models (Pydantic) 📝
│   ├── prompts.py       # All LLM prompts 💬
│   └── workflow.py      # Workflow for research and recommendations 🔄
│   ├── streamlit.py     #Gul
│   ├──requirements.txt
└── uv.lock              # Dependency lock file 🔒

````

> **Explanation:**  
- `main.py`: Launches the agent and handles user queries.  
- `src/firecrawl.py`: Communicates with Firecrawl API for searching and scraping web data.  
- `src/models.py`: Defines structured data models for companies, tools, and research state.  
- `src/prompts.py`: Contains all AI prompts for tool extraction, analysis, and recommendations.  
- `src/workflow.py`: Implements the workflow steps: extract tools → research → analyze → recommend.  

---

## 🛠️ Project Overview

**ToolScoutAgent** is a developer-focused AI agent that:

- 🔹 **Extracts** relevant developer tools from online articles and company websites.  
- 🔹 **Analyzes** companies and tools from a developer’s perspective: tech stack, APIs, integration, pricing, and language support.  
- 🔹 **Provides concise recommendations** to help developers choose the right tools quickly.  

---

## ✨ Key Features

- 🔍 **Automatic tool discovery**  
- 📊 **Structured insights** on pricing, tech stack, APIs, languages, and integrations  
- 📝 **Actionable recommendations** for developers  
- 🤖 **AI-powered analysis** with GPT-4o-mini for developer-focused insights  

---

## ⚡ Installation

1. Clone the repository:
```bash
git clone https://github.com/mohammed-alhaj-7ds/ToolScoutAgent.git
cd ToolScoutAgent
````

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Set your Firecrawl API key in a `.env` file:

```env
FIRECRAWL_API_KEY=your_api_key_here
```

---

## ▶️ Usage

Run the main script:

```bash
python main.py
```

* Type your query about developer tools.
* The agent will automatically search, scrape, and analyze relevant tools and companies.
* To exit, type `exit` or `quit`.

---

## 📚 Example Output

```
🔍 Developer Tools Query: Python database tools

1. 🏢 Supabase
   🌐 Website: https://supabase.com
   💰 Pricing: Freemium
   🛠️ Tech Stack: PostgreSQL, JavaScript, Python
   💻 Language Support: JavaScript, Python, Go
   🔌 API: ✅ Available
   🔗 Integrations: GitHub, Docker, AWS
   📝 Description: Open-source backend as a service for developers.

Developer Recommendations:
- Supabase is ideal for rapid backend development with free tier options. 
- Strong API support and seamless integration with popular tools.
```

---

## 🎨 Screenshots

> **Example interaction in terminal:**

```
🔍 Developer Tools Query: CI/CD tools

1. 🏢 GitHub Actions
   🌐 Website: https://github.com/features/actions
   💰 Pricing: Free/Paid tiers
   🛠️ Tech Stack: GitHub, YAML, Docker
   🔌 API: ✅ Available
   🔗 Integrations: GitHub, AWS, Docker
   📝 Description: Automate workflows and CI/CD pipelines directly in GitHub.

Developer Recommendations:
- GitHub Actions is best for projects already hosted on GitHub.
- Provides deep integration with GitHub repositories and CI/CD workflows.
```

---

## 💡 How It Works

1. **Tool Extraction:** Searches articles for relevant tools using AI.
2. **Research & Scraping:** Uses Firecrawl API to get company/tool pages.
3. **Analysis:** AI analyzes pricing, APIs, integrations, and tech stack.
4. **Recommendations:** Generates concise developer-focused suggestions.

---

## 📌 Contribution

Contributions are welcome!

* Fork the repo
* Create your feature branch (`git checkout -b feature/your-feature`)
* Commit your changes (`git commit -m 'Add new feature'`)
* Push to the branch (`git push origin feature/your-feature`)
* Open a Pull Request

---

## 📝 License

MIT License © 2025

