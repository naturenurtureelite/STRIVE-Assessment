import re

def extract_strengths_weaknesses(text):
    # Keywords to identify strengths and weaknesses
    strengths_keywords = ["strength"]
    weaknesses_keywords = ["weakness"]

    # Compile regex patterns
    strengths_pattern = re.compile(r'\b(?:' + '|'.join(strengths_keywords) + r')\b', re.IGNORECASE)
    weaknesses_pattern = re.compile(r'\b(?:' + '|'.join(weaknesses_keywords) + r')\b', re.IGNORECASE)

    # Split text into sentences
    sentences = re.split(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', text)

    # Extract sentences matching strengths and weaknesses
    strengths = [sentence for sentence in sentences if strengths_pattern.search(sentence)]
    weaknesses = [sentence for sentence in sentences if weaknesses_pattern.search(sentence)]

    return {"strengths": strengths, "weaknesses": weaknesses}


# Example usage
text = """<Put your text here> """

results = extract_strengths_weaknesses(text)

print("Strengths:")
for strength in results["strengths"]:
    print(f"- {strength.strip()}")

print("\nWeaknesses:")
for weakness in results["weaknesses"]:
    print(f"- {weakness.strip()}")