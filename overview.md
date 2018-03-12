# Topics

## Project Overview

- High Level Overview
  - Public projects
    - OpenCafe
    - CloudCafe
    - CloudRoast
    - Design reasoning
  - Internal projects
    - RaxRoast
- Acquisition
  - Getting the code
  - Installing the projects
  - Initializing OpenCafe
  - Installing plugins
  - Walkthrough of OpenCafe on-disk file structure

## Client Design

- Terminology
  - Client
  - Model
  - Composite
  - Behavior
- Use of constants (avoid using magic strings)
- Implementation
  - Package structure
  - Config classes
    - Return type of config values
    - Defaults
  - Serialization
   - __json_to_obj
   - request_entity and response_entity_type
  - requestlibkawrgs
- Metatests

## Test Design

- Fixtures and fixture inheritance
  - Basics of unittest order of execution
  - How base classes impact order of test execution
- Test decorators
  - skipIf
    - Skipping based on feature availability
  - tags
    - Selecting or deselecting tests based on tags
  - data_driven_test
- Brew tests (limited audience)

## Configuration and Execution

- Cafe command line options
  - List
    - cafe-runner compute -l tests
    - cafe-runner compute -l configs
  - dry run
  - How <project> argument impacts other commands
  - Test selection by
    - Package
    - Method
    - Module
  - xunit output
- Configuration and logging
  - How <project> arguments which directories are used

## Test Execution and Debugging
- Null entity exceptions
  - Request likely failed (check logs to see actual response )
- Timeouts
  - Do not assume you know what status the item was in while looping. Weird and unexpected things do happen with state (pending -> deleted)
- 503's
  - Service unavailable. Re-run?
- Tracing errors with request ids
- Unable to ping server
  - Check if you can ping any node built on that host (host may have networking issues)
- No host available

## Links
- Docs: http://opencafe.readthedocs.io/en/latest/
- Quickstart: http://opencafe.readthedocs.io/en/latest/quickstart/index.html