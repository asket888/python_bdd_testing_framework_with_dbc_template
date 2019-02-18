@project @create_project
Feature: Create Project. As a user I should be able to create new projects

  Background: Setup before Create Project tests
    Given I create new account with "[AT] Account" name using DB
    And I go to "/projects" url page
    And "Projects" tab is active in main menu

  @create_project_1
  Scenario: [@create_project_1] Create Project with correct data
    When I click [Create Project] button on Projects page
    Then "Create Project" popup appears on the page
    When I fill Create Project popup fields with following values
      | input            | value                 |
      | Project Name     | [AT] Project          |
      | Account          | [AT] Account          |
      | DV360 Advertiser | [AT] Advertiser       |
    And I click [Create Project] button in Create Project popup
    And "[AT] Project" title appears on the page
    When I go to "/projects" url page
    Then "[AT] Project" project card presented on the page and contains following data
      | column           | value                 |
      | Account          | Account: [AT] Account |
      | Project Name     | [AT] Project          |
      | Flight Dates     | Flight Dates: --      |
      | Last SDF Upload  | --                    |

  @create_project_2
  Scenario: [@create_project_2] Create Project. Cancel button checking
    When I click [Create Project] button on Projects page
    Then "Create Project" popup appears on the page
    When I fill Create Project popup fields with following values
      | input            | value                 |
      | Project Name     | [AT] Project          |
      | Account          | [AT] Account          |
      | DV360 Advertiser | [AT] Advertiser       |
    And I click [Cancel] button in Create Project popup
    Then "Projects" tab is active in main menu
    And "[AT] Project" is not presented on Projects page

  @create_project_3
  Scenario: [@create_project_3] Create Project. Validations checking
    Given I create new "[AT] Project" project for "[AT] Account" account using DB
    And I refresh browser page
    When I click [Create Project] button on Projects page
    And I fill "Project Name" field by " " value in Create Project popup
    Then "This field is required" error message appears under "Project Name" input in Create Project popup
    And [Create Project] button is disabled in Create Project popup
    When I fill "Account" field by " " value in Create Project popup
    Then "This field is required" error message appears under "Account" input in Create Project popup
    And [Create Project] button is disabled in Create Project popup
    When I fill "DV360 Advertiser" field by " " value in Create Project popup
    Then "This field is required" error message appears under "DV360 Advertiser" input in Create Project popup
    And [Create Project] button is disabled in Create Project popup
    When I fill Create Project popup fields with following values
      | input            | value                 |
      | Project Name     | [AT] Project          |
      | Account          | [AT] Account          |
      | DV360 Advertiser | [AT] Advertiser       |
    When I click [Create Project] button in Create Project popup
    Then "There is already a project with this name" error message appears under "Project Name" input in Create Project popup
