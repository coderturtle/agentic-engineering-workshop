from collections import Counter


def top_n_words(text: str, n: int) -> list:
    """Return the n most frequent words in text, most frequent first."""
    words = text.lower().split()
    counts = Counter(words)
    ranked = sorted(counts.items(), key=lambda kv: (-kv[1], kv[0]))
    return [w for w, _ in ranked[:n]]
