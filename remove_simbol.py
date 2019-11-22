def remove_simbol(word):
    al = "\"abcdefghijklmnopqrstuvwxyz0123456789,!@#$%^&*()<>?/+=-_{}|\'"
    word = list(word)
    for ix, i in enumerate(word):
        i = i.lower()
        if i not in al:
            word[ix]=""
    return "".join(word).strip()