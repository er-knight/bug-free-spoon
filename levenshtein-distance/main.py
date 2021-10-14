def levenshtein_distance(s: str, t: str) -> int:

    m, n = len(s), len(t)

    if any([m == 0, n == 0]):
        return max(m, n)

    distances = [[0 for j in range(n + 1)] for i in range(m + 1)]

    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0: 
                distances[i][j] = j 
            elif j == 0:
                distances[i][j] = i 
            elif s[i - 1] == t[j - 1]:
                distances[i][j] = distances[i - 1][j - 1]
            else:
                distances[i][j] = 1 + min(
                    distances[i][j - 1],
                    distances[i - 1][j],
                    distances[i - 1][j - 1]
                )
            
    return distances[m][n]

if __name__ == "__main__":

    correct, incorrect = "harry potter", "hary poter"

    assert levenshtein_distance(correct, correct)   == 0
    assert levenshtein_distance(correct, incorrect) == 2
    assert levenshtein_distance(incorrect, correct) == 2

# make 10-characters game based on this
