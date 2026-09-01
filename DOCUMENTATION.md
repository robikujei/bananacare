# BananaCare Project Documentation

## 1. System Title

**BananaCare: A Banana Farm Monitoring and Farmer Assistance Information System**

## 2. Problem Statement

Banana farmers and agriculture personnel may have difficulty maintaining organized farm records, documenting disease or pest incidents, and following assistance requests. BananaCare centralizes those records in a simple web application.

## 3. Objectives

**General objective:** Develop a simple information system that improves the recording, monitoring, and management of banana-farming information.

**Specific objectives:**

1. Store and update farmer, farm, variety, size, and production details.
2. Record and monitor diseases, pests, affected areas, and report status.
3. Track assistance requests, support status, recommendations, and completion dates.

## 4. Features and Requirements

- Separate Farmer and Admin authentication routes
- Farmer registration and editable farm profile
- Condition reporting with Reported, Under Monitoring, and Resolved states
- Assistance requests with Pending, In Progress, and Completed states
- Admin monitoring dashboard and follow-up remarks
- Required-field, numeric-range, duplicate-username, and role validation
- Responsive browser interface

## 5. Technology and AI Tools Used

- Python 3.13 and Flask
- PostgreSQL with SQLAlchemy and Psycopg
- HTML5, CSS3, and Jinja templates
- Werkzeug password hashing and Flask-Login sessions
- OpenAI Codex for planning, code assistance, debugging, refactoring, and test/documentation assistance

## 6. AI Prompt and Output Evidence

Insert screenshots of the actual conversation beneath each entry. Do not invent screenshots or claim edits you did not make.

| Stage | Purpose | Prompt/evidence to capture | What was reviewed or changed |
|---|---|---|---|
| Planning | Select an appropriate architecture | Initial project request and stack discussion | Chose Flask/PostgreSQL and separate roles; removed fixed geographic scope |
| Code generation | Build the three required modules | Request and generated application files | Review models, routes, templates, and explain their relationships |
| Debugging/testing review | Check for issues in the required workflows | Add the real review prompt and passing test output here | State that no bugs were observed in the executed tests |
| Refactoring | Improve a real section of code | Add a later refactoring prompt and before/after code | Explain why the changed version is clearer or safer |
| Documentation/testing | Verify and document the system | Capture the test/documentation request and output | Confirm test cases and correct any inaccurate text |

Use this sequence in your explanation: **Prompt → AI Output → Your Analysis → Modification → Testing → Final Result**.

## 7. Testing Results

| Test | Input | Expected result | Actual result | Status |
|---|---|---|---|---|
| Valid login | Existing farmer credentials | Farmer dashboard opens | Farmer dashboard opens | PASS |
| Invalid login | Incorrect admin password | Error message; no login | Error message displayed | PASS |
| Valid report | 0.5 ha on a 2 ha farm | Report saved | Report saved and listed | PASS |
| Edge case | 3 ha affected on a 2 ha farm | Reject report | Validation error displayed | PASS |
| Access control | Farmer opens admin dashboard | HTTP 403 response | HTTP 403 response | PASS |
| Admin overview | Existing admin credentials | Monitoring dashboard opens | Dashboard and farmer record displayed | PASS |
| Assistance request | Farm Visit with notes | Request saved as Pending | Request saved and listed | PASS |

Run `python -m unittest discover -s tests -v` and replace the table's actual-result wording if your local result differs.

## 8. Debugging and Testing Review

During AI-assisted development, the AI tool encountered an error while checking the application and corrected it immediately before presenting the completed output. Because the error was handled within the AI tool's working process, no separate user-facing screenshot of the error was captured. The final version was then tested, and no bugs were found in the executed tests. The tested login, reporting, access-control, administrative, and assistance-request workflows produced their expected results, so no additional fix was required after delivery. This observation is limited to the tested scenarios and does not claim that the application is free of every possible defect. Include the actual review prompt and passing test output as evidence for the submission.

## 9. Refactoring Example

The refactor preserved all routes and workflows while moving repeated form parsing into `forms.py` and duplicated role/status/type strings into `constants.py`. Route bodies now use descriptive local names and readable query formatting. The two login pages continue to share `_login(expected_role)` while retaining separate `/farmer/login` and `/admin/login` routes. The original source is preserved in `backups/bananacare-pre-refactor/` for the required before/after evidence. See `ARCHITECTURE.md` for the current module and data-flow documentation.

## 10. Final System Screenshots

Add screenshots of:

1. Landing page
2. Farmer registration or farm profile
3. Farmer condition report and assistance history
4. Admin monitoring dashboard
5. A validation error
6. Passing automated tests

## 11. Responsible and Secure AI Use

No PostgreSQL passwords or private data should appear in prompts or screenshots. Credentials are stored in the ignored `.env` file, passwords are hashed, and the project team remains responsible for reading, testing, and explaining the final code.
