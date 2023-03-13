# def are_you_playing_banjo(name):
#     if name.lower()[0] == 'r' :
#         return name + ' plays banjo'
#     else:
#         return name + ' does not play banjo'

def are_you_playing_banjo(name):
    # Implement me!
    if name[0] == 'r' :
        final = name + ' plays banjo'
    elif name[0] == 'R' :
        final = name + ' plays banjo'
    else:
        final = name + ' does not play banjo'
    return final