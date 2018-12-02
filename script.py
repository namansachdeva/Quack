import sys
from allennlp.predictors.predictor import Predictor

predictor = Predictor.from_path("./model/bidaf-model.tar.gz")

passage = sys.argv[1]
question = sys.argv[2]

ans = predictor.predict(passage=passage, question=question)['best_span_str']

print(ans)