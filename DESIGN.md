# Design Documentation

## Frontend Architecture
The frontend is built using **React** with **Vite** as the build tool, ensuring fast development and optimized production builds.

### Tech Stack
- **Framework**: React 19
- **Build Tool**: Vite
- **Styling**: TailwindCSS 4
- **Routing**: React Router DOM 7
- **Icons**: React Icons
- **Animations**: Framer Motion

## Design System
The application uses a modern, clean design with a focus on usability and visual appeal.

### Styling Approach
- **TailwindCSS**: Utility-first CSS framework for rapid UI development.
- **Custom CSS**: `App.css` and `index.css` for global styles and specific component overrides.
- **Responsive Design**: Mobile-first approach ensuring compatibility across devices.

### Color Palette
(Inferred from visual inspection and CSS)
- **Primary**: Deep Blues/Purples (often used in gradients or headers).
- **Secondary**: Lighter accents for buttons and highlights.
- **Background**: Light/Dark modes (implied by modern design trends, though specific implementation details may vary).

## Component Structure
The application follows a modular component structure located in `src/Components`.

### Core Components
- **`App.jsx`**: Main application entry point, handling routing and layout.
- **`Navbar.jsx`**: Top navigation bar, conditionally rendered based on authentication state.
- **`LoginRegister`**: Unified component for Login, Registration, Forgot Password, and Reset Password flows.
- **`Profile`**: Displays user profile information.
- **`EditProfile`**: Form to update user details.
- **`SuccessPage`**: Landing page after successful actions (e.g., login).

## User Flow
1. **Authentication**: Users land on the Login/Register page.
2. **Dashboard/Home**: After login, users are redirected to the main feed (implementation pending/in-progress).
3. **Navigation**: Navbar provides access to Profile, Home, and Logout.

## Key Design Decisions
- **Unified Auth Page**: Combining Login and Register into a single view with a toggle for a smoother user experience.
- **Conditional Layout**: Hiding the Navbar on authentication pages to minimize distractions.
