# Created by Tracy Arispe at 5/29/2024
# There are scenarios: 15,16,17,30

Feature: Test Scenarios for login functionality

  @TestLP_1
  Scenario: User can login to account with proper credentials
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type user email arispe.tracy@gmail.com into email textbox
    When Type user password abc123 into password textbox
    When Click Continue button
    Then Verify that Main Menu Button text is displayed

