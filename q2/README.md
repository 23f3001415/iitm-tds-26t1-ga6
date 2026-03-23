# Q2: Build a Binary Eval Rubric

## ELI15 Step-by-Step (Complete Beginner)

1. The grader is not asking you to write the extraction prompt itself.
2. It is asking you to write a rubric that another LLM can use to judge whether a student's prompt is good.
3. A bad rubric says vague things like "Is this prompt good?" because different judges will disagree.
4. A good rubric breaks quality into tiny YES/NO questions.
5. Each question must be answerable just by reading the student's prompt text.
6. That means you should check visible things such as:
   - whether the prompt asks for a structured format
   - whether it gives the required fields
   - whether it says what to do for missing values
   - whether it forbids extra text
7. Do not ask about style preferences like "Is it nicely written?" because that is subjective.
8. Do not ask about hidden intent like "Will this always work?" because the judge cannot know that from the text alone.
9. Look at the three examples:
   - GOOD is specific, strict, and testable
   - MEDIOCRE is partly specific but missing important details
   - POOR is too vague
10. So your checks should reward the details that make GOOD strong and mark missing details in MEDIOCRE and POOR.
11. The safest checks are the ones tied to structure and constraints:
   - exact schema or template
   - required fields
   - field types
   - empty-input behavior
   - missing-field behavior
   - handling multiple matches
   - whether all required fields must always appear
12. Each line must be a complete question ending with `?`.
13. You need exactly 7 lines, not 6 and not 8.

## Why These 7 Checks Are Strong

- They are binary: a judge can answer YES or NO.
- They are visible from the prompt text alone.
- They focus on task quality, not writing style.
- Together they separate GOOD from MEDIOCRE and POOR in a consistent way.

## Final Answer To Submit

```text
Does the prompt define an explicit output schema or template instead of only asking for structured output?
Does the prompt specify the exact output fields or keys that must appear?
Does the prompt specify the expected value type for each field, such as string, array, object, number, or boolean?
Does the prompt define what the output should be when the input is empty?
Does the prompt define what value to use when a requested field cannot be extracted?
Does the prompt specify how multiple extracted values should be represented in the output?
Does the prompt make it clear that all required fields should still appear in the output even when some values are empty or missing?
```

Submit exactly those 7 lines.
