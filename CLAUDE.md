# Project Engineering Standards

Project-wide coding standards and conventions for this codebase.

---

## Working Relationship

We're colleagues working together - no formal hierarchy.

**Core principles:**
- If you lie to me, I'll find a new partner
- YOU MUST speak up immediately when you don't know something or we're in over our heads
- When you disagree with my approach, YOU MUST push back, citing specific technical reasons if you have them. If it's just a gut feeling, say so. If you're uncomfortable pushing back out loud, just say "I have a bad feeling about this". I'll know what you mean
- YOU MUST call out bad ideas, unreasonable expectations, and mistakes - I depend on this
- NEVER be agreeable just to be nice - I need your honest technical judgment
- NEVER utter the phrase "You're absolutely right!" You are not a sycophant. We're working together because I value your opinion
- YOU MUST ALWAYS ask for clarification rather than making assumptions
- If you're having trouble, YOU MUST STOP and ask for help, especially for tasks where human input would be valuable
- You have issues with memory formation both during and between conversations. Use your journal to record important facts and insights, as well as things you want to remember before you forget them
- You search your journal when you're trying to remember or figure stuff out

**Rule #1**: If you want exception to ANY rule, YOU MUST STOP and get explicit permission from the user first. BREAKING THE LETTER OR SPIRIT OF THE RULES IS FAILURE.

---

## Software Design Philosophy

**YAGNI**: The best code is no code. Don't add features we don't need right now.

**Design principles:**
- Design for extensibility and flexibility
- Prefer simple, clean, maintainable solutions over clever or complex ones, even if the latter are more concise or performant
- Readability and maintainability are primary concerns
- Good naming is very important. Name functions, variables, classes, etc so that the full breadth of their utility is obvious
- Reusable, generic things should have reusable generic names

---

## Code Implementation Standards

**Atomic changes:**
- YOU MUST ALWAYS break a plan into small atomic and fully functional steps
- Each step should encapsulate the smallest reasonable change to the code
- Each step should include unit tests. All tests should pass
- Each such step should be wrapped into a commit
- YOU MUST ALWAYS adhere to clean git history principle: we want to be able to track atomic changes and be able to git bisect to find elusive bugs
- YOU MUST ALWAYS perform prefactory refactoring (preparatory refactoring) if you're working on a complex task that requires this in order to follow our rules

**Code quality:**
- YOU MUST make the SMALLEST reasonable changes to achieve the desired outcome
- YOU MUST WORK HARD to reduce code duplication, even if the refactoring takes extra effort
- YOU MUST MATCH the style and formatting of surrounding code, even if it differs from standard style guides. Consistency within a file trumps external standards
- YOU MUST NOT change whitespace that does not affect execution or output. Otherwise, use a formatting tool
- Follow Python 3.11+ standards with Google's PEP8 (100 char line limit)

**Test requirements:**
- YOU MUST run and verify ALL specified tests pass before committing
- If tests fail, timeout, or cannot run: YOU MUST STOP immediately and consult user
- NEVER proceed with "tests will be verified later" or "tests probably work"
- Test evidence: Run command cleanly (success = no error field populated in tool response)
- ❌ NEVER use `;` followed by `echo "Exit code: $?"` - triggers approval prompts repeatedly
- ✅ The Bash tool automatically shows command success/failure - no manual exit code checking needed
- If you lack observability into why tests fail (no server logs, etc): YOU MUST STOP and consult user
- DO NOT investigate test failures outside the scope of your task - consult user first

**What to NEVER do:**
- YOU MUST NEVER make code changes unrelated to your current task. If you notice something that should be fixed but is unrelated, document it in your journal rather than fixing it immediately
- YOU MUST NEVER throw away or rewrite implementations without EXPLICIT permission. If you're considering this, YOU MUST STOP and ask first
- YOU MUST get user's explicit approval before implementing ANY backward compatibility changes
- NEVER implement a mock mode for testing or for any purpose. We always use real data and real APIs, never mock implementations
- NEVER name things as "improved" or "new" or "enhanced", etc. Code naming should be evergreen. What is new someday will be "old" someday

**Comments and documentation:**
- YOU MUST explain WHY (complex business logic) over WHAT (code should be simple to speak for itself) in comments
- YOU MUST NEVER add comments about what used to be there or how something has changed
- YOU MUST NEVER refer to temporal context in comments (like "recently refactored" "moved") or code. Comments should be evergreen and describe the code as it is

---

## Unit Testing Principles

When reviewing or writing unit tests:

**YOU MUST ALWAYS:**
- Inject all dependencies via constructor parameters, method parameters, or test fixtures
- Maintain clear separation between test and production code
- Focus on observable results, state changes, and return values
- Test public interfaces and contracts, not internal implementation details
- Verify external interactions through their results, not method calls
- Write tests that survive refactoring when behavior remains unchanged
- Test all execution paths and conditional branches
- Use clear descriptive names: `test_method_scenario` or `test_behavior_when_condition`
- Use one logical assertion per test case
- Follow: verbose is better than complex - tests can repeat themselves for readability
- One test case per input example - each specific input-output pair gets its own test
- Test failures should make it immediately clear why they failed

**YOU MUST NEVER:**
- Use `unittest.mock.patch`, monkeypatch, or global variable modifications (except in CLI/integration tests where mocking AWS/external services is necessary)
- Implement complex logic in tests - avoid loops, conditionals, or "tests for tests"
- Test internal method call sequences using assert_called_with or similar patterns
- Miss edge cases or error scenario coverage
- Test with unclear purpose or multiple unrelated assertions
- Hard-code dependencies in test setup

**Private method testing guidance:**
- Prefer testing through public interfaces when practical
- Test private methods directly when:
  1. They have complex logic with many edge cases (especially security-critical functions like SQL escaping)
  2. Failure would be hard to diagnose through public interface alone
  3. The private method is a pure utility function
- If a private method needs extensive testing, consider extracting to a public utility module (e.g., `api/app/lib/sql/escaping.py`)

---

## Shared Code Organization

Follow these conventions for organizing shared code:

### Three Levels of Sharing

1. **Repo-level libraries** (`api/app/lib/`)
   - Used by 3+ packages across different domains
   - Examples: `lib/pagination/`, `lib/geo/`, `lib/csv/`
   - Pure utilities with no domain-specific coupling

2. **Package-level helpers** (`package/helpers.py`)
   - Used by multiple modules within one package
   - Examples: `contractors/helpers.py`, `geo_metrics/helpers.py`
   - Domain-specific utilities (query builders, formatters)

3. **Inline utilities**
   - Used by single module only
   - Keep in the module file itself
   - Extract to helpers.py if ≥3 functions or >50 LOC

### Decision Criteria

**Move to `lib/` when:**
- Function is pure utility (no domain coupling)
- Used across 3+ different packages
- Consolidates duplication (e.g., geo ID formatting used by all geo_* packages)

**Keep in `package/helpers.py` when:**
- Domain-specific (e.g., contractor-specific query logic)
- Used by 2+ modules in same package only

**Keep inline when:**
- Single module usage
- < 50 LOC of shared code

---

## Python Execution

**ALWAYS use absolute imports** in this project.
**ALWAYS run `uv run`. NEVER execute `python` directly.**

`uv` automatically adds project root to `PYTHONPATH`.

---

## Version Control & Git

**Commit frequency:**
- YOU MUST commit frequently throughout the development process, even if your high-level tasks are not yet done

**Pre-commit hooks:**
- NEVER SKIP OR EVADE OR DISABLE A PRE-COMMIT HOOK

**Staging changes:**
- NEVER use `git add -A` unless you've just done a `git status` - You don't want to add random test files to the repo

**Temporal context:**
- YOU MUST NEVER leave temporal context in git description (like "recently refactored" "moved") or code
- Body should be evergreen and describe the code as it is
- If you name something "new" or "enhanced" or "improved", you've probably made a mistake and MUST STOP and ask me what to do

---

## Commit Message Guidelines

Follow these rules for great Git commit messages:

### Format Rules

1. **Separate subject from body** with a blank line
2. **Limit subject line to 50 characters** - forces concise, thoughtful descriptions
3. **Capitalize the subject line** - begin with capital letter
4. **No period at end** of subject line - saves space
5. **Use imperative mood** in subject line - write as command ("Add feature" not "Added feature")
6. **Wrap body at 72 characters** - ensures readability across tools
7. **Explain what and why, not how** - focus on reasons for change and problem solved

### Content Rules

** NEVER include:**
- Process tracking: "Step 5", "Phase 2", "Task ABC-123"
- Ticket IDs: ENG-123, JIRA-456, issue #789, Linear references
- Metrics: "200 LOC", "95% coverage", "within target"
- Temporal context (past): "recently refactored", "previously moved", "used to be"
- Temporal context (future): "will fix later", "next step", "TODO", "this prepares for"
- Self-praise: "successfully", "perfect", "excellent"
- Irrelevant details: test counts, files changed, tool promotions
- Verbose bloat: Restating subject line, over-explaining obvious changes

** ALWAYS include:**
- Technical rationale (WHY architecturally)
- Timeless context (readable in 6 months without project docs)
- Tradeoffs (if accepting debt, explain)

### Examples

**Bad - Temporal context (future):**
```
Create lib/geo/formatting module

Extract formatting utilities to shared library.

Next step: Update route modules to import from lib/geo.
```
**BAD** - "Next step" refers to future work - not evergreen

**Bad - Temporal context (past):**
```
Move formatting functions to lib/geo

These were previously in geo_search/addresses.py but
recently refactored to be shared across modules.
```
**BAD** - "previously", "recently refactored" - refers to history

**Bad - Process tracking:**
```
Extract addresses endpoint (Step 2, Phase 4.1 complete)

Files changed: 3, Tests: 15 passing
```
**BAD** - "Step 2", "Phase 4.1", metrics

**Bad - Ticket references and verbose bloat:**
```
Update geo routes to import from lib/geo

Replace local function definitions with imports from centralized
api.app.lib.geo.formatting module.

This follows ENG-613 Goal #3 to consolidate duplicated code into
well-defined libraries. All route modules now use shared geo
utilities instead of maintaining local copies.
```
**BAD** - "ENG-613" ticket reference, verbose restatement of obvious

**Good - Evergreen, explains WHY:**
```
Extract addresses endpoint to dedicated module

Move address search logic to addresses.py following Single
Responsibility Principle. Shared helpers remain in legacy
file temporarily to support remaining endpoints during
incremental migration.
```
**GOOD** - Timeless context, explains architectural reasoning

**Good - Concise architectural context:**
```
Update geo routes to import from lib/geo

Replace local function definitions with imports from centralized
api.app.lib.geo.formatting module. Consolidates duplicate utility
code across route packages following three-level sharing convention.
```
**GOOD** - Clear WHY (consolidation), no ticket refs, no bloat

**Key principles:**
- Subject line communicates the change clearly
- Body provides context and reasoning
- Focus on why the change was necessary
- Help future developers understand the decision
- Write as if describing the codebase NOW, not its history or future

---

## Repository Integration

**Project documentation:**
- YOU MUST read README.md for project overview
- YOU MUST read pyproject.toml for available `uv` commands for this project

**Linear Issue Integration:**
- ALWAYS use Linear MCP to read Linear issues and get correct git branch names
- Use Linear MCP tools to fetch issue details before starting work
- Get the git branch name from the Linear issue to ensure automatic linking

---
