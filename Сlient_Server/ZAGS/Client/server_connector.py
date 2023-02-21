import requests


class SecurityError(Exception):
    pass


class ServerConnector:

    def __init__(self, address, port):
        self.url = f"{address}:{port}"
        self.views = set()
        self.user_id = None
        self.user_role = None
        self._password = None

    def set_user(self, user_id, user_password):
        result = requests.get(f"{self.url}/users/{user_id}",
                              json={'user_id': user_id,
                                    'password': user_password}).json()
        if result['status'] == 'error':
            if result['message'] == 'wrong user or password':
                raise SecurityError
            raise Exception
        self.user_id = user_id
        self._password = user_password
        self.user_role = result['role']


    def add_view(self, view):
        self.views.add(view)

    def update_data(self):
        for view in self.views:
            view.update_data()

    def delete_death(self, death_id):
        result = requests.delete(f"{self.url}/death/{death_id}/delete").json()
        self.update_data()
        return result['status'] == 'ok'

    def delete_born(self, born_id):
        result = requests.delete(f"{self.url}/born/{born_id}/delete").json()
        self.update_data()
        return result['status'] == 'ok'

    def delete_marriage(self, marriage_id):
        result = requests.delete(f"{self.url}/marriage/{marriage_id}/delete").json()
        self.update_data()
        return result['status'] == 'ok'

    def get_death(self):
        content = requests.get(f"{self.url}/death").json()
        return content

    def get_born(self):
        content = requests.get(f"{self.url}/born").json()
        return content

    def get_marriage(self):
        content = requests.get(f"{self.url}/marriage").json()
        return content

    def get_born_key(self, key, value):
        content = requests.get(f"{self.url}/born/{key}/{value}/get").json()
        return content

    def get_marriage_key(self, key, value):
        content = requests.get(f"{self.url}/marriage/{key}/{value}/get").json()
        return content

    def get_death_key(self, key, value):
        content = requests.get(f"{self.url}/death/{key}/{value}/get").json()
        return content

    def add_death(self, id, date, place, description):
        result = requests.post(f"{self.url}/death", json={
            'id': id,
            'date': date,
            "place": place,
            "description": description
        }).json()
        self.update_data()
        return result['status'] == 'ok'

    def add_born(self, fio, date, gender, id_parents):
        result = requests.post(f"{self.url}/born", json={
            'fio': fio,
            'date': date,
            "gender": gender,
            "id_parents": id_parents
        }).json()
        self.update_data()
        return result['status'] == 'ok'

    def add_marriage(self, id_husband, id_wife, date):
        result = requests.post(f"{self.url}/marriage", json={
            'id_husband': id_husband,
            "id_wife": id_wife,
            'date': date
        }).json()
        self.update_data()
        return result['status'] == 'ok'

    def edit_death(self, death_id, new_date, new_place, new_description):
        result = requests.post(f"{self.url}/death/{death_id}/edit", json={

            'date': new_date,
            "place": new_place,
            "description": new_description

        }).json()
        self.update_data()
        return result['status'] == 'ok'

    def edit_born(self, born_id, new_fio, new_date, new_gender, new_id_parents):
        result = requests.post(f"{self.url}/born/{born_id}/edit", json={
            'fio': new_fio,
            'date': new_date,
            "gender": new_gender,
            "id_parents": new_id_parents,

        }).json()
        self.update_data()
        return result['status'] == 'ok'

    def edit_marriage(self, marriage_id, id_husband, id_wife, date):
        result = requests.post(f"{self.url}/marriage/{marriage_id}/edit", json={
            'id_husband': id_husband,
            "id_wife": id_wife,
            'date': date
        }).json()
        self.update_data()
        return result['status'] == 'ok'

    def edit_marriage_push_divorce(self, marriage_id, date_divorce):
        result = requests.post(f"{self.url}/marriage/{marriage_id}/edit/divorce", json={
            'date_divorce': date_divorce

        }).json()
        self.update_data()
        return result['status'] == 'ok'
