@accounts @create_account
Feature: Create Account. As a user I should be able to create new accounts

  Background: Setup before Create Account tests
    Given I go to "/accounts" url page
    And "Accounts" tab is active in main menu

  @create_account_1
  Scenario: [@create_account_1] Create Account with '% of Budget Margin' Calculation
    When I click [Create Account] button on Accounts page
    And I fill Create Account popup fields with following values
      | input              | value              |
      | Account Name       | [AT] Account       |
      | Vertical           | Automotive         |
      | Default Margin     | 10                 |
      | Margin Calculation | % of Budget        |
    And I click [Create Account] button on Create Account popup
    And Account with name "[AT] Account" has following column values in DB
      | column             | value              |
      | brand_vertical_id  | 2                  |
      | default_margin     | 0.1                |
      | margin_option      | Budget             |

  @create_account_2
  Scenario: [@create_account_2] Create Account. Cancel button checking
    When I click [Create Account] button on Accounts page
    And I fill Create Account popup fields with following values
      | input              | value              |
      | Account Name       | [AT] Account       |
      | Vertical           | Automotive         |
      | Default Margin     | 10                 |
      | Margin Calculation | % of Budget        |
    And I click [Cancel] button on Create Account popup
    When I refresh browser page
    Then "[AT] Account" is not presented on Accounts page

  @create_account_3
  Scenario: [@create_account_3] Create Account. Validations checking
    Given I create new account with "[AT] Account" name using DB
    And I refresh browser page
    When I click [Create Account] button on Accounts page
    And I fill "Account Name" field by " " value on Create Account popup
    Then "This field is required" error message appears under "Account Name" input on Create Account popup
    And [Create Account] button is disabled on Create Account popup
    When I fill "Vertical" field by " " value on Create Account popup
    Then "This field is required" error message appears under "Vertical" input on Create Account popup
    And [Create Account] button is disabled on Create Account popup
    When I fill Create Account popup fields with following values
      | input              | value              |
      | Account Name       | [AT] Account       |
      | Vertical           | Automotive         |
      | Default Margin     | 10                 |
      | Margin Calculation | % of Budget        |
    When I click [Create Account] button on Create Account popup
    Then "There is already an Account with this name" error message appears under "Account Name" input on Create Account popup
