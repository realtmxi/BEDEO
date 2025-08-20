# BEDEO - Multi-Agent Research & Data Extraction System

A comprehensive research assistant and data extraction platform built with **AutoGen AgentChat**, **Chainlit UI**, and **GitHub-hosted LLMs** on Azure Inference. BEDEO combines academic research capabilities with advanced web crawling and ontology-based data structuring.

It simulates a full AI research and data extraction pipeline:
- 📚 **Literature Agent** – searches papers from arXiv & web sources
- 🕷️ **Web Crawling Agent** – extracts and structures data from websites using BEDEO ontology
- 📄 **Document Analysis Agent** – analyzes PDFs and documents
- ❓ **Q&A Agent** – answers follow-up questions from extracted content
- 🏗️ **BEDEO Ontology Tools** – transforms unstructured data into structured formats

---

## 🚀 Features

### 🔍 Academic Research
- Dynamic academic search with arXiv integration
- Multi-source literature discovery and recommendation
- Citation analysis and research trend identification

### 🕷️ Web Crawling & Data Extraction
- **Enhanced Web Crawling Agent** with ontology-based transformations
- **BEDEO Ontology Integration** for structured data output
- Customizable schemas and few-shot learning capabilities
- PDF content extraction from web URLs
- Multi-depth crawling with configurable parameters

### 📄 Document Intelligence
- Multi-mode document analysis: "rapid", "academic", "visual", "enhanced"
- PDF processing and text extraction
- Content summarization and key insight identification
- Data visualization from document content

### 🧠 Smart Q&A System
- Context-aware question answering
- Integration with crawled and analyzed content
- External search augmentation for comprehensive responses

### 🗂 Modular Architecture
- **AutoGen + Chainlit** integration for conversational AI
- **Multi-Agent Router** for intelligent task distribution
- **Pluggable LLMs**: `gpt-4o`, `LLaMA`, `Mistral`, or custom Azure deployments

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **Agents** | `autogen-agentchat`, `autogen-core` |
| **Web Crawling** | `requests`, `beautifulsoup4`, `PyPDF2` |
| **Ontology** | `rdflib`, Custom BEDEO TTL parser |
| **LLMs** | GitHub-hosted models on Azure Inference |
| **Frontend** | `Chainlit` for conversational UI |
| **PDF Processing** | `PyMuPDF`, `PyPDF2` |
| **Data Processing** | `pandas`, `numpy`, `matplotlib` |

---

## 📂 Project Structure

```
BEDEO/
├── agents/
│   ├── literature_agent.py              # Academic paper search
│   ├── enhanced_web_crawling_agent.py   # Advanced web crawling
│   ├── web_crawling_agent.py           # Basic web crawling
│   ├── paper_review_agent.py           # Document analysis
│   └── qa_agent.py                     # Question answering
├── tools/
│   ├── web_crawling_tools.py           # Web scraping utilities
│   ├── bedeo_ontology_tool.py          # BEDEO ontology parser
│   ├── arxiv_search_tool.py            # ArXiv integration
│   ├── review_tools.py                 # Document processing
│   └── qa_tools.py                     # Q&A utilities
├── orchestrator/
│   └── multi_agent_router.py           # Intelligent agent routing
├── ontology/
│   └── bedeo.ttl                       # BEDEO ontology definition
├── app.py                              # Chainlit entry point
├── requirements.txt                     # Python dependencies
├── environment.yml                      # Conda environment
└── README.md
```

---

## ⚙️ Setup

### 📦 Option 1: Conda Environment (Recommended)

```bash
conda env create -f environment.yml
conda activate agent
```

### 💡 Option 2: Pip Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```

---

## 🔐 Configure Environment

Create a `.env` file:
```env
GITHUB_TOKEN=ghp_XXXXXXXXXXXXXXXXXXXXX
```

---

## 🚀 Run the System

```bash
chainlit run app.py
```

Then open [http://localhost:8000](http://localhost:8000)

---

## 🎯 Use Cases

### 🔍 Academic Research
- "Search for top papers on temporal graph neural networks"
- "Find recent research on quantum machine learning"
- "Recommend papers in computer vision"

### 🕷️ Web Crawling & Data Extraction
- "Crawl this website and extract structured data"
- "Extract real estate opportunities from this URL"
- "Transform this webpage content using BEDEO ontology"
- "Scrape and structure data from multiple URLs"

### 📄 Document Analysis
- "Analyze this PDF in enhanced mode"
- "Give me a visual summary of this paper"
- "Extract key findings from this document"

### ❓ Knowledge Q&A
- "What is a temporal point process?"
- "Explain the BEDEO ontology structure"
- "How does web crawling work in this system?"

---

## 🏗️ BEDEO Ontology

The system includes a comprehensive ontology for structuring real estate and development opportunity data:

- **Organization** → **Opportunity** → **RealEstateAsset** → **Address**
- Supports structured data transformation from unstructured web content
- Customizable schemas for different data domains
- RDF/Turtle output format for semantic web integration

---

## 🔧 Key Components

### Enhanced Web Crawling Agent
- **URL Processing**: Handles single URLs and URL lists
- **Content Extraction**: HTML, PDF, and text content parsing
- **Ontology Integration**: Transforms data using BEDEO vocabulary
- **Structured Output**: Generates organized (URL, content) pairs

### Multi-Agent Router
- **Intelligent Routing**: Automatically detects user intent
- **Dynamic Agent Selection**: Routes to appropriate specialized agents
- **Streaming Support**: Real-time token streaming for better UX

### Literature Agent
- **ArXiv Integration**: Direct access to academic papers
- **Web Search**: DuckDuckGo integration for broader research
- **Citation Analysis**: Identifies research trends and connections

---

## 📊 Limitations

- Azure Inference requires correct PAT and model permissions
- Some models do not support auto tool calling (manual fix required)
- Large PDFs are chunked to avoid context overflows
- Web crawling respects robots.txt and implements rate limiting

---

## 🔮 Future Work

- [ ] Add memory and persistent context across sessions
- [ ] Integrate PubMed, Semantic Scholar APIs
- [ ] Stream output for long responses
- [ ] Full PDF upload pipeline via Chainlit
- [ ] Enhanced BEDEO ontology extensions
- [ ] Multi-language web crawling support
- [ ] Advanced data visualization tools

---

## 🤝 Contributing

We welcome contributions! Please feel free to:
- Report bugs and feature requests
- Submit pull requests
- Improve documentation
- Extend the BEDEO ontology

---

## 📜 License

MIT License. Use freely, modify creatively, contribute collaboratively.

---

## 🙏 Credits

- **Microsoft AutoGen** - Multi-agent framework
- **GitHub Models on Azure Inference** - LLM hosting
- **Chainlit.io** - Conversational UI framework
- **BEDEO Project** - Ontology and domain expertise