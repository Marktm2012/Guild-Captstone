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
        - enrollments (manytomany to course)

- Course Model
    - Title (CharField)
    - Overview (TextField)
    - Start Date (DateField)
    - Instructor (ForeignKey to User)
    - Price (FloatField)
- Lesson Model
    - Course (ForeignKey to Course)
    - Title (CharField)
    - Overview (TextField)
    - Due Date (DateField)
- Lesson Uploads Model
    - Lesson (ForeignKey to Lesson)
    - Title (CharField)
    - Media (FileField)
- Student Submission Model
    - Lesson (ForeignKey to Lesson)
    - Student (ForeignKey to User)
    - Submission (FileField)
    - Feedback (TextField)

## Schedule
- Week 1
    - Create custom user model
    - Create models
    - render registration/login page
    - Get form submission for user creation and login working
    - Troubleshooting
- Week 2
    - Create Course Page
        - Add Course/Lesson Creation (Only available to Instructor)
        - Add Assignment submission (student side only)
        - Add feedback submission (Instructor side only)
- Week 3
    - Invoice, payments
    - Media Uploads
    - Styling
    - Testing