import pandas as pd
from rasa.core.actions.forms import FormAction


class GetQuestion(FormAction):
    def name(self):
        self.faq_d = pd.read_csv('./data/hddt_qa.csv')
        qs = list(self.faq_d['Question'])
        with open("./data/nlu/hddt_qa.yml", "wt", encoding="utf-8") as f:
            f.write('version: "3.1"\n')
            f.write("nlu: \n- intent: question\n  examples: | \n")
            for q in qs:
                f.write(f"    - {q}\n")
        return []