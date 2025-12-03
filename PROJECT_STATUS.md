# Project Status & Milestones

This document tracks the progress of the BragBoard project against the 8-Week Milestone Plan.

## ✅ Milestone 1: User System & Basic UI (Weeks 1–2)
**Status: COMPLETED**

- [x] **Project Setup**
    - [x] Set up React + FastAPI structure
    - [x] Configure PostgreSQL database
- [x] **User Authentication (Backend)**
    - [x] User Registration endpoint (`/auth/register`)
    - [x] User Login endpoint (`/auth/login`)
    - [x] JWT Token generation & validation
    - [x] Password Hashing (bcrypt)
- [x] **User Management (Backend)**
    - [x] User Model (Name, Email, Password, Role, Department)
    - [x] Get Current User endpoint (`/users/me`)
    - [x] Update User Profile endpoint
- [x] **Frontend UI**
    - [x] Login / Register Pages
    - [x] Profile Page (View & Edit)
    - [x] Basic Routing & Layout

---

## 🚧 Milestone 2: Shout-Out Posting & Feed (Weeks 3–4)
**Status: PENDING**

- [ ] **Backend API**
    - [ ] Create Shoutout endpoint (`POST /shoutouts`)
    - [ ] Get Shoutouts Feed endpoint (`GET /shoutouts`)
    - [ ] Filter Shoutouts (by department, date)
- [ ] **Frontend Components**
    - [ ] Shoutout Creation Form (with recipient tagging)
    - [ ] Shoutout Feed Display (Cards)
    - [ ] Department Filtering UI

---

## 🚧 Milestone 3: Reactions & Comments (Weeks 5–6)
**Status: PENDING**

- [ ] **Backend API**
    - [ ] Add Reaction endpoint (`POST /shoutouts/{id}/react`)
    - [ ] Add Comment endpoint (`POST /shoutouts/{id}/comment`)
    - [ ] Get Comments for Shoutout
- [ ] **Frontend Components**
    - [ ] Reaction Buttons (Like, Clap, Star) with counters
    - [ ] Comment Section (Input & List)
    - [ ] Real-time updates (optional/polling)

---

## 🚧 Milestone 4: Admin Tools & Analytics (Weeks 7–8)
**Status: PENDING**

- [ ] **Backend API**
    - [ ] Admin Middleware (Role check)
    - [ ] Admin Analytics endpoints (Top contributors, etc.)
    - [ ] Moderation endpoints (Delete post/comment)
    - [ ] Reporting system
- [ ] **Frontend Components**
    - [ ] Admin Dashboard Layout
    - [ ] Analytics Charts/Stats
    - [ ] Moderation Queue (Reported items)
    - [ ] User Management (Admin view)
