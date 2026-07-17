# GRC Platform Architecture

## System Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Presentation Layer                        │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  React Web Application (SPA)                         │   │
│  │  ├── Dashboards & Analytics                          │   │
│  │  ├── Policy Management UI                            │   │
│  │  ├── Risk Assessment Forms                           │   │
│  │  ├── Compliance Tracking                             │   │
│  │  └── Audit Management                               │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                           │
           ┌───────────────┴───────────────┐
           │                               │
┌──────────▼──────────────┐    ┌──────────▼─────────────┐
│  API Gateway/Load      │    │  Authentication        │
│  Balancer              │    │  Service (Keycloak)    │
│  (FastAPI)             │    │  ├── SSO               │
│                        │    │  ├── JWT Tokens        │
└──────────┬─────────────┘    │  └── RBAC              │
           │                  └────────────────────────┘
           │
┌──────────▼─────────────────────────────────────────────────┐
│              Business Logic Layer (FastAPI)                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Microservices / Modular Services                    │  │
│  │                                                      │  │
│  │  ┌────────────────────────────────────────────────┐ │  │
│  │  │ Governance Module                              │ │  │
│  │  │ - Policy Management                            │ │  │
│  │  │ - Control Registry                             │ │  │
│  │  │ - Standards Management                         │ │  │
│  │  └────────────────────────────────────────────────┘ │  │
│  │                                                      │  │
│  │  ┌────────────────────────────────────────────────┐ │  │
│  │  │ Risk Management Module                         │ │  │
│  │  │ - Risk Register                                │ │  │
│  │  │ - Risk Assessment Engine                       │ │  │
│  │  │ - Risk Scoring & Metrics                       │ │  │
│  │  └────────────────────────────────────────────────┘ │  │
│  │                                                      │  │
│  │  ┌────────────────────────────────────────────────┐ │  │
│  │  │ Compliance Module                              │ │  │
│  │  │ - ISO 27001                                    │ │  │
│  │  │ - NIST CSF                                     │ │  │
│  │  │ - CIS Controls                                 │ │  │
│  │  │ - Compliance Gap Analysis                      │ │  │
│  │  └────────────────────────────────────────────────┘ │  │
│  │                                                      │  │
│  │  ┌────────────────────────────────────────────────┐ │  │
│  │  │ Asset Management Module                        │ │  │
│  │  │ - Asset Inventory                              │ │  │
│  │  │ - Asset Tracking                               │ │  │
│  │  │ - Asset Risk Association                       │ │  │
│  │  └────────────────────────────────────────────────┘ │  │
│  │                                                      │  │
│  │  ┌────────────────────────────────────────────────┐ │  │
│  │  │ Audit Module                                   │ │  │
│  │  │ - Audit Planning                               │ │  │
│  │  │ - Finding Management                           │ │  │
│  │  │ - Corrective Action Tracking                   │ │  │
│  │  └────────────────────────────────────────────────┘ │  │
│  │                                                      │  │
│  │  ┌────────────────────────────────────────────────┐ │  │
│  │  │ Dashboard & Reporting Module                   │ │  │
│  │  │ - KPI Calculation                              │ │  │
│  │  │ - Report Generation                            │ │  │
│  │  │ - Analytics                                    │ │  │
│  │  └────────────────────────────────────────────────┘ │  │
│  │                                                      │  │
│  │  ┌────────────────────────────────────────────────┐ │  │
│  │  │ AI Integration Service                         │ │  │
│  │  │ - Risk Analysis Engine                         │ │  │
│  │  │ - Compliance Recommendations                   │ │  │
│  │  │ - Policy Generation                            │ │  │
│  │  │ - Anomaly Detection                            │ │  │
│  │  └────────────────────────────────────────────────┘ │  │
│  │                                                      │  │
│  └──────────────────────────────────────────────────────┘  │
└──────────┬──────────────────────────────────────────────────┘
           │
┌──────────┴───────────────────────────────────────────────────┐
│                    Data Access Layer                         │
│  ┌────────────────────────────────────────────────────────┐ │
│  │  Repository Pattern / DAOs                             │ │
│  │  ├── Policy Repository                                 │ │
│  │  ├── Risk Repository                                   │ │
│  │  ├── Compliance Repository                             │ │
│  │  ├── Asset Repository                                  │ │
│  │  └── Audit Repository                                  │ │
│  └────────────────────────────────────────────────────────┘ │
└──────────┬───────────────────────────────────────────────────┘
           │
    ┌──────┴──────────────┬──────────────┬──────────────┐
    │                     │              │              │
┌───▼──────┐      ┌──────▼────┐    ┌───▼────┐    ┌───▼────┐
│PostgreSQL│      │   Redis   │    │ Ollama │    │ Logs   │
│Database  │      │  Cache    │    │ LLM    │    │ Store  │
└──────────┘      └───────────┘    └────────┘    └────────┘
```

## Database Schema

### Core Tables

#### Users & Roles
```sql
users
├── id (PK)
├── username (UNIQUE)
├── email (UNIQUE)
├── password_hash
├── is_active
├── created_at
└── updated_at

roles
├── id (PK)
├── name (UNIQUE)
├── description
└── permissions (JSON)

user_roles (Junction)
├── user_id (FK)
└── role_id (FK)
```

#### Governance
```sql
policies
├── id (PK)
├── name
├── description
├── policy_type (enum)
├── status (draft/active/archived)
├── effective_date
├── version
├── created_by (FK users)
├── created_at
└── updated_at

standards
├── id (PK)
├── name
├── description
├── framework (ISO27001/NIST/CIS)
├── version
└── metadata (JSON)

controls
├── id (PK)
├── name
├── description
├── control_type (preventive/detective/corrective)
├── standard_id (FK standards)
├── owner_id (FK users)
└── implementation_status
```

#### Risk Management
```sql
risks
├── id (PK)
├── title
├── description
├── risk_category
├── likelihood (1-5)
├── impact (1-5)
├── calculated_score
├── status (identified/mitigating/mitigated/accepted)
├── owner_id (FK users)
├── created_at
└── updated_at

risk_assessments
├── id (PK)
├── risk_id (FK risks)
├── assessment_date
├── likelihood
├── impact
├── mitigation_strategy
├── assessed_by (FK users)
└── notes

mitigations
├── id (PK)
├── risk_id (FK risks)
├── strategy
├── responsible_party (FK users)
├── due_date
├── status
└── progress (%)
```

#### Compliance
```sql
compliance_frameworks
├── id (PK)
├── name (ISO27001/NIST/CIS)
├── version
└── requirements (JSON)

compliance_requirements
├── id (PK)
├── framework_id (FK)
├── requirement_id
├── description
└── controls (array FK controls)

compliance_mappings
├── id (PK)
├── policy_id (FK policies)
├── control_id (FK controls)
├── requirement_id (FK)
└── evidence

compliance_gaps
├── id (PK)
├── framework_id (FK)
├── requirement_id (FK)
├── gap_description
├── severity (high/medium/low)
├── remediation_plan
└── target_date
```

#### Assets
```sql
assets
├── id (PK)
├── name
├── asset_type (hardware/software/data/people)
├── description
├── owner_id (FK users)
├── criticality (high/medium/low)
├── status
├── location
├── created_at
└── updated_at

asset_risks (Junction)
├── asset_id (FK assets)
└── risk_id (FK risks)
```

#### Audit
```sql
audits
├── id (PK)
├── title
├── audit_type (internal/external/compliance)
├── start_date
├── end_date
├── status (planned/in_progress/completed)
├── audit_lead_id (FK users)
├── created_at
└── updated_at

findings
├── id (PK)
├── audit_id (FK audits)
├── title
├── description
├── severity (critical/high/medium/low)
├── finding_date
├── evidence
├── identified_by (FK users)
└── created_at

corrective_actions
├── id (PK)
├── finding_id (FK findings)
├── action_description
├── responsible_party (FK users)
├── due_date
├── status (open/in_progress/completed/verified)
├── target_date
└── completion_date
```

## API Design Patterns

### RESTful Principles
- Resource-based URLs
- Standard HTTP methods (GET, POST, PUT, DELETE)
- Proper status codes
- JSON request/response format

### Request/Response Format
```json
// Success Response
{
  "success": true,
  "data": { /* resource data */ },
  "timestamp": "2026-07-17T10:30:00Z"
}

// Error Response
{
  "success": false,
  "error": {
    "code": "INVALID_INPUT",
    "message": "Detailed error message",
    "details": { /* validation errors */ }
  },
  "timestamp": "2026-07-17T10:30:00Z"
}
```

## Security Architecture

### Authentication Flow
1. User logs in with credentials
2. Keycloak validates and issues JWT token
3. Frontend stores JWT in secure storage
4. Subsequent requests include JWT in Authorization header
5. Backend validates JWT and extracts user info
6. Authorization checks via role-based access control

### Authorization Levels
- **Admin**: Full system access
- **Manager**: Governance, risk, and compliance management
- **Auditor**: Audit and compliance viewing
- **Owner**: Asset and risk ownership
- **Viewer**: Read-only access

### Data Protection
- Passwords hashed with bcrypt
- Sensitive data encrypted at rest
- HTTPS for all communications
- API rate limiting
- SQL injection prevention via ORM

## Caching Strategy

### Redis Cache Layers
- **User Cache**: 1 hour TTL
- **Policy Cache**: 2 hours TTL
- **Risk Scores**: 30 minutes TTL
- **Compliance Status**: 1 hour TTL
- **Dashboard Data**: 15 minutes TTL

### Cache Invalidation
- Event-driven invalidation on data updates
- Time-based expiration (TTL)
- Manual cache clearing for critical updates

## AI Integration Architecture

### Ollama Integration
```python
# Service structure
AI Service
├── Request Handler
├── Prompt Engineering
├── Response Processing
├── Result Caching
└── Fallback Logic
```

### Use Cases
1. **Risk Analysis**: Analyze risks and suggest mitigation strategies
2. **Compliance Gap Identification**: Identify missing compliance controls
3. **Policy Generation**: Draft policies based on frameworks
4. **Anomaly Detection**: Identify unusual patterns in risk assessments

## Deployment Architecture

### Docker Containerization
- Microservices in separate containers
- Container orchestration with Docker Compose
- Volume mounting for persistent data
- Health checks for service availability

### Scaling Strategy
- Horizontal scaling of API servers
- Database read replicas
- CDN for static assets
- Message queue for async tasks (RabbitMQ/Celery)

## Monitoring & Logging

### Application Monitoring
- Real-time error tracking
- Performance metrics
- API response times
- Database query performance

### Logging Strategy
- Structured JSON logging
- Centralized log aggregation
- Log retention policies
- Audit logging for compliance

## Performance Considerations

### Query Optimization
- Database indexes on frequently queried fields
- Query result pagination
- N+1 query prevention
- Connection pooling

### Frontend Performance
- Code splitting by routes
- Lazy loading of components
- Image optimization
- Browser caching

## Technology Decisions

| Component | Technology | Rationale |
|-----------|-----------|----------|
| Backend | FastAPI | High performance, async support, automatic API docs |
| Frontend | React | Component-based, rich ecosystem, large community |
| Database | PostgreSQL | ACID compliance, JSON support, mature |
| Cache | Redis | High performance, atomic operations, TTL support |
| Auth | Keycloak | Enterprise-grade, SSO support, RBAC |
| AI | Ollama + Llama 3 | Open-source, local deployment, privacy-focused |
| Containers | Docker | Consistency across environments, easy deployment |

---

**Document Version:** 1.0.0
**Last Updated:** July 17, 2026
