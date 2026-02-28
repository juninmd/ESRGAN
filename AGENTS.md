```markdown
# AGENTS.md File Guidelines

These guidelines are designed to ensure consistent, maintainable, and high-quality code for our AGENTS project. Adherence to these principles is mandatory for all development efforts.

## 1. DRY (Don't Repeat Yourself)

*   **Single Responsibility Principle:** Each agent module should have a single, well-defined purpose. Avoid creating overly complex modules with multiple responsibilities.
*   **Component Reusability:** Design components to be reusable across different agents or projects.  Utilize generic interfaces and data structures.
*   **Abstraction:**  Define abstract interfaces for agents and their interactions. This reduces code duplication and improves flexibility.
*   **Pattern Matching:** Implement pattern matching where possible to simplify conditional logic and reduce code repetition.

## 2. KISS (Keep It Simple, Stupid)

*   **Minimize Complexity:** Strive for clear and concise code. Avoid unnecessary complexity.
*   **Readability:** Prioritize code readability. Use descriptive variable names and comments judiciously.
*   **Small Units:** Break down large tasks into smaller, manageable units. Each unit should have a well-defined purpose.
*   **Avoid Over-Engineering:** Resist the urge to over-optimize.  Focus on the core requirements first.

## 3. SOLID Principles

*   **Single Responsibility Principle (SRP):**  Each class should have one and only one reason to change.
*   **Open/Closed Principle:**  The software should be open for extension but closed for modification.  This is key for agent development.
*   **Liskov Substitution Principle (LSP):**  For every replacement of a class by a subclass, where some of the old class’s behavior is still valid.
*   **Interface Segregation Principle (ISP):** Clients shouldn't be forced to bound to methods they don’t use.
*   **Dependency Inversion Principle (DIP):**  High-level modules should be dependent on low-level modules, and modules should be dependent on abstractions.

## 4. YAGNI (You Aren't Gonna Need It)

*   **Avoid Unnecessary Code:**  Don’t add features or code that is not currently required.
*   **Focus on Requirements:**  Implement only what is explicitly needed to meet the current requirements.
*   **Refactor Only When Necessary:** Refactor only when the code is causing problems or is no longer meet its purpose.

## 5. Development Guidelines

*   **Code Style:** Follow a consistent code style using a linter (e.g., ESLint, PyLint) and formatting rules.  The core style guide is outlined in the `style.md` file.
*   **Naming Conventions:**  Use clear and consistent naming conventions (e.g., camelCase, snake\_case).
*   **Documentation:**  Document code effectively using docstrings, comments, and READMEs.
*   **Testing:**  All code must be thoroughly tested.  Write unit tests for all components. Aim for a minimum of 80% test coverage across all modules.
*   **Error Handling:** Implement robust error handling to prevent crashes and provide informative error messages.
*   **Logging:** Use logging strategically to track events and debug issues.
*   **Version Control:** Use a version control system (e.g., Git) with clear branching strategies.
*   **Code Reviews:**  All code should be reviewed by at least one other developer before being merged.
*   **Documentation Updates:** Any changes to the code should be documented.

## 6. File Size & Structure

*   **Maximum File Size:**  Each file should not exceed 180 lines of code.
*   **File Organization:**  Organize code into logical modules and packages.  Use clear directory structures.
*   **Comments:**  Add comments to explain complex logic, algorithms, and design decisions. Don’t over-comment.

## 7. Testing

*   **Unit Tests:** Each agent module must have a comprehensive suite of unit tests.
*   **Test Coverage:** Achieve at least 80% test coverage across all modules.
*   **Test Case Design:** Tests should be designed to cover all possible input and edge cases.
*   **Test Framework:** Utilize a testing framework suitable for the chosen language (e.g., Jest, Pytest).

## 8.  Future Considerations

*   **API Design:** Design clear and consistent APIs for agent interaction.
*   **Data Structures:**  Establish well-defined data structures for efficient agent operation.
*   **Error Model:** Define a clear error model and exception handling strategy.

These guidelines are a living document and will be updated as needed.  All developers are responsible for understanding and adhering to them.
```