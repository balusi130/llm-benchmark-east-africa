import argparse
import json
import os
from datetime import datetime


def generate_report(results: list, output_path: str):
    """Generate a simple HTML report from benchmark results."""
    total = len(results)
    if total == 0:
        print("No results to report.")
        return

    avg_score = sum(r["score"] for r in results) / total
    by_category = {}
    for r in results:
        cat = r["category"]
        by_category.setdefault(cat, []).append(r["score"])

    rows = ""
    for r in results:
        color = "#d4edda" if r["score"] >= 0.7 else "#fff3cd" if r["score"] >= 0.4 else "#f8d7da"
        rows += f"<tr style='background:{color}'><td>{r['category']}</td><td>{r['prompt'][:80]}...</td><td>{r['score']*100:.0f}%</td></tr>"

    category_summary = ""
    for cat, scores in by_category.items():
        avg = sum(scores) / len(scores)
        category_summary += f"<li><strong>{cat}</strong>: {avg*100:.1f}% avg ({len(scores)} prompts)</li>"

    html = f"""<!DOCTYPE html>
<html>
<head><title>LLM Benchmark Report</title>
<style>body{{font-family:sans-serif;max-width:900px;margin:40px auto;padding:0 20px}}
table{{width:100%;border-collapse:collapse}}th,td{{padding:8px;text-align:left;border:1px solid #ddd}}
th{{background:#343a40;color:white}}</style></head>
<body>
<h1>LLM Benchmark — East African Dialects</h1>
<p>Generated: {datetime.now().strftime("%Y-%m-%d %H:%M")}</p>
<h2>Overall Score: {avg_score*100:.1f}%</h2>
<h3>By Category</h3><ul>{category_summary}</ul>
<h3>All Results</h3>
<table><tr><th>Category</th><th>Prompt</th><th>Score</th></tr>{rows}</table>
</body></html>"""

    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as f:
        f.write(html)
    print(f"Report saved to {output_path}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="results/results.json")
    parser.add_argument("--output", default="results/report.html")
    args = parser.parse_args()

    with open(args.input) as f:
        results = json.load(f)
    generate_report(results, args.output)


if __name__ == "__main__":
    main()
