def dominant_prob(DD, Dd, dd):
    """
    :param k: 'DD'
    :param m_: 'Dd'
    :param n: 'dd'
    :return: probability of dominant allel processing
    """
    whole = DD + Dd + dd
    recessive_prob_Dd = (Dd * (Dd - 1)) / (whole * (whole - 1)) * 0.25 + (Dd * dd) / (whole * (whole - 1)) * 0.5
    # print(recessive_prob_Dd)
    recessive_prob_dd = ((dd * Dd) / (whole * (whole - 1))) * 0.5 + ((dd * (dd - 1)) / (whole * (whole - 1)))
    # print(recessive_prob_dd)
    return 1 - recessive_prob_Dd - recessive_prob_dd


if __name__ == '__main__':
    print(dominant_prob(2, 2, 2))