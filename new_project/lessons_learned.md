# Lessons Learned from Bajaj API Project

This document captures the key concepts and techniques learned from the previous Bajaj Webhook API project so they can be easily referenced and applied to future projects.

## 1. Automated API Workflows
- **Multi-step Authentication & Submission**: The workflow involved making an initial `POST` request with user details to receive a dynamic `webhookUrl` and an `accessToken`.
- **Dynamic Endpoints**: Instead of a hardcoded submission URL, the second step required dynamically parsing the `webhookUrl` from the first response and sending the final payload (SQL query) to it.
- **Authorization Headers**: The `accessToken` received from step 1 must be passed as an `Authorization` header in step 2.

## 2. Transitioning from Scripts to Web Apps
- Scripts (like Python's `requests`) run natively on the operating system and do not face Cross-Origin Resource Sharing (CORS) restrictions.
- When migrating script logic to a browser-based web application (HTML/JS), you will often encounter CORS errors (`Failed to fetch`) if the target API doesn't allow cross-origin requests.

## 3. Resolving CORS with Proxies
- **Netlify Redirects**: A clean way to solve CORS on static frontends hosted on Netlify is to use a `_redirects` file.
- **Implementation**:
  ```text
  /api/*  https://target-api-domain.com/:splat  200
  ```
  This tells the Netlify Edge servers to act as a proxy. The browser sends the request to the same origin (`/api/...`), and Netlify forwards it to the external API, effectively bypassing CORS.
- **Client-Side URL Rewriting**: If an API returns absolute URLs (e.g., a webhook URL) that also need to be called from the browser, the client-side JavaScript must intercept and rewrite that URL to pass through the `/api/` proxy path before calling `fetch()`.

## 4. Environment & Deployment
- Deploying pure frontend implementations of backend workflows allows for easier distribution.
- Providing users with multiple ways to interact with APIs (e.g., Postman Collections + a Web UI) greatly improves the developer/user experience.
