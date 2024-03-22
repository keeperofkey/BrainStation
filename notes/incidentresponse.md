1. How and when did Okta communicate the security incident to its customers and the broader public?

- published indicators of compromise (IOCs), and provided a customized impact report to affected customers.

2. What steps did Okta take to ensure that external parties, potentially affected by the incident, were appropriately notified?

- independent investigation of the October 2023 security incident.
- security incident forensic report is now available to our customers and partners
- notified regulators
- shared recommendations to mitigate phishing and social engineering attacks

3. What was compromised in this attack? Ie. which specific files did the threat actor access during the security incident, and how were they used for potential attacks?

- HAR files that contained session tokens which could in turn be used for session hijacking attacks.

4. How did the threat actor gain unauthorized access to Okta's customer support system, and what was the role of the compromised service account?

- leveraged a service account stored in the system itself.
- The username and password of the service account had been saved into the employee’s personal Google account.

5. What was the reason for the delayed identification of suspicious downloads in Okta's logs during the incident?

- Okta’s initial investigations focused on access to support cases
- They did not check logs generated when user accesses files directly

6. When did Okta first become aware of the security incident, and what actions were taken during the investigation?

- 2023-09-29 to 2023-10-02 Okta Security meets with 1Password on 9/29, 9/30, 10/1 and 10/2 in an attempt to resolve their support case.

1. What remediation steps were taken by Okta in response to the security incident?
1. What proactive measures did Okta deploy to prevent session token theft against Okta administrators?
