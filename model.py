

def hospital_model(city, district, n, isCardiology, isOntology, isPulmotology, isNeurology, isTheraphy, isSurgery):
    return round(social_act(city, n, isCardiology, isOntology, isPulmotology, isNeurology, isTheraphy, isSurgery) +\
           socialSec(n, isCardiology, isOntology, isPulmotology, isNeurology, isTheraphy, isSurgery) /\
            17.4 * geo_coeff(city, district), 2)


def school_model(city, district, student_quant, isUsual, isMathem, isLingvistic, isNaturalScience, isTechnic, isTechnologic):
    return 0


def social_impact_one_person(city):
    if city=='Москва':
        return 845
    if city=='Санкт-Петербург':
        return 1531


def getpercvolunter(city):
    if city == 'Москва':
        return 0.45
    if city == 'Санкт-Петербург':
        return 0.35


def social_act(city, n, isCardiology, isOntology, isPulmotology, isNeurology, isTheraphy, isSurgery):
    return social_impact_one_person(city)*sum_people_per_year(n)*getpercvolunter(city)*0.95*(setCardi2(isCardiology)+setOntology2(isOntology)+setPulmology2(isPulmotology)+setNeurology2(isNeurology)+setTheraphy2(isTheraphy)+setSurgery2(isSurgery))


def get_injured_percent(city):
    if city == 'Москва':
        return 0.9415
    if city == 'Санкт-Петербург':
        return 0.931


def sum_people_per_year(n):
    return 0.8 * 365 * n


def person_value(city):
    if city == 'Москва':
        return 23465028
    if city == 'Санкт-Петербург':
        return 15676104


def cured_per_year(n, city, isCardiology, isOntology, isPulmotology, isNeurology, isTheraphy, isSurgery):
    curedperyear = (sum_people_per_year(n)*
                    person_value(city)*0.78*0.78*
                    (0.05*(setCardi1(isCardiology)
                           +setOntology1(isOntology)+
                           setPulmology1(isPulmotology)+
                           setNeurology1(isNeurology)+
                           setTheraphy1(isTheraphy)+
                           setSurgery1(isSurgery)
                           )+
                     0.95*(setCardi2(isCardiology)+
                           setOntology2(isOntology)+
                           setPulmology2(isPulmotology)+
                           setNeurology2(isNeurology)+
                           setTheraphy2(isTheraphy)+
                           setSurgery2(isSurgery)))+
                    0.0495*(setCardi1(isCardiology)+
                            setOntology1(isOntology)+
                            setPulmology1(isPulmotology)+
                            setNeurology1(isNeurology)+
                            setTheraphy1(isTheraphy)+
                            setSurgery1(isSurgery)
                            )*get_injured_percent(city)
                    )
    return curedperyear


def socialSec(n, isCardiology, isOntology, isPulmotology, isNeurology, isTheraphy, isSurgery):
    return (90118*sum_people_per_year(n)*
            0.787*(0.95*(setCardi2(isCardiology)+
                         setOntology2(isOntology)+
                         setPulmology2(isPulmotology)+
                         setNeurology2(isNeurology)+
                         setTheraphy2(isTheraphy)+
                         setSurgery2(isSurgery)
                         )
                   )
            )


def setCardi1(isCardiology):
    if isCardiology:
        return 0.33
    return 0


def setCardi2(isCardiology):
    if isCardiology:
        return 0.07
    return 0


def setOntology1(isOntology):
    if isOntology:
        return 0.22
    return 0

def setOntology2(isOntology):
    if isOntology:
        return 0.01
    return 0

def setPulmology1(isPulmotology):
    if isPulmotology:
        return 0.19
    return 0

def setPulmology2(isPulmotology):
    if isPulmotology:
        return 0.02
    return 0

def setNeurology1(isNeurology):
    if isNeurology:
        return 0.11
    return 0

def setNeurology2(isNeurology):
    if isNeurology:
        return 0.1
    return 0

def setTheraphy1(isTheraphy):
    if isTheraphy:
        return 0.09
    return 0

def setTheraphy2(isTheraphy):
    if isTheraphy:
        return 0.49
    return 0

def setSurgery1(isSurgery):
    if isSurgery:
        return 0.06
    return 0

def setSurgery2(isSurgery):
    if isSurgery:
        return 0.31
    return 0


def geo_coeff(city, district):
    n = 0
    if city=="Санкт-Петербург":
        if district=="Центральный":
            n+=1.36
        if district=="Адмиралтейский":
            n+=1.13
        if district=="Василеостровский":
            n+=1.56
        if district=="Выборгский":
            n+=1.36
        if district=="Калининский":
            n+=1.5
        if district=="Кировский":
            n+=3.02
        if district=="Колпинский":
            n+=0.52
        if district=="Красногвардейский":
            n+=1.37
        if district=="Красносельский":
            n+=4.39
        if district=="Кронштадский":
            n+=1.02
        if district=="Курортный":
            n+=0.52
        if district=="Московский":
            n+=1.6
        if district=="Невский":
            n+=1.75
        if district=="Петроградский":
            n+=0.26
        if district=="Петродворцовый":
            n+=0.65
        if district=="Приморский":
            n+=1.7
        if district=="Пушкинский":
            n+=1.82
        if district=="Фрунзенский":
            n+=1.62
    if city=="Москва":
        if district=="ЦАО":
            n+=0.62
        if district=="САО":
            n+=0.86
        if district=="СВАО":
            n+=1.31
        if district=="ВАО":
            n+=0.99
        if district=="ЮВАО":
            n+=1.86
        if district=="ЮАО":
            n+=1.48
        if district=="ЮЗАО":
            n+=0.77
        if district=="ЗАО":
            n+=1.12
        if district=="СЗАО":
            n+=0.72
        if district=="Зеленоградский":
            n+=1.58
        if district=="Новомосковский":
            n+=2.9
        if district=="Троицкий":
            n+=0.85
    return n

# def city_and_district_to_digit(city, district):
#     n = ""
#     if city == "Санкт-Петербург":
#         n += "1"
#         if district == "Центральный":
#             n += "1"
#         if district == "Адмиралтейский":
#             n += "2"
#         if district == "Василеостровский":
#             n += "3"
#         if district == "Выборгский":
#             n += "4"
#         if district == "Калининский":
#             n += "5"
#         if district == "Кировский":
#             n += "6"
#         if district == "Колпинский":
#             n += "7"
#         if district == "Красногвардейский":
#             n += "8"
#         if district == "Красносельский":
#             n += "9"
#         if district == "Кронштадский":
#             n += "10"
#         if district == "Курортный":
#             n += "11"
#         if district == "Московский":
#             n += "12"
#         if district == "Невский":
#             n += "13"
#         if district == "Петроградский":
#             n += "14"
#         if district == "Петродворцовый":
#             n += "15"
#         if district == "Приморский":
#             n += "16"
#         if district == "Пушкинский":
#             n += "17"
#         if district == "Фрунзенский":
#             n += "18"
#     if city == "Москва":
#         n += "2"
#         if district == "ЦАО":
#             n += "1"
#         if district == "САО":
#             n += "2"
#         if district == "СВАО":
#             n += "3"
#         if district == "ВАО":
#             n += "4"
#         if district == "ЮВАО":
#             n += "5"
#         if district == "ЮАО":
#             n += "6"
#         if district == "ЮЗАО":
#             n += "7"
#         if district == "ЗАО":
#             n += "8"
#         if district == "СЗАО":
#             n += "9"
#         if district == "Зеленоградский":
#             n += "10"
#         if district == "Новомосковский":
#             n += "11"
#         if district == "Троицкий":
#             n += "12"
#     return n


locals = {
    "Москва": ["ЦАО", "САО", "СВАО", "ВАО", "ЮВАО", "ЮЗАО", "ЗАО", "СЗАО", "Зеленоградский", "Новомосковский",
               "Троицкий"],
    "Санкт-Петербург": ["Центральный", "Адмиралтейский", "Василеостровский", "Выборгский", "Калининский", "Кировский",
                        "Колпинский", "Красногвардейский", "Красносельский", "Кронштадский", "Курортный", "Московский",
                        "Невский", "Петроградский", "Петродворцовый", "Приморский", "Пушкинский", "Фрунзенский"]
}

# Данные разные входные: город 1 - Питер 2 - Москва, берется из поля с городом
# Район: (вообще комбинация из город+район нелишней будет)


def school_model(city, district, student_quant, school_type):
    return higherEdPerYear(city, student_quant, school_type)*geo_coeff_school(city, district)*social_act_students(city, student_quant)

def higherEdPerYear (city, student_quant, schooltype):
    return (schoolGradPerYear(city, student_quant)*percentofHigherinRussia(city))-(0.725*costPerYear(city, schooltype))

def schoolGradPerYear(city, student_quant):
    if city=='Москва':
        return 0.3*(0.46*student_quant/11+0.54*student_quant/9)+0.7*(0.58*student_quant/11+0.42*student_quant/9)
    if city=='Санкт-Петербург':
        return 0.4*(0.41*student_quant/11+0.59*student_quant/9)+0.6*(0.64*student_quant/11+0.36*student_quant/9)


def getPercentOf9ClassGraduated(schooltype):
    if schooltype=='Не выбрано':
        return 0.65
    if schooltype=='Математический':
        return 0.55
    if schooltype=='Лингвистический':
        return 0.35
    if schooltype=='Естественнонаучный':
        return 0.32
    if schooltype=='Технический':
        return 0.31
    if schooltype=='Технологический':
        return 0.41

def getCoeffForHigherEdInCity(city):
    if city=='Москва':
        return 0.8
    if city=='Санкт-Петербург':
        return 0.7

def costofMiddle(city):
    if city=='Москва':
        return 168
    if city=='Санкт-Петербург':
        return 110

def percentofHigherinRussia(city):
    if city=='Москва':
        return 0.94
    if city=='Санкт-Петербург':
        return 0.975


def costofHigher(city):
    if city=='Москва':
        return 312
    if city=='Санкт-Петербург':
        return 248
def costPerYear(city, schooltype):
    return getPercentOf9ClassGraduated(schooltype)*((((1-getCoeffForHigherEdInCity(city))*costofMiddle(city))
            +((1-getCoeffForHigherEdInCity(city))*95))
            +((1-getPercentOf9ClassGraduated(schooltype))*getCoeffForHigherEdInCity(city)*costofHigher(city))
            +(getCoeffForHigherEdInCity(schooltype)*197))

def social_act_students(city, student_quant):
    return social_impact_one_student(city)*student_quant*getpercvolunter_student(city)*0.85

def social_impact_one_student(city):
    if city=='Москва':
        return 711
    if city=='Санкт-Петербург':
        return 1423

def getpercvolunter_student(city):
    if city=='Москва':
        return 0.32
    if city=='Санкт-Петербург':
        return 0.28


def geo_coeff_school(city, district):
    n = 0
    if city=="Санкт-Петербург":
        if district=="Центральный":
            n+=1.36
        if district=="Адмиралтейский":
            n+=1.13
        if district=="Василеостровский":
            n+=1.56
        if district=="Выборгский":
            n+=1.36
        if district=="Калининский":
            n+=1.5
        if district=="Кировский":
            n+=3.02
        if district=="Колпинский":
            n+=0.52
        if district=="Красногвардейский":
            n+=1.37
        if district=="Красносельский":
            n+=4.39
        if district=="Кронштадский":
            n+=1.02
        if district=="Курортный":
            n+=0.52
        if district=="Московский":
            n+=1.6
        if district=="Невский":
            n+=1.75
        if district=="Петроградский":
            n+=0.26
        if district=="Петродворцовый":
            n+=0.65
        if district=="Приморский":
            n+=1.7
        if district=="Пушкинский":
            n+=1.82
        if district=="Фрунзенский":
            n+=1.62
    if city=="Москва":
        if district=="ЦАО":
            n+=0.62
        if district=="САО":
            n+=0.86
        if district=="СВАО":
            n+=1.31
        if district=="ВАО":
            n+=0.99
        if district=="ЮВАО":
            n+=1.86
        if district=="ЮАО":
            n+=1.48
        if district=="ЮЗАО":
            n+=0.77
        if district=="ЗАО":
            n+=1.12
        if district=="СЗАО":
            n+=0.72
        if district=="Зеленоградский":
            n+=1.58
        if district=="Новомосковский":
            n+=2.9
        if district=="Троицкий":
            n+=0.85