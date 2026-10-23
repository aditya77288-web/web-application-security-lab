Web Application Security Assessment & Hardening Lab

A hands-on cybersecurity portfolio project focused on web application testing, security evidence collection, database error analysis, and secure SQL coding practices.

Project Overview

This project documents a limited security assessment of OWASP Juice Shop running locally in a controlled lab environment. Burp Suite Community Edition was used to inspect and replay HTTP requests, and Python with SQLite was used to demonstrate SQL injection prevention through parameterized queries.

Important: This was a limited educational assessment, not a full penetration test. SQL injection exploitability was not conclusively confirmed in Juice Shop.

Objectives

- Set up a local web application security testing environment.
- Inspect HTTP requests and responses using Burp Suite.
- Compare normal and unusual product-search inputs.
- Document database error disclosure and potential SQL injection risk.
- Demonstrate parameterized SQL queries using Python and SQLite.
- Record evidence and recommend security improvements.

Tools and Technologies

Tool| Purpose
OWASP Juice Shop| Deliberately vulnerable training application
Burp Suite Community Edition| HTTP request inspection and replay
Docker Desktop| Local application environment
Python| Secure SQL coding demonstration
SQLite| Database for the isolated demonstration
Windows 11| Host operating system

Key Findings

1. Database Error Disclosure

A crafted SQL-like search input produced an HTTP 500 response containing SQLite error details and query information.

- Status: Open; further validation required.
- Provisional severity: Medium.
- Risk: Database implementation details were exposed.
- Limitation: The recorded evidence did not conclusively establish exploitable SQL injection.

Recommended remediation:

- Use parameterized SQL queries.
- Return generic error messages to clients.
- Keep detailed exceptions in server-side logs.
- Add regression tests for malformed inputs.

2. Cross-Site Scripting Checks

Two basic XSS payloads were tested through the product-search interface. No JavaScript alert was observed.

Result: XSS was not demonstrated by these tests. This does not establish that the application is free from XSS vulnerabilities.

3. Secure SQL Demonstration

A separate Python/SQLite script compared unsafe SQL string concatenation with parameterized queries.

The unsafe demonstration allowed SQL-like input to change query logic and return multiple demo records. The parameterized version treated the input as data and returned no matches.

Security lesson: User input should be passed as query parameters rather than concatenated into SQL statements.

This demonstration is separate from Juice Shop and is not a patch to that application.

Repository Structure

web-application-security-lab/
├── README.md
├── evidence/
│   ├── README.md
│   └── [security testing screenshots]
├── reports/
│   ├── README.md
│   └── OWASP_Juice_Shop_Web_Application_Security_Assessment_Report_UPDATED.docx
└── scripts/
    ├── README.md
    └── secure_sql_demo.py

The structure above describes the intended organization. Evidence filenames may vary slightly from the examples in the report.

Evidence and Documentation

- "evidence/" — Screenshots of baseline requests, input tests, database errors, and the Python demonstration.
- "reports/" — Detailed assessment report, observations, limitations, and remediation recommendations.
- "scripts/" — Python script demonstrating parameterized SQL queries.

How to Run the Python Demonstration

Ensure Python 3 is installed, then run:

python secure_sql_demo.py

Run this command from the "scripts" directory.

The script uses an in-memory SQLite database and is intended for educational purposes.
- SQL injection exploitability in Juice Shop was not conclusively established.
- The tested XSS payloads did not demonstrate XSS.
- Comprehensive authentication, authorization, session, and file-upload testing was not completed.
- Juice Shop itself was not patched or retested after remediation.
- The Python demonstration is a separate secure-coding example.

Learning Outcomes

- HTTP request and response analysis.
- Manual web application security testing.
- Evidence collection and technical reporting.
- Recognition of database error disclosure.
- Secure SQL coding with parameterized queries.
- Communicating findings and limitations accurately.

Authorization and Responsible Testing

All testing was conducted against a local training application. Test only systems you own or have explicit authorization to assess.

Project Status

Completed so far: Local lab setup, selected manual tests, evidence collection, assessment report, and Python SQL injection prevention demonstration.

Potential future improvements: Expand the test coverage, add automated regression tests, and document a genuine before-and-after remediation test.

Limitations

- Testing focused on a limited set of inputs for one search endpoint.
