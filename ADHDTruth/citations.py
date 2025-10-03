"""
Citation management for ADHD medication facts website.
Maps citation numbers to source URLs (PDFs and official documents).
"""

# Citation database mapping reference numbers to source URLs
CITATIONS = {
    1: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5933297/", # Symptom reduction meta-analysis
    2: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3724232/", # Classroom behavior study
    3: "https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-safety-review-update-cardiovascular-risk-associated-attention", # FDA safety data
    4: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4164252/", # Growth velocity study
    5: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2661127/", # MTA follow-up study
    6: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5070026/", # Swedish traffic crash study
    7: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6390815/", # Danish pregnancy study
    8: "https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3970207/", # Economic impact study
    9: "https://publications.aap.org/pediatrics/article/144/4/e20192528/81590/Clinical-Practice-Guideline-for-the-Diagnosis", # AAP guidelines
    10: "https://www.cms.gov/newsroom/press-releases/cms-announces-new-actions-protect-consumers-and-improve-compliance-mental-health-parity-laws", # CMS parity letter
    11: "https://www.cdc.gov/vaccinesafety/ensuringsafety/monitoring/vaers/index.html" # VAERS information
}

def get_citation_url(citation_number: int) -> str:
    """
    Get the URL for a given citation number.
    
    Args:
        citation_number (int): The citation reference number
        
    Returns:
        str: The URL to the source document
    """
    return CITATIONS.get(citation_number, "#")

def get_all_citations() -> dict:
    """
    Get all available citations.
    
    Returns:
        dict: Dictionary of all citation numbers and their URLs
    """
    return CITATIONS.copy()

def validate_citation(citation_number: int) -> bool:
    """
    Validate if a citation number exists.
    
    Args:
        citation_number (int): The citation reference number
        
    Returns:
        bool: True if citation exists, False otherwise
    """
    return citation_number in CITATIONS
