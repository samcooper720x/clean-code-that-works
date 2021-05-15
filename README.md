# Why?
After listening to [this](https://www.youtube.com/watch?v=EZ05e7EMOLM) talk, I decided that rather than continue to wade through opinionated blog posts and tutorials on TDD it might be better to go straight to the source: Kent Beck's _Test-Driven Development By Example_.

## What?
As suggested in the preface, I have run the examples and tests myself alongside reading the book. To ensure I was doing so actively I've chosen to use Python for this, translating the original Java / JUnit implementation to Python / Pytest. I used Pytest over Unittest because Unittest so closely resembles JUnit and I wanted to be forced to consider precisely what Kent Beck was trying to do, rather than just typing up from the book.

## Notes from the book
### Two Rules
+ Write new code only if an automated test has failed.
+ Eliminate duplication.

### Red -> Green -> Refactor
Adhering to these rules enforces an order:
1. Red: Write a failing test (it might not even compile)
2. Green: Make it work as quickly as possible (quick and dirty > clean)
3. Refactor: Clean it up, eliminate the duplication

### Part One Review
+ There are three ways to make a test work cleanly:
    1. fake it
    2. triangulation
    3. obvious implementation
+ You can drive the design by trying to remove duplication between the test and the code.
+ Adjust the gap between tests to exercise more control or work faster, as the situation dictates.

