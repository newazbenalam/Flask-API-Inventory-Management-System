import unittest
import requests
import time


class TestInventoryAPI(unittest.TestCase):
    base_url = "http://localhost:5000/api/products"
    existing_product_id = None

    def set_id(self):
        tmpresponse = requests.get(self.base_url)
        self.assertEqual(tmpresponse.status_code, 200)
        data = tmpresponse.json()
        if data:
            self.existing_product_id = data[0]['id']

    def test_get_single_product(self):
        task_name = "Test - Get Single Product"
        self.set_id()
        product_id = self.existing_product_id  # Replace with an existing product ID
        response = requests.get(f"{self.base_url}/{product_id}")
        self.assertEqual(response.status_code, 200)
        print(f"{task_name} ✔ done!")

    def test_get_all_products(self):
        task_name = "Test - Get All Products"
        response = requests.get(self.base_url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        if data:
            self.existing_product_id = data[0]['id']
        print(f"{task_name} ✔ done!")
        
    def test_add_product(self):
        task_name = "Test - Add Product"
        data = {
            "name": "New Product",
            "description": "Test product",
            "price": 99.99
        }
        response = requests.post(self.base_url, json=data)
        self.assertEqual(response.status_code, 200)
        print(f"{task_name} ✔ done!")

    def test_update_product(self):
        task_name = "Test - Update Product"
        tmpresponse = requests.get(self.base_url)
        self.assertEqual(tmpresponse.status_code, 200)
        data = tmpresponse.json()
        if data:
            self.existing_product_id = data[0]['id']
        if self.existing_product_id:
            update_data = {
                "name": "Updated Product",
                "description": "New description",
                "price": 50.0
            }
            response = requests.put(
                f"{self.base_url}/{self.existing_product_id}", json=update_data)
            self.assertEqual(response.status_code, 200)
            print(f"{task_name} ✔ done!")
        else:
            print("No existing product ID found to update.")

    def test_delete_product(self):
        task_name = "Test - Delete Product"
        tmpresponse = requests.get(self.base_url)
        self.assertEqual(tmpresponse.status_code, 200)
        data = tmpresponse.json()
        if data:
            self.existing_product_id = data[0]['id']
        if self.existing_product_id:
            response = requests.delete(
                f"{self.base_url}/{self.existing_product_id}")
            self.assertEqual(response.status_code, 200)
            print(f"{task_name} ✔ done!")
        else:
            print("No existing product ID found to delete.")


if __name__ == '__main__':
    unittest.main()
