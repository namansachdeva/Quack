from allennlp.predictors.predictor import Predictor
predictor = Predictor.from_path("https://s3-us-west-2.amazonaws.com/allennlp/models/bidaf-model-2017.09.15-charpad.tar.gz")

passage = "Will Wheaton is a good actor. He also appeared in Star Trek."
question = "Who appeared in Star Trek?"
ans = predictor.predict(passage=passage, question=question)['best_span_str']
print("passage: " + passage)
print("question: " + question)
print("Answer: " + ans)
