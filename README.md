# Integrated Governance, Risk & Compliance (GRC) Platform with AI-Assisted Risk Analysis

## Overview

A comprehensive, open-source GRC platform designed to help organizations manage security policies, assess and monitor risks, ensure compliance with industry standards, and conduct security audits. The platform leverages AI capabilities with Ollama and Llama 3 to provide intelligent risk analysis, compliance gap identification, and policy recommendations.

## Key Features

✅ **Governance Management** - Policy, standards, and control management
✅ **Risk Assessment** - Intelligent risk calculation based on likelihood and impact
✅ **Compliance Monitoring** - Support for ISO 27001, NIST CSF, and CIS Controls
✅ **Asset Inventory** - Comprehensive asset tracking and management
✅ **Audit Management** - Recording findings, tracking corrective actions
✅ **AI-Assisted Analysis** - Ollama/Llama 3 integration for intelligent recommendations
✅ **Interactive Dashboards** - Real-time risk scores, compliance status, and audit progress
✅ **Advanced Reporting** - Comprehensive reports for management and auditors
✅ **Role-Based Access Control** - Keycloak-based authentication and authorization

## Architecture

```
┌─────────────────────────────────────────┐
│         Frontend (React)                 │
│  - Dashboards                           │
│  - Policy Management UI                 │
│  - Risk Assessment Forms                │
│  - Compliance Tracking                  │
└──────────────┬──────────────────────────┘
               │
      ┌────────┴────────┐
      │                 │
  ┌───▼───────────┐  ┌──▼──────────────┐
  │ API Gateway   │  │  Auth Service   │
  │ (FastAPI)     │  │  (Keycloak)     │
  └───┬───────────┘  └─────────────────┘
      │
┌─────┴──────────────────────────────────┐
│      Backend Services (FastAPI)         │
│  ├── Governance Module                  │
│  ├── Risk Assessment Engine             │
│  ├── Compliance Module                  │
│  ├── Asset Inventory Service            │
│  ├── Audit Management Service           │
│  └── AI Integration Service (Ollama)    │
└─────┬──────────────────────────────────┘
      │
┌─────┴──────────────────────────────────┐
│      Data Layer                         │
│  ├── PostgreSQL Database                │
│  ├── Cache Layer (Redis)                │
│  └── Document Storage                   │
└─────────────────────────────────────────┘
      │
┌─────┴──────────────────────────────────┐
│      AI Engine (Ollama + Llama 3)       │
│  - Risk Analysis                        │
│  - Compliance Gap Identification        │
│  - Policy Recommendations               │
└─────────────────────────────────────────┘
```

## Tech Stack

### Frontend
- **React** - UI framework
- **Chart.js** - Data visualization
- **Axios** - HTTP client
- **React Router** - Navigation

### Backend
- **Python 3.9+** - Core language
- **FastAPI** - Web framework
- **SQLAlchemy** - ORM
- **Pydantic** - Data validation

### Database
- **PostgreSQL** - Primary database
- **Redis** - Caching layer

### Authentication & Security
- **Keycloak** - Identity and access management
- **JWT** - Token-based authentication

### AI & ML
- **Ollama** - LLM runtime
- **Llama 3** - Language model

### DevOps
- **Docker** - Containerization
- **Docker Compose** - Orchestration
- **Git** - Version control

## Project Structure

```
riskmanagement/
├── frontend/                    # React application
│   ├── public/
│   ├── src/
│   │   ├── components/         # Reusable components
│   │   ├── pages/              # Page components
│   │   ├── services/           # API services
│   │   ├── contexts/           # React contexts
│   │   ├── styles/             # CSS files
│   │   └── App.js
│   └── package.json
│
├── backend/                     # FastAPI application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py             # FastAPI app initialization
│   │   ├── config.py           # Configuration
│   │   ├── database.py         # Database setup
│   │   ├── dependencies.py     # Dependencies
│   │   ├── models/             # SQLAlchemy models
│   │   ├── schemas/            # Pydantic schemas
│   │   ├── routers/            # API routes
│   │   ├── services/           # Business logic
│   │   ├── utils/              # Utility functions
│   │   └── ai/                 # AI integration
│   ├── tests/                  # Unit tests
│   ├── requirements.txt        # Python dependencies
│   └── main.py                 # Entry point
│
├── docker-compose.yml          # Container orchestration
├── Dockerfile.backend          # Backend Docker image
├── Dockerfile.frontend         # Frontend Docker image
├── .env.example                # Environment variables template
└── README.md                   # This file
```

## Installation & Setup

### Prerequisites
- Docker and Docker Compose
- Node.js 16+ (for local frontend development)
- Python 3.9+ (for local backend development)
- PostgreSQL 12+ (or use Docker)
- Ollama (for AI features)

### Quick Start with Docker

1. **Clone the repository**
   ```bash
   git clone https://github.com/techmahindrahero-png/riskmanagement.git
   cd riskmanagement
   ```

2. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your settings
   ```

3. **Start all services**
   ```bash
   docker-compose up -d
   ```

4. **Initialize database**
   ```bash
   docker-compose exec backend python app/database.py
   ```

5. **Access the application**
   - Frontend: http://localhost:3000
   - API: http://localhost:8000
   - API Docs: http://localhost:8000/docs
   - Keycloak: http://localhost:8080

### Local Development Setup

#### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run migrations
alembic upgrade head

# Start development server
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

#### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/logout` - User logout
- `POST /api/auth/refresh` - Refresh token

### Governance
- `GET /api/governance/policies` - List policies
- `POST /api/governance/policies` - Create policy
- `GET /api/governance/policies/{id}` - Get policy details
- `PUT /api/governance/policies/{id}` - Update policy
- `DELETE /api/governance/policies/{id}` - Delete policy

### Risk Management
- `GET /api/risks/register` - List risk register
- `POST /api/risks/register` - Add risk
- `GET /api/risks/assessments` - List assessments
- `POST /api/risks/assessments` - Create assessment
- `GET /api/risks/score` - Calculate risk score

### Compliance
- `GET /api/compliance/frameworks` - List compliance frameworks
- `GET /api/compliance/status` - Compliance status
- `POST /api/compliance/gaps` - Identify compliance gaps
- `GET /api/compliance/gaps` - View identified gaps

### Assets
- `GET /api/assets/inventory` - List assets
- `POST /api/assets/inventory` - Add asset
- `PUT /api/assets/inventory/{id}` - Update asset
- `DELETE /api/assets/inventory/{id}` - Delete asset

### Audits
- `GET /api/audits` - List audits
- `POST /api/audits` - Create audit
- `GET /api/audits/{id}/findings` - List findings
- `POST /api/audits/{id}/findings` - Add finding
- `POST /api/audits/{id}/corrective-actions` - Add corrective action

### AI Services
- `POST /api/ai/risk-analysis` - Get AI risk analysis
- `POST /api/ai/compliance-recommendations` - Get compliance recommendations
- `POST /api/ai/policy-generation` - Generate policies with AI

### Dashboards & Reports
- `GET /api/dashboard/summary` - Dashboard summary
- `GET /api/reports/risk-assessment` - Risk assessment report
- `GET /api/reports/compliance` - Compliance report
- `GET /api/reports/audit` - Audit report

## Configuration

### Environment Variables (.env)

```env
# Database
DATABASE_URL=postgresql://user:password@localhost:5432/grcdb
REDIS_URL=redis://localhost:6379/0

# JWT
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Keycloak
KEYCLOAK_SERVER_URL=http://localhost:8080
KEYCLOAK_REALM=grc
KEYCLOAK_CLIENT_ID=grc-app
KEYCLOAK_CLIENT_SECRET=your-client-secret

# Ollama
OLLAMA_API_URL=http://localhost:11434
OLLAMA_MODEL=llama2

# API
API_TITLE=GRC Platform API
API_VERSION=1.0.0
API_HOST=0.0.0.0
API_PORT=8000

# Frontend
REACT_APP_API_URL=http://localhost:8000
REACT_APP_KEYCLOAK_URL=http://localhost:8080
```

## Database Schema

Key tables:
- `users` - User accounts
- `roles` - User roles
- `policies` - Governance policies
- `controls` - Control definitions
- `risks` - Risk register
- `risk_assessments` - Risk assessment records
- `assets` - Asset inventory
- `compliance_frameworks` - Compliance standards
- `compliance_mappings` - Policy-to-compliance mappings
- `audits` - Audit records
- `findings` - Audit findings
- `corrective_actions` - Corrective action tracking

## Development Workflow

1. **Create Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make Changes**
   - Follow code style guidelines
   - Write tests for new features
   - Update documentation

3. **Commit Changes**
   ```bash
   git add .
   git commit -m "feat: add your feature description"
   ```

4. **Push & Create PR**
   ```bash
   git push origin feature/your-feature-name
   ```

## Testing

### Run Backend Tests
```bash
cd backend
pytest tests/ -v
```

### Run Frontend Tests
```bash
cd frontend
npm test
```

## Deployment

### Production Deployment

1. **Build Docker images**
   ```bash
   docker build -f Dockerfile.backend -t grc-backend:latest .
   docker build -f Dockerfile.frontend -t grc-frontend:latest .
   ```

2. **Push to registry**
   ```bash
   docker tag grc-backend:latest your-registry/grc-backend:latest
   docker push your-registry/grc-backend:latest
   ```

3. **Deploy with docker-compose**
   ```bash
   docker-compose -f docker-compose.prod.yml up -d
   ```

## Security Considerations

- ✅ JWT token-based authentication
- ✅ Role-based access control (RBAC)
- ✅ SQL injection prevention via SQLAlchemy ORM
- ✅ CORS configuration for API security
- ✅ Rate limiting on API endpoints
- ✅ Input validation with Pydantic
- ✅ HTTPS support (configure in production)
- ✅ Secure secret management via environment variables

## Performance Optimization

- 🚀 Redis caching for frequently accessed data
- 🚀 Database query optimization with indexes
- 🚀 Lazy loading for large datasets
- 🚀 Frontend component code splitting
- 🚀 API response pagination

## Compliance Standards Supported

- 🏆 **ISO 27001** - Information Security Management
- 🏆 **NIST CSF** - Cybersecurity Framework
- 🏆 **CIS Controls** - Critical Security Controls
- 🏆 **GDPR** - General Data Protection Regulation
- 🏆 **SOC 2** - Service Organization Control

## Troubleshooting

### Database Connection Issues
```bash
# Check if PostgreSQL is running
docker ps | grep postgres

# View database logs
docker logs grc-postgres
```

### API Connection Issues
```bash
# Check if API is running
curl http://localhost:8000/docs

# View API logs
docker logs grc-backend
```

### Ollama Connection Issues
```bash
# Verify Ollama is running
curl http://localhost:11434/api/tags

# Pull the model
ollama pull llama2
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Write/update tests
5. Submit a pull request

## License

MIT License - See LICENSE file for details

## Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Check existing documentation
- Contact the development team

## Roadmap

### Phase 1 (Q3 2026)
- ✅ Core GRC framework
- ✅ User authentication
- ✅ Basic dashboards

### Phase 2 (Q4 2026)
- 🔄 AI integration with Ollama
- 🔄 Advanced reporting
- 🔄 Mobile app

### Phase 3 (Q1 2027)
- 📋 Multi-tenant support
- 📋 Advanced analytics
- 📋 Integration APIs

---

**Last Updated:** July 17, 2026
**Version:** 1.0.0
