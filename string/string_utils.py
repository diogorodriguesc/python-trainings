class StringUtils(object):

    def combo_string(a, b):
        a_len = len(a)
        b_len = len(b)

        # Ternary - Awesome!
        short = a if a_len < b_len else b
        long = a if a_len > b_len else b

        return short + long + short

    def first_half(str):
        len_str = len(str)
        half_str = len_str / 2

        if (half_str%2 != 0):
            raise Exception(str + " length is not even")

        half_str = int(half_str)

        return str[:half_str]

    def first_two(str):
        return str[:2:]

    def hello_name(name):
        return "Hello " + name + "!"

    def left2(a):
        return a[2:] + a[:2:]
    
    def make_abba(a, b):
        return a + b * 2 + a

    def make_out_word(out, word):
        len_out = len(out)
        half_middle_out = int(len_out / 2)
        
        return out[:half_middle_out] + word + out[half_middle_out:]

    def make_tags(tag, word):
        starting_tag = "<" + tag + ">"
        ending_tag = starting_tag[:1] + "/" + starting_tag[1:]

        return starting_tag + word + ending_tag

    def extra_end(str):
        return str[len(str)-2:] * 3
    
    def without_end(str):
        return str[1:len(str)-1]