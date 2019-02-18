@main_menu
Feature: Main Menu. As a user I should be able to use application main menu on each page

    Background: Setup before Main Menu tests
    Given I go to "/projects" url page
    And "Projects" tab is active in main menu

  @main_menu_1
  Scenario: [@main_menu_1] Main Menu navigation checking
    When I click "Targeting" tab in Main Menu
    Then "Targeting" tab is active in main menu
    And "Custom Keyword Lists" title appears on the page
    And All Main Menu elements display on the page
    When I click "Projects" tab in Main Menu
    Then "Projects" tab is active in main menu
    And All Main Menu elements display on the page
    When I click "Accounts" tab in Main Menu
    Then "Accounts" tab is active in main menu
    And All Main Menu elements display on the page
    When I click "Archive" tab in Main Menu
    Then "Archive" tab is active in main menu
    And All Main Menu elements display on the page
