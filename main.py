import requests
from fast_bitrix24 import Bitrix

apiKey = "Your API key"
webhook = "https://your_domain.bitrix24.ru/rest/1/your_code/"
BX = Bitrix(webhook)


def get_contact(person_id):
    contact = BX.get_all(
        'crm.contact.get',
        params={'id': person_id}
    )
    return contact['NAME']


def define_gender(contact_name):
    request = requests.get(f'https://genderapi.io/api/?key={apiKey}&name={contact_name}')
    data = request.json()
    return data['gender']


def update_contact_gender(person_id, gender):
    fields = {'GENDER': gender} # Предполагается, что в CRM созано пользовательское поле GENGER
    update_data = BX.call('crm.contact.update', {'id': person_id, 'fields': fields})
    return update_data


if __name__ == '__main__':
    contact_id = 11111 # ID контакта. Либо передается из функции получения ID
    contact_info = get_contact(contact_id)
    gender_response = define_gender(contact_info)

    if gender_response == 'male':
        gender = 'Мужчина'
    else:
        gender = 'Женщина'

    update_contact_gender(contact_id, gender)
