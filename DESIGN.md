# Design Documentation

## Frontend Architecture
The frontend is built using **React** with **Vite** as the build tool, ensuring fast development and optimized production builds.

### Tech Stack
- **Framework**: React v19.2.0
- **Build Tool**: Vite v7.2.4
- **Styling**: TailwindCSS v4.1.17
- **Routing**: React Router DOM v7.10.0
- **Animations**: Framer Motion v12.23.25
- **Icons**: React Icons v5.5.0

## Design System
The application uses a modern, clean design with a focus on usability and visual appeal.

### Styling Approach
- **TailwindCSS**: Used for 95% of styling. We utilize utility classes for layout, spacing, typography, and colors.
    - *Example*: `className="flex flex-col items-center justify-center min-h-screen bg-gray-100"`
- **Custom CSS**: `App.css` and `index.css` are used for:
    - Global resets.
    - Complex animations not easily achievable with utility classes.
    - Custom scrollbar styling.
- **Responsive Design**: Mobile-first approach using Tailwind's breakpoints (`sm`, `md`, `lg`, `xl`).
    - *Pattern*: `w-full md:w-1/2 lg:w-1/3` ensures components adapt to screen width.

### Color Palette
- **Primary**: Deep Blue/Purple gradients for branding and headers.
- **Secondary**: Soft grays and whites for content backgrounds to ensure readability.
- **Accents**: Vibrant colors for actions (e.g., Green for success, Red for errors/logout).
- **Feedback**:
    - **Success**: Green-500
    - **Error**: Red-500
    - **Warning**: Yellow-500

## Component Structure
The application follows a modular component structure located in `src/Components`.

### Core Components
- **`App.jsx`**: Main application entry point.
    - **Role**: Sets up the `Router`, defines `Routes`, and manages the global layout (e.g., `Navbar` visibility).
- **`Navbar.jsx`**: Top navigation bar.
    - **Logic**: Conditionally rendered based on the current path (hidden on Login/Register).
    - **Features**: Links to Home, Profile, and Logout functionality.
- **`LoginRegister`**: Unified component for Auth.
    - **State**: Uses a `mode` state (`login`, `register`, `forgot`) to toggle between different forms within the same container.
    - **Animation**: Uses CSS transitions to smoothly switch between modes.
- **`Profile`**: Displays user profile.
    - **Data Fetching**: Fetches user data on mount using `useEffect`.
- **`EditProfile`**: Form to update user details.
    - **Validation**: Basic HTML5 validation + controlled inputs.

## User Flow & Routing
- **Routing Library**: `react-router-dom` v7
- **Route Configuration**:
    - `/`: Login/Register Page (Public)
    - `/success`: Success Landing Page (Protected/Public)
    - `/profile`: User Profile (Protected)
    - `/profile/edit`: Edit Profile (Protected)
- **Navigation**: `useNavigate` hook is used for programmatic navigation after actions (e.g., redirect to `/success` after login).

## Key Design Decisions
- **Unified Auth Page**: Combining Login and Register into a single view with a toggle reduces friction and keeps the user context.
- **Conditional Layout**: Hiding the Navbar on authentication pages minimizes distractions and focuses the user on the entry task.
- **Feedback Loops**: Immediate visual feedback (toast messages or inline text) for all user actions (login success, error messages).
