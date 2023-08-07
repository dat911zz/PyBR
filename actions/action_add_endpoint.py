from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionAddingPoints(Action):
    def name(self):
        return 'action_add_points'

    def run(self, dispatcher, tracker, domain):
        response = """Your points added for. Enjoy !!"""
        dispatcher.utter_message(response)