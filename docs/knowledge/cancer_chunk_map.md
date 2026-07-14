# Cancer Knowledge Map

## Document

**Source:** `2024-guide-to-preventing-cancer-web.pdf`

**Total Chunks:** 72

---

# Purpose

This knowledge map groups semantically related chunks into logical knowledge units.

Instead of treating every chunk independently, retrieval benchmarks and future retrieval strategies operate at the knowledge-unit level. This makes evaluation more meaningful because multiple adjacent chunks often describe the same topic.

---

# Knowledge Unit 1 — General Cancer Prevention

**Chunks**

1–14

## Topics

- Guide overview
- Cancer prevention
- Early detection
- MCED
- Family history
- Lifestyle modification
- Smoking
- Diet
- Alcohol
- Exercise
- HPV
- Hepatitis B
- Vaccination
- Safer sex

## Important Concepts

- Early detection saves lives
- MCED blood tests
- Family history
- Smoking causes cancer
- Healthy diet
- Alcohol increases cancer risk
- Obesity
- Physical activity
- HPV
- Hepatitis B
- Vaccination

## Example Retrieval Questions

- What are the major causes of cancer?
- How can cancer be prevented?
- What lifestyle changes reduce cancer risk?
- What is MCED?
- Why is family history important?
- Can HPV cause cancer?
- Can vaccines prevent cancer?
- How does alcohol increase cancer risk?

---

# Knowledge Unit 2 — Breast Cancer

**Chunks**

15–22

## Topics

- Symptoms
- Screening
- Mammography
- MRI
- Genetics
- BRCA
- Risk Factors
- Prevention

## Important Concepts

- Breast lump
- Mammography
- 3D Mammogram
- MRI
- BRCA1
- BRCA2
- PALB2
- Family history

## Example Questions

- What are breast cancer symptoms?
- Who should receive mammograms?
- What is BRCA?
- Who is at high risk?
- What lifestyle changes reduce breast cancer risk?

---

# Knowledge Unit 3 — Cervical Cancer

**Chunks**

23–28

## Topics

- HPV
- Pap Test
- HPV Test
- Vaccination
- Symptoms
- Risk Factors

## Important Concepts

- HPV
- Pap smear
- Co-testing
- Vaccination
- Cervical screening

## Example Questions

- What causes cervical cancer?
- What is a Pap test?
- When should cervical cancer screening begin?
- Can HPV vaccination prevent cervical cancer?

---

# Knowledge Unit 4 — Colorectal Cancer

**Chunks**

29–34

## Topics

- Colonoscopy
- FIT
- Stool DNA
- Screening
- Symptoms
- Prevention

## Important Concepts

- Screening age 45+
- Colonoscopy
- FIT
- Stool DNA
- Blood in stool

## Example Questions

- When should colorectal screening begin?
- What are colorectal cancer symptoms?
- Which colorectal screening tests exist?

---

# Knowledge Unit 5 — Liver Cancer

**Chunks**

35–41

## Topics

- Hepatitis B
- Hepatitis C
- Screening
- Vaccination
- Symptoms
- Treatment

## Important Concepts

- Chronic hepatitis
- Liver cancer
- Hepatitis screening
- Vaccination

## Example Questions

- How does hepatitis cause liver cancer?
- Who should receive hepatitis screening?
- How can liver cancer be prevented?

---

# Knowledge Unit 6 — Lung Cancer

**Chunks**

42–47

## Topics

- Smoking
- Radon
- CT Screening
- Symptoms
- Treatment

## Important Concepts

- Pack-year
- Low-dose CT
- Smoking
- Secondhand smoke

## Example Questions

- Who should receive lung cancer screening?
- What is a pack-year?
- Does smoking cause lung cancer?

---

# Knowledge Unit 7 — Oral Cancer

**Chunks**

48–50

## Topics

- Symptoms
- Risk Factors
- Tobacco
- Alcohol
- HPV

## Example Questions

- What causes oral cancer?
- What are oral cancer symptoms?

---

# Knowledge Unit 8 — Prostate Cancer

**Chunks**

51–54

## Topics

- PSA
- Screening
- Symptoms
- Active Surveillance

## Example Questions

- What is PSA screening?
- What is active surveillance?
- Who should undergo prostate screening?

---

# Knowledge Unit 9 — Skin Cancer

**Chunks**

55–60

## Topics

- UV Radiation
- Sunscreen
- ABCDE Rule
- Melanoma

## Example Questions

- What is the ABCDE rule?
- How can skin cancer be prevented?
- What causes melanoma?

---

# Knowledge Unit 10 — Testicular Cancer

**Chunks**

61–63

## Topics

- Self Examination
- Symptoms
- Risk Factors

## Example Questions

- How do you perform a testicular self-exam?
- What increases the risk of testicular cancer?

---

# Knowledge Unit 11 — Viruses and Cancer

**Chunks**

64–69

## Topics

- HPV
- Hepatitis B
- Hepatitis C
- Vaccination

## Important Concepts

- Viral cancers
- HPV vaccination
- Hepatitis vaccination

## Example Questions

- Which viruses cause cancer?
- Which cancers are linked to HPV?
- Can hepatitis vaccination reduce cancer risk?

---

# Knowledge Unit 12 — Cancer Screening Summary

**Chunks**

70–72

## Topics

- Screening by age
- Vaccinations
- Prevention checklist

## Example Questions

- Which cancer screenings are recommended?
- Which vaccines prevent cancer?
- What routine screenings should adults undergo?

---

# Notes for Retrieval Benchmark

For benchmark creation:

- Prefer evaluating retrieval at the **knowledge-unit** level rather than an individual chunk when multiple adjacent chunks cover the same concept.
- Use chunk-level validation only when the expected information is localized to a specific passage.
- Future retrieval strategies (Hybrid Search, BM25, Multi-Query Retrieval, Reranking) should be evaluated against this knowledge map.

---

# Future Extensions

- Add BM25 keywords for every knowledge unit.
- Add semantic tags.
- Add expected benchmark questions.
- Add retrieval difficulty (Easy / Medium / Hard).
- Add related knowledge units.