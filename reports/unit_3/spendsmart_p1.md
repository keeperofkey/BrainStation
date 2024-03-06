# Case Brief

### Company Profile:

Spendology Solutions is a fictional digital age start-up fintech company dedicated to revolutionizing the personal financial management experience. Established in 2017, the company is driven by a passion for delivering innovative financial solutions that empower users to take control of their personal finances. With a commitment to security, usability, and efficiency, Spendology Solutions aims to set new standards in the ever-evolving landscape of digital financial management.

Our mission at Spendology Solutions is to simplify and enhance the financial lives of individuals through the creation of intuitive, secure, and feature-rich digital banking applications. We strive to provide our users with tools that enable efficient budgeting, seamless data integration, and a trustworthy platform for managing their financial activities.

### SpendSmart digital budgeting app

The SpendSmart digital budgeting app is designed to empower customers with efficient monthly budgeting capabilities, consolidating data from multiple credit card statements and utilities companies. This feature aims to provide a seamless and secure experience for users to manage their financial activities, all within the app.

## Technical Implementation:

#### Data Integration:

- Fetch and integrate data from various external sources, including credit card and utilities companies, leveraging token-based authentication.
- Utilize encryption protocols during data transmission to ensure the confidentiality and integrity of the transferred data.
  Data Parsing and Normalization:
- Develop algorithms to parse and normalize data from diverse sources, ensuring consistency in formatting and structure.
- Implement error handling mechanisms to address discrepancies and anomalies in the incoming data.
- User Authentication and Authorization:
- Integrate multi factor authentication mechanisms to protect user portals, ensuring that only authorized users can access their financial data.
- Implement role-based access controls for admins/staff engineers to restrict access to specific features and functionalities based on user roles.

#### Secure Storage:

- Employ industry-standard encryption algorithms for storing sensitive financial data in databases.

  - Encrypt sensitive fields in the database before storage using AES-256 encryption.
  - Employ proper key management practices to safeguard encryption keys.

- Regularly audit and update encryption mechanisms to comply with evolving security standards.

#### Transaction Logging:

- Establish a secure logging mechanism to record user interactions and financial transactions for audit purposes.

  - Log relevant events, including user logins, financial transactions, and system activities, using a secure and standardized logging framework.
  - Include timestamp information, user identifiers, and transaction details in each log entry.

- Ensure logs are protected against unauthorized access and regularly reviewed for potential security incidents.

  - Store logs in a secure location with restricted access, ensuring that only authorized personnel can view or modify the log files.
  - Implement access controls and encryption to protect logs from unauthorized tampering or disclosure.

#### User Education and Communication:

- Implement user-friendly interfaces and informative tooltips to guide users on secure financial practices.

- Communicate security features to users, fostering a sense of trust in the application.

## Database Schema:

```
`budget_categories` (
  `budget_category_id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned DEFAULT NULL,
  `category_name` varchar(255) DEFAULT NULL,
  `budget_limit` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`budget_category_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `budget_categories_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) 

`credit_card_statements` (
  `credit_card_statement_id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned DEFAULT NULL,
  `credit_card_number` varchar(16) DEFAULT NULL,
  `institution` varchar(255) DEFAULT NULL,
  `transaction_date` date DEFAULT NULL,
  `merchant` varchar(255) DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  PRIMARY KEY (`credit_card_statement_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `credit_card_statements_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
)

`user` (
  `user_id` int unsigned NOT NULL AUTO_INCREMENT,
  `username` varchar(255) DEFAULT NULL,
  `password_hash` varchar(255) DEFAULT NULL,
  `email` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
)

`user_expenses` (
  `user_expense_id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned DEFAULT NULL,
  `category_id` int unsigned DEFAULT NULL,
  `expense_date` date DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `description` text,
  PRIMARY KEY (`user_expense_id`),
  KEY `user_id` (`user_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `user_expenses_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `user_expenses_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `budget_categories` (`budget_category_id`)
)

`utility_bills` (
  `utility_bill_id` int unsigned NOT NULL AUTO_INCREMENT,
  `user_id` int unsigned DEFAULT NULL,
  `utility_company` varchar(255) DEFAULT NULL,
  `bill_date` date DEFAULT NULL,
  `amount` decimal(10,2) DEFAULT NULL,
  `category` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`utility_bill_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `utility_bills_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
)
```

## SDLC Proccess:

### Phase 1: Planning

- Objective: Define the project scope, requirements, and feasibility.
  - Activities:
    - Define Project Scope:
      - Collaborate with stakeholders to clearly outline the project boundaries.
      - Use Jira and Confluence for capturing and organizing project requirements.
    - Feasibility Study:
      - Conduct a detailed analysis of technical, operational, and economic feasibility.
      - Microsoft Project helps in creating a realistic project timeline and resource allocation.
  - Tools:
    - Jira: For project management and issue tracking.
    - Confluence: To collaborate on requirements and documentation.
    - Microsoft Project: For creating project timelines and Gantt charts.

### Phase 2: Analysis

- Objective: Gather and analyze requirements in detail.
  - Activities:
    - Requirements Gathering:
      - Interview stakeholders, conduct surveys, and utilize Google Forms for user feedback.
      - Document requirements with the help of Confluence and Jira.
    - User Feedback:
      - Design and distribute surveys using Google Forms or SurveyMonkey.
      - Incorporate user feedback into the requirement specifications.
  - Tools:
    - Figjam: For creating visual diagrams such as flowcharts and data models.
    - Figma: For creating interactive prototypes.
    - Google Forms: To gather user feedback and requirements.
    - Jira: Project management.
    - Confluence: Project documentation & knowledge base.

### Phase 3: Design

- Objective: Create detailed system design based on analyzed requirements.
  - Activities:
    - User Interface (UI) Design:
      - Create wireframes and interactive prototypes using Figma.
      - Share and iterate on designs with stakeholders.
    - System Architecture Design:
      - Utilize Enterprise Architect to create detailed system architecture and UML diagrams.
      - Share architecture documentation on Confluence for team collaboration.
  - Tools:
    - Figma: For designing the user interface and user experience.
    - Enterprise Architect: For creating detailed system architecture and UML diagrams.
    - Draw.io: For additional diagramming needs.

### Phase 4: Implementation (Coding)

- Activities:
  - Coding Standards:
    - Establish coding standards and guidelines for the team.
    - Use IDEs (Integrated Development Environments) like Visual Studio to enforce coding standards.
  - Version Control:
    - Implement branching strategies using Git for efficient collaboration.
    - Conduct regular code reviews through pull requests.
  - Build Automation:
    - Set up Jenkins or Travis CI for continuous integration to catch integration issues early.
- Objective: Translate design specifications into working code.
  - Tools:
    - IDEs (Integrated Development Environments):
      - Visual Studio
    - Version Control:
      - Gitlab: For source code version control.
    - Build Automation:
      - Gitlab CI: For continuous integration and automated builds.

### Phase 5: Testing

- Objective: Verify that the software meets the specified requirements.
  - Activities:
    - Unit Testing:
      - Develop and run unit tests using JUnit or TestNG.
      - Integrate automated tests into the build process.
    - Integration and System Testing:
      - Use Selenium for automated web application testing.
      - Postman for API testing and integration tests.
    - Test Case Management:
      - Organize and manage test cases in Jira (Zephyr).
      - Execute test cases and report issues.
  - Tools:
    - JUnit or TestNG: For unit testing (Java).
    - Selenium: For automated web application testing.
    - Postman: For API testing.
    - Zephyr: For test case management.

### Phase 6: Deployment

- Objective: Release the software to production.
  - Activities:
    - Containerization:
      - Containerize the application using Docker.
      - Define deployment configurations for different environments.
    - Continuous Deployment:
      - Implement GitLab CI/CD pipelines for automated deployment.
      - Utilize Kubernetes for container orchestration.
  - Tools:
    - Docker: For containerization.
    - Kubernetes: For container orchestration.
    - GitLab CI/CD pipelines: For continuous deployment.

### Phase 7: Maintenance and Support

- Objective: Provide ongoing support, address issues, and release updates.
  - Activities:
    - Monitoring and Performance:
      - Set up monitoring tools like or Datadog.
      - Regularly analyze performance metrics and address bottlenecks.
    - Issue Resolution:
      - Use Jira Service Management to manage and prioritize support tickets.
      - Regularly release updates with bug fixes and new features.
  - Tools:
    - Jira Service Management (formerly Jira Service Desk): For managing support tickets.
    - or Datadog: For monitoring and performance management.
    - Snyk: For continuous code quality inspection.
    -

## Planning phase:

- Security requirements are explicitly defined through the technical implementation details provided. Areas like data encryption, access controls, logging, and secure storage indicate a focus on security as a key project goal.

- The technical implementation section does not mention a formal risk assessment process. However, the security measures described, like encryption and access controls, indicate an effort to mitigate common risks like data breaches.

- Regulatory and compliance requirements are not directly referenced. But the use of encryption, logging, and access controls follows common security best practices and likely supports compliance needs. Formal compliance processes are not described.

## Analysis phase:

- How is sensitive data identified and classified?
- What measures are in place to protect different categories of data?
- What is the threat model of the application, and how does it change with the new feature? Are least privilege principles considered when determining user access levels?

## Design phase

- What security controls are integrated into the overall system architecture?
- Are secure design principles followed in the creation of system components?
- How is input validation implemented to prevent common security vulnerabilities?
- How is encryption integrated into the design?

## Development phase:

- Is there a code review process that includes security considerations?
- Are automated code analysis tools used to identify potential security vulnerabilities?
- How are the results of code analysis tools addressed and remediated?
- Is there a process for scanning and monitoring third-party dependencies for security vulnerabilities?
- How are vulnerabilities in external libraries and frameworks addressed?
- How is code version control and access control implemented to prevent unauthorized access or code tampering?

## Testing phase:

- Are comprehensive security tests (SAST, DAST, Penetration testing) conducted during the testing phase?
- Is security testing automated to ensure consistent and repeatable results?
- How quickly are identified vulnerabilities remediated, and is there a defined process for prioritizing and addressing them?

## Implementation phase:

- Are deployment scripts and configurations reviewed for security considerations?
- Is there a configuration management process in place to maintain the security of deployed systems?
- How are changes to production configurations reviewed and approved?
- Is there a well-defined incident response plan for security incidents that may occur during deployment?

## Maintenance phase

- Is there a process for timely applying security patches to address known vulnerabilities?
- Is there continuous monitoring for security events and anomalies during the maintenance phase?
- How are logs reviewed, and what actions are taken based on security events?
- Based on your analysis, prepare a report that summarizes the following:

## Security Requirements:

- Enumerates and explains each security requirement.
- Evaluates the clarity and specificity of each requirement.
- Identifies potential gaps or areas where the requirements may be strengthened.
- Provides recommendations for improvement.

## SDLC Process:

- Summarizes the overall security posture of the SDLC process.
- Highlights key strengths and areas of improvement identified during the assessment.
- Provides a list of critical findings in any phase of the SDLC
- Proposes strategies for improving the SDLC
