from Client import Client
from Social_Network import SocialNetwork


class Client_Social_Network:
    def __init__(self,client, social_network):
        self.client = client
        self.social_network = social_network
    pass


client1 = Client('Cristiane', 'Pitana', 'Rua Santa fé, 92', '5199999999', 'cristianepitana@hotmail.com', 'f')
sc = SocialNetwork('exemplo', 'desc')
Client_Social_Network(client1, sc)        
