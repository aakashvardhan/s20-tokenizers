from base import Tokenizer, get_stats, merge


class BasicTokenizer(Tokenizer):

    def __init__(self):
        super().__init__()

    def train(self, text, vocab_size, verbose=False):
        # Tokenizer can train a vocabulary of size vocab_size from text
        assert vocab_size >= 256, "vocab_size must be at least 256"
        num_merges = vocab_size - 256

        # Input text preprocessing
        text = text.encode("utf-8")  # convert to bytes
        ids = list(map(int, text))  # convert to list of integers

        # Iterate over the number of merges
        merges = {}  # (int, int) -> int
        vocab = {idx: bytes([idx]) for idx in range(256)}  # int -> bytes
        for i in range(num_merges):
            # Get the stats
            pairs = get_stats(ids)
            # Merge the most frequent pair
            best = max(pairs, key=pairs.get)
            idx = 256 + i
            ids = merge(ids, best, idx)
            merges[best] = idx
            # Update the vocab
            vocab[idx] = vocab[best[0]] + vocab[best[1]]

            if verbose and (i + 1) % 100 == 0:
                print(
                    f"Merge {i + 1} / {num_merges}: {best} -> {idx} ({vocab[idx]}) had {pairs[best]} occurrences"
                )
        self.merges = merges
        self.vocab = vocab

    def encode(self, text):
        # Tokenizer can encode a string into a list of integers
        text = text.encode("utf-8")  # convert to bytes
        ids = list(map(int, text))  # convert to list of integers
        while len(ids) >= 2:
            # find pair with lowest merge idx
            stats = get_stats(ids)
            best = min(stats, key=lambda p: (self.merges.get(p, float("inf"))))
            if best not in self.merges:
                break

            idx = self.merges[best]
            ids = merge(ids, best, idx)
        return ids

    def decode(self, ids):
        # Tokenizer can decode a list of integers into a string
        text_bytes = b"".join([self.vocab[i] for i in ids])
        text = text_bytes.decode("utf-8", errors="replace")
        return text
