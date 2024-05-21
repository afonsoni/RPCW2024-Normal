import csv
import json

ttl = f'''@prefix : <http://www.example.org/disease-ontology#> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .
@prefix swrl: <http://www.w3.org/2003/11/swrl#> .
@prefix swrlb: <http://www.w3.org/2003/11/swrlb#> .

:Ontology a owl:Ontology .

# Classes
:Disease a owl:Class .
:Symptom a owl:Class .
:Treatment a owl:Class .
:Patient a owl:Class .

# Properties
:hasSymptom a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Symptom .

:hasTreatment a owl:ObjectProperty ;
    rdfs:domain :Disease ;
    rdfs:range :Treatment .

:exhibitsSymptom a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Symptom .

:hasDisease a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Disease .

:receivesTreatment a owl:ObjectProperty ;
    rdfs:domain :Patient ;
    rdfs:range :Treatment .

# Disease instances
:Flu a :Disease ;
    :hasSymptom :Fever, :Cough, :SoreThroat ;
    :hasTreatment :Rest, :Hydration, :AntiviralDrugs .

:Diabetes a :Disease ;
    :hasSymptom :IncreasedThirst, :FrequentUrination, :Fatigue ;
    :hasTreatment :InsulinTherapy, :DietModification, :Exercise .

# Symptom instances
:Fever a :Symptom .
:Cough a :Symptom .
:SoreThroat a :Symptom .
:IncreasedThirst a :Symptom .
:FrequentUrination a :Symptom .
:Fatigue a :Symptom .

# Treatment instances
:Rest a :Treatment .
:Hydration a :Treatment .
:AntiviralDrugs a :Treatment .
:InsulinTherapy a :Treatment .
:DietModification a :Treatment .
:Exercise a :Treatment .


# Patient instances
:Patient1 a :Patient ;
    :name "Paul Harrods" ;
    :exhibitsSymptom :Fever ;
    :exhibitsSymptom :Cough ;
    :exhibitsSymptom :SoreThroat .

:Patient2 a :Patient ;
    :name "Ana Montana" ;
    :exhibitsSymptom :IncreasedThirst ;
    :exhibitsSymptom :FrequentUrination ;
    :exhibitsSymptom :Fatigue .

'''

existingSymptoms = ['Fever', 'Cough', 'SoreThroat', 'IncreasedThirst', 'FrequentUrination', 'Fatigue']
existingTreatments = ['Rest', 'Hydration', 'AntiviralDrugs', 'InsulinTherapy', 'DietModification', 'Exercise']

with open('Disease_Syntoms.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        symptoms = []
        disease = row['Disease'].strip().replace(' ', '_').replace('(', '_').replace(')', '_')
        ttl += f":{disease} rdf:type :Disease .\n"
        for i in range(1, 18):  # Supondo que há até 17 sintomas por doença
            symptom_key = f'Symptom_{i}'
            symptom = row[symptom_key].strip().replace(' ', '_').replace('(', '_').replace(')', '_')
            if symptom:
                if symptom not in existingSymptoms:
                    existingSymptoms.append(symptom)
                    ttl += f":{symptom} rdf:type :Symptom .\n"
                if symptom not in symptoms:
                    symptoms.append(symptom)
                    ttl += f":{disease} :hasSymptom :{symptom} .\n"
    print("Sintomas adicionados.")

with open('Disease_Description.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        disease = row['Disease'].strip().replace(' ', '_').replace('(', '_').replace(')', '_')
        description = row['Description'].strip().replace('\"', '\'')
        ttl += f"\n:{disease} :hasDescription \"{description}\"^^xsd:string .\n"
    print("Descrições adicionadas.")

with open('med_doencas.ttl', 'w', encoding='utf-8') as output_file:
    output_file.write(ttl)

with open('Disease_Treatment.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    # iterate over the rows
    for row in reader:
        disease = row['Disease'].strip().replace(' ', '_').replace('(', '_').replace(')', '_')
        for i in range(1, 5):  # Supondo que há até 4 precauções por doença
            treatment_key = f'Precaution_{i}'
            treatment = row[treatment_key].strip().replace(' ', '_').replace('(', '_').replace(')', '_')
            if treatment:
                if treatment not in existingTreatments:
                    existingTreatments.append(treatment)
                    ttl += f":{treatment} rdf:type :Treatment .\n"
                ttl += f":{disease} :hasTreatment :{treatment} .\n"
    print("Tratamentos adicionados.")

with open('med_tratamentos.ttl', 'w', encoding='utf-8') as output_file:
    output_file.write(ttl)

with open('doentes/pg52669.json', encoding='utf-8') as jsonfile:
    reader = json.load(jsonfile)
    # iterar sobre os doentes
    for patient in reader:
        name = patient['nome'].strip().replace(' ', '_').replace('(', '_').replace(')', '_')
        symptoms = patient['sintomas']
        ttl += f"\n:{name} rdf:type :Patient ;\n"
        ttl += f'    :name "{patient["nome"]}"^^xsd:string ;\n'
        for symptom in symptoms:
            if symptom:
                symptom = symptom.strip().replace(' ', '_').replace('(', '_').replace(')', '_')
                ttl += f'    :exhibitsSymptom :{symptom} ;\n'
        ttl = ttl.rstrip(' ;\n') + " .\n"
    print("Doentes adicionados.")

with open('med_doentes.ttl', 'w', encoding='utf-8') as output_file:
    output_file.write(ttl)

print("Ontologias criadas.")