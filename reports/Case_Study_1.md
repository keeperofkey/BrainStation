## Section 1 - Incident Overview

  -  Date and Time of Detection
      - Friday, October 10th within working hours after fake IT emails have been sent.
  -  Date and Time of Resolution
      - December 17th
  -  Duration of Incident
      - 9 weeks and 5 days
  -  Incident Severity
      - Medium from [National Cyber Incident Scoring System](https://www.cisa.gov/sites/default/files/2023-01/cisa_national_cyber_incident_scoring_system_s508c.pdf)
  -  Incident Classification
      - Phishing Attack, Ransomware, Privilege escalation

## Section 2 - Executive Summary

  -  Briefly describe what happened during the incident, highlighting key events.
      <p>
        The incident began the threat actor gathering open source intelligence on MOVR Employee's to determine a good target and proceeded with a purchase of credentials on the darkweb from a previous data leak. The threat actor then crafted a Phishing email to trick the target into accepting a MFA request and thereby compromise the account. Once the actor had access they were able to elevate their privileges through an unencrypted CSV from a shared password manager export. Once the actor had the master login credentials they were able to delete the database and exfiltrate sensitive data. Additionally the cyber criminals were able to launch a large Phishing attack using the targets email account to spread ransomware.
      </p>
  -  Explain the impact of the incident on the organization, including financial, reputation, and operational impacts.
      <p>
        The organization's decision to pay the ransom, while deemed the most cost-effective, still had a significant financial impact. Additionally due to the operational disruption many clients were dissatisfied and frustrated which can impact the organizations reputation. A lack of transparency in the disclosure process can also lead to mistrust between the organization and its clients. They also experienced some partial loss of records for the day of the breach.
      </p>
  -  Provide a high-level overview of the actions taken to mitigate and resolve the incident.
      <p>
        Immediately after detection IT was able to identify the source of the breach however restoring the database proved difficult and the hackers maintained access for 2 months. The investigation process took time and while issues were addressed promptly the nature of the attack and technical complexities inherent in large organizations delayed remediation.
      </p>

## Section 3 - Incident Timeline

### Detection Phase

  -  List key events and actions during the detection phase, starting from the initial alert or notification. Across this and future sections of this report, be sure to provide your own commentary around what went wrong and how you believe it contributed to the incident, using concepts discussed throughout the week.
      - Phishing email from IT
          - the organization could implement email filtering to try to detect Phishing.
          - utilize more secure channels of communication for IT services.
      - MFA login attempt
          - the MFA notification didn't provide any information on the IP location of the login attempt which could have allowed Donovan to question the notification.
      - Master login notification
          - the login credentials should never be stored in unencrypted formats and the organization should not allow sharing of the password manager.
          - access credentials should expire to enforce Least Privilege and minimize who has access. Credentials can be easily reissued for users who require them.
  -  If there was no initial alert, what indicators or anomalies could the security team have picked up on at an early stage? Please explain the reasons why indicators might have been missed by the security team.
      <p>Without the initial alert it would have been difficult for the security team to detect the intrusion because the rate at which the data was exfiltrated was hidden by the hourly backups so the network didn't seem anomalous</p>
### Containment Phase

  -  If applicable, list key events and actions taken to contain the incident and prevent further damage.
      - Reset Donovan's account
      - Terminated active sessions however it does not specify if any actions were taken to contain the ransomware from spreading on Teams
      - Removed his master access
      - These actions however didn't contain the ransomware

### Eradication Phase

  -  If applicable, list key events and actions taken to remove the threat from the affected systems.
      - While they team did revoke Donovan's credentials and end the master account sessions the attackers were still able to maintain access for two months so we can assume that they were able to maintain a backdoor and the organizations attempts to eradicate the threat were insufficient.

### Recovery Phase

  -  If applicable, list key events and actions taken to restore normal operations and services.
      - restore backups to minimize outage
      - Paid the ransom of $150,000 to access the compromised devices and stated logistical challenges in retrieving the computers due to work from home policies. However this decision is questionable because it doesn't guaranty the compromised device and data will be usable again. In Veeam's ransomware trends report from 2023 they estimate a 25% chance that organizations that pay the ransom never retrieve their data ([Veeam](https://www.veeam.com/ransomware-trends-report-2023)). Additionally, if the devices are usable again they should still be inspected before being used for sensitive information which poses the same logistical difficulties. While it is easy to say to never pay the ransom it becomes much more difficult when your data and livelihood are at stake.

## Section 4 - Root Cause Analysis

  - Initial Attack Vector:
      - Phishing email impersonating IT to trick users into giving up credentials.
  - Weaknesses and Vulnerabilities:
      - Infrequent security awareness training.
          - Initial training should be required before new employees get access.
          - Regular training every 6 months would help reinforce best practices.
      - Lack of remote work policies.
          - Should require VPN usage to limit exposure of devices.
  - Human Factors:
      - Stigma - There may have been stigma associated with reporting the incident or seeking help, which could have prevented early detection and intervention.
      - Compliance - Failure to comply with policies, procedures, or regulations may have contributed to the conditions that allowed the incident to occur.
      - Convenience - Choosing the convenient option rather than the proper safety protocols could have played a role.
  - Recommendations:
    - Provide initial security training upon hiring and routine training every 3-6 months.
    - Implement MFA for all accounts to prevent unauthorized access via stolen credentials.
    - Establish a remote access policy requiring VPN usage and limit network access to only the VPN for remote users.
    - Perform periodic incident response simulations to test and improve readiness.
    - Segment the network and implement least privilege principles to limit attack surface.

## Section 5 - Lessons Learned

  -  Key Takeaways:
      - Annual security training is inadequate
      - MFA should be required for all accounts and the notification should provide important details of login attempt.
      - Never store passwords unencrypted for any reasons.
      - Revoke access when privilege is not longer required.
  -  Improvements:
      - Remote workers need to be using a VPN to encrypt their traffic
      - Monitoring and response tools should be regularly tested to identify Weaknesses and blind spots.
  -  Training and Awareness:
      - Providing adequate and frequent security training is key to reducing human vulnerabilities.
      - Some onboarding training should be required
  -  Policy and Procedure Updates:
      - Forbid password sharing even in development environments.
      - Use secure channels of communication for IT to avoid impersonation.
      - Require the use of VPN when working remote.
      - Update passwords regularly including ones used internally.

## Section 6 - Response & Recovery Assessment

  -  Effectiveness of Response:
      - While the initial response successfully restored service they were unable to fully eradicate the threat which prolonged the event.
  -  Timeliness:
      - The timeliness of the detection and containment was impressive especially considering it occurred on a Friday making it more difficult to contain on a weekend.
  -  Communication:
      - While MOVR did inform their customers and shareholders of the outage in service they failed to mention it was the result of a cyber attack and didn't aknoledge to loss of data until much later. They also did not communicate the ransomware as they believed it to be an internal matter.
  -  Resource Allocation:
      - They were able to allocate resources to address the service interuptions and were able to hire security consultants to provide analysis but they did not focus on eradication allowing the bad actors to maintain access. They also did contract a darkweb monitoring firm in case the data surfaced.

## Section 7 - Next Steps
-  Short-term:
      - Reset all account credentials and enforce mandatory password changes - IT team
      - Conduct forensic investigation to identify and remove any backdoors or malware - Security team
      - Isolate and rebuild compromised systems from clean backups - IT team
      - Implement stronger email security controls like filtering and employee training - Security team
      - Limit use of shared accounts and enforce principle of least privilege - IT team 
      - Improve logging and monitoring to more quickly detect anomalies - Security team
      - Develop remote response plan for compromised endpoints - IT and Security teams
      - Review incident and identify process improvements - Security team
      - Keep leadership and stakeholders updated on response progress - Security team 
-  Long-term:
      - Implement a cybersecurity awareness training program for all employees - Security team
      - Strengthen identity and access management controls, like MFA and role-based access - IT team
      - Expand logging and threat detection capabilities - Security team
      - Perform regular incident response simulations - Security team
      - Establish relationships with cyber threat intelligence partners - Security team
      - Implement new data protection mechanisms like data loss prevention - IT team

## Data Classification
| Data | Category | [Classification](https://www.cmu.edu/data/guidelines/data-classification.html) |
|-|-|-|  
| Location, Location History, IP Addresses | Customer | Private |
| Social Security Number | Employee | Restricted |
| Salary, Pay Stubs, Banking Information | Employee | Restricted |
| Name, Phone Number, Service History | Customer | Private |
| Name, Address, Phone Number, DOB | Employee | Private |
| Benifits | Employee | Public |
| Payment Information | Customer | Restricted |
| Driver's Licenses, License Plates | Customer | Private |
| Transaction Amounts, Service History, Delivery Data, Device Data, Other | Customer | Public |

## Section 8 - Reflection

-  Having performed a recap of the case events and identified key issues, what do you believe the main source of weakness was? Is it a single point or multiple points? Were they people-based, process-based, or technology-based?
      <p>
        I think the main source of weakness was people-based which is often the case and I think there were multiple points of failure. Firstly, there is a stigma around reaching out to IT because of a fear of causing more problems and sometime embarrassment about a lack of technical literacy. Convenience also played a large part in the extent of the access the threat actors were able achieve, if the development team was not in the habit of sharing a password manager with an unencrypted export in CSV it would have been much more difficult for the attackers to gain master access. The CSV invalidated the use of a password manager.
      </p>

-  Provide your analysis and commentary on the ethics presented throughout the case. Were there any shortcomings, ethical issues, or areas of ambiguity?
      <p>
        I think that the ethics around disclosure are difficult and can be ambiguous but failure to disclose key elements of the event to both their shareholders and customers is problematic. It creates mistrust especially when the information changes later on the extent of the breach is much more damaging to the companies reputation. Even though there was not concrete evidence of customer data being leaked it is often better to assume the worst and inform those affected so they can reduce their exposure by resetting acounts especially as many people reuse password rather then follow best practices.
      </p>

-  Given the unknown extent of the breach, do you think that MOVR’s disclosure approach was justified? What could or should have been done differently, if anything?
      <p>
        I do not believe their approach was justified as it put their customers at risk because of their lack of knowledge of the breach. They should have disclosed the possiblity of data leakage within the first disclosure at which point they knew the actor had access for months as this greatly increases the chance customer data was access.
      </p>

-  Would you have paid the ransom? Why or why not?
      <p>
        While the initial ransom $150,000 doesn't seem like a unreasonable sum to ensure availability of your service it can be quite risky. As mentioned before there is a chance that paying the ransom will not restore the machines and data effected and it signals to other ransomware groups that your organization is willing to pay making it a viable target. However it is easy for a bystander to have this opinion and there are many factors including the emotional response to such an event that can make it difficult in the moment.
      </p>

-  In Unit 1, we discussed the concept of risk in Cybersecurity. Given what you know about the scenario, what Cybersecurity risks exist for MOVR and other large technology companies?
      <p>
      There are many cybersecurity risks in our increasing digital world including malware, phishing attacks, denial of service, insider threats, and advanced persistent threats. Depending on an organizations field and data the risk  can drastically increase for more sophisticated attacks. MOVR is unlikely to become the target of a APT because their data while valuable is not that valuable however they are at risk from many other attacks especially phishing as it make up a large amount of incidents and requires relatively low technical skill.
      </p>

-  What do you think MOVR’s attitude towards Cybersecurity risk should be? Why should they hold this attitude towards risk?
      <p>
        I think MOVR should try to minimize risk where possible within reason focusing on the "low hanging fruit" attacks like phishing and malware. They should probably not invest in extreme security measures as their data doesn't have implication to national security. By adopting an attitude of being slightly more secure then their competitors will help limit their risk.
      </p>

<style>
  p {
      text-indent: 30px;
      font-weight: normal;
  }
  ul {
      list-style-type: none;
      font-weight: Bold;
  }
  ul ul {
      list-style-type: circle;
      font-weight: normal;
      }
</style>
