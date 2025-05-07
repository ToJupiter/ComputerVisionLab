import re

def fix_math_dollars(md_text):
    # Replace inline math $...$ with $$...$$, but not if already $$...$$
    # Negative lookbehind and lookahead to avoid $$...$$
    pattern = re.compile(r'(?<!\$)\$(?!\$)(.+?)(?<!\$)\$(?!\$)', re.DOTALL)
    fixed_text = pattern.sub(r'$$\1$$', md_text)
    return fixed_text

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    fixed_content = fix_math_dollars(content)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(fixed_content)

if __name__ == "__main__":
    # Change the path to your markdown file
    md_file = "../docs/LinearAlgebra/Chapter1_2.md"
    process_file(md_file)
    print("Math dollar signs fixed.")