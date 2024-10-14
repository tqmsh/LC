class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False
        self.word = None  # Store the word at the end of the word

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True
        node.word = word  # Store the full word

    def search_prefix(self, prefix):
        node = self.root
        for char in prefix:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def find_words_with_length(self, node, length):
        result = []
        if node.is_end_of_word and len(node.word) == length:
            result.append(node.word)  # Matching word found
        for child in node.children.values():
            result.extend(self.find_words_with_length(child, length))
        return result

def match_coding_strings(dictionary, coding_strings):
    # Build the Trie
    trie = Trie()
    for word in dictionary:
        trie.insert(word)

    results = []
    for coding in coding_strings:
        # Extract prefix and length from the coding string
        prefix = ''.join([char for char in coding if char.isalpha()])
        length = int(''.join([char for char in coding if char.isdigit()])) + len(prefix)

        # Search for matching prefix in Trie
        node = trie.search_prefix(prefix)
        if node:
            # If prefix exists, find words with the exact length
            matches = trie.find_words_with_length(node, length)
            if matches:
                results.extend(matches)  # Collect matching words

    return list(set(results))

# Example usage
dictionary = ["google", "goose", "goal", "goober", "gold", "gopher"]
coding_strings = ["g4e"]

print(match_coding_strings(dictionary, coding_strings))
