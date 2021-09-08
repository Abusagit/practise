import random
import os

manipulations = {
    1: "Ведение медицинской документации в процедурном кабинете",
    2: "Накрытие стерильного стола в процедурном кабинете",
    3: "Кварцевание процедурного кабинета",
    4: "Проведение подкожных инъекций",
    5: "Проведение внутримышечных инъекций",
    6: "Проведение внутривенных инъекций",
    7: "Проведение внутривенных капельных инъекций",
    8: "Взятия крови из вены для различных видов исследований",
    9: "Определение группы крови больного с помощью цоликлонов и стандартных гемагглютинирующих сывороток",
    10: "Проведение проб на совместимость: групповую, по резус-фактору и биологическую",
    11: "Проведение уборки в процедурном кабинете",
    12: "Разведение антибиотиков",
    13: "Набор инсулина в шприц",
    14: "Сбор и постановки системы для внутривенного капельного вливания",
    15: "Проведение дезинфекционных мероприятий",
    16: "Проведение предстерилизационной очистки изделий медицинского назначения",
    17: "Проведение стерилизации изделий медицинского назначения",
}


def auto_practise(name):
    global manipulations
    counter = {number: 0 for number in range(1, 18)}

    path = r"C:\Users\Fyodor\Desktop\{}".format(name)
    os.mkdir(path)
    os.chdir(path)

    for i in range(1, 17):
        number_of_manipulations = random.randint(8, 15)
        randoms = set()
        with open(fr"Day {i}.txt", 'w') as f_write:
            while number_of_manipulations:
                random_manipulation_index = random.randint(1, 17)
                if random_manipulation_index not in randoms:
                    randoms.add(random_manipulation_index)
                    number_of_manipulations -= 1
            randoms = random.sample(randoms, k=len(randoms))
            for manipulation_index in randoms:
                counter[manipulation_index] += 1
            f_write.write('\n'.join(manipulations[i] for i in randoms))

    with open(r"Summary.txt", 'w') as f_write:
        f_write.write('\n'.join(f'{counter[i]}' for i in range(1, 18)))

    print("DONE")


if __name__ == '__main__':
    a = input()
    auto_practise(a)
