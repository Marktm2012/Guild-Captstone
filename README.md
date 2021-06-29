# Guild-Captstone

## Project Overview
The Instructor's Agenda is a Django application for Private Lesson management. Where private instructors can upload and manage documentation, media, track grading and due dates. I would also like to add invoicing and maybe a payment system.

Libraries Used:
    - Django
    - Bootstrap
    - Vue/Vuetify
    - Axios

## Functionality
- Custom User System
    - Teacher/Instructor
        - Login
        - New Instructor Registration
    - Student
        - Login
        - New Student Registration
- Instructor Page
    - Document Upload
    - Media uploads (audio/video)
    - Scheduling (Google Calenders?)
    - Cancel/Add Lessons
- Course Catalouge
    - Description of Course
    - Course Length
    - Cost
- Student Page
    - View lesson Documentation/Media
    - Upload course completed assignments
    - View due dates for lessons and payments
- Billing
    - Track Payments
    - Alerts student and teacher when a new payment is due
## Data Model
- Custom User model
    - User
        - First/Last Name (CharField)
        - Birthday (DateField)
        - email (emailField)
        - Bio (CharField)
        - Location (Charfield)
        - Phone Number (CharField)
        - Instructor T/F (BoolField)

- Course Uploads
    - Course Descriptions (TextField)
    - Instructor (Foreign Key to Instructor)
    - Media(Audio/Video) (FileField)
    - Due Dates (DateTimeField)
    - Pricing (IntegerField)
## Schedule
- Week 1
    - Create custom user model
    - Create models
    - render registration/login page
    - Get form submission for user creation and login working
    - Troubleshooting
- Week 2
    - Troubleshooting
- Week 3
    - Invoice, payments
    - Media Uploads
    - Styling
    - Testing