# BananaCare: Banana Farm Monitoring and Farmer Assistance Information System

## Problem

Banana farmers may have difficulty keeping organized records of their farm details, production information, disease or pest incidents, and requests for agricultural assistance. Agriculture personnel may also rely on separate or manual records, making it difficult to monitor reported farm conditions, review the history of each farmer, and follow up on pending assistance.

## Objectives

To develop a Banana Farm Monitoring and Farmer Assistance Information System that efficiently manages farmer and farm information, reported farm conditions, and agricultural assistance records.

## Specific Objectives

1. To provide a system for registering and managing farmer and farm records.
2. To allow farmers to report banana diseases, pest infestations, and other farm conditions.
3. To allow agriculture staff to monitor reported conditions and update their status.
4. To provide an assistance-tracking feature for farmer requests, recommendations, and follow-up actions.
5. To make banana farm information and assistance records easier to access and manage.

## System Features

### 1. Farmer and Farm Profile

Stores the basic information of every registered farmer and farm.

Information may include:

- Farmer's full name
- Contact number
- Farm location
- Farm size in hectares
- Banana variety
- Planting date
- Estimated production

### 2. Disease and Farm-Condition Monitoring

This feature allows farmers to report observed farm problems and allows the Admin to monitor each report.

Reported problems may include:

- Fusarium Wilt
- Sigatoka
- Pest Infestation
- Weather Damage
- Soil Condition
- Other farm conditions

Report status may be:

- Reported
- Under Monitoring
- Resolved

### 3. Assistance and Recommendation Tracking

This feature allows farmers to request agricultural assistance and allows the Admin to record progress, recommendations, and completion details.

Assistance may include:

- Seedlings
- Fertilizer
- Training
- Disease-Control Support
- Farm Visit
- Other assistance

Assistance status may be:

- Pending
- In Progress
- Completed

---

## System Requirements

| Requirement | BananaCare Implementation |
|---|---|
| Working User Interface | Python/Flask, HTML, CSS, and Jinja-based BananaCare interface |
| At least 3 major features | 1. Farmer and Farm Profile 2. Disease and Farm-Condition Monitoring 3. Assistance and Recommendation Tracking |
| Data Input and Processing | Register farmers, update farm profiles, submit condition reports, request assistance, update report status, and record recommendations |
| Output/Result | Farmer and Admin dashboards, farm records, report histories, assistance status, staff remarks, and recommendations |
| Input Validation | Required fields, password length, unique username, valid dates, positive farm size, and affected-area limits |
| Error Handling | Invalid login, duplicate username, missing information, invalid numeric values, unauthorized access, and invalid status updates |
| At least 3 test cases | Valid input, invalid input/error handling, and edge cases |

## Technology Used

| Technology | Purpose |
|---|---|
| Python | Used as the main programming language for the application's backend logic. |
| Flask | Used for routing, request processing, authentication workflows, validation, and rendering system pages. |
| HTML5 | Used to structure the system's pages, forms, tables, navigation, and dashboards. |
| CSS3 | Used to create the BananaCare-themed responsive interface, including layouts, cards, forms, tables, and buttons. |
| Jinja | Used to display dynamic records and reusable page content inside HTML templates. |
| SQLAlchemy | Used to define database models and perform database operations through Python. |
| SQLite | Used as the default local classroom and demonstration database. |
| PostgreSQL/Psycopg | Supported as an alternative local database through the configured `DATABASE_URL`. |
| Flask-Login | Used to manage user sessions and protect authenticated pages. |
| Werkzeug | Used to securely hash and verify account passwords. |
| Python unittest | Used to run automated tests using an isolated in-memory database. |

## AI Used

ChatGPT was used during the early planning stage to brainstorm an appropriate mini-system topic and generate the initial Markdown proposal. OpenAI Codex was then used throughout system development as an AI-assisted programming, debugging, refactoring, testing, and documentation tool. The development team reviewed the generated suggestions, requested changes where necessary, tested the resulting system, and remained responsible for verifying that the final implementation met the project requirements.

---

# AI PROMPT AND OUTPUT EVIDENCE

## Brainstorming and Markdown Proposal Prompt

**AI Tool Used:** ChatGPT

**Purpose of the Prompt:**

The purpose of this prompt was to brainstorm an appropriate agriculture-related mini information system and organize the selected idea into a clear Markdown proposal. The prompt asked ChatGPT to identify a practical problem, suggest a system title, define three manageable features, and prepare general and specific objectives suitable for the module assessment.

**What We Used/Changed from the AI Output:**

We selected the suggested Banana Farm Monitoring and Farmer Assistance concept because it provided a clear real-world problem and three features that could be completed within the required project scope. We used the generated Markdown structure as the basis of `BananaCare_Panabo_Mini_System_Proposal.md`. During later planning, we changed the location-specific scope into a reusable theoretical template, retained the farm-location field, and kept the three core modules: farmer and farm records, farm-condition monitoring, and assistance tracking.

**Prompt Screenshot:**

> [INSERT SCREENSHOT OF THE CHATGPT BRAINSTORMING PROMPT HERE]

**Output:**

> [INSERT SCREENSHOT OF CHATGPT GENERATING THE MARKDOWN PROPOSAL HERE]

**Generated File:**

`BananaCare_Panabo_Mini_System_Proposal.md`

> [INSERT SCREENSHOT OF THE GENERATED MARKDOWN FILE HERE]

---

## System Planning Prompt

**AI Tool Used:** OpenAI Codex

**Purpose of the Prompt:**

The purpose of this prompt was to help us establish the overall structure, workflow, user roles, database choice, and main features of the BananaCare system before starting development.

**What We Used/Changed from the AI Output:**

We used the proposed Flask application structure and three-module workflow as a guide. We selected Python and Flask for the web application, PostgreSQL as the preferred database with SQLite as a local fallback, and separate Farmer and Admin login routes. We changed the original location-specific scope into a reusable theoretical template.

**Prompt Screenshot:**

> [INSERT SCREENSHOT OF THE SYSTEM PLANNING PROMPT HERE]

**Output:**

> [INSERT SCREENSHOT OF THE AI PLANNING OUTPUT HERE]

---

## Code Generation Prompt

**AI Tool Used:** OpenAI Codex

**Purpose of the Prompt:**

The purpose of this prompt was to generate the necessary code for the Farmer and Admin portals and the three major BananaCare modules while maintaining a simple project structure suitable for a classroom assessment.

**What We Used/Changed from the AI Output:**

We used the relevant generated Python, Flask, SQLAlchemy, HTML, Jinja, and CSS code. We reviewed the routes, model relationships, input handling, authentication rules, and page content. The implementation was adjusted to support a location-neutral farm template, separate user roles, local demonstration data, and the project requirements from the activity instructions.

**Prompt Screenshot:**

> [INSERT SCREENSHOT OF THE CODE GENERATION PROMPT HERE]

**Output:**

> [INSERT SCREENSHOT/S OF THE GENERATED CODE OR AI OUTPUT HERE]

---

## Debugging Prompt

**AI Tool Used:** OpenAI Codex

**Purpose of the Prompt:**

The purpose of this prompt was to review the application during testing and verify that its required workflows behaved as expected.

**Testing Observation:**

During AI-assisted development, the AI tool encountered an error while checking the application and corrected it immediately before presenting the completed output. Because the error was handled within the AI tool's working process, no separate user-facing screenshot of the error was captured. When the final version was tested, no bugs were found in the executed tests. The tested login, reporting, access-control, administrative, and assistance-request workflows produced their expected results.

**What We Used/Changed from the AI Output:**

The corrected output provided by the AI tool was reviewed through the application's tests. The final executed tests passed, so no additional bug fix was required after the output was delivered. This result only applies to the scenarios that were tested and does not claim that the application is free of all possible defects.

**Prompt Screenshot:**

> [INSERT SCREENSHOT OF THE DEBUGGING PROMPT HERE]

**Output:**

> [INSERT SCREENSHOT OF THE AI REVIEW AND PASSING TEST RESULTS HERE; NO SEPARATE ERROR SCREENSHOT WAS CAPTURED]

---

## Refactoring Prompt

**AI Tool Used:** OpenAI Codex

**Purpose of the Prompt:**

The purpose of this prompt was to improve the readability, organization, maintainability, and consistency of the BananaCare source code without changing its intended behavior.

**What We Used/Changed from the AI Output:**

We centralized repeated status, role, problem-type, and assistance-type values in `constants.py`. We moved repeated form trimming and parsing into `forms.py`, improved names and formatting in the route modules, and updated the templates to use the centralized choices. The original version was retained in `backups/bananacare-pre-refactor/`, and both versions were tested to confirm that functionality was preserved.

**Prompt Screenshot:**

> [INSERT SCREENSHOT OF THE REFACTORING PROMPT HERE]

**Output:**

> [INSERT SCREENSHOT OF THE AI REFACTORING OUTPUT HERE]

### BEFORE

> [INSERT SCREENSHOT OF PRE-REFACTOR CODE HERE]

Suggested source: `backups/bananacare-pre-refactor/bananacare/main.py`

### AFTER REFACTORING

> [INSERT SCREENSHOT OF REFACTORED CODE HERE]

Suggested sources: `bananacare/main.py`, `bananacare/constants.py`, and `bananacare/forms.py`

---

# OUR ANALYSIS AND MODIFICATIONS

## Planning

**Analysis** – We reviewed the AI-generated system plan and compared it with the BananaCare proposal and activity requirements. We identified the necessary Farmer and Admin roles, the three required modules, the data each module needed, and the main workflow from farmer registration to Admin follow-up.

**Modification** – We selected Flask as the web framework and designed the system as a reusable template rather than limiting it to a specific barangay or location. We retained a free-text farm location field so the system can still be adapted to a real area later.

## Code Generation

**Analysis** – We reviewed the generated application structure and checked how the models, routes, templates, login sessions, validation rules, and database connection worked together. We also compared every implemented feature with the requirements in the project proposal.

**Modification** – We adjusted the generated code to provide separate Farmer and Admin login routes, a responsive farm-themed interface, environment-based PostgreSQL configuration, an SQLite fallback, demonstration accounts, and automated tests. Only features within the required mini-system scope were included.

## Debugging

**Analysis** – We examined the failed test import and verified that the application code was not the cause. The dependency installation had not completed before test discovery was attempted. We also reviewed a Python 3.13 warning and identified the outdated timestamp function.

**Modification** – We installed the requirements in a separate command, reran the tests, and confirmed that they passed. We replaced the deprecated UTC timestamp function with a timezone-aware implementation and ran the complete test suite again.

## Refactoring

**Analysis** – We reviewed the existing source and identified repeated form-processing code, duplicated roles and status strings, dense route formatting, and hard-coded choices shared by routes and templates.

**Modification** – We added focused `constants.py` and `forms.py` modules, improved naming and layout in the route and model files, and made templates read their choices from shared constants. We avoided adding unnecessary design layers. The same seven tests passed in both the original and refactored versions.

---

# TEST CASES

**AI Tool Used:** OpenAI Codex

**Purpose of the Prompt:**

The purpose of this prompt was to help us identify appropriate valid, invalid, and edge test cases and document the functionality of the completed BananaCare system.

**What We Used/Changed from the AI Output:**

We used the suggested testing structure as a guide and adjusted the test cases according to the actual features implemented in BananaCare. Actual results were based on our automated tests and manual system checks rather than relying only on the AI response.

**Prompt Screenshot:**

> [INSERT SCREENSHOT OF THE DOCUMENTATION/TESTING PROMPT HERE]

**Output:**

> [INSERT SCREENSHOT OF THE AI TESTING OUTPUT HERE]

---

# TESTING PHASE / TEST CASES

## LOGIN AND REGISTRATION

| Test Case | Test Scenario | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| 1. Valid Input | Farmer logs in using a registered account with correct credentials. | Username: `farmer1`; Password: `farmer123` | The system accepts the credentials and redirects the Farmer to the Farmer dashboard. | The Farmer successfully logged in and was redirected to the Farmer dashboard. | PASS |
| 2. Invalid Input | Admin attempts to log in using an incorrect password. | Username: `admin`; Password: incorrect password | The system rejects the login, displays an invalid-credentials message, and does not create a session. | The system rejected the login and displayed the error message. | PASS |
| 3. Edge Case | A user attempts to register using an existing username. | Existing username with otherwise valid registration information | The system prevents duplicate registration and displays a duplicate-username message. | The duplicate account was not created and the error message was displayed. | PASS |

## FARMER

| Test Case | Test Scenario | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| 1. Valid Input | Farmer updates their farm profile. | Complete farmer details, positive farm size, valid planting date, and production value | The system saves the changes and shows them on the Farmer dashboard. | The profile was updated and the saved details remained after refresh. | PASS |
| 2. Valid Input | Farmer submits a condition report. | Problem: Sigatoka; Affected area: 0.5 ha; Description: Leaf spots observed | The report is saved with `Reported` status and appears in the Farmer and Admin dashboards. | The report was saved and displayed with `Reported` status. | PASS |
| 3. Invalid Input | Farmer submits an affected area larger than the farm. | Farm size: 2 ha; Affected area: 3 ha | The system rejects the report and displays a validation message. No report is created. | The system displayed the affected-area error and did not save the report. | PASS |
| 4. Edge Case | Farmer requests assistance without optional details. | Assistance type: Farm Visit; Details: blank | The request is accepted because the details field is optional and begins with `Pending` status. | The request was saved successfully with `Pending` status. | PASS |

## ADMIN

| Test Case | Test Scenario | Input | Expected Result | Actual Result | Status |
|---|---|---|---|---|---|
| 1. Valid Input | Admin opens the monitoring dashboard. | Valid Admin username and password | The dashboard displays registered farmers, reports, and assistance requests. | The Admin dashboard opened and displayed the test farmer record. | PASS |
| 2. Valid Input | Admin updates a condition report. | Status: Under Monitoring; Staff remarks: Follow-up farm inspection needed | The updated status and remarks are saved and become visible to the Farmer. | The report was updated and the changes appeared on the Farmer dashboard. | PASS |
| 3. Valid Input | Admin completes an assistance request. | Status: Completed; Recommendation entered | The status and recommendation are saved and the current date is recorded as the date provided. | The assistance record was completed with a provided date. | PASS |
| 4. Invalid Access | Farmer attempts to open the Admin dashboard. | Authenticated Farmer requests `/admin/dashboard` | The system denies access and returns HTTP 403. | The system returned HTTP 403 and did not display Admin information. | PASS |

---

# FINAL SYSTEM SCREENSHOTS

## Landing Page

> [INSERT LANDING PAGE SCREENSHOT HERE]

## Login / Registration

> [INSERT FARMER LOGIN SCREENSHOT HERE]

> [INSERT ADMIN LOGIN SCREENSHOT HERE]

> [INSERT FARMER REGISTRATION SCREENSHOT HERE]

## Farmer Side (Pages)

> [INSERT FARMER DASHBOARD SCREENSHOT HERE]

> [INSERT FARM AND FARMER PROFILE SCREENSHOT HERE]

> [INSERT NEW FARM-CONDITION REPORT SCREENSHOT HERE]

> [INSERT ASSISTANCE REQUEST SCREENSHOT HERE]

> [INSERT VALIDATION ERROR SCREENSHOT HERE]

## Admin Side (Pages)

> [INSERT ADMIN MONITORING DASHBOARD SCREENSHOT HERE]

> [INSERT CONDITION-REPORT STATUS UPDATE SCREENSHOT HERE]

> [INSERT ASSISTANCE STATUS/RECOMMENDATION UPDATE SCREENSHOT HERE]

## Automated Testing

> [INSERT SCREENSHOT OF `python -m unittest discover -s tests -v` HERE]

---

# PROFILES

## Farmer Profile

> [INSERT FARMER PROFILE SCREENSHOT HERE]

## Admin Profile / Account

BananaCare uses a separate Admin account and dashboard but does not currently include an editable Admin profile page.

> [INSERT ADMIN LOGIN OR ADMIN ACCOUNT SCREENSHOT HERE]

---

# DATABASE

The default classroom version stores its records in the local SQLite database located at `instance/bananacare.db`. The database can be inspected using DB Browser for SQLite. PostgreSQL can also be used by configuring `DATABASE_URL` in the local `.env` file.

The database contains the following main tables:

- `user` – stores account credentials, roles, and creation dates.
- `farmer_profile` – stores farmer and farm information.
- `disease_report` – stores reported farm conditions, affected area, status, and Admin remarks.
- `assistance` – stores farmer assistance requests, progress, recommendations, and provided dates.

> [INSERT SCREENSHOT OF THE DATABASE TABLE LIST HERE]

> [INSERT SCREENSHOT OF THE `user` TABLE HERE]

> [INSERT SCREENSHOT OF THE `farmer_profile` TABLE HERE]

> [INSERT SCREENSHOT OF THE `disease_report` TABLE HERE]

> [INSERT SCREENSHOT OF THE `assistance` TABLE HERE]
