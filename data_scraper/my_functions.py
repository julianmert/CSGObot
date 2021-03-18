def calc_match_type(team_1_score, team_2_score):
    '''
    A function to take in the 2 respective scores of a game and
    return whether its a b01, b03 or b05.

    '''
    score_1 = int(team_1_score)
    score_2 = int(team_2_score)
    score_tup = (score_1, score_2)
    match_type = None

    # defining possible score combinations for each match_type.
    bo3s = [(2,0), (0,2), (2,1), (1,2)]
    bo5s = [(3,0),(0,3),(3,1),(1,3),(3,2),(2,3)]

    # assigning match_types
    if (score_1>=16) or (score_2>=16):
        match_type = 'bo1'
    if score_tup in bo3s:
        match_type = 'bo3'
    if score_tup in bo5s:
        match_type = 'bo5'


    return match_type
