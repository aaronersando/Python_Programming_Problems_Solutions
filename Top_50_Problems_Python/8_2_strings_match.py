# Read the pattern (may contain '?' and '*') and the text to match
pattern = input("Enter pattern (use ? and *): ")
text = input("Enter text to match: ")

m = len(pattern)
n = len(text)

# dp[i][j] will be True if pattern[:i] matches text[:j]
# We create a (m+1) x (n+1) table initialized to False
dp = [[False] * (n + 1) for _ in range(m + 1)]

# Empty pattern matches empty text
dp[0][0] = True

# If pattern starts with '*' it can match an empty text.
# For pattern prefixes like "*", "**", "***", dp[i][0] should be True
for i in range(1, m + 1):
    if pattern[i - 1] == '*':
        dp[i][0] = dp[i - 1][0]
    else:
        dp[i][0] = False  # not strictly necessary since default is False

# Fill the DP table
for i in range(1, m + 1):
    for j in range(1, n + 1):
        p_char = pattern[i - 1]
        t_char = text[j - 1]

        if p_char == '?':
            # '?' matches exactly one character
            dp[i][j] = dp[i - 1][j - 1]
        elif p_char == '*':
            # '*' matches zero characters (dp[i-1][j]) OR
            # '*' matches one more character (dp[i][j-1])
            dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
        else:
            # exact character match required
            dp[i][j] = (p_char == t_char) and dp[i - 1][j - 1]

# Final answer: does full pattern match full text?
if dp[m][n]:
    print("Match")
else:
    print("Not match")

# Optional: show result table for debugging / learning (comment out if not wanted)
# Uncomment the block below to see the DP table (rows=pattern prefixes, cols=text prefixes)
# print("\nDP table (rows=pattern up to i, cols=text up to j):")
# for i in range(m + 1):
#     row = ["T" if dp[i][j] else "F" for j in range(n + 1)]
#     print(f"{pattern[:i]:<10} {row}")
