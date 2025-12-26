# Project Setup Guide

Welcome to this amazing project! This guide will help you set up your development environment quickly and efficiently.

## Prerequisites

Before you begin, make sure you have the following installed:
- Python 3.x
- pip3

## Installation Steps

### 1. Create Virtual Environment

First, install virtualenv and create a new virtual environment:

```bash
pip3 install virtualenv
virtualenv my_env
```

### 2. Activate Virtual Environment

Activate your virtual environment:

```bash
# On Windows
my_env\Scripts\activate

# On macOS/Linux
source my_env/bin/activate
```

### 3. Install Required Dependencies

Install all the necessary libraries for the project:

```bash
pip install langchain==0.1.11 gradio==5.23.2 transformers==4.38.2 bs4==0.0.2 requests==2.31.0 torch==2.2.1
```

## 📦 Dependencies

| Package | Version | Description |
|---------|---------|-------------|
| `langchain` | 0.1.11 | 🔗 Framework for developing applications powered by language models |
| `gradio` | 5.23.2 | 🎨 Machine learning model interfaces |
| `transformers` | 4.38.2 | 🤗 State-of-the-art Natural Language Processing |
| `bs4` | 0.0.2 | 🕷️ Beautiful Soup for web scraping |
| `requests` | 2.31.0 | 🌐 HTTP library for Python |
| `torch` | 2.2.1 | 🔥 PyTorch deep learning framework |

## Quick Start

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd <your-project-name>
   ```

2. **Follow the installation steps above**

3. **Run your application**
   ```bash
   python main.py
   ```

## 🔧 Troubleshooting

### Common Issues

- **Virtual environment not activating?** Make sure you're using the correct path separator for your OS
- **Package installation fails?** Try upgrading pip: `pip install --upgrade pip`
- **Permission errors?** On some systems, you might need to use `pip3` instead of `pip`

## 📚 Additional Resources

- [Python Virtual Environments Guide](https://docs.python.org/3/tutorial/venv.html)
- [LangChain Documentation](https://python.langchain.com/)
- [Gradio Documentation](https://gradio.app/docs/)

## License
Copyrights : IBM Coursera Course

This Project is from IBM's GenAI Speciliazation Course


