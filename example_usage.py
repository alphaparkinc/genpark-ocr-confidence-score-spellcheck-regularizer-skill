import json
from client import OCRConfidenceScoreSpellcheckRegularizer

def main():
    regularizer = OCRConfidenceScoreSpellcheckRegularizer()
    tokens = [
        {"text": "The", "confidence": 0.98},
        {"text": "rnodern", "confidence": 0.62},
        {"text": "ﬁnancial", "confidence": 0.85},
        {"text": "sys1em", "confidence": 0.55}
    ]
    result = regularizer.regularize_tokens(tokens)
    print("OCR Regularization Result:")
    print(json.dumps(result, indent=2))
    assert result["tokens"][1]["repaired_text"] == "modern"
    assert result["tokens"][2]["repaired_text"] == "financial"
    assert result["tokens"][3]["repaired_text"] == "system"
    print("OCR spellcheck regularizer verification: PASS")

if __name__ == "__main__":
    main()
