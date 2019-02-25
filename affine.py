def alphabet(cipher):
    """
    This function performs decrption based on the Affine Cipher
    :param: a string which is to be decrypted
    :return: the decrpyted string
    """
    dictionary = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4,
                  'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9,
                  'k': 10, 'l': 11, 'm': 12, 'n': 13, 'o': 14,
                  'p': 15, 'q': 16, 'r': 17, 's': 18, 't': 19,
                  'u': 20, 'v': 21, 'w': 22, 'x': 23, 'y': 24, 'z': 25,
                  }
    list = []

    for each in cipher:
        for every in dictionary.keys():
            if each == every:
                decr_num = ((15) * (((dictionary.get(every)) - 22) % 26)) % 26
                letter = [key for (key, value) in dictionary.items() if value == decr_num]
                list.append(letter[0])
                my_lst_str = ''.join(map(str, list))
    print(my_lst_str)
    return my_lst_str


if __name__ == '__main__':
    alphabet('falszztysyjzyjkywjrztyjztyynaryjkyswarztyegyyj')
