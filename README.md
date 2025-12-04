# BragBoard - Peer Recognition Platform

BragBoard is an internal employee engagement platform designed to foster a culture of appreciation. It allows team members to send "shoutouts" to colleagues, celebrating their achievements and contributions.

## 📚 Documentation

For detailed information about the project, please refer to the following documents:

- **[Project Status](PROJECT_STATUS.md)**: Current progress tracking against the 8-week milestone plan.
- **[Features](FEATURES.md)**: Comprehensive list of application features, user workflows, and technical implementation details.
- **[Design](DESIGN.md)**: Frontend architecture, design system, component structure, and tech stack versions.
- **[Backend](BACKEND.md)**: Backend architecture, API endpoints, database schema, and security practices.

## 🛠️ Tech Stack

### Frontend
- **Framework**: React 19
- **Build Tool**: Vite 7
- **Styling**: TailwindCSS 4
- **Routing**: React Router DOM 7
- **Icons**: React Icons
- **Animations**: Framer Motion

### Backend
- **Framework**: FastAPI
- **Server**: Uvicorn
- **Database ORM**: SQLAlchemy
- **Authentication**: JWT (JSON Web Tokens) with `python-jose`
- **Validation**: Pydantic

### Database
- **Development**: SQLite
- **Production**: PostgreSQL (Supported via `psycopg2-binary`)

## 🚀 Getting Started

### Prerequisites
- Node.js (v18+)
- Python (v3.8+)

### Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd infosysSpringboard-Batch2
   ```

2. **Backend Setup**
   ```bash
   cd backend
   # Create virtual environment
   python -m venv venv
   
   # Activate virtual environment
   # Windows:
   venv\Scripts\activate
   # macOS/Linux:
   # source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run the server
   python -m uvicorn app.main:app --reload
   ```
   The API will be available at `http://localhost:8000`.
   API Documentation (Swagger UI) is available at `http://localhost:8000/docs`.

3. **Frontend Setup**
   ```bash
   cd frontend
   # Install dependencies
   npm install
   
   # Run the development server
   npm run dev
   ```
   The application will be available at `http://localhost:5173`.

## 📂 Project Structure

```
infosysSpringboard-Batch2/
├── backend/                # FastAPI Backend
│   ├── app/
│   │   ├── routers/        # API Routes (auth, users, etc.)
│   │   ├── models.py       # Database Models
│   │   ├── schemas.py      # Pydantic Schemas
│   │   └── main.py         # Application Entry Point
│   ├── requirements.txt    # Python Dependencies
│   └── bragboard.db        # SQLite Database (Dev)
├── frontend/               # React Frontend
│   ├── src/
│   │   ├── Components/     # React Components
│   │   ├── App.jsx         # Main Component
│   │   └── main.jsx        # Entry Point
│   ├── package.json        # Node.js Dependencies
│   └── vite.config.js      # Vite Configuration
└── README.md               # Project Documentation
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
