def make_out_word(out, word):
    len_out = len(out)
    half_middle_out = int(len_out / 2)
    
    return out[:half_middle_out] + word + out[half_middle_out:]

print(make_out_word("[[]]", "Diogo"))
print(make_out_word("[[[[]]]]", "Diogo"))
