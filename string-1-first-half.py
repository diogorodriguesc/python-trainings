# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

def first_half(str):
    len_str = len(str)
    half_str = len_str / 2

    if (half_str%2 != 0):
        raise Exception(str + " length is not even")

    half_str = int(half_str);

    return str[:half_str]

print(first_half("José"))
print(first_half("Diogo"))