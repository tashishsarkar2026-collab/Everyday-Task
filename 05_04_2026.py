%%{init: {'theme': 'base', 'themeVariables': { 'primaryColor': '#e1f5fe', 'edgeLabelBackground':'#ffffff', 'tertiaryColor': '#fff'}}}%%

graph LR
    %% --- Cross-Cutting Layer ---
    subgraph Governance ["&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Enterprise Security, Observability & Governance&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;"]
        direction LR
        style Governance fill:#f1f8e9,stroke:#558b2f,stroke-width:2px,color:#000,font-weight:bold
        
        IDA[("fa:fa-id-card Identity & Access<hr/>- Azure AD (Entra ID)<br/>- RBAC<br/>- Managed Identity")]
        NET[( "fa:fa-shield-alt Network Security<hr/>- VNet Isolation<br/>- Private Endpoints")]
        DAT[( "fa:fa-lock Data Security<hr/>- Encryption at rest/transit<br/>- PII Masking")]
        OBS[( "fa:fa-eye Observability<hr/>- Azure Monitor<br/>- Application Insights<br/>- Log Analytics")]
        AUD[( "fa:fa-clipboard-check Audit & Compliance<hr/>- Activity Logs<br/>- Data Access Tracking<br/>- Decision Traceability")]

        style IDA fill:#fff,stroke:#777
        style NET fill:#fff,stroke:#777
        style DAT fill:#fff,stroke:#777
        style OBS fill:#fff,stroke:#777
        style AUD fill:#fff,stroke:#777
    end

    %% --- Main Flow: Layer by Layer ---

    %% 1. Input Layer
    subgraph InputLayer ["&nbsp;&nbsp;Input Layer&nbsp;&nbsp;<br/>(External Systems)"]
        direction TB
        style InputLayer fill:#f5f5f5,stroke:#9e9e9e,stroke-width:1px,color:#000
        Outlook[("fa:fa-envelope Outlook<br/>(Email Sources)")]
        GraphAPI[("fa:fa-plug Microsoft Graph API<br/>(APIs)")]
        Outlook -->|Polls| GraphAPI
        style Outlook fill:#fff,stroke:#0277bd,color:#0277bd
        style GraphAPI fill:#fff,stroke:#0277bd,color:#0277bd
    end

    %% 2. Ingestion Gateway
    subgraph Ingestion["&nbsp;&nbsp;Secure Ingestion Gateway&nbsp;&nbsp;<br/>(FastAPI)"]
        direction TB
        style Ingestion fill:#e3f2fd,stroke:#1565c0,stroke-width:1px,color:#000,font-weight:bold
        AuthV[("Azure AD Auth<br/>Validation")]
        FileTypeV["File Type Validation"]
        FileSizeV["File Size Validation"]
        SchemaV["Basic Schema Validation"]
        
        AuthV --> FileTypeV --> FileSizeV --> SchemaV
        style AuthV fill:#fff,stroke:#1565c0
        style FileTypeV fill:#fff,stroke:#1565c0
        style FileSizeV fill:#fff,stroke:#1565c0
        style SchemaV fill:#fff,stroke:#1565c0
    end

    %% 3. Content Security
    subgraph ContentSec["&nbsp;&nbsp;Content Security Layer&nbsp;&nbsp;"]
        direction TB
        style ContentSec fill:#f9fbe7,stroke:#827717,stroke-width:1px,color:#000
        Blob[( "fa:fa-file-alt Azure Blob Storage<br/>(document storage)")]
        Defender{{"fa:fa-user-shield Microsoft Defender<br/>for Cloud<br/>(malware scanning)"}}
        MaliciousDecision{"Malicious?"}
        Quarantine[("fa:fa-biohazard Quarantine/<br/>Reject")]

        Blob --> Defender --> MaliciousDecision
        MaliciousDecision -->|Yes| Quarantine
        style Blob fill:#fff,stroke:#827717
        style Defender fill:#fff,stroke:#827717,color:#bf360c
        style MaliciousDecision fill:#fff,stroke:#827717
        style Quarantine fill:#ffebee,stroke:#c62828,color:#c62828
    end

    %% 4. Messaging
    subgraph MsgLayer["&nbsp;&nbsp;Messaging Layer&nbsp;&nbsp;"]
        style MsgLayer fill:#e1f5fe,stroke:#0277bd,stroke-width:1px,color:#000
        ServiceBus[("fa:fa-exchange-alt Azure Service Bus (Queue)<hr/>- Asynchronous processing<br/>- Retry handling<br/>- Decoupling services")]
        style ServiceBus fill:#fff,stroke:#0277bd,stroke-width:2px
    end

    %% 5. Processing
    subgraph ProcLayer["&nbsp;&nbsp;Processing Layer&nbsp;&nbsp;"]
        direction TB
        style ProcLayer fill:#f3e5f5,stroke:#6a1b9a,stroke-width:1px,color:#000
        DocIntel[("fa:fa-file-contract Azure Document<br/>Intelligence (OCR)")]
        TextExt["Text Extraction Service"]
        ExtractedStore[("fa:fa-file-signature Extracted Text<br/>(Blob Storage)")]

        DocIntel --> TextExt --> ExtractedStore
        style DocIntel fill:#fff,stroke:#6a1b9a
        style TextExt fill:#fff,stroke:#6a1b9a
        style ExtractedStore fill:#fff,stroke:#6a1b9a
    end

    %% 6. LLM Security (New!)
    subgraph LLMSec["&nbsp;&nbsp;LLM Security Layer&nbsp;&nbsp;"]
        direction TB
        style LLMSec fill:#fffde7,stroke:#fbc02d,stroke-width:1px,color:#000
        Masking["PII Masking /<br/>Redaction"]
        Minimization["Data Minimization"]
        SecureOpenAI["fa:fa-link Secure Azure OpenAI<br/>access (Private Endpoint)"]

        Masking --> Minimization --> SecureOpenAI
        style Masking fill:#fff,stroke:#fbc02d
        style Minimization fill:#fff,stroke:#fbc02d
        style SecureOpenAI fill:#fff,stroke:#fbc02d
    end

    %% 7. AI / Agent
    subgraph AILayer["&nbsp;&nbsp;AI / Agent Layer&nbsp;&nbsp;<br/>(LangChain + Azure OpenAI)"]
        direction TB
        style AILayer fill:#e8f5e9,stroke:#2e7d32,stroke-width:1px,color:#000,font-weight:bold
        Classifier["fa:fa-filter Classifier<br/>(Identifies claim type)"]
        Extractor["fa:fa-box-open Extractor<br/>(Unstructured -> JSON)"]
        Validator["fa:fa-tasks Validator<br/>(Completeness, Rules,<br/>Confidence, Errors)"]

        Classifier --> Extractor --> Validator
        style Classifier fill:#fff,stroke:#2e7d32
        style Extractor fill:#fff,stroke:#2e7d32
        style Validator fill:#fff,stroke:#2e7d32
    end

    %% 8. Routing & Decision
    subgraph RouteLayer["&nbsp;&nbsp;Routing & Decision Layer&nbsp;&nbsp;"]
        direction TB
        style RouteLayer fill:#fff3e0,stroke:#ef6c00,stroke-width:1px,color:#000
        RouteRules{"Routing based on:<br/>- Claim type<br/>- Confidence score<br/>- Business rules"}
        ValidDecision{"Is data<br/>valid?"}
        
        RouteRules --> ValidDecision
        style RouteRules fill:#fff,stroke:#ef6c00
        style ValidDecision fill:#fff,stroke:#ef6c00
    end

    %% 9. Human-in-the-loop
    subgraph HITLLayer["&nbsp;&nbsp;Human-in-the-loop Layer&nbsp;&nbsp;"]
        direction TB
        style HITLLayer fill:#fce4ec,stroke:#c2185b,stroke-width:1px,color:#000
        ReviewQueue[("fa:fa-list-ol Human Review<br/>Queue")]
        ManualInterface["fa:fa-desktop Manual Fix<br/>Interface"]
        HumanAction["fa:fa-user-edit Human validates<br/>and corrects data"]
        
        ReviewQueue --> ManualInterface --> HumanAction
        style ReviewQueue fill:#fff,stroke:#c2185b
        style ManualInterface fill:#fff,stroke:#c2185b
        style HumanAction fill:#fff,stroke:#c2185b
    end

    %% 10. Integration & Output
    subgraph OutLayer["&nbsp;&nbsp;Integration & Output Layer&nbsp;&nbsp;"]
        direction TB
        style OutLayer fill:#eceff1,stroke:#546e7a,stroke-width:1px,color:#000
        CreateClaimAPI["fa:fa-rocket Create Claim API"]
        ClaimsBackend[("fa:fa-server Claims Backend System<br/>(External API)<br/>→ System of Record")]
        SQLDB[("fa:fa-database SQL Database<br/>(metadata and tracking)")]
        
        CreateClaimAPI --> ClaimsBackend
        CreateClaimAPI --> SQLDB
        
        style CreateClaimAPI fill:#e3f2fd,stroke:#1565c0,font-weight:bold
        style ClaimsBackend fill:#fff,stroke:#546e7a
        style SQLDB fill:#fff,stroke:#546e7a
    end

    %% --- Connectors (The Flow) ---
    GraphAPI ==> Ingestion
    Ingestion ==> Blob
    MaliciousDecision -->|No| MsgLayer
    ServiceBus ==> DocIntel
    ExtractedStore ==> Masking
    SecureOpenAI ==> Classifier
    Validator ==> RouteRules
    ValidDecision ==>|YES| CreateClaimAPI
    ValidDecision ==>|NO| ReviewQueue
    HumanAction ==> CreateClaimAPI

    %% Define thick connection style
    linkStyle 16,17,19,20,22 stroke-width:3px,stroke:#1565c0;
    linkStyle 25 stroke-width:3px,stroke:#c2185b;
