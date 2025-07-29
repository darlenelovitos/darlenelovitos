#!/usr/bin/env python3
"""
Script to update README.md with a random developer quote.
This script fetches quotes from a curated list and updates the README file.
"""

import random
import re
from pathlib import Path

# Curated list of inspiring developer quotes
DEV_QUOTES = [
    {
        "quote": "The most important single aspect of software development is to be clear about what you are trying to build.",
        "author": "Bjarne Stroustrup"
    },
    {
        "quote": "Code is like humor. When you have to explain it, it's bad.",
        "author": "Cory House"
    },
    {
        "quote": "First, solve the problem. Then, write the code.",
        "author": "John Johnson"
    },
    {
        "quote": "Experience is the name everyone gives to their mistakes.",
        "author": "Oscar Wilde"
    },
    {
        "quote": "In order to be irreplaceable, one must always be different.",
        "author": "Coco Chanel"
    },
    {
        "quote": "Java is to JavaScript what car is to Carpet.",
        "author": "Chris Heilmann"
    },
    {
        "quote": "Knowledge is power.",
        "author": "Francis Bacon"
    },
    {
        "quote": "Sometimes it pays to stay in bed on Monday, rather than spending the rest of the week debugging Monday's code.",
        "author": "Dan Salomon"
    },
    {
        "quote": "Perfection is achieved not when there is nothing more to add, but rather when there is nothing more to take away.",
        "author": "Antoine de Saint-Exupery"
    },
    {
        "quote": "Ruby is rubbish! PHP is phpantastic!",
        "author": "Nikita Popov"
    },
    {
        "quote": "Code never lies, comments sometimes do.",
        "author": "Ron Jeffries"
    },
    {
        "quote": "Simplicity is the soul of efficiency.",
        "author": "Austin Freeman"
    },
    {
        "quote": "Before software can be reusable it first has to be usable.",
        "author": "Ralph Johnson"
    },
    {
        "quote": "Make it work, make it right, make it fast.",
        "author": "Kent Beck"
    },
    {
        "quote": "Clean code always looks like it was written by someone who cares.",
        "author": "Robert C. Martin"
    },
    {
        "quote": "Any fool can write code that a computer can understand. Good programmers write code that humans can understand.",
        "author": "Martin Fowler"
    },
    {
        "quote": "Programming isn't about what you know; it's about what you can figure out.",
        "author": "Chris Pine"
    },
    {
        "quote": "The best error message is the one that never shows up.",
        "author": "Thomas Fuchs"
    },
    {
        "quote": "A language that doesn't affect the way you think about programming is not worth knowing.",
        "author": "Alan Perlis"
    },
    {
        "quote": "The most disastrous thing that you can ever learn is your first programming language.",
        "author": "Alan Kay"
    }
]

def get_random_quote():
    """Get a random quote from the quotes list."""
    return random.choice(DEV_QUOTES)

def update_readme_quote():
    """Update the README.md file with a new random quote."""
    readme_path = Path("README.md")
    
    if not readme_path.exists():
        print("ERROR: README.md not found!")
        return False
    
    # Read current README content
    content = readme_path.read_text(encoding='utf-8')
    
    # Get a random quote
    quote_data = get_random_quote()
    new_quote_line = f'*"{quote_data["quote"]}"* - **{quote_data["author"]}**'
    
    # Pattern to match the quote section
    pattern = r'<!-- QUOTE:START -->\n.*?\n<!-- QUOTE:END -->'
    replacement = f'<!-- QUOTE:START -->\n{new_quote_line}\n<!-- QUOTE:END -->'
    
    # Replace the quote section
    new_content = re.sub(pattern, replacement, content, flags=re.DOTALL)
    
    # Write back to README
    readme_path.write_text(new_content, encoding='utf-8')
    
    print(f"✅ Updated README with quote from {quote_data['author']}")
    print(f"📝 Quote: {quote_data['quote']}")
    
    return True

if __name__ == "__main__":
    success = update_readme_quote()
    if not success:
        exit(1)
