# 🎯 Pytest-Playwright Testing Project (UI + API)

This project is a comprehensive **Pytest-Playwright Testing** solution, combining UI and API testing capabilities. The project features a login functionality, state preservation, and integration with multiple reporting tools.

---

## 🛠️ Technologies Used

The project leverages the following technologies:

- **pytest-playwright**: For UI automation and browser interaction.
- **pytest**: As the core testing framework.
- **pytest-allure**: For generating detailed and interactive reports.
- **pytest-html**: For HTML-based reporting.
- **requests**: For API testing.
- **poetry**: For dependency management and virtual environment handling.

---

## ✨ Features

- **User Login and State Preservation**:

  - The user login functionality is implemented to save the state (e.g., cookies, sessions).
  - This state is reused in subsequent tests.
  - The state-saving logic is powered by fixtures defined in the `conftest.py` file.

- **Centralized Configuration**:

  - Credentials and base URLs (for both UI and API) are stored in `config.conf`.
  - These parameters are read using the `readConfig` file, which provides utility functions to pass configuration data into tests.

- **Framework Behavior Customization**:

  - Default command-line options, test paths, and markers are configured in the `pytest.ini` file.

- **Custom Logging**:

  - A `customLogger` file is included for detailed logging of test executions.

- **Page Object Model**:
  - The `pages` directory contains classes and methods for interacting with various application pages.

---

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/your-repository.git
   cd your-repository
   ```
2. Install Poetry (if not already installed):
   ```bash
   pip3 install poetry
   ```
3. Install project dependencies:
   ```bash
   poetry install
   ```

---

## 🚀 Running Tests

1. **Run all tests:**

   ```bash
   pytest

   ```

2. **Run tests with specific markers:**
   ```bash
   pytest -m [tag]
   ```

## 📊 Viewing Test Reports

**Allure report**

1. Install Allure:
   ```bash
   brew install allure  # For macOS
   choco install allure # For Windows
   ```
2. Generate and view the Allure report:
   ```bash
   allure serve allure-results
   ```

**HTML Report:**
Open the test_report.html file located in the reports folder in any browser.

## 📂 Project Structure

📁 root
├── 📂 pages # Page classes and methods (Page Object Model)
├── 📂 tests # Test cases (UI and API)  
│ └── 📂 api # API tests
│ └── 📂 ui # UI tests
├── 📂 reports # Generated test reports (HTML)
├── 📂 allure-reports # Generated test reports (Allure)
├── 📂 screenshots # Screenshots of failed tests
├── 📂 configurations # Configuration files
│ └── 📜 config.conf # Base URLs and credentials
├── 📂 utilities # Utility scripts
│ └── 📜 readConfig.py # Reads configuration parameters
└── 📜 cookie.py # Store cookie
├── 📂 logs # Custom logging utility
│ └── 📜 customLogger.py # Logging utility for test execution
├── 📜 pytest.ini # Pytest configuration (default args, markers, etc.)
