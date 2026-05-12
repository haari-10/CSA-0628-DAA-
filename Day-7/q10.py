def full_justify(words, maxWidth):

    result = []

    i = 0

    while i < len(words):

        line = []
        line_len = 0

        while i < len(words) and \
              line_len + len(words[i]) + len(line) <= maxWidth:

            line.append(words[i])
            line_len += len(words[i])

            i += 1

        spaces = maxWidth - line_len

        if i == len(words) or len(line) == 1:

            current = " ".join(line)
            current += " " * (maxWidth - len(current))

        else:

            gaps = len(line)-1

            even = spaces // gaps
            extra = spaces % gaps

            current = ""

            for j in range(gaps):

                current += line[j]
                current += " " * (even +
                                  (1 if j < extra else 0))

            current += line[-1]

        result.append(current)

    return result


words = ["This","is","an","example",
         "of","text","justification."]

output = full_justify(words, 16)

for line in output:
    print(f'"{line}"')