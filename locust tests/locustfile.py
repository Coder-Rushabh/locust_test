from locust import HttpUser, task, between
import time

class HelloWorldUser(HttpUser):

    @task
    def net_positions_netwise(self):
        self.client.get("/net-positions-netwise")
        time.sleep(5)  

    @task
    def other_endpoints(self):
        self.client.get("/health")
        self.client.get("/net-positions")
        self.client.get("/order-book")
        self.client.get("/trade-book")
        self.client.get("/holding")
        time.sleep(15)  
