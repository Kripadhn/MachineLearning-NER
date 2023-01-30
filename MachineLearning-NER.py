import spacy

# Load the NER model
nlp = spacy.load('en_core_web_sm')

# Define the data
text = 'Apple was founded by Steve Jobs in 1976 in Cupertino, California.'

# Process the data with spaCy
doc = nlp(text)

# Extract the entities
entities = [(ent.text, ent.label_) for ent in doc.ents]
print(entities)
# Output: [('Apple', 'ORG'), ('Steve Jobs', 'PERSON'), ('1976', 'DATE'), ('Cupertino, California', 'GPE')]
