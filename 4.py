a = "GHIJKLMNOPQRSTUVWXYZABCDEF"

stringVal = "TECHCHALLENGECODINGSPEEDRUN"

print ''.join(sorted(stringVal, key=a.index))
