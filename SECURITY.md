# Security Policy

## Supported Versions

| Version | Supported          |
| ------- | ------------------ |
| latest  | :white_check_mark: |

## Reporting a Vulnerability

If you discover a security vulnerability, please do **not** open a public issue.
Instead, send a report to the repository maintainers via a private method
(e.g., GitHub Security Advisory or direct email).

Please include:
- A description of the vulnerability
- Steps to reproduce
- Potential impact

You should receive an acknowledgment within 48 hours, and a detailed response
within 5 business days.

## Security Best Practices

### Secrets Management
- Never commit `.env`, `*.key`, `*.pem`, or `secrets/` directories
- All sensitive configuration must use environment variables
- API keys, tokens, and credentials must never be hardcoded

### Dependencies
- Dependency updates are automated via Dependabot (weekly)
- Run `pip-audit` locally before deploying: `pip install pip-audit && pip-audit`
- Pin production dependencies to specific versions

### Code Security
- All user inputs must be validated and sanitized
- Use parameterized queries for any database operations
- Implement rate limiting on exposed APIs
- Enable CORS only for trusted origins

### CI/CD
- Secrets stored in GitHub Secrets, never in code or config files
- CI tokens use least-privilege permissions
- Secret scanning runs on every push and pull request
- SAST (Bandit) scans run automatically

### Infrastructure
- Enable HTTPS/TLS for all network communication
- Set security headers (CSP, HSTS, X-Frame-Options)
- Apply regular security patches
- Use proper error handling to avoid information leakage

## OWASP Top 10 Coverage

1. **Broken Access Control** - Verify authorization on all endpoints
2. **Cryptographic Failures** - Use strong encryption for data at rest and in transit
3. **Injection** - Validate and sanitize all inputs
4. **Insecure Design** - Follow least-privilege principle
5. **Security Misconfiguration** - Regular security reviews and automated scanning
6. **Vulnerable Components** - Automated dependency updates via Dependabot
7. **Auth Failures** - Implement strong authentication mechanisms
8. **Integrity Failures** - Code signing and verification
9. **Logging Failures** - Enable audit logging for security events
10. **SSRF** - Validate and restrict outbound network requests
