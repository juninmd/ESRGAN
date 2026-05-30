# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

We take the security of ESRGAN seriously. If you believe you have found a security vulnerability, please report it to us as described below.

**Please do not report security vulnerabilities through public GitHub issues.**

Instead, please report them via email to the repository maintainer.

You should receive a response within 48 hours. If for some reason you do not, please follow up via email to ensure we received your original message.

Please include the following information in your report:

- Type of issue (e.g., buffer overflow, SQL injection, cross-site scripting, etc.)
- Full paths of source file(s) related to the manifestation of the issue
- The location of the affected source code (tag/branch/commit or direct URL)
- Any special configuration required to reproduce the issue
- Step-by-step instructions to reproduce the issue
- Proof-of-concept or exploit code (if possible)
- Impact of the issue, including how an attacker might exploit it

## Preferred Languages

We prefer all communications to be in English.

## Policy

- We will acknowledge receipt of your vulnerability report within 48 hours.
- We will send a more detailed response within 72 hours indicating the next steps.
- We will keep you informed of the progress towards a fix.
- After the initial reply, we will endeavor to keep you informed of the progress.
- We will publicly credit you as the reporter (unless you prefer to remain anonymous).

## Security Best Practices

When contributing to or deploying ESRGAN, please follow these security best practices:

1. **Secrets Management**: Never commit secrets, API keys, or credentials to the repository. Use environment variables for all sensitive configuration.
2. **Dependency Updates**: Keep dependencies up to date. Dependabot is configured to automatically create PRs for dependency updates.
3. **Input Validation**: Validate all inputs, especially file paths and user-supplied data.
4. **Least Privilege**: Run processes with the minimum privileges necessary.
5. **Secure Configuration**: Review configuration files for any embedded secrets before committing.
