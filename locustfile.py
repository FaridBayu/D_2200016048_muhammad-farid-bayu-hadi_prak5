from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 5)  # Tunggu antara 1 hingga 5 detik sebelum request

    @task
    def get_users(self):
        self.client.get("/users")
    
    @task
    def get_user_by_id(self):
        # Mengakses detail pengguna dengan ID tertentu
        user_id = 1  # Contoh ID pengguna
        self.client.get(f"/users/{user_id}")

