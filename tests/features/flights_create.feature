@flights @create_flight
Feature: Create Flight. As a user I should be able to create new flight

  Background: Setup before Create Flight tests
    Given I create new account with "[AT] Account" name using DB
    Given I create new "[AT] Project" project for "[AT] Account" account using DB
    And I go to "/projects" url page
    And I click on "[AT] Project" card Projects page

  @create_flight_1
  Scenario: [@create_flight_1] Create Flight with 'In-Stream' format
    When I click [Add Flight] button in "Flight" section on Project Card page
    Then "Add Flight" title appears on the page
    When I fill Add Flight page fields with following values
      | input         | value                          |
      | Flight Name   | [AT] Flight                    |
      | Location      | All Locations                  |
      | Language      | All Languages                  |
      | Ad Format     | Display Network                |
    And I click [Save & Collapse] button on Add Flight page
    And "[AT] Flight" title appears on the page
    And Following data presented in "Flight Info" section on Flight Overview page
      | column        | value                          |
      | Language      | All Languages                  |
      | Location      | All Locations                  |
      | Status        | Active                         |
      | Ad Format     | In-Stream Display Network      |

  @create_flight_5
  Scenario: [@create_flight_5] Create Flight. Cancel button checking
    Given Add Flight message presented in Flight section on Project Card page
    When I click [Add Flight] button in "Flight" section on Project Card page
    Then "Add Flight" title appears on the page
    When I fill Add Flight page fields with following values
      | input         | value                          |
      | Flight Name   | [AT] Flight                    |
      | Location      | All Locations                  |
      | Language      | All Languages                  |
      | Ad Format     | Display Network                |
    And I click [Cancel] button on Add Flight page
    Then "[AT] Project" title appears on the page
    And Add Flight message presented in Flight section on Project Card page

  @create_flight_6
  Scenario: [@create_flight_6] Create Flight. Validations checking
    Given I create new "[AT] Flight" flight for "[AT] Project" project using DB
    And I refresh browser page
    When I click [Add Flight] button on Project Card page
    Then "Add Flight" title appears on the page
    When I fill Flight Name field by " " value on Add Flight page
    Then "This field is required" error message appears under "Flight Name" input on Add Flight page
    And [Save & Collapse] button is disabled on Add Flight page
    When I fill Flight Name field by "[AT] Flight" value on Add Flight page
    And I click [Save & Collapse] button on Add Flight page
    Then "There is already a flight with this name" error message appears under "Flight Name" input on Add Flight page
