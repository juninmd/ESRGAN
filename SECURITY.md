# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

This project uses automated security scanning to detect vulnerabilities. If you discover a security issue, please do **not** open a public issue.

Instead, report it privately by:

1. Opening a [GitHub Security Advisory](https://github.com/juninmd/ESRGAN/security/advisories/new)
2. Contacting the maintainer directly

You should receive a response within 48 hours. If the issue is confirmed, a fix will be released as soon as possible depending on complexity.

## Security Scanning

The following automated scans run on every push and PR:

- **Gitleaks**: Scans for hardcoded secrets and credentials
- **Bandit**: Static Application Security Testing (SAST) for Python
- **Safety**: Scans Python dependencies for known vulnerabilities
- **Dependency Review**: Reviews new dependency changes for license and vulnerability issues

## Best Practices

- Never commit `.env` files or secrets to the repository
- Use environment variables for all sensitive configuration
- Pin dependency versions in production
- Validate all user inputs (command-line arguments, file paths, etc.)
- Run security scans locally before pushing: `pip install bandit safety && bandit -r . && safety check`
