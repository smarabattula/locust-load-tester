from locust import HttpUser, TaskSet, task, constant
from locust import LoadTestShape
import random

class UserTasks(TaskSet):
    @task(1)
    def root(self):
        self.client.get("/")

    # @task(2)
    # def userlogin(self):
    #    self.client.get("/login/admin")

    # @task(3)
    # def login(self):
    #    self.client.get("/login")
    
    # @task(4)
    # def logout(self):
    #     self.client.get("/logout")

    # @task(5)
    # def process(self):
        
    #     n = random.randint(1, 50)
    #     self.client.get("/process/" + str(n))


class WebsiteUser(HttpUser):
    wait_time = constant(0.0)
    tasks = [UserTasks]


class StagesShape(LoadTestShape):
    """
    A simply load test shape class that has different user and spawn_rate at
    different stages.

    Keyword arguments:

        stages -- A list of dicts, each representing a stage with the following keys:
            duration -- When this many seconds pass the test is advanced to the next stage
            users -- Total user count
            spawn_rate -- Number of users to start/stop per second
            stop -- A boolean that can stop that test at a specific stage

        stop_at_end -- Can be set to stop once all stages have run.
    """

    stages = [
        {"duration": 60, "users": 20, "spawn_rate": 1.0},
        {"duration": 120, "users": 60, "spawn_rate": 2.0},
        # {"duration": 999, "users": 99, "spawn_rate": 00},
        # Add more stages
        ]

    def tick(self):
        run_time = self.get_run_time()

        for stage in self.stages:
            if run_time < stage["duration"]:
                tick_data = (stage["users"], stage["spawn_rate"])
                return tick_data

        return None
