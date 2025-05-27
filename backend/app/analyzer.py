import spacy
import json
from pathlib import Path
from transformers import pipeline

scam_data = json.loads(Path(__file__).with_name("scam_patterns.json").read_text())
scam_phrases = scam_data["phrases"]
scam_entities = scam_data["entities"]

nlp = spacy.load("en_core_web_sm")
classifier = pipeline("text-classification", model="distilbert-base-uncased-finetuned-sst-2-english")

def analyze_message(text: str) -> dict:
    doc = nlp(text)
    entities = [ent.text for ent in doc.ents]
    
    classification = classifier(text)[0]
    label = classification['label']
    score = classification['score']

    flags = []

    for phrase in scam_phrases:
        if phrase.lower() in text.lower():
            flags.append(f"Suspicious phrase: '{phrase}'")

    for ent in scam_entities:
        if ent.lower() in text.lower():
            flags.append(f"Known entity mentioned: '{ent}'")

    if label == "NEGATIVE" and score > 0.7:
        flags.append("Negative tone detected (potential fear/guilt tactic)")

    return {
        "text": text,
        "classification": label,
        "confidence": round(score, 2),
        "entities": entities,
        "flags": flags
    }
