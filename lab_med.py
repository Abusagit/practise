def international_normalizing_ratio(t_patient, t_norm, ISI) -> float:
    return (t_patient / t_norm) ** ISI

def prothrombine_ratio(t_observing, t_standard):
    return t_observing / t_standard


if __name__ == '__main__':
    patients = {
        1: (16, 12, 3.2),
        2: (18, 12, 2.4),
        3: (21, 13, 2.0),
        4: (24, 11, 1.2),
        5: (38, 14.5, 1.0),
    }
    for i in sorted(patients.keys()):
        inr = round(international_normalizing_ratio(patients[i][0], patients[i][1], patients[i][2]), 2)
        pr = round(prothrombine_ratio(patients[i][0], patients[i][1]), 2)
        print(f'Пациент {i}: МНО - {inr}, ПО - {pr}')