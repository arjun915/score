# consumers.py
from channels.generic.websocket import AsyncWebsocketConsumer
import json

class ScoreUpdateConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.event_name = self.scope['url_route']['kwargs']['event_name']
        self.room_group_name = f"score_{self.event_name}"

        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        team_id = text_data_json['team_id']
        score = text_data_json['score']

        # Send score update to room group
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'score_update',
                'team_id': team_id,
                'score': score
            }
        )

    async def score_update(self, event):
        team_id = event['team_id']
        score = event['score']

        # Send score to WebSocket
        await self.send(text_data=json.dumps({
            'team_id': team_id,
            'score': score
        }))
