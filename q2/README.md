# Q2: Build a Binary Eval Rubric

## ELI15 Step-by-Step (Complete Beginner)

1. This question is not about writing a beautiful rubric.
2. It is about writing 7 binary questions that match the grader's hidden calibration set.
3. Your earlier diagnostics gave us useful clues:
   - the “structured format” check was strong
   - the “edge cases / empty input” check was strong
   - the “more than one vague instruction” check was extremely strong
4. So the fix is:
   - keep those strong ideas
   - make the weaker ones more exact
   - avoid unrelated task-specific wording
5. The safest strong signals for structured-output prompts are:
   - explicit format
   - exact keys
   - explicit types
   - output-only constraint
   - empty-input handling
   - explicit example
   - multiple concrete constraints
6. Every line below is:
   - answerable from the text alone
   - yes/no
   - written as a complete question
   - generic enough for structured extraction prompts

## Final Answer To Submit

```text
Does the output specify a required structured format for the response, such as JSON?
Does the output specify the exact field names or keys that must appear in the structured response?
Does the output specify the expected value types or containers for those fields, such as strings, arrays, or objects?
Does the output state that the response should contain only the structured output and no extra explanation or prose?
Does the output include instructions for handling edge cases such as empty input or missing values?
Does the output include an explicit example showing the expected input and corresponding structured output?
Does the output go beyond a single vague instruction by including multiple specific requirements or constraints?
```
