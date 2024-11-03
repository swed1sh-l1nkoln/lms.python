#Функция для нахождения общих участников из двух групп.
def find_common_participants(group1, group2, separator=','):
    # Разделяем строки на списки участников
    participants1 = set(group1.split(separator))
    participants2 = set(group2.split(separator))
    
    # Находим пересечение двух множеств
    common_participants = participants1.intersection(participants2)

    # Возвращаем отсортированный список
    return sorted(common_participants)

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции с разделителем '|' и 'запятая'
common_participants = find_common_participants(participants_first_group, participants_second_group, separator='|')
print("Общие участники (|):", common_participants)

# Можно также проверить с разделителем запятая
participants_first_group_comma = "Иванов,Петров,Сидоров"
participants_second_group_comma = "Петров,Сидоров,Смирнов"

common_participants_comma = find_common_participants(participants_first_group_comma, participants_second_group_comma, separator=',')
print("Общие участники (,):", common_participants_comma)

