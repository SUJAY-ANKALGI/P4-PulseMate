import streamlit as st
from transformers import pipeline
import nltk 
nltk.download('punkt')
nltk.download('punkt_tab')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download necessary NLTK data
nltk.download('stopwords')

#Load a pre-trained Hugging Face model
chatbot=pipeline("question-answering", model="deepset/bert-base-cased-squad2")

#Preprocess user input
def preprocess_input(user_input):
 stop_words=set(stopwords.words('english'))
 words=word_tokenize(user_input)
 filtered_words=[word for word in words if word.lower() not in stop_words]
 return''.join(filtered_words)

# Define healthcare-specific response logic
def healthcare_chatbot(user_input):
 user_input = preprocess_input(user_input).lower()
 if "sneeze" in user_input or "sneezing" in user_input:
  return """**General Health Tips:** Maintain good hygiene, stay hydrated, and avoid allergens to reduce sneezing.  
**Symptom Guidance:** Sneezing is often caused by allergies, colds, or irritants. If accompanied by fever or congestion, consult a doctor.  
**Medication Guidance:** Over-the-counter antihistamines may help with allergy-related sneezing, but consult a healthcare provider before use.  
**Preventive Care & Wellness:** Regular cleaning, air purifiers, and avoiding triggers like dust or pollen can help prevent excessive sneezing."""
 elif "symptow" in user_input:
  return """**General Health Tips:** Monitor your symptoms and practice self-care.  
**Symptom Guidance:** If symptoms persist or worsen, seek medical attention.  
**Medication Guidance:** Avoid self-medication and consult a healthcare professional for proper diagnosis.  
**Preventive Care & Wellness:** Maintain a healthy lifestyle and regular check-ups to prevent illnesses."""
 elif "appointment" in user_input:
  return "Would you like me to assist in scheduling an appointment with a doctor for further evaluation?"
 elif "medication" in user_input:
  return """**General Health Tips:** Always follow your doctor’s instructions when taking medication.  
**Symptom Guidance:** If you experience side effects, consult a doctor immediately.  
**Medication Guidance:** Never skip doses, and take medications as prescribed.  
**Preventive Care & Wellness:** Store medicines properly and keep track of expiration dates."""
 elif "fever" in user_input or "high temperature" in user_input:
  return """**General Health Tips:** Stay hydrated, get enough rest, and monitor your temperature.  
**Symptom Guidance:** Fever can indicate infections like flu or viral illness. Seek medical attention if it exceeds 102°F (39°C) or lasts more than three days.  
**Medication Guidance:** Over-the-counter medications like paracetamol may help, but consult a doctor before taking them.  
**Preventive Care & Wellness:** Regular handwashing and vaccinations can help prevent infections causing fever."""
 elif "cough" in user_input or "coughing" in user_input:
  return """**General Health Tips:** Stay hydrated and avoid irritants like smoke and dust.  
**Symptom Guidance:** A cough can be caused by colds, allergies, or infections. If persistent, see a doctor.  
**Medication Guidance:** Cough syrups or lozenges may provide relief, but proper diagnosis is recommended.  
**Preventive Care & Wellness:** Strengthen immunity through proper nutrition and vaccinations."""
 elif "headache" in user_input or "migraine" in user_input:
  return """**General Health Tips:** Drink plenty of water, get enough sleep, and reduce stress.  
**Symptom Guidance:** Headaches can be due to dehydration, stress, or underlying conditions. Seek medical advice if frequent or severe.  
**Medication Guidance:** Pain relievers can help, but long-term headaches may need medical evaluation.  
**Preventive Care & Wellness:** Regular breaks from screens and stress management techniques may reduce headache frequency."""
 elif "stomach pain" in user_input or "abdominal pain" in user_input:
  return """**General Health Tips:** Eat a balanced diet and avoid foods that trigger discomfort.  
**Symptom Guidance:** Stomach pain can result from indigestion, infections, or ulcers. Severe pain or vomiting requires urgent medical attention.  
**Medication Guidance:** Antacids or digestive aids might help, but prolonged pain should be evaluated by a doctor.  
**Preventive Care & Wellness:** Maintain good gut health with fiber-rich foods and probiotics."""
 elif "tired" in user_input or "fatigue" in user_input:
  return """**General Health Tips:** Ensure proper rest, hydration, and a balanced diet.  
**Symptom Guidance:** Fatigue may be due to stress, lack of sleep, or an underlying condition. Seek medical advice if it persists.  
**Medication Guidance:** Some deficiencies (e.g., iron, vitamin D) may cause fatigue. Consult a doctor before taking supplements.  
**Preventive Care & Wellness:** Maintain a healthy sleep schedule and manage stress effectively."""
 elif "blood pressure" in user_input or "hypertension" in user_input:
  return """**General Health Tips:** Reduce salt intake, exercise regularly, and maintain a healthy weight.  
**Symptom Guidance:** High blood pressure often has no symptoms but can lead to serious health issues. Regular check-ups are essential.  
**Medication Guidance:** Follow your doctor’s advice regarding medication and lifestyle changes.  
**Preventive Care & Wellness:** Monitor your blood pressure at home and manage stress levels."""
 elif "diabetes" in user_input or "sugar levels" in user_input:
  return """**General Health Tips:** Monitor blood sugar levels and follow a healthy eating plan.  
**Symptom Guidance:** Symptoms of diabetes include excessive thirst, frequent urination, and fatigue. Seek medical advice if you experience these.  
**Medication Guidance:** Insulin or oral medications may be required. Follow your doctor’s recommendations.  
**Preventive Care & Wellness:** Regular physical activity and a balanced diet help manage diabetes effectively."""
 elif "skin rash" in user_input or "itching" in user_input:
  return """**General Health Tips:** Keep your skin clean and avoid irritants.  
**Symptom Guidance:** Rashes may be caused by allergies, infections, or skin conditions. Seek medical advice if persistent.  
**Medication Guidance:** Over-the-counter creams may help, but consult a doctor for severe cases.  
**Preventive Care & Wellness:** Maintain proper hygiene and avoid known allergens."""
 elif "mental health" in user_input or "stress" in user_input:
  return """**General Health Tips:** Engage in activities that promote relaxation, such as meditation or hobbies.  
**Symptom Guidance:** Persistent stress, anxiety, or depression may require professional support.  
**Medication Guidance:** Some conditions may require medication—consult a healthcare professional.  
**Preventive Care & Wellness:** Practice self-care and seek therapy or counseling if needed."""
 elif "exercise" in user_input or "workout" in user_input:
  return """**General Health Tips:** Exercise improves heart health, mental well-being, and overall fitness.  
**Symptom Guidance:** If you experience pain or discomfort during workouts, consult a specialist.  
**Medication Guidance:** Some medical conditions may require exercise modifications—consult a doctor.  
**Preventive Care & Wellness:** Stay consistent with your workouts and choose activities you enjoy."""
 elif "diet" in user_input or "nutrition" in user_input:
  return """**General Health Tips:** A well-balanced diet supports overall health and prevents diseases.  
**Symptom Guidance:** Poor nutrition can lead to deficiencies and health issues like fatigue or weakened immunity.  
**Medication Guidance:** Some conditions may require dietary supplements—consult a healthcare provider.  
**Preventive Care & Wellness:** Eat a variety of nutrient-rich foods and stay hydrated daily."""
 elif "diet" in user_input or "nutrition" in user_input:
  return """**General Health Tips:** A balanced diet supports immunity, digestion, and overall health.  
**Symptom Guidance:** Poor nutrition may lead to deficiencies, fatigue, or weakened immunity.  
**Medication Guidance:** Some conditions may require dietary supplements—consult a healthcare provider.  
**Preventive Care & Wellness:** Eat a variety of nutrient-rich foods and stay hydrated daily."""
 elif "flu" in user_input or "influenza" in user_input:
  return """**General Health Tips:** Rest, hydration, and nutritious food help in recovery.  
**Symptom Guidance:** Flu symptoms include fever, chills, and body aches. Seek medical help if symptoms worsen.  
**Medication Guidance:** Over-the-counter medications may help, but consult a doctor for severe cases.  
**Preventive Care & Wellness:** Get vaccinated annually and practice good hygiene to prevent the flu."""
 elif "emergency" in user_input or "urgent" in user_input:
  return """**General Health Tips:** In an emergency, act quickly and seek professional help.  
**Symptom Guidance:** Signs of a medical emergency include severe pain, difficulty breathing, or unconsciousness.  
**Medication Guidance:** Certain conditions require immediate medical intervention—do not self-medicate.  
**Preventive Care & Wellness:** Keep emergency contacts handy and be aware of first aid basics."""
 elif "dizziness" in user_input:
  return """**General Health Tips:** Stay hydrated and avoid sudden movements if you feel dizzy.  
**Symptom Guidance:** Dizziness may be caused by dehydration, low blood sugar, or inner ear issues.  
**Medication Guidance:** Some medications may cause dizziness as a side effect—consult your doctor.  
**Preventive Care & Wellness:** Regular check-ups can help detect underlying causes early."""
 elif "chest pain" in user_input:
  return """**General Health Tips:** If experiencing chest pain, seek immediate medical attention.  
**Symptom Guidance:** Chest pain may indicate heart issues or other serious conditions.  
**Medication Guidance:** Do not self-medicate—seek a doctor’s advice if you have heart disease risk factors.  
**Preventive Care & Wellness:** Maintain a heart-healthy lifestyle with regular exercise and a balanced diet."""
 elif "rash" in user_input:
  return """**General Health Tips:** Keep the affected area clean and avoid irritants.  
**Symptom Guidance:** A rash could be due to allergies, infections, or skin conditions.  
**Medication Guidance:** Over-the-counter creams may help, but consult a doctor if it worsens.  
**Preventive Care & Wellness:** Proper hygiene and avoiding allergens can help prevent skin reactions."""
 elif "depression" in user_input:
  return """**General Health Tips:** Mental well-being is as important as physical health—seek support when needed.  
**Symptom Guidance:** Persistent sadness, loss of interest, and fatigue may indicate depression.  
**Medication Guidance:** Antidepressants and therapy may help—consult a healthcare professional.  
**Preventive Care & Wellness:** Engage in stress-relieving activities and maintain social connections."""
 elif "anxiety" in user_input:
  return """**General Health Tips:** Manage stress through mindfulness, exercise, and relaxation techniques.  
**Symptom Guidance:** Anxiety can cause restlessness, rapid heartbeat, or panic attacks.  
**Medication Guidance:** Some cases may require therapy or medication—consult a professional.  
**Preventive Care & Wellness:** Regular meditation, physical activity, and a healthy routine can help manage anxiety."""
 elif "fatigue" in user_input:
  return """**General Health Tips:** Ensure adequate sleep, hydration, and a nutritious diet.  
**Symptom Guidance:** Fatigue can be caused by stress, poor sleep, or underlying conditions.  
**Medication Guidance:** Deficiencies like iron or vitamin D may contribute—consult a doctor for advice.  
**Preventive Care & Wellness:** Establish a regular sleep schedule and manage stress effectively."""
 elif "weight loss" in user_input:
  return """**General Health Tips:** Maintain a balanced diet and exercise regularly for healthy weight management.  
**Symptom Guidance:** Unexplained weight loss could indicate underlying health issues such as thyroid disorders or digestive problems.  
**Medication Guidance:** Some medications can affect weight—consult a doctor if concerned.  
**Preventive Care & Wellness:** Regular health check-ups can help identify causes of weight loss early."""
 elif "high blood pressure" in user_input:
  return """**General Health Tips:** A heart-healthy diet and regular exercise can help manage blood pressure.  
**Symptom Guidance:** High blood pressure often has no symptoms but can increase the risk of heart disease and stroke.  
**Medication Guidance:** Blood pressure medications should be taken as prescribed—consult a doctor for guidance.  
**Preventive Care & Wellness:** Monitor blood pressure regularly and reduce salt intake to maintain healthy levels."""
 elif "pregnancy" in user_input:
  return """**General Health Tips:** Prenatal care is crucial for a healthy pregnancy—eat well and take recommended vitamins.  
**Symptom Guidance:** Pregnancy symptoms include nausea, fatigue, and missed periods. Take a test and consult a doctor if unsure.  
**Medication Guidance:** Some medications are unsafe during pregnancy—consult a healthcare provider before taking any.  
**Preventive Care & Wellness:** Regular prenatal check-ups ensure both maternal and fetal health."""
 elif "diabetes" in user_input:
  return """**General Health Tips:** A well-balanced diet and regular exercise can help regulate blood sugar.  
**Symptom Guidance:** Common symptoms of diabetes include excessive thirst, frequent urination, and fatigue.  
**Medication Guidance:** Insulin or oral medications may be required—follow your doctor’s treatment plan.  
**Preventive Care & Wellness:** Regular blood sugar monitoring and lifestyle management can prevent complications."""
 elif "cold" in user_input:
  return """**General Health Tips:** Stay hydrated, rest well, and eat immune-boosting foods.  
**Symptom Guidance:** Cold symptoms include a runny nose, sore throat, and cough—usually mild but can be uncomfortable.  
**Medication Guidance:** Over-the-counter medications like decongestants and pain relievers can help relieve symptoms.  
**Preventive Care & Wellness:** Wash hands frequently and avoid close contact with sick individuals to prevent colds."""
 elif "cancer" in user_input:
  return """**General Health Tips:** Early detection and a healthy lifestyle can improve cancer outcomes.  
**Symptom Guidance:** Symptoms like unexplained weight loss, persistent pain, or unusual lumps should be checked by a doctor.  
**Medication Guidance:** Cancer treatments vary and may include chemotherapy, radiation, or immunotherapy.  
**Preventive Care & Wellness:** Regular screenings and avoiding risk factors like smoking can reduce cancer risk."""
 elif "constipation" in user_input:
  return """**General Health Tips:** Increase fiber intake, drink plenty of water, and stay active.  
**Symptom Guidance:** Constipation can result from poor diet, stress, or dehydration.  
**Medication Guidance:** Some medications can cause constipation—check with your doctor if you’re concerned.  
**Preventive Care & Wellness:** Regular exercise and a balanced diet can help prevent constipation."""
 elif "insomnia" in user_input:
  return """**General Health Tips:** Maintain a regular sleep schedule and create a relaxing bedtime routine.  
**Symptom Guidance:** Insomnia can be caused by stress, poor sleep hygiene, or underlying conditions.  
**Medication Guidance:** Over-the-counter or prescription sleep aids may help, but consult a doctor before use.  
**Preventive Care & Wellness:** Reduce screen time before bed and avoid caffeine late in the day."""
 elif "arthritis" in user_input:
  return """**General Health Tips:** Stay active with low-impact exercises and maintain a healthy weight.  
**Symptom Guidance:** Arthritis causes joint pain, stiffness, and reduced mobility.  
**Medication Guidance:** Pain relievers, anti-inflammatory drugs, and physical therapy can help manage symptoms.  
**Preventive Care & Wellness:** Regular joint care and stretching exercises can help reduce stiffness."""
 elif "asthma" in user_input:
  return """**General Health Tips:** Avoid asthma triggers like smoke, dust, and strong odors.  
**Symptom Guidance:** Asthma can cause difficulty breathing, wheezing, and coughing.  
**Medication Guidance:** Keep your inhaler accessible and follow your doctor's prescribed treatment.  
**Preventive Care & Wellness:** Regular check-ups can help adjust medications for better asthma control."""
 elif "back pain" in user_input:
  return """**General Health Tips:** Maintain good posture and engage in back-strengthening exercises.  
**Symptom Guidance:** Back pain can result from muscle strain, poor posture, or underlying conditions.  
**Medication Guidance:** Pain relievers and muscle relaxants may help, but consult a doctor if pain persists.  
**Preventive Care & Wellness:** Avoid prolonged sitting and lift heavy objects properly."""
 elif "dehydration" in user_input:
  return """**General Health Tips:** Drink at least 8 glasses of water daily to stay hydrated.  
**Symptom Guidance:** Signs of dehydration include dry mouth, dizziness, and dark urine.  
**Medication Guidance:** Oral rehydration solutions can help restore fluids if dehydration is severe.  
**Preventive Care & Wellness:** Increase water intake during hot weather or physical activity."""
 elif "vomiting" in user_input:
  return """**General Health Tips:** Stay hydrated and rest your stomach by consuming light foods.  
**Symptom Guidance:** Vomiting can be caused by infections, food poisoning, or digestive issues.  
**Medication Guidance:** Anti-nausea medications may help, but consult a doctor if vomiting is persistent.  
**Preventive Care & Wellness:** Wash hands regularly and avoid contaminated food to prevent infections."""
 elif "heart palpitations" in user_input:
  return """**General Health Tips:** Reduce caffeine, manage stress, and stay hydrated.  
**Symptom Guidance:** Palpitations can be caused by stress, dehydration, or heart conditions.  
**Medication Guidance:** If frequent, consult a doctor for tests and potential medication adjustments.  
**Preventive Care & Wellness:** Regular heart check-ups and a balanced diet can support heart health."""
 elif "eczema" in user_input:
  return """**General Health Tips:** Keep skin moisturized and avoid triggers like allergens and harsh soaps.  
**Symptom Guidance:** Eczema causes itchy, dry, and inflamed skin.  
**Medication Guidance:** Topical steroids and moisturizers can help relieve symptoms—consult a dermatologist.  
**Preventive Care & Wellness:** Wear breathable fabrics and use hypoallergenic skincare products."""
 elif "sleep apnea" in user_input:
  return """**General Health Tips:** Maintain a healthy weight and sleep on your side to reduce symptoms.  
**Symptom Guidance:** Sleep apnea causes pauses in breathing, snoring, and daytime fatigue.  
**Medication Guidance:** CPAP therapy is often recommended for sleep apnea—consult a doctor for evaluation.  
**Preventive Care & Wellness:** Avoid alcohol and sedatives before bedtime to improve breathing during sleep."""
 elif "blood donation" in user_input:
  return """**General Health Tips:** Ensure you are well-hydrated and have eaten a healthy meal before donating blood.  
**Symptom Guidance:** Some people may feel lightheaded after donating, but this usually resolves quickly.  
**Medication Guidance:** Avoid blood thinners before donating—consult a doctor if unsure.  
**Preventive Care & Wellness:** Blood donation helps save lives—consider donating regularly if you are eligible."""
 elif "vaccine" in user_input:
  return """**General Health Tips:** Vaccines protect against serious diseases—keep up with recommended immunizations.  
**Symptom Guidance:** Mild side effects like fever or soreness at the injection site are common but temporary.  
**Medication Guidance:** Some vaccines require booster shots—consult your doctor for a vaccination schedule.  
**Preventive Care & Wellness:** Stay updated on seasonal vaccines like flu shots to prevent infections."""
 elif "cold sore" in user_input:
  return """**General Health Tips:** Avoid touching the cold sore and wash your hands frequently to prevent spreading.  
**Symptom Guidance:** Cold sores are caused by the herpes simplex virus and usually appear around the lips.  
**Medication Guidance:** Antiviral creams or oral medications can speed healing—consult a doctor for advice.  
**Preventive Care & Wellness:** Avoid triggers like stress or excessive sun exposure to reduce outbreaks."""
 elif "hives" in user_input:
  return """**General Health Tips:** Avoid known allergens and take antihistamines if needed.  
**Symptom Guidance:** Hives are itchy red welts that can result from allergies, stress, or infections.  
**Medication Guidance:** Antihistamines or corticosteroids may help—consult a healthcare provider if symptoms persist.  
**Preventive Care & Wellness:** Identify and avoid allergens or triggers that cause hives."""
 elif "UTI" in user_input:
  return """**General Health Tips:** Drink plenty of water to flush out bacteria and maintain urinary hygiene.  
**Symptom Guidance:** UTIs cause painful urination, frequent urges to urinate, and lower abdominal pain.  
**Medication Guidance:** Antibiotics are often prescribed for UTIs—consult a doctor for diagnosis and treatment.  
**Preventive Care & Wellness:** Wipe from front to back and urinate after intercourse to reduce the risk of UTIs."""
 elif "liver health" in user_input:
  return """**General Health Tips:** Maintain a healthy diet, avoid alcohol, and exercise regularly to support liver health.  
**Symptom Guidance:** Symptoms of liver issues may include jaundice, fatigue, and abdominal pain.  
**Medication Guidance:** Consult a healthcare provider for liver enzyme tests if concerned.  
**Preventive Care & Wellness:** Avoid excessive alcohol and manage your weight to maintain a healthy liver."""
 elif "kidney health" in user_input:
  return """**General Health Tips:** Stay hydrated and avoid excessive salt to support kidney function.  
**Symptom Guidance:** Symptoms of kidney problems include swelling, fatigue, and pain during urination.  
**Medication Guidance:** Seek medical advice for early detection of kidney disease.  
**Preventive Care & Wellness:** Regular check-ups and a balanced diet can support kidney health."""
 elif "thyroid" in user_input:
  return """**General Health Tips:** Eat a balanced diet with adequate iodine and selenium to support thyroid function.  
**Symptom Guidance:** Thyroid problems can cause weight changes, fatigue, or mood swings.  
**Medication Guidance:** Thyroid medications can help balance hormone levels—consult a healthcare provider for proper treatment.  
**Preventive Care & Wellness:** Regular thyroid check-ups can catch issues early and help maintain balance."""
 elif "lactose intolerance" in user_input:
  return """**General Health Tips:** Avoid dairy products or choose lactose-free alternatives.  
**Symptom Guidance:** Symptoms of lactose intolerance include bloating, gas, and diarrhea after consuming dairy.  
**Medication Guidance:** Lactase supplements can help with digestion of lactose—consult your doctor for advice.  
**Preventive Care & Wellness:** Monitor your symptoms and adjust your diet accordingly to avoid discomfort."""
 elif "allergy" in user_input:
  return """**General Health Tips:** Identify and avoid allergens, and use antihistamines to manage symptoms.  
**Symptom Guidance:** Allergies can cause sneezing, itching, rashes, and more, depending on the trigger.  
**Medication Guidance:** Over-the-counter antihistamines may help alleviate symptoms.  
**Preventive Care & Wellness:** Regular cleaning, dusting, and using air purifiers can reduce allergens at home."""
 elif "anemia" in user_input:
  return """**General Health Tips:** Ensure adequate iron intake through diet or supplements as recommended by a healthcare provider.  
**Symptom Guidance:** Anemia causes fatigue, weakness, and pale skin.  
**Medication Guidance:** Iron supplements may be prescribed to manage anemia—consult a doctor for proper diagnosis and treatment.  
**Preventive Care & Wellness:** Regular blood tests can detect anemia early, especially if you're at risk."""
 elif "pneumonia" in user_input:
  return """**General Health Tips:** Stay hydrated, rest, and follow your doctor's advice for recovery.  
**Symptom Guidance:** Pneumonia causes cough, fever, and difficulty breathing—seek medical help if symptoms worsen.  
**Medication Guidance:** Antibiotics or antivirals may be prescribed depending on the cause of pneumonia.  
**Preventive Care & Wellness:** Get vaccinated against pneumonia and practice good hygiene to reduce the risk."""
 elif "gout" in user_input:
  return """**General Health Tips:** Stay hydrated, avoid alcohol, and reduce purine-rich foods like red meat.  
**Symptom Guidance:** Gout causes sudden, intense pain and swelling in joints, especially the big toe.  
**Medication Guidance:** Medications to reduce uric acid may be prescribed—consult your doctor for appropriate treatment.  
**Preventive Care & Wellness:** Maintaining a healthy weight and avoiding trigger foods can reduce gout flare-ups."""
 elif "strep throat" in user_input:
  return """**General Health Tips:** Gargle with warm salt water, stay hydrated, and rest.  
**Symptom Guidance:** Strep throat causes a sore throat, fever, and difficulty swallowing—seek medical attention for a test.  
**Medication Guidance:** Antibiotics are required to treat strep throat—consult a healthcare provider for prescription.  
**Preventive Care & Wellness:** Wash hands regularly and avoid close contact with infected individuals to prevent the spread of strep."""
 elif "chickenpox" in user_input:
  return """**General Health Tips:** Keep the skin clean, avoid scratching, and stay hydrated.  
**Symptom Guidance:** Chickenpox causes itchy red spots and flu-like symptoms—consult a doctor for diagnosis.  
**Medication Guidance:** Antiviral medications may be prescribed—consult a doctor for advice.  
**Preventive Care & Wellness:** Vaccination against chickenpox is recommended to prevent infection."""
 elif "scabies" in user_input:
  return """**General Health Tips:** Avoid scratching and wash affected areas thoroughly.  
**Symptom Guidance:** Scabies causes intense itching and a rash—seek medical treatment for proper diagnosis.  
**Medication Guidance:** Prescription creams are usually recommended to treat scabies.  
**Preventive Care & Wellness:** Avoid close contact with infected individuals to prevent the spread of scabies."""
 elif "shingles" in user_input:
  return """**General Health Tips:** Rest, avoid stress, and keep the affected area clean.  
**Symptom Guidance:** Shingles causes a painful rash, often on one side of the body. Seek medical care for treatment options.  
**Medication Guidance:** Antiviral medications can reduce the severity of shingles—consult a healthcare provider.  
**Preventive Care & Wellness:** The shingles vaccine is recommended for older adults to reduce the risk of infection."""
 elif "menopause" in user_input:
  return """**General Health Tips:** Eat a balanced diet, stay active, and manage stress during menopause.  
**Symptom Guidance:** Symptoms include hot flashes, mood swings, and sleep disturbances—consult a doctor for management.  
**Medication Guidance:** Hormone replacement therapy may help manage symptoms—consult a healthcare provider for options.  
**Preventive Care & Wellness:** Regular check-ups can help manage symptoms and reduce the risk of bone loss or heart disease during menopause."""
 elif "dental health" in user_input:
  return """**General Health Tips:** Brush twice daily, floss regularly, and visit the dentist every 6 months.  
**Symptom Guidance:** Symptoms of dental issues include tooth pain, sensitivity, and gum bleeding.  
**Medication Guidance:** Over-the-counter pain relievers can help with discomfort—consult a dentist for treatment.  
**Preventive Care & Wellness:** Maintain a healthy diet low in sugar to promote dental health."""
 elif "urinary retention" in user_input:
  return """**General Health Tips:** Stay hydrated and avoid holding urine for long periods.  
**Symptom Guidance:** Urinary retention causes difficulty urinating and a feeling of fullness in the bladder.  
**Medication Guidance:** Medications to help relax the bladder or reduce swelling may be prescribed—consult a doctor for evaluation.  
**Preventive Care & Wellness:** Regular bladder health check-ups can help prevent retention issues."""
 elif "sleep disorders" in user_input:
  return """**General Health Tips:** Practice good sleep hygiene by maintaining a regular sleep schedule.  
**Symptom Guidance:** Sleep disorders can cause insomnia, snoring, or excessive daytime sleepiness—consult a healthcare provider for diagnosis.  
**Medication Guidance:** Medications may help improve sleep quality—consult your doctor for advice.  
**Preventive Care & Wellness:** Reduce caffeine and screen time before bed to improve sleep quality."""
 elif "testicular pain" in user_input:
  return """**General Health Tips:** Rest and avoid any strenuous activities that could aggravate the pain.  
**Symptom Guidance:** Testicular pain can be caused by injury, infection, or other conditions—seek immediate medical attention if pain is severe.  
**Medication Guidance:** Pain relievers may help—consult a doctor for proper diagnosis and treatment.  
**Preventive Care & Wellness:** Practice safe sexual health and protect the area during physical activities to prevent injury."""
 elif "burns" in user_input:
  return """**General Health Tips:** Rinse burns under cool water, avoid popping blisters, and apply soothing creams.  
**Symptom Guidance:** Burns can cause redness, swelling, and pain. Severe burns require immediate medical attention.  
**Medication Guidance:** Over-the-counter creams or ointments may help soothe burns—consult a doctor if the burn is serious.  
**Preventive Care & Wellness:** Take precautions when handling hot objects or chemicals to prevent burns."""
 elif "toothache" in user_input:
  return """**General Health Tips:** Rinse your mouth with warm salt water and avoid chewing on the affected side.  
**Symptom Guidance:** Toothaches can be caused by cavities, gum infections, or trauma—consult a dentist for evaluation.  
**Medication Guidance:** Over-the-counter pain relievers can alleviate discomfort temporarily—see a dentist for a permanent solution.  
**Preventive Care & Wellness:** Regular dental visits and proper oral hygiene can prevent toothaches."""
 elif "leg cramps" in user_input:
  return """**General Health Tips:** Stretch and stay hydrated to reduce the occurrence of leg cramps.  
**Symptom Guidance:** Leg cramps are sudden, painful muscle contractions often occurring at night.  
**Medication Guidance:** Over-the-counter pain relief or magnesium supplements may help—consult a healthcare provider if cramps persist.  
**Preventive Care & Wellness:** Maintaining a balanced diet and staying active can help prevent leg cramps."""
 elif "cough" in user_input:
  return """**General Health Tips:** Stay hydrated and rest to support your immune system.  
**Symptom Guidance:** A cough can be caused by many factors, including infections, allergies, or irritants.  
**Medication Guidance:** Over-the-counter cough medicines may help alleviate symptoms—consult a doctor if the cough persists.  
**Preventive Care & Wellness:** Avoid exposure to irritants and get vaccinated against respiratory infections."""
 elif "congestion" in user_input:
  return """**General Health Tips:** Use saline nasal sprays, stay hydrated, and rest.  
**Symptom Guidance:** Nasal congestion is caused by inflammation of the nasal passages due to infections, allergies, or irritants.  
**Medication Guidance:** Over-the-counter decongestants may help reduce symptoms—consult a healthcare provider if symptoms persist.  
**Preventive Care & Wellness:** Maintain a clean environment and wash hands frequently to prevent infections."""
 elif "mpox" in user_input or "monkeypox" in user_input:
    return """**General Health Tips:** Avoid close contact with infected individuals and practice good hygiene.  
**Symptom Guidance:** Mpox symptoms include fever, swollen lymph nodes, and rash. If you develop these symptoms, seek testing and medical attention.  
**Medication Guidance:** Vaccines and antivirals may be used for prevention and treatment. Consult a healthcare provider.  
**Preventive Care & Wellness:** Stay informed about vaccination availability and avoid exposure to animals or individuals who may be infected."""
 elif "TB" in user_input or "tuberculosis" in user_input:
    return """**General Health Tips:** Avoid close contact with infected individuals and cover your mouth when coughing.  
**Symptom Guidance:** TB symptoms include persistent cough, weight loss, fever, and night sweats. If symptoms persist, consult a doctor.  
**Medication Guidance:** TB is treated with a combination of antibiotics for several months. Consult your healthcare provider for the right treatment plan.  
**Preventive Care & Wellness:** Maintain regular check-ups if you are at high risk for TB and follow infection control practices."""
 elif "bird flu" in user_input or "H5N1" in user_input:
    return """**General Health Tips:** Avoid close contact with infected birds and practice proper hygiene.  
**Symptom Guidance:** Bird flu can cause fever, cough, and respiratory distress. If you’ve been exposed to infected birds, seek medical attention.  
**Medication Guidance:** Antiviral medications may help reduce symptoms if taken early. Consult your healthcare provider for advice.  
**Preventive Care & Wellness:** Avoid handling sick birds and follow safety guidelines if you work in areas where bird flu outbreaks occur."""
 elif "malaria" in user_input:
    return """**General Health Tips:** 
- Use mosquito repellents, nets, and protective clothing to avoid mosquito bites.
- Stay in air-conditioned or well-screened areas to reduce exposure to mosquitoes.
**Symptom Guidance:** 
- Malaria symptoms typically include fever, chills, sweats, fatigue, and flu-like symptoms.
- If symptoms develop after visiting malaria-endemic areas, seek medical attention immediately for proper testing and treatment.
**Medication Guidance:** 
- Antimalarial medications are prescribed for both prevention (for travelers) and treatment (for those diagnosed).
- Common treatments include artemisinin-based combination therapies (ACTs). Ensure treatment is completed as prescribed by your healthcare provider.
**Preventive Care & Wellness:** 
- If traveling to areas with malaria risk, take prescribed preventive medications.
- Use mosquito nets, wear long sleeves, and apply insect repellent to reduce mosquito bites.
- Regular health check-ups are essential, especially after visiting endemic regions."""
 elif "HIV" in user_input or "AIDS" in user_input:
    return """**General Health Tips:** 
- Practice safe sex by using condoms and avoid sharing needles or other drug paraphernalia.
- Regular HIV testing is crucial for early detection.
**Symptom Guidance:** 
- Early HIV infection can present as flu-like symptoms, but some individuals may not show symptoms for years.
- Symptoms of AIDS include weight loss, recurring infections, fever, and extreme fatigue. Regular screening helps manage the disease.
**Medication Guidance:** 
- Antiretroviral therapy (ART) is the main treatment for managing HIV, and it helps individuals live a longer, healthier life.
- Adherence to ART is critical in controlling the virus and preventing progression to AIDS.
**Preventive Care & Wellness:** 
- Pre-exposure prophylaxis (PrEP) can help prevent HIV infection in high-risk individuals.
- Live a balanced lifestyle, get adequate nutrition, and have regular check-ups to monitor the immune system's health."""
 elif "COVID-19" in user_input or "coronavirus" in user_input or "covid19" in user_input or "COVID19" in user_input:
    return """**General Health Tips:** 
- Follow hygiene practices such as frequent handwashing, wearing masks in crowded places, and practicing physical distancing where appropriate.
- Stay home if you're sick, and avoid close contact with those who may be symptomatic.
**Symptom Guidance:** 
- Common COVID-19 symptoms include fever, cough, fatigue, and loss of taste or smell.
- If you experience symptoms, especially if you've been exposed to someone with COVID-19, seek testing and medical care.
**Medication Guidance:** 
- Vaccines are effective in reducing severe illness and hospitalization related to COVID-19. Stay updated on booster shots.
- Antiviral treatments, such as Paxlovid, are available for early treatment in high-risk individuals—consult a healthcare provider for guidance.
**Preventive Care & Wellness:** 
- Maintain good hygiene practices, stay informed about local COVID-19 variants, and follow guidelines from health authorities.
- Stay up to date with vaccination schedules and protect vulnerable populations through herd immunity."""
 else:
  context = "Error: Unable to process the request. Please ensure that your input is related to healthcare symptoms or general health inquiries."
  response=chatbot({
        "question": "What is your question?",
        "context": context
    })
  return response['answer']
 
# Streamlit web app interface

def main():
    st.markdown("<h1 style='text-align: center; font-size: 36px;'>PulseMate</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 18px; color: gray;'>Keeping track of your health</p>", unsafe_allow_html=True)

    user_input =st.text_input("Do you need any healthcare guidance today?", "")
    if st.button("Submit"):
        if user_input:
            st.write("User:", user_input)
            response = healthcare_chatbot(user_input)
            st.write("Healthcare Assistant: ", response)
        else:
            st.write("Feel free to ask any health-related questions.")

if __name__=="__main__":
    main()
 