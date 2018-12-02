import sys
# from allennlp.predictors.predictor import Predictor
# predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")

passage = sys.argv[1]
question = sys.argv[2]
# ans = predictor.predict(passage=passage, question=question)['best_span_str']

# print("passage: " + passage)
# print("question: " + question)
# print("Answer: " + ans)

print('ans')
sys.stdout.flush()
