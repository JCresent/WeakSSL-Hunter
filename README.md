# WeakSSL-Hunter
> Tool to analyze and find SSL related vulnerabilites in android apps (APKs)   
## Looks for within the app (misuse cases):
- Allows all hostnames
- If using HTTPS or HTTP (unsecured) (Mixed-mode/No SSL use)
- Overides SslErrorHandler method used with the android.webkit (Incorrectly/Without checking certificate)
- Overriden TrustManager methods: specifically looked for overriden checkServerTrusted method  
---
Future improvements:
- More thorough testing (androguard, etc.)
- Implementing static parsing into one method (too much repeated code)
