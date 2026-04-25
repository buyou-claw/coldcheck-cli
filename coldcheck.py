#!/usr/bin/env python3
"""
ColdCheck CLI - AI-powered cold email analysis tool
Analyzes cold emails for effectiveness and provides improvement suggestions.
"""

import anthropic
import os
import sys
import argparse
from urllib.parse import urlparse

# Use environment variables for API access
client = anthropic.Anthropic(
    base_url=os.environ.get("ANTHROPIC_BASE_URL", "https://api.anthropic.com"),
    api_key=os.environ.get("ANTHROPIC_AUTH_TOKEN"),
)

ANALYSIS_PROMPT = """You are an expert at analyzing cold emails for sales, outreach, and networking purposes.

Analyze the cold email below and provide:
1. **Overall Score** (1-10) - How effective is this email?
2. **Subject Line** - What's good/bad about it? Suggestions?
3. **Personalization** - Does it feel personalized or generic?
4. **Value Proposition** - Is the benefit clear? Compelling?
5. **Call to Action** - Clear? Easy to respond to?
6. **Length** - Too long, too short, or just right?
7. **Top 3 Specific Improvements** - Actionable suggestions

Be direct and specific. Give real examples of what to change.

EMAIL TO ANALYZE:
---
{email_content}
---

Respond in this format exactly:
SCORE: [1-10]
SUBJECT: [analysis]
PERSONALIZATION: [analysis]
VALUE_PROP: [analysis]
CTA: [analysis]
LENGTH: [analysis]
TOP_IMPROVEMENTS:
1. [specific improvement]
2. [specific improvement]
3. [specific improvement]
"""


def analyze_email(email_content: str) -> str:
    """Send email to Claude for analysis."""
    try:
        response = client.messages.create(
            model=os.environ.get("ANTHROPIC_MODEL", "MiniMax-M2.7-highspeed"),
            max_tokens=1024,
            messages=[{
                "role": "user",
                "content": ANALYSIS_PROMPT.format(email_content=email_content)
            }]
        )

        # Extract text from response
        for block in response.content:
            if hasattr(block, 'text'):
                return block.text

        return "Error: No text in response"

    except Exception as e:
        return f"Error analyzing email: {e}"


def main():
    parser = argparse.ArgumentParser(
        description="ColdCheck CLI - Analyze cold emails for effectiveness"
    )
    group = parser.add_mutually_exclusive_group()
    group.add_argument(
        "-f", "--file",
        type=argparse.FileType('r'),
        help="Read email from file"
    )
    group.add_argument(
        "-t", "--text",
        type=str,
        help="Email text directly on command line"
    )
    group.add_argument(
        "url",
        nargs="?",
        type=str,
        help="URL to fetch email from"
    )

    args = parser.parse_args()

    email_content = None

    if args.file:
        email_content = args.file.read()
    elif args.text:
        email_content = args.text
    elif args.url:
        # Simple URL fetching - just get the page text
        try:
            import requests
            resp = requests.get(args.url, timeout=10)
            email_content = resp.text[:5000]  # Limit to first 5000 chars
        except Exception as e:
            print(f"Error fetching URL: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        # Interactive mode - read from stdin
        print("Paste your cold email below (Ctrl+D to finish):")
        print("---")
        email_content = sys.stdin.read()

    if not email_content or not email_content.strip():
        print("Error: No email content provided", file=sys.stderr)
        sys.exit(1)

    print("\n🔍 Analyzing your cold email...\n")
    result = analyze_email(email_content.strip())
    print(result)


if __name__ == "__main__":
    main()