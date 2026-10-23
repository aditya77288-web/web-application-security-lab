# Web Application Security Assessment & Hardening Lab

A hands-on cybersecurity portfolio project documenting a limited assessment of OWASP Juice Shop in a local lab, alongside a separate Python demonstration of SQL injection prevention with parameterized queries.

> **Scope note:** This is an educational lab report, not a full penetration test. The observed Juice Shop behavior indicates database error disclosure and a potential SQL injection risk; exploitability was not confirmed. The XSS payloads tested did not demonstrate XSS.

## Project Goals

- Set up a local web application security testing environment.
- Inspect and replay HTTP requests with Burp Suite Community Edition.
- Compare normal search behavior with selected unusual inputs.
- Document security observations with supporting evidence.
- Demonstrate parameterized SQL queries in Python and SQLite.
- Recommend remediation and retesting steps.

## Lab Environment

| Component | Use |
|---|---|
| Windows 11 | Host operating system |
| Docker Desktop | Runs the local target application |
| OWASP Juice Shop | Deliberately vulnerable training application |
| Burp Suite Community Edition | HTTP request inspection and Repeater testing |
| Python 3.13 | Runs the secure SQL demonstration |
| SQLite | In-memory database used by the demonstration |

**Local target:** `http://localhost:3000`

Testing described here was limited to the locally hosted training application. Do not test systems without explicit authorization.

## Assessment Summary

### Finding F-01 — Database Error Disclosure / Potential SQL Injection

A crafted product-search input caused an HTTP `500 Internal Server Error`. The response exposed SQLite error text (`incomplete input`) and SQL query details.

**Assessment:** This demonstrates verbose database error disclosure and suggests a potential SQL injection risk. It does **not** independently prove exploitable SQL injection because successful query manipulation or unauthorized data access was not established.

**Recommended remediation:**
- Use prepared statements / parameterized queries for user-controlled values.
- Do not concatenate user input into SQL statements.
- Return generic error messages to clients.
- Store detailed exceptions in server-side logs.
- Repeat the original test after a real fix and record before/after evidence.

### Basic XSS Checks

Two payloads were tried in the product-search interface:

- `<script>alert('XSS')</script>`
- `<img src=x onerror=alert(1)>`

No JavaScript alert appeared; the interface displayed “No results found.”

**Assessment:** XSS was not demonstrated with these tested payloads. This does not prove that the application is free from XSS.

## Python Secure SQL Demonstration

The script `scripts/secure_sql_demo.py` compares an unsafe SQL query built through string concatenation with a parameterized query using a temporary in-memory SQLite database.

For the SQL-like input `' OR '1'='1' --`:

- The unsafe query returned all three demo usernames.
- The parameterized query returned no matches.

This illustrates how parameterized queries treat user input as data rather than allowing it to change query logic.

**Important:** This is a separate, deliberately simplified coding demonstration. It is not a patch to OWASP Juice Shop and does not confirm or remediate the Juice Shop finding.

## Repository Structure

```text
web-application-security-lab/
├── README.md
├── reports/
│   └── OWASP_Juice_Shop_Web_Application_Security_Assessment_Report_UPDATED.docx
├── evidence/
│   ├── 03_Search_Endpoint_Baseline.png
│   ├── Evidence-01-SQL-Error.png
│   └── Evidence-02-SQL-Injection-Prevention-Demo.png
├── notes/
└── scripts/
    └── secure_sql_demo.py
```

The evidence filenames above are examples based on the files recorded during the lab. Confirm that each referenced file exists before publishing the repository. Add other relevant screenshots as needed, and avoid treating duplicate screenshots as separate findings.

## Reproduce the Python Demonstration

From the project directory, run:

```bat
cd scripts
python secure_sql_demo.py
```

The script uses Python's built-in `sqlite3` module and requires no additional packages.

## Evidence and Report

The full report should document:
- Scope and methodology
- Test inputs and observed responses
- The provisional finding and its limitations
- XSS test results
- Python demonstration results
- Remediation recommendations and a retest plan

Keep screenshots in the `evidence/` folder and ensure they do not contain passwords, tokens, personal data, or unrelated private messages before publishing.

## Limitations

- Testing covered a small set of inputs on one search endpoint.
- SQL injection exploitability was not conclusively established.
- The two XSS payloads did not trigger JavaScript; other contexts were not comprehensively tested.
- Authentication, authorization, session handling, file uploads, and broad API coverage are not documented as completed.
- No comprehensive automated scanner results are claimed.
- The Python example is separate from the target application.

## Learning Outcomes

- Intercepting and replaying HTTP requests
- Comparing baseline and unusual input responses
- Recognizing verbose database error disclosure
- Understanding parameterized SQL queries
- Recording evidence and writing cautious security findings
- Recommending remediation and retesting

## Responsible Use

OWASP Juice Shop is intentionally vulnerable and is used here as a local training target. Only assess systems you own or have explicit permission to test.
