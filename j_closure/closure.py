def set_topic(topic):
    # def set_value(value):
    #     formatting = f'{topic}: {value}'
    #     return formatting
    # return set_value
    return lambda value: f'{topic}: {value}'


set_name = set_topic("이름")
name = set_name("한동석")

set_age = set_topic("나이")
age = set_age(20)

print(f'{name}, {age}')