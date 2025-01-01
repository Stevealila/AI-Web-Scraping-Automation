# AI Web Scraping Automation

This project demonstrates web scraping automation using LangChain, OpenAI, and Playwright. The script leverages a LangChain-powered agent to interact with web pages and extract structured information based on user commands.

## Features

- Automates web scraping tasks using natural language commands.
- Uses Playwright for browser automation.
- Employs OpenAI models for decision-making and reasoning.

---

## Installation

Follow the steps below to set up the project on your system.

### Prerequisites

- Python 3.11 or higher
- A valid OpenAI API key

---

### Setup on Windows

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/Stevealila/AI-Web-Scraping-Automation.git
   cd AI-Web-Scraping-Automation
   ```

2. **Create a Virtual Environment**:

   ```sh
   python -m venv .venv
   .\.venv\Scripts\activate
   ```

3. **Install Python Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Install Playwright Browsers**:

   ```sh
   playwright install
   ```

5. **Configure Environment Variables**:

   - Copy `.env.example` to `.env`:

     ```sh
     copy .env.example .env
     ```

   - Open `.env` and add your OpenAI API key:

     ```
     OPENAI_API_KEY=<your_openai_api_key>
     ```

6. **Run the Application**:

   ```sh
   python app.py
   ```

---

### Setup on Linux/macOS

1. **Clone the Repository**:

   ```sh
   git clone https://github.com/Stevealila/AI-Web-Scraping-Automation.git
   cd AI-Web-Scraping-Automation
   ```

2. **Create a Virtual Environment**:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install Python Dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Install Playwright Browsers**:

   ```sh
   playwright install
   ```

5. **Configure Environment Variables**:

   - Copy `.env.example` to `.env`:

     ```sh
     cp .env.example .env
     ```

   - Open `.env` and add your OpenAI API key:

     ```
     OPENAI_API_KEY=<your_openai_api_key>
     ```

6. **Run the Application**:

   ```sh
   python app.py
   ```

---

## Usage

- The application takes commands as input and uses LangChain and Playwright to execute them in the browser.

- Example command in the script:

  ```python
  command = {
      "input": "Go to https://github.com/stevealila and list highlighted the repositories. Print out url at each step."
  }
  ```

- The result will be printed in the terminal.

---

## Contributing

Feel free to fork this repository and submit pull requests for improvements or new features.

---

## License

This project is licensed under the MIT License. 
