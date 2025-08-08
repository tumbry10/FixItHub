# 🛠️ FixItHub

**FixItHub** is a community-driven fault reporting system built with Django. It allows users to report issues (e.g., infrastructure faults), track their status, and communicate with system administrators. It's designed to streamline communication between users and system administrators.

---

## 🔧 Core Features Implemented

### 👥 User Management
- Custom user model with two user types:
  - `SystAdmin`: System administrator (registered via admin site/terminal only)
  - `SystUser`: Regular users who can register via the web
- Login, logout, registration
- UserProfile created automatically via Django signals
- Profile editing and viewing, including uploading a profile picture

### 📝 Issue Reporting
- SystUsers can:
  - Report new issues
  - View and edit **only their own issues**, if the status is still "Pending"
  - Delete their own issues
- SystAdmins can:
  - View all issues
  - Edit any issue (via a separate admin-specific edit view)
  - Delete issues

### 🖥️ Dashboards
- Separate dashboard views for:
  - SystAdmin (manage all issues)
  - SystUser (see and manage their own reports)

### 📸 Profile Management
- Profile view includes:
  - User bio, address, phone number
  - Uploaded profile picture (displayed and stored properly)
- Profile edit view with image upload support

---

## ⚙️ Technologies Used

- Django
- Django Templates
- SQLite (default dev DB)
- Custom signals for profile + user type creation

---