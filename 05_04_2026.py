🔹 Secure Ingestion Gateway
Email retrieval via Microsoft Graph API / Gmail API
Authentication & authorization via Azure AD (RBAC)
Token validation and request enforcement at FastAPI gateway
Input validation: file type, size, and basic schema checks
🔹 Content Storage & Malware Protection
Documents persisted in Azure Blob Storage
Malware scanning using Microsoft Defender for Cloud
Only verified files are allowed into downstream processing
🔹 Asynchronous Processing Layer
Event-driven pipeline using Azure Service Bus
Decouples ingestion from processing for scalability and resilience
Supports retry and failure handling mechanisms
🔹 Document Processing
OCR and document parsing via Azure Document Intelligence
Extraction of raw text and structured content
Storage of both raw and processed artifacts for traceability
🔹 AI-Orchestrated Processing
Agent orchestration using LangChain
LLM inference using Azure OpenAI

Processing stages:

Classifier: identifies claim type
Extractor: generates structured data (JSON)
Validator: applies business rules, completeness checks, and confidence scoring
🔹 Decision & Routing
Routing based on:
Validation outcome
Confidence thresholds
Business rules
High-confidence → automated claim creation
Low-confidence → routed to human review
🔹 Human-in-the-loop Validation
Manual review and correction of extracted data
Ensures accuracy for edge cases and exceptions
Final submission follows same claim creation pathway
🔹 Integration & System of Record
Claim creation via external Claims Backend API
Backend system acts as system of record
Optional storage of metadata and processing logs in SQL DB
🔹 Security, Monitoring & Audit
Identity and access via Azure AD (RBAC, Managed Identity)
End-to-end observability using Azure Monitor & Application Insights
Audit logging for data access, processing steps, and decisions
⚡ Why this version is correct
No wrong attribution (auth handled by Azure AD, not FastAPI)
Defender correctly placed at storage level
Clear separation of layers
No generic statements
Matches your architecture exactly
