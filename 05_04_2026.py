🔹 Identity & Access Control
Authentication and authorization via Azure AD (Entra ID)
Role-based access control (RBAC) across all services
Managed identities for secure service-to-service communication
Token-based access enforced at application entry points
🔹 Secure Ingestion Controls
Controlled system entry via FastAPI gateway
Validation of incoming data (file type, size, schema)
Azure AD token validation for all incoming requests
Prevents unauthorized or malformed data from entering the system
🔹 Data & Storage Security
Secure document storage in Azure Blob Storage (encrypted at rest)
Malware detection using Microsoft Defender for Cloud
All data transfers secured via HTTPS (encryption in transit)
Ensures only verified and safe data is processed
🔹 AI / LLM Security Controls
PII masking and data minimization before LLM interaction
Secure access to Azure OpenAI via private endpoints
Controlled prompt execution and output handling
Prevents sensitive data exposure during AI processing
🔹 Monitoring, Audit & Compliance
End-to-end observability using Azure Monitor & Application Insights
Centralized logging via Log Analytics
Audit trails for data access, processing steps, and decisions
Ensures full traceability and compliance readiness
