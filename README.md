# WeakSSL-Hunter
> Tool to analyze and find SSL related vulnerabilites in android apps (APKs)   
## Looks for within the app (misuse cases):
- Allows all hostnames
- If using HTTPS or HTTP (unsecured) (Mixed-mode/No SSL use)
- Overides SslErrorHandler method used with the android.webkit (Incorrectly/Without checking certificate)
- Overriden TrustManagers which allows trust to all certificates
