import replicate

def get_diagnosis(symptoms):
    model = replicate.models.get("your-replicate-model-id")
    output = model.predict(prompt=symptoms)
    return output
