def validParanthesis(str):
    cleaned_s_array=[ch.lower() for ch in str if ch.isalnum()]
    return cleaned_s_array== cleaned_s_array[::-1]


a=validParanthesis("A man, a plan acanal: panama")
print(a)