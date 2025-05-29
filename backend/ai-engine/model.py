# ai-engine/model.py
from transformers import pipeline
from config import MODEL_NAME


classifier = pipeline("text-classification", model=MODEL_NAME)

def analyze_message(message: str):
    result = classifier(message)
    label = result[0]['label']
    score = result[0]['score']
    verdict = "fraud" if label.lower() in ["negative", "spam", "toxic"] else "safe"
    return {
        "label": label,
        "score": score,
        "verdict": verdict
    }

# At the bottom of ai-engine/model.py

if __name__ == "__main__":
    test_msg = "Congratulations! You've won a $1000 gift card. Click the link to claim now."
    result = analyze_message(test_msg)
    print("AI Engine Test Result:")
    print(result)
