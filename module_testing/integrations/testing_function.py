from openAI_module import openAI_function, Models

models = []
models.append(Models("davinci custom config 1", "text-davinci-003", "", 0.9, 256, 1, 0, 0))
models.append(Models("davinci custom config 2", "text-davinci-003", "", 0.1, 256, 1, 0, 0))

print("models configured.  starting completion process")

openAI_function(key=0, models=models, FILEPATH='./automation_testing/sample_data/test26.csv', promptColumn="prompt")

print("success")