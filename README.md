# AI Solution for SQL Queries

AI-powered CLI tool that converts natural language questions into SQL queries, executes them on Excel data, and provides human-readable explanations of results.

## Features

- Natural language to SQL query generation using OpenAI GPT-4o-mini
- Interactive CLI interface for asking data questions
- Automatic query validation and error handling
- Human-readable explanations of query results
- Excel file support via pandas and DuckDB

## Prerequisites

- Python 3.7+
- OpenAI API key

## Installation

1. Clone the repository:
```bash
git clone https://github.com/KostyaGost/ai-solution-for-sql-queries.git
```

2. Navigate to directory:
```bash
cd ai-solution-for-sql-queries
```

3. Create venv:
```bash
python -m venv .venv
```

4. Acivate venv:
```bash
source .venv/Scripts/activate
```

5. Install dependencies:
```bash
pip install -r requirements.txt
```

6. Configure environment:
```bash
cp .env.example .env && rm .env.example
```

7. Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=your-actual-api-key
```


## Running the Project

Start the CLI:
```bash
python main.py
```

The CLI will prompt you for questions. Type your data-related questions and press Enter. Type `exit` to quit.

### Example Usage

```
Question: Show me the top 5 records
Question: exit
```

## Running Tests

```bash
 python -m unittest tests.integrational_tests
```

## Project Structure


### Root Files

- **`main.py`** - Entry point that starts the CLI application
- **`cli.py`** - Interactive command-line interface implementation with user input validation and result display
- **`config.py`** - Configuration management: environment variables, valid keywords, and file paths
- **`llm_client.py`** - OpenAI API wrapper for creating chat completions with GPT-4o-mini
- **`client_api_request.py`** - Orchestrates LLM requests for input validation, SQL generation, and result explanations
- **`data_manager.py`** - Handles Excel data loading, SQL query execution via DuckDB, and schema generation
- **`prompts.py`** - Utility functions to load system prompt templates from text files
- **`requirements.txt`** - Python package dependencies
- **`.env.example`** - Template for environment variables (copy to `.env` and configure)
- **`README.md`** - Project documentation

### Directories

#### `data/`
Contains Excel data files for querying.

#### `tests/`
Contains **`integrational_tests.py`** - contains all integrational test for checking
correct working of program.  



### Environment Variables

- `OPENAI_API_KEY`: Your OpenAI API key (required)

### Data Configuration

- `DATA_PATH`: Path to Excel file (default: `data/Data Dump - Accrual Accounts.xlsx`)


## How It Works

1. User enters a natural language question
2. System validates question contains relevant keywords
3. LLM validates question is answerable with available schema
4. LLM generates SQL query based on schema and question
5. DuckDB executes query on DataFrame
6. Results displayed as markdown table
7. LLM generates explanation of results
8. Process repeats until user types `exit`
