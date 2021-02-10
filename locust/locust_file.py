from locust import HttpUser, task, between

class QuickstartUser(HttpUser):
    wait_time = between(1, 2)

    # def on_start(self):
    #     self.client.post("/login", json={"username":"foo", "password":"bar"})

    @task
    def index_page(self):
        self.client.post("/op3840078v1", 
            json={  "codigoChaveFuncionario": "J9999999",
                    "numeroProtocoloIdentificacaoImagem": "20202590000649462",
                    "codigoTipoImagem": "1"
                })
        #self.client.get("/world")

