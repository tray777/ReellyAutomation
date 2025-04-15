# Created by Tracy Arispe at 4/8/2025
Feature: Test [Scenario 30] for login functionality

  @Test_sp_1

  Scenario: User can filter by Out of Stock
    Given Open Reelly main page
    Then Verify user is on the login page
    When Type user email arispe.tracy@gmail.com into email textbox
    When Type user password abc123 into password textbox
    When Click Continue button
    Then Verify that Main Menu Button text is displayed
    When click the Total Projects New page button
    Then Verify user is on the Off-plan New page
    When Click Sale status drop down menu locator
    When Click Out of Stock button
    When Click Sale status drop down menu locator
    Then Verify each product picture contains Out of stock tag
