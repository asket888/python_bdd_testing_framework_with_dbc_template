@login
Feature: Login. As a user I should be able to login only with correct credentials

  Background: Setup before Login tests
    Given I delete all browser cookies
    And I refresh browser page
    And Login page appears

  @login_1
  Scenario Outline: [@login_1] Login to application with incorrect credentials. Error message checking
    When I login with following "<login>" and "<password>"
    And I click [Sign In] button
    Then "Password or Email is incorrect." error message appears on Login page
    Examples:
      | login                   | password        |
      | correct_login@gmail.com | WrongPass123    |
      | wrong_login@gmail.com   | CorrectPass_123 |

  @login_2
  Scenario: [@login_2] Login to application with incorrect credentials. Empty field
    Given [Sign In] button is enabled
    When I click [Sign In] button
    Then "Password or Email is incorrect." error message appears on Login page

  @login_3
  Scenario: [@login_3] Login to application with correct credentials
    When I login with correct credentials
    Then "Tab_name" tab is active in main menu
