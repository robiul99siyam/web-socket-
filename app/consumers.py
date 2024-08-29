from channels.generic.websocket import SyncConsumer,AsyncConsumer

class MySyncConsumer(SyncConsumer):

    def websocket_connect(self,event):

        self.send({
            "type":"websocket.connect",
        })
    
    def websocket_recevie(self,event):
        print("message recevice")
    
    def websocket_disconnect(self,event):
        print("discount ")