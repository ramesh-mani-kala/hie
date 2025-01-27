*** Settings ***
Library    OperatingSystem
Library    Collections

*** Test Cases ***
Test Case 1 - Verify File Exists
    [Documentation]    Verify if a file exists in the current directory
    Create File    testfile1.txt
    File Should Exist    testfile1.txt

Test Case 2 - Check Directory Creation
    [Documentation]    Verify if a directory can be created successfully
    Create Directory    TestDirectory
    Directory Should Exist    TestDirectory

Test Case 3 - Validate String Equality
    [Documentation]    Verify if two strings are equal
    Should Be Equal    Hello    Hello

Test Case 4 - Validate List Length
    [Documentation]    Verify if a list has the expected number of elements
    ${list}=    Create List    One    Two    Three
    Length Should Be    ${list}    3

Test Case 5 - Check Number Equality
    [Documentation]    Verify if two numbers are equal
    Should Be Equal As Numbers    10    10

Test Case 6 - Verify File Removal
    [Documentation]    Verify if a file can be removed successfully
    Create File    testfile2.txt
    Remove File    testfile2.txt
    File Should Not Exist    testfile2.txt

Test Case 7 - Check Dictionary Key
    [Documentation]    Verify if a dictionary contains a specific key
    ${dict}=    Create Dictionary    key1=value1    key2=value2
    Dictionary Should Contain Key    ${dict}    key1

Test Case 8 - Validate Substring
    [Documentation]    Verify if a string contains a specific substring
    Should Contain    Hello, World!    Hello

Test Case 9 - Check List Contains Item
    [Documentation]    Verify if a list contains a specific item
    ${list}=    Create List    Item1    Item2    Item3
    List Should Contain Value    ${list}    Item2

Test Case 10 - Confirm Current Directory
    [Documentation]    Verify if the current directory is accessible
    [Tags]    high
    ${current_dir}=    Get Current Directory
    Log    Current directory: ${current_dir}
    Directory Should Exist    ${current_dir}