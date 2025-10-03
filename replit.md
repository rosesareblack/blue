# ADHD Medication Facts Website

## Overview

This is a single-page, data-driven advocacy website built with Streamlit that provides evidence-based counterarguments to common misconceptions about ADHD medication. The site presents verified medical research in a minimal, professional format designed to quickly address stigma and misinformation with citations to peer-reviewed sources.

The application displays three core data categories (Efficacy, Safety, Risk of Not Treating) with embedded citations that link directly to source PDFs, and includes ready-to-use responses for common medication refusal scenarios (school administration, insurance denials, social media misinformation).

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Framework**: Streamlit (Python-based web framework)
- **Rendering Pattern**: Single-page application with server-side rendering
- **Styling**: Custom CSS loaded via `style.css` with professional typography (Inter font family, IBM Plex Mono for headers)
- **Layout Strategy**: Wide layout with collapsed sidebar, centered content container (max-width 1200px)

**Rationale**: Streamlit was chosen for rapid deployment of data-focused applications without requiring separate frontend framework. The single-page design ensures all critical information is immediately accessible without navigation, which is essential for the site's purpose as a quick reference tool during confrontational conversations.

### Content Architecture
- **Separation of Concerns**: Citation data isolated in `citations.py` module
- **Data Structure**: Static citation mapping (dictionary) linking reference numbers to authoritative source URLs
- **Content Organization**: Full-width hero section emphasizing "RISK OF NOT TREATING" at the top, followed by two-column supporting evidence (Efficacy & Safety), and refusal scenarios at bottom
- **Visual Hierarchy**: Risk section uses larger typography (24px headline, 16-17px data) and subtle CSS border pulse animation to draw attention

**Design Decision**: Citations are managed as a separate Python module rather than embedded in the UI code. This allows for easy updates to sources and potential future expansion (e.g., adding citation metadata like author, year, title). The hero layout prioritizes the cost-of-delay narrative per user requirements, making untreated ADHD consequences the focal point.

### Styling Architecture
- **CSS Strategy**: Single external stylesheet (`style.css`) loaded at runtime
- **Typography System**: Two-font hierarchy (Inter for body, IBM Plex Mono for headers) with defined weight scales
- **Visual Design**: Minimal color palette focused on readability (black/dark gray text on white background)
- **Streamlit Overrides**: Hides default Streamlit UI elements (header, menu, footer, deploy button) to maintain professional appearance

**Rationale**: External CSS file provides better maintainability than inline styles and allows for consistent design language. The decision to hide Streamlit branding creates a more serious, authoritative presentation suitable for the medical/advocacy context.

### Data Presentation Pattern
- **Inline Data Structures**: Risk metrics stored as tuples within `app.py` for immediate rendering
- **Dynamic Citation Links**: Citation numbers dynamically link to URLs via the `citations.py` module
- **HTML Injection**: Uses `unsafe_allow_html=True` for custom formatting within Streamlit's component model

**Alternatives Considered**: Could have used a JSON file or database for content storage, but inline data was chosen for simplicity given the static, curated nature of the content and small dataset size.

## External Dependencies

### Core Framework
- **Streamlit**: Primary web application framework
  - Handles routing, rendering, and page configuration
  - Version not pinned (assumes latest stable)

### Data Sources
All citations link to external authoritative sources:
- **NCBI/PubMed Central**: Primary source for peer-reviewed medical research (citations 1, 2, 4, 5, 6, 7, 8)
- **FDA.gov**: Official drug safety communications (citation 3)
- **AAP (American Academy of Pediatrics)**: Clinical practice guidelines (citation 9)
- **CMS.gov**: Healthcare policy documentation (citation 10)
- **CDC.gov**: Vaccine safety monitoring information (citation 11)

**Note**: The application does not consume these sources via API; citations are static reference links that open in the user's browser.

### Font Resources
- **Google Fonts API**: Loads Inter and IBM Plex Mono font families
  - Loaded via CSS `@import` directive
  - Requires external internet connection for font rendering

### No Backend Services
This application has:
- No database (all data is static and embedded)
- No authentication/authorization system
- No user accounts or session management
- No API endpoints (pure presentation layer)
- No third-party analytics or tracking

**Architectural Philosophy**: The application is intentionally stateless and dependency-minimal to ensure maximum uptime, fast load times, and zero data privacy concerns—critical for a public advocacy resource.