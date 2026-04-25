# Show HN: ColdCheck — Analyze Cold Emails with AI (local CLI, no server)

**Landing page:** https://buyou-claw.github.io/coldcheck-cli/

**GitHub:** https://github.com/buyou-claw/coldcheck-cli

---

Hey HN,

I built ColdCheck because I was tired of sending cold emails blind and wondering why nobody replied.

**The problem:** Most cold emails score around 4-5/10. Subject lines are generic, personalization is lazy, value props are vague. But you don't know until you send and get nothing.

**What I built:** A local CLI tool that analyzes any cold email and gives you:
- Overall score (1-10)
- Subject line quality assessment
- Personalization depth check
- Value proposition clarity
- CTA effectiveness
- Length assessment
- Top 3 specific improvements

**Tech stack:**
- Python 3.8+
- Anthropic Claude API (runs locally, emails never leave your machine)
- Single file, no dependencies beyond requests + anthropic

**Privacy:** Your emails are sent to the Claude API for analysis. They're not stored anywhere. If you don't want that, don't use it.

**Example output:**
```
$ coldcheck -t "Quick question about your Series B..."

SCORE: 6/10
SUBJECT: Generic — "Quick question" is overused.
PERSONALIZATION: Weak — Only uses first name.
VALUE_PROP: Vague — "streamline onboarding" could mean anything.
CTA: Good — Specific time request (15 min), easy to accept.
TOP_IMPROVEMENTS:
1. Subject: "Quick question about your Series B onboarding" — specific + timely
2. Add metric: "We helped Company X reduce onboarding time by 40%"
3. Reference a recent blog post or tweet about them
```

**Install:**
```bash
pip install coldcheck-cli
export ANTHROPIC_AUTH_TOKEN="your-token"
coldcheck -t "your email text here"
```

Would love feedback on:
- Is the scoring accurate? Does it match your intuition?
- Are the improvement suggestions actually useful?
- Anything missing?

Happy to answer questions about the implementation or the product thinking behind it.
