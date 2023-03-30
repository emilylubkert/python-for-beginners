import json

person_dict = {'first': 'Emily', 'last': 'Lubkert'}
person_dict['city'] = 'Lakewood'

person_json = json.dumps(person_dict)
print(person_json)

#created nested json
staff_dict = {}
staff_dict['Software Developer'] = person_dict
staff_json = json.dumps(staff_dict)
print(staff_json)

languages_list = ['CSharp', 'Python', 'Javascript']
person_dict['languages'] = languages_list
person_json = json.dumps(person_dict)
print(person_json)