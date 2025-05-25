# 🧠 Stock Analysis using MCP Local LLM (Ollama Qwen3) with LangChain

This project demonstrates how to build a fully local AI assistant that provides detailed stock analysis using:

- **MCP (Model Context Protocol)**: Enables structured tool usage by the language model.

- **Ollama**: A tool for running large language models locally.(**Qwen3**)

- **LangChain**: A framework for developing applications powered by language models and run as MCP Client

- **BeautifulSoup**: For web scraping financial data from Screener.in.

## 📦 Features

    🔍 Company Details: Retrieve company name, current price, market cap, PE ratio, ROE, ROCE, and more.

    📈 Profit Analysis: Extract quarterly and yearly net profit data.

    👥 Shareholding Patterns: Analyze holdings by promoters, DIIs, FIIs, and the public.

    🔧 Tool Integration: Seamless integration with MCP tools for enhanced functionality.


## ⚙️ Configuration
    MCP Server Setup
    
    The MCP server is defined in mcp_config.json.

    {
      "mcpServers": {
        "stock": {
          "command": "python",
          "args": ["StockMcp.py"],
          "transport": "stdio"
        }
      }
    }
    
    
    Give me the company details of CREDITACC.NS

## 🛠️ Project Structure

    ├── StockMcp.py         # MCP server with tool definitions
    ├── requirements.txt    # Python dependencies
    ├── README.md           # Project documentation

## 📚 Resources

    MCP Github

    Ollama Documentation

    LangChain MCP Documentation

    BeautifulSoup Documentation

