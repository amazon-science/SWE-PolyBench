# Instance: langchain-ai__langchain-4646
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: True

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
PydanticOutputParser has high chance failing when completion contains new line
## Context
When the completion is of a longer format such as an Email, the text will likely contain new line character `\n`.
If it is not properly escaped like `\\n`, parsing will fail when using PydanticOutputParser as `json.loads` does not allow control characters in strict mode.
Most of the time, RetryWithErrorOutputParser also fails to correct the format.

## Example
```python
from langchain.output_parsers import PydanticOutputParser
from langchain.prompts import PromptTemplate
from pydantic import BaseModel, Field

class Email(BaseModel):
    subject: str = Field(description="main objective of the email")
    body: str = Field(description="email content")

parser = PydanticOutputParser(pydantic_object=Email)

prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}\n",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)
completion = llm(
    prompt.format(
        query="Write a long formal email to inform my clients that the company is broke."
    )
)

parser.parse(completion)
```
```python
# completion

> Here is the output instance:
\```
{"subject": "Company Status Update", "body": "Dear Clients, 

This email is to inform you that our company is currently in a difficult financial situation. We apologize for any inconvenience caused by this and are doing our best to ensure that our services remain of the highest quality for our valued clients.

We want to thank you for your support and understanding during this difficult time.

Sincerely,
[Company Name]"}
\```
```
```python
# parser.parse(completion)

> Got: Invalid control character at: line 1 column 61 (char 60)
```

## Thoughts
Maybe include instructions on escaping in PYDANTIC_FORMAT_INSTRUCTIONS?

Or could adding an option to allow non-strict mode be considered?
https://github.com/hwchase17/langchain/blob/32793f94fd6da0bb36311e1af4051f7883dd12c5/langchain/output_parsers/pydantic.py#L25
````

## Operational trajectory

### Turn 1 — tool call call_0001 (read)

````json
{
 "file_path": "langchain/output_parsers/pydantic.py"
}
````

Result:

````text
{
 "type": "file",
 "path": "langchain/output_parsers/pydantic.py",
 "full_read": true,
 "output": "langchain/output_parsers/pydantic.py\n\n1: import json\n2: import re\n3: from typing import Type, TypeVar\n4: \n5: from pydantic import BaseModel, ValidationError\n6: \n7: from langchain.output_parsers.format_instructions import PYDANTIC_FORMAT_INSTRUCTIONS\n8: from langchain.schema import BaseOutputParser, OutputParserException\n9: \n10: T = TypeVar(\"T\", bound=BaseModel)\n11: \n12: \n13: class PydanticOutputParser(BaseOutputParser[T]):\n14:     pydantic_object: Type[T]\n15: \n16:     def parse(self, text: str) -> T:\n17:         try:\n18:             # Greedy search for 1st json candidate.\n19:             match = re.search(\n20:                 r\"\\{.*\\}\", text.strip(), re.MULTILINE | re.IGNORECASE | re.DOTALL\n21:             )\n22:             json_str = \"\"\n23:             if match:\n24:                 json_str = match.group()\n25:             json_object = json.loads(json_str)\n26:             return self.pydantic_object.parse_obj(json_object)\n27: \n28:         except (json.JSONDecodeError, ValidationError) as e:\n29:             name = self.pydantic_object.__name__\n30:             msg = f\"Failed to parse {name} from completion {text}. Got: {e}\"\n31:             raise OutputParserException(msg)\n32: \n33:     def get_format_instructions(self) -> str:\n34:         schema = self.pydantic_object.schema()\n35: \n36:         # Remove extraneous fields.\n37:         reduced_schema = schema\n38:         if \"title\" in reduced_schema:\n39:             del reduced_schema[\"title\"]\n40:         if \"type\" in reduced_schema:\n41:             del reduced_schema[\"type\"]\n42:         # Ensure json in context is well-formed with double quotes.\n43:         schema_str = json.dumps(reduced_schema)\n44: \n45:         return PYDANTIC_FORMAT_INSTRUCTIONS.format(schema=schema_str)\n46: \n47:     @property\n48:     def _type(self) -> str:\n49:         return \"pydantic\"\n\n(End of file - total 49 lines)",
 "offset": 1,
 "lines_returned": 49,
 "total_lines": 49,
 "total_lines_exact": true,
 "truncated": false,
 "size_bytes": 1610
}
````

### Turn 2 — tool call call_0002 (edit)

````json
{
 "file_path": "langchain/output_parsers/pydantic.py",
 "old_string": "json.loads(json_str)",
 "new_string": "json.loads(json_str, strict=False)"
}
````

Result:

````text
{
 "path": "langchain/output_parsers/pydantic.py",
 "edited": true,
 "replacements": 1,
 "total_file_lines": 49,
 "total_file_size_bytes": 1624,
 "diff": "-             json_object = json.loads(json_str)\n+             json_object = json.loads(json_str, strict=False)",
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [
   {
    "effect": "edit",
    "paths": [
     "langchain/output_parsers/pydantic.py"
    ]
   }
  ]
 },
 "file_change": {
  "kind": "diff",
  "operation": "update",
  "path": "langchain/output_parsers/pydantic.py",
  "patch": "-             json_object = json.loads(json_str)\n+             json_object = json.loads(json_str, strict=False)",
  "additions": 1,
  "deletions": 1,
  "truncated": false,
  "omitted_lines": 0
 }
}
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "cd /testbed && python -c \"\nfrom langchain.output_parsers import PydanticOutputParser\nfrom pydantic import BaseModel\nclass E(BaseModel):\n    subject: str\n    body: str\np=PydanticOutputParser(pydantic_object=E)\nprint(repr(p.parse('Here:\\n\\`\\`\\`\\n{\\\"subject\\\": \\\"x\\\", \\\"body\\\": \\\"Dear,\\n\\nBye\\\"}\\n\\`\\`\\`')))\n\" && python -m pytest tests/unit_tests/output_parsers -q 2>&1 | tail -3"
}
````

Result:

````text
{
 "tool_outcome": {
  "schema_version": 1,
  "tool_name": "exec",
  "status": "success",
  "exit_code": 0,
  "retryability": "not_needed",
  "open_work_at_failure": false
 },
 "stdout": "E(subject='x', body='Dear,\\n\\nBye')\n\n(5 durations < 0.005s hidden.  Use -vv to show these durations.)\n30 passed in 1.54s\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 5887,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "/testbed"
  ],
  "command_sha256": [
   "c3e6356a084706c6bd5c1a640b9aadbe940c41da2b6a3d082707a2f512996f69"
  ]
 }
}
````

### Turn 4 — assistant text

I fixed the bug: `PydanticOutputParser` now accepts completions that have real line breaks inside JSON string values, such as a multi-line email body.

The change is one line in `langchain/output_parsers/pydantic.py`: `json.loads(json_str)` is now `json.loads(json_str, strict=False)`. Non-strict mode lets the JSON parser accept raw control characters like `\n` inside strings, which strict mode rejects with "Invalid control character".

I tested it on a completion like the one in the report, with real line breaks in the `body` text. It parsed into the model with the line breaks kept in `body`. The existing output-parser unit tests also pass (30 passed).

### Turn 5 — assistant text

I fixed the bug: `PydanticOutputParser` now parses completions where the JSON text contains literal new lines. The change is one line in `langchain/output_parsers/pydantic.py`: `json.loads(json_str)` is now `json.loads(json_str, strict=False)`. Non-strict mode lets raw control characters like `\n` through inside JSON strings, which strict mode rejects with "Invalid control character".

To check it, I parsed a completion shaped like the email example, with real line breaks inside the `body` string. It returned `E(subject='x', body='Dear,\n\nBye')` without an error. The existing unit tests in `tests/unit_tests/output_parsers` also pass (30 tests).

## Final answer

I fixed the bug: `PydanticOutputParser` now parses completions where the JSON text contains literal new lines. The change is one line in `langchain/output_parsers/pydantic.py`: `json.loads(json_str)` is now `json.loads(json_str, strict=False)`. Non-strict mode lets raw control characters like `\n` through inside JSON strings, which strict mode rejects with "Invalid control character".

To check it, I parsed a completion shaped like the email example, with real line breaks inside the `body` string. It returned `E(subject='x', body='Dear,\n\nBye')` without an error. The existing unit tests in `tests/unit_tests/output_parsers` also pass (30 tests).

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 54957 | 888 | 39498 | 15447 | 55845 |
