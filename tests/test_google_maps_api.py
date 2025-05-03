import json
import allure
from requests import Response
from utils.check import Check
from utils.api import GoogleMapsApi


"""Создание, изменение и удаление новой локации"""
@allure.epic("Test create place")
class TestCreatePlace():

    @allure.description('Test create, update, delete new place')
    def test_create_new_place(self):

        print("Метод POST")
        result_post: Response = GoogleMapsApi.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Check.check_status_code(result_post, 200)
        Check.check_json_token(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)
        # print(list(token))
        Check.check_json_value(result_post, 'status', 'OK')

        print("Метод GET POST")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Check.check_status_code(result_get, 200)
        Check.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Check.check_json_value(result_get, 'name', 'Frontline house')

        print("Метод PUT")
        result_put: Response = GoogleMapsApi.put_new_place(place_id)
        Check.check_status_code(result_put, 200)
        Check.check_json_token(result_put, ['msg'])
        Check.check_json_value(result_put, 'msg', 'Address successfully updated')

        print("Метод GET PUT")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Check.check_status_code(result_get, 200)
        Check.check_json_token(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])
        Check.check_json_value(result_get, 'name', 'Frontline house')


        print("Метод DELETE")
        result_delete: Response = GoogleMapsApi.delete_new_place(place_id)
        Check.check_status_code(result_delete, 200)
        Check.check_json_token(result_delete, ['status'])
        Check.check_json_value(result_delete, 'status', 'OK')

        print("Метод GET DELETE")
        result_get: Response = GoogleMapsApi.get_new_place(place_id)
        Check.check_status_code(result_get, 404)
        Check.check_json_token(result_get, ['msg'])
        Check.check_json_value(result_get, 'msg', "Get operation failed, looks like place_id  doesn't exists")