# Boot.dev Static Site Generator (Python)

A guided project from [Boot.dev](https://boot.dev) where you'll build your own static site generator from scratch in Python—learning core principles of OOP and functional programming along the way.

---

## Overview

This project is designed as a guided learning experience rather than a production-ready SSG. You'll learn by implementing:

- Parsing of content files (Markdown, HTML)
- Applying templates (e.g., via HTML templates like `template.html`)
- Building a basic development server (`server.py`)
- Automating generation through shell scripts (`build.sh`, `main.sh`)
- Validating output with tests (`test.sh`)
- Organizing assets in a `static/` directory

---

## Prerequisites

- **Python 3.7+**  
- A terminal or shell environment (macOS/Linux/WSL or PowerShell/Command Prompt on Windows)  
- Optional: A modern code editor (e.g., VS Code) for ease of editing and running scripts

---
## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <your-project>
   ```
2. Install any dependencies (if specified in src/requirements.txt, otherwise just proceed).

## How it works
1. Write your content in content/—this might include Markdown or HTML files.
2. Build command (./build.sh or ./main.sh) runs the generator:
   - Reads content/, processes with logic from src/
   - Wraps content with template.html
   - Copies static files from static/ to the output directory (e.g., dist/)
3. View locally with python server.py—often hosting at http://localhost:8000
4. Run tests via ./test.sh to ensure everything works as expected.

## Usage
to build and preview the site
```bash
./build.sh
python server.py
# Navigate to: http://localhost:8000
```
to run tests
```bash
./test.sh
```

