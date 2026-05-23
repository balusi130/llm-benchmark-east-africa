import argparse
import json
import os
from scoring.evaluator import evaluate_response
from openai import OpenAI
import anthropic

CATEGORIES = ["swahili_grammar", "code_switched", "fintech_reasoning", "cot_logic"]

openai_client = OpenAI()
anthropic_client = anthropic.Anthropic()


def load_prompts(category):
    path = os.path.join("prompts", f"{category}.json")
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)


def run_openai(prompt):
    response = openai_client.chat.completions.create(
        model="gpt-4o",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def run_anthropic(prompt):
    response = anthropic_client.messages.create(
        model="claude-3-5-sonnet-20241022",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.content[0].text


def run_benchmark(model, category):
    categories = CATEGORIES if category == "all" else [category]
    results = []

    for cat in categories:
        prompts = load_prompts(cat)
        print(f"\nRunning {cat} ({len(prompts)} prompts) on {model}...")

        for item in prompts:
            if model == "gpt-4o":
                response = run_openai(item["prompt"])
            elif model == "claude-3-5":
                response = run_anthropic(item["prompt"])
            else:
                print(f"Unknown model: {model}")
                return

            score = evaluate_response(response, item.get("expected"))
            results.append({
                "category": cat,
                "prompt": item["prompt"][:80],
                "score": score
            })
            print(f"  [{score:.0%}] {item[prompt][:60]}...")

    total = sum(r["score"] for r in results) / len(results) if results else 0
    print(f"\nOverall score on {model}: {total:.1%}")
    return results


def main():
    parser = argparse.ArgumentParser(description="LLM Benchmark — East African Dialects")
    parser.add_argument("--model", required=True, choices=["gpt-4o", "claude-3-5"], help="Model to benchmark")
    parser.add_argument("--category", default="all", choices=CATEGORIES + ["all"])
    args = parser.parse_args()
    run_benchmark(args.model, args.category)


if __name__ == "__main__":
    main()
