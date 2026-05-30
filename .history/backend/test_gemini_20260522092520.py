import google.generativeai as genai

genai.configure(api_key="AIzaSyAYq6eiVsxfYlnejr8JyJ_w3fUjpjFoVo0")


try:

    models = genai.list_models()

    for model in models:
        print(model.name)

except Exception as e:
    print(e)