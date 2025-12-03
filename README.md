# BragBoard - Peer Recognition Platform

BragBoard is an internal employee engagement platform designed to foster a culture of appreciation. It allows team members to send "shoutouts" to colleagues, celebrating their achievements and contributions.

## 📚 Documentation

For detailed information about the project, please refer to the following documents:

- **[Features](FEATURES.md)**: Comprehensive list of application features and user workflows.
- **[Design](DESIGN.md)**: Frontend architecture, design system, and component structure.
- **[Backend](BACKEND.md)**: Backend architecture, API endpoints, and database schema.

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
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   # source venv/bin/activate
   pip install -r requirements.txt
   uvicorn app.main:app --reload
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   npm install
   npm run dev
   ```

## 🛠️ Tech Stack

- **Frontend**: React, Vite, TailwindCSS
- **Backend**: FastAPI, SQLAlchemy
- **Database**: SQLite (Dev) / PostgreSQL (Prod)

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request
