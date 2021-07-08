# Guild-Captstone

## Project Overview
The Instructor's Agenda is a Django application for Private Lesson management. Where private instructors can upload and manage documentation, media, track grading and due dates. I would also like to add invoicing and maybe a payment system.

Libraries Used:
    - Django
    - Bootstrap
    - Vue
    - Axios
    - CKEditor

## Functionality
- Custom User System
    - Teacher/Instructor
        - Login
        - New Instructor Registration
    - Student
        - Login
        - New Student Registration
- User Profile
    - Displays user information and can be edited if needed
    - View instructing/enrolled classes
    - Create a new course
- Course Page
    - Displays Overview of the course
    - Create/Edit lessons as needed
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