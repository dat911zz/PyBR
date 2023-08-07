from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionDefaultFallback(Action):
    def name(self) -> Text:
        return "action_default_fallback"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        dispatcher.utter_message(text="Xin lỗi, tôi chưa hiểu câu hỏi này của bạn!"
                                      "\nBạn có thể hỏi lại câu khác hoặc "
                                      "yêu cầu liên hệ hỗ trợ trực tiếp bằng câu lệnh /call-help")
        return []
