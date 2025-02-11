class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        # Precompute KMP longest prefix-suffix array for the pattern
        kmp_lps = self._compute_longest_prefix_suffix(part)

        # Using list as a stack to track characters and support pattern matching
        char_stack = []

        # Array to store pattern matching indices during traversal
        pattern_indexes = [0] * (len(s) + 1)

        str_index = 0
        pattern_index = 0
        while str_index < len(s):
            current_char = s[str_index]
            char_stack.append(current_char)

            if current_char == part[pattern_index]:
                # Track the next pattern index when characters match
                pattern_indexes[len(char_stack)] = pattern_index + 1
                pattern_index += 1

                if pattern_index == len(part):
                    # Remove entire matched pattern from stack
                    for _ in range(len(part)):
                        char_stack.pop()

                    # Restore pattern index for next potential match
                    pattern_index = (
                        0
                        if not char_stack
                        else pattern_indexes[len(char_stack)]
                    )
            else:
                if pattern_index != 0:
                    # Backtrack pattern matching using KMP LPS
                    str_index -= 1
                    pattern_index = kmp_lps[pattern_index - 1]
                    char_stack.pop()
                else:
                    # Reset pattern index tracking when no match is possible
                    pattern_indexes[len(char_stack)] = 0

            str_index += 1

        # Convert remaining stack characters to result string
        return "".join(char_stack)

    def _compute_longest_prefix_suffix(self, pattern: str) -> list:
        # Array to store the longest proper prefix which is also a suffix
        lps = [0] * len(pattern)

        # Initialize tracking variables for prefix and current position
        current = 1
        prefix_length = 0
        while current < len(pattern):
            # If characters match, extend the prefix length
            if pattern[current] == pattern[prefix_length]:
                # Store the length of matching prefix
                prefix_length += 1
                lps[current] = prefix_length
                current += 1

            # If characters don't match and we're not at the start of the pattern
            elif prefix_length != 0:
                # Backtrack to the previous longest prefix-suffix
                prefix_length = lps[prefix_length - 1]

            # If no match and no prefix to backtrack
            else:
                # No prefix-suffix match found
                lps[current] = 0
                current += 1

        # Return the computed longest prefix-suffix array
        return lps 