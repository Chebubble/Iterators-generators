def flat_generator(list_of_list):
    generator = (list_of_list[i][j] for i in range(0, len(list_of_list)) for j in range(0, len(list_of_list[i])))
    return generator