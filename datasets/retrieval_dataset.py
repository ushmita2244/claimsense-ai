from models.retrieval_test_case import RetrievalTestCase

PDF_SOURCE = "2024-guide-to-preventing-cancer-web.pdf"

RETRIEVAL_DATASET = [

    # ============================================================
    # GENERAL PREVENTION
    # ============================================================

    RetrievalTestCase(
        question="Why is early detection important for cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[5],
        description="Early detection"
    ),

    RetrievalTestCase(
        question="What is a multi-cancer early detection test?",
        expected_source=PDF_SOURCE,
        expected_chunks=[6],
        description="MCED"
    ),

    RetrievalTestCase(
        question="Why should I know my family medical history?",
        expected_source=PDF_SOURCE,
        expected_chunks=[7],
        description="Family history"
    ),

    RetrievalTestCase(
        question="How does smoking increase cancer risk?",
        expected_source=PDF_SOURCE,
        expected_chunks=[9],
        description="Smoking"
    ),

    RetrievalTestCase(
        question="How does alcohol increase cancer risk?",
        expected_source=PDF_SOURCE,
        expected_chunks=[10, 11],
        description="Alcohol"
    ),

    RetrievalTestCase(
        question="Can HPV cause cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[12, 13],
        description="HPV"
    ),

    RetrievalTestCase(
        question="How can vaccines help prevent cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[13],
        description="Vaccination"
    ),

    # ============================================================
    # BREAST CANCER
    # ============================================================

    RetrievalTestCase(
        question="What are the symptoms of breast cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[15],
        description="Breast symptoms"
    ),

    RetrievalTestCase(
        question="What screening tests are available for breast cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[16, 21, 22],
        description="Breast screening"
    ),

    RetrievalTestCase(
        question="Who is at increased risk for breast cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[17, 19],
        description="Breast risk"
    ),

    RetrievalTestCase(
        question="What is BRCA genetic testing?",
        expected_source=PDF_SOURCE,
        expected_chunks=[19, 20],
        description="BRCA"
    ),

    # ============================================================
    # CERVICAL CANCER
    # ============================================================

    RetrievalTestCase(
        question="What causes cervical cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[23, 25],
        description="Cervical cancer"
    ),

    RetrievalTestCase(
        question="What is a Pap test?",
        expected_source=PDF_SOURCE,
        expected_chunks=[24],
        description="Pap test"
    ),

    RetrievalTestCase(
        question="What are the symptoms of cervical cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[26],
        description="Cervical symptoms"
    ),

    # ============================================================
    # COLORECTAL CANCER
    # ============================================================

    RetrievalTestCase(
        question="At what age should colorectal cancer screening begin?",
        expected_source=PDF_SOURCE,
        expected_chunks=[29, 30],
        description="Colorectal screening"
    ),

    RetrievalTestCase(
        question="What are the symptoms of colorectal cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[33],
        description="Colorectal symptoms"
    ),

    # ============================================================
    # LIVER CANCER
    # ============================================================

    RetrievalTestCase(
        question="What causes liver cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[35],
        description="Liver causes"
    ),

    RetrievalTestCase(
        question="How can liver cancer be prevented?",
        expected_source=PDF_SOURCE,
        expected_chunks=[38, 39, 41],
        description="Liver prevention"
    ),

    # ============================================================
    # LUNG CANCER
    # ============================================================

    RetrievalTestCase(
        question="Who should get lung cancer screening?",
        expected_source=PDF_SOURCE,
        expected_chunks=[42, 43, 44],
        description="Lung screening"
    ),

    RetrievalTestCase(
        question="What increases the risk of lung cancer?",
        expected_source=PDF_SOURCE,
        expected_chunks=[45, 46],
        description="Lung risk"
    ),
]