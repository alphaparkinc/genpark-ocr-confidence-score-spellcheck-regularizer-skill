import re
from typing import Dict, Any, List, Optional

class OCRConfidenceScoreSpellcheckRegularizer:
    """
    Repairs common optical character recognition (OCR) transcription artifacts,
    such as 'rn' -> 'm', digit-letter confusions ('0' vs 'O', '1' vs 'l'), and ligature splitting.
    """
    COMMON_OCR_GLYPH_FIXES = [
        (r"\brn(?=[aeiou])", "m"),
        (r"(\d+)O(\d+)", r"\g<1>0\g<2>"),
        (r"\b([A-Z]+)0([A-Z]+)\b", r"\g<1>O\g<2>"),
        (r"\b([a-z]+)1([a-z]+)\b", r"\g<1>l\g<2>"),
        (r"ﬁ", "fi"),
        (r"ﬂ", "fl"),
        (r"æ", "ae")
    ]

    def regularize_tokens(self, tokens: List[Dict[str, Any]], min_confidence_threshold: float = 0.75) -> Dict[str, Any]:
        corrected_tokens: List[Dict[str, Any]] = []
        corrections_count = 0

        for tok in tokens:
            text = tok.get("text", "")
            conf = tok.get("confidence", 1.0)
            orig_text = text

            for pat, repl in self.COMMON_OCR_GLYPH_FIXES:
                if re.search(pat, text):
                    text = re.sub(pat, repl, text)

            was_repaired = text != orig_text
            if was_repaired:
                corrections_count += 1

            corrected_tokens.append({
                "original_text": orig_text,
                "repaired_text": text,
                "confidence": conf,
                "was_repaired": was_repaired
            })

        repaired_string = " ".join(t["repaired_text"] for t in corrected_tokens)

        return {
            "total_tokens": len(tokens),
            "corrections_applied": corrections_count,
            "repaired_string": repaired_string,
            "tokens": corrected_tokens
        }
