# ColdCheck CLI

AI-powered cold email analysis tool that runs locally. No Cloudflare, no Stripe, no deployment needed.

## What it does

Analyzes cold emails for:
- Overall effectiveness score (1-10)
- Subject line quality
- Personalization assessment
- Value proposition clarity
- Call-to-action effectiveness
- Length assessment
- Top 3 specific improvements

## Quick Start

```bash
# Set up environment (once)
export ANTHROPIC_BASE_URL="https://api.minimaxi.com/anthropic"
export ANTHROPIC_AUTH_TOKEN="your-api-token"

# Run with email text
python3 coldcheck.py -t "Subject: Quick question...

Hi Sarah,

I noticed your company just raised a Series B. Congratulations!

I'm reaching out because we help B2B SaaS companies streamline their onboarding process. Would you be open to a quick 15-minute call this week?

Best,
John"

# Run with file input
python3 coldcheck.py -f email.txt

# Interactive mode (paste email)
python3 coldcheck.py

# From URL (if email is hosted somewhere)
python3 coldcheck.py https://example.com/email.txt
```

## Requirements

- Python 3.8+
- `requests` library (`pip install requests`)
- `anthropic` library (`pip install anthropic`)
- ANTHROPIC_AUTH_TOKEN environment variable

## Example Output

```
SCORE: 6/10
SUBJECT: Generic - "Quick question" is overused. Try something more specific.
PERSONALIZATION: Weak - Only uses first name. Reference something specific.
VALUE_PROP: Vague - "streamline onboarding" could mean anything.
CTA: Good - Specific time request (15 min), easy to accept.
LENGTH: Short - Good for cold outreach, but could use more credibility proof.
TOP_IMPROVEMENTS:
1. Subject: "Quick question about your Series B onboarding" - specific + timely
2. Add one specific result metric: "We helped Company X reduce onboarding time by 40%"
3. Personalization: Reference a recent blog post, tweet, or news about them
```

## Use Cases

- Sales teams improving outreach templates
- Recruiters writing better candidate messages
- Founders crafting investor introductions
- Anyone doing cold outreach

## Privacy

Your emails are sent to the Claude API for analysis. The emails are not stored anywhere.

## License

MIT