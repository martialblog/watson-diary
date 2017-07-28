#!/usr/bin/python3


import json
from watson_developer_cloud import ConversationV1


class Chatbot:

    def __init__(self, url, username, password, version, workspace_id):

        self.conversation = ConversationV1(
            url=url,
            version=version,
            username=username,
            password=password,
            use_vcap_services= False
        )

        self.workspace_id = workspace_id

    def conversate(self, text, context):

        response = self.conversation.message(
            workspace_id=self.workspace_id,
            message_input={'text': text},
            context=context
        )

        return response
