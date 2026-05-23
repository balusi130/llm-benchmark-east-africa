# LLM Benchmark — East African Dialects

Most LLM benchmarks are built entirely on Western English datasets, which makes it hard to know how well these models actually perform in East African contexts — whether that is formal Swahili, code-switched English/Swahili conversations, Sheng, or fintech reasoning grounded in things like M-Pesa transactions.

This project is my attempt to fill that gap. I built a benchmarking suite that tests frontier models across 500+ carefully written prompts covering grammar, logical reasoning, cultural context, and multi-step fintech problem solving. The results were interesting — and in some areas, pretty damning for the models.

---

## What it tests

| Category | Prompts | Description |
|----------|---------|-------------|
| Swahili Grammar & Syntax | 120 | Formal grammar, tense agreement, vocabulary |
| Code-Switched Dialogue | 150 | Mixed English/Swahili as used in real conversations |
| Fintech Reasoning (M-Pesa) | 130 | Multi-step transaction problems, fee calculations, error handling |
| CoT Logic & Math | 100 | Chain-of-thought reasoning grounded in local contexts |
| **Total** | **500+** | |

---

## Models tested

- GPT-4o
- Claude 3.5 Sonnet
- Gemini Pro

---

## Stack

- Python 3.10+
- OpenAI API / Anthropic API
- Pandas + NumPy for scoring
- Matplotlib for visualisation
- JSON prompt datasets

---

## Setup

```bash
git clone https://github.com/balusi130/llm-benchmark-east-africa.git
cd llm-benchmark-east-africa
pip install -r requirements.txt
```

Set your API keys:

```bash
export OPENAI_API_KEY=your_key_here
export ANTHROPIC_API_KEY=your_key_here
```

---

## Running the benchmarks

Run everything:

```bash
python benchmark.py --model gpt-4o --category all
```

Run a specific category:

```bash
python benchmark.py --model claude-3-5 --category swahili_grammar
```

Generate an HTML report:

```bash
python report.py --output results/report.html
```

---

## Key findings

- GPT-4o scored highest on formal Swahili grammar (78% accuracy)
- All three models struggled significantly with Sheng — average accuracy was 34%
- Fintech CoT reasoning showed hallucination rates between 22–41% across all models
- Claude 3.5 outperformed on multi-step logical reasoning in code-switched prompts
- None of the models handled M-Pesa error codes or edge case transactions reliably

---

## Project layout

```
llm-benchmark-east-africa/
├── benchmark.py
├── report.py
├── prompts/
│   ├── swahili_grammar.json
│   ├── code_switched.json
│   ├── fintech_reasoning.json
│   └── cot_logic.json
├── scoring/
│   └── evaluator.py
├── results/
│   └── sample_report.html
├── requirements.txt
└── README.md
```

---

## Contributing

If you have East African language datasets, prompt ideas, or want to add more models to the comparison, open an issue or a PR — contributions are very welcome.

---

MIT License