import pandas as pd
import numpy as np
from typing import Any, Text, Dict, List
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionGetAnswer(Action):
    def name(self) -> Text:
        return "action_get_answer"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Get the user's question
        user_question = tracker.latest_message['text']

        # Read the CSV file
        df = pd.read_csv("./data/hddt_qa.csv")

        # Use CountVectorizer to convert questions to vectors
        vectorizer = CountVectorizer()
        vectors = vectorizer.fit_transform(df['Question']).toarray()

        # Convert the user question to a vector
        user_vector = vectorizer.transform([user_question]).toarray()

        # Calculate cosine similarity between user question and all questions in the CSV
        similarity_scores = cosine_similarity(user_vector, vectors)

        # Find the index of the most similar question
        most_similar_index = np.argmax(similarity_scores)

        # Get the corresponding answer
        answer = df.iloc[most_similar_index]['Answer']

        # Respond with the answer
        dispatcher.utter_message(text=answer)

        return []
