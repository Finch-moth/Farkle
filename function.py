# creating a Farkle class
import re

class Score_Evaluator():
    def __init__(self):
        self.dice_rules = [
            # regular expressions
            (r"(\d)\1{5}", 3000), # 6 of a kind
            (r"(\d)\1{4}", 2000), # 5 of a kind
            (r"(\d)\1{3}(\d)\2{1}", 1500), # 4 of a kind & pair
            (r"(\d)\1{3}", 1000), # 4 of a kind
            (r"123456", 1500), # 1-6 straight
            (r"(\d)\1{1}(\d)\2{1}(\d)\3{1}", 1500), # 3 pairs
            (r"(\d)\1{2}(\d)\2{2}", 2500), # Two Triples
            (r"1{3}", 700), # 3 of a kind(1)
            (r"2{3}", 200), # 3 of a kind(2)
            (r"3{3}", 300), # 3 of a kind(3)
            (r"4{3}", 400), # 3 of a kind(4)
            (r"5{3}", 500), # 3 of a kind(5)
            (r"6{3}", 600), # 3 of a kind(6)
            (r"1", 100), # 1 -- single
            (r"1", 100), # 1 -- single
            (r"5", 50), # 5 -- single
            (r"5", 50), # 5 -- single
        ]
        
    def evaluate_dice(self, dice):
        dice_str = "".join(map(str, sorted(dice)))
        components = []
        scores = []
        for rule, score in self.dice_rules:
            match = re.search(rule, dice_str)
            if match is not None:
                scores.append(score)
                components.append(match.group(0))
                span = match.span(0)
                dice_str = dice_str[:span[0]] + dice_str[span[1]:]
        components.append(dice_str)
        scores.append(0)
        return components, scores

