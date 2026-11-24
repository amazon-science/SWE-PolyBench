# Instance: langchain-ai__langchain-5450
# Model: claude-opus-5-5
# Run status: ok
# Final resolved: False

## Task prompt

````text
You are in a git repository at the current working directory that has a bug described below. Investigate the code, then fix the bug by editing the source code only. Do not modify tests. Make the minimal correct change. Apply the edits now.

## Problem statement
Embeddings normalization and similarity metric
I am new to using Langchain and attempting to make it work with a locally running LLM (Alpaca) and Embeddings model (Sentence Transformer). When configuring the sentence transformer model with `HuggingFaceEmbeddings` no arguments can be passed to the encode method of the model, specifically `normalize_embeddings=True`. Neither can I specify the distance metric that I want to use in the `similarity_search` method irrespective of what vector store I am using. So it seems to me I can only create unnormalized embeddings with huggingface models and only use L2 distance as the similarity metric by default. Whereas I want to use the cosine similarity metric or have normalized embeddings and then use the dot product/L2 distance.

If I am wrong here can someone point me in the right direction. If not are there any plans to implement this?
````

## Operational trajectory

### Turn 1 — tool call call_0001 (exec)

````json
{
 "command": "cat langchain/embeddings/huggingface.py | head -80; git log --oneline -2"
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
 "stdout": "\"\"\"Wrapper around HuggingFace embedding models.\"\"\"\nfrom typing import Any, Dict, List, Optional\n\nfrom pydantic import BaseModel, Extra, Field\n\nfrom langchain.embeddings.base import Embeddings\n\nDEFAULT_MODEL_NAME = \"sentence-transformers/all-mpnet-base-v2\"\nDEFAULT_INSTRUCT_MODEL = \"hkunlp/instructor-large\"\nDEFAULT_EMBED_INSTRUCTION = \"Represent the document for retrieval: \"\nDEFAULT_QUERY_INSTRUCTION = (\n    \"Represent the question for retrieving supporting documents: \"\n)\n\n\nclass HuggingFaceEmbeddings(BaseModel, Embeddings):\n    \"\"\"Wrapper around sentence_transformers embedding models.\n\n    To use, you should have the ``sentence_transformers`` python package installed.\n\n    Example:\n        .. code-block:: python\n\n            from langchain.embeddings import HuggingFaceEmbeddings\n\n            model_name = \"sentence-transformers/all-mpnet-base-v2\"\n            model_kwargs = {'device': 'cpu'}\n            hf = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)\n    \"\"\"\n\n    client: Any  #: :meta private:\n    model_name: str = DEFAULT_MODEL_NAME\n    \"\"\"Model name to use.\"\"\"\n    cache_folder: Optional[str] = None\n    \"\"\"Path to store models. \n    Can be also set by SENTENCE_TRANSFORMERS_HOME environment variable.\"\"\"\n    model_kwargs: Dict[str, Any] = Field(default_factory=dict)\n    \"\"\"Key word arguments to pass to the model.\"\"\"\n    encode_kwargs: Dict[str, Any] = Field(default_factory=dict)\n    \"\"\"Key word arguments to pass when calling the `encode` method of the model.\"\"\"\n\n    def __init__(self, **kwargs: Any):\n        \"\"\"Initialize the sentence_transformer.\"\"\"\n        super().__init__(**kwargs)\n        try:\n            import sentence_transformers\n\n        except ImportError as exc:\n            raise ImportError(\n                \"Could not import sentence_transformers python package. \"\n                \"Please install it with `pip install sentence_transformers`.\"\n            ) from exc\n\n        self.client = sentence_transformers.SentenceTransformer(\n            self.model_name, cache_folder=self.cache_folder, **self.model_kwargs\n        )\n\n    class Config:\n        \"\"\"Configuration for this pydantic object.\"\"\"\n\n        extra = Extra.forbid\n\n    def embed_documents(self, texts: List[str]) -> List[List[float]]:\n        \"\"\"Compute doc embeddings using a HuggingFace transformer model.\n\n        Args:\n            texts: The list of texts to embed.\n\n        Returns:\n            List of embeddings, one for each text.\n        \"\"\"\n        texts = list(map(lambda x: x.replace(\"\\n\", \" \"), texts))\n        embeddings = self.client.encode(texts, **self.encode_kwargs)\n        return embeddings.tolist()\n\n    def embed_query(self, text: str) -> List[float]:\n        \"\"\"Compute query embeddings using a HuggingFace transformer model.\n\n        Args:\n            text: The text to embed.\n64b4165c bump 185 (#5442)\n9d658aaa Add more code splitters (go, rst, js, java, cpp, scala, ruby, php, swift, rust) (#5171)\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 139,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "langchain/embeddings/huggingface.py"
  ],
  "command_sha256": [
   "0f46ddbff7f4e6cc7f0978f5982b3cb86d4d078e65f0a3e73d043ca6fca86eda"
  ]
 }
}
````

### Turn 2 — thinking

````text
Since encode_kwargs is already present, I'm wondering if the issue lies elsewhere—perhaps embed_query doesn't actually use those kwargs, or maybe it's related to instruct embeddings or the vector store's distance strategy like FAISS. I should check further.
````

### Turn 2 — tool call call_0002 (exec)

````json
{
 "command": "sed -n 80,200p langchain/embeddings/huggingface.py; grep -rn \"distance_strategy\\|DistanceStrategy\\|normalize_L2\" langchain/vectorstores | head -30"
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
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "langchain/embeddings/huggingface.py",
   "langchain/vectorstores"
  ],
  "command_sha256": [
   "61b4c567737623ddfd919715f7aca90776edf882b77fdd861dcf509d7d74d502"
  ]
 },
 "_agent_context_projection": {
  "schema_version": "agent.exec_tool_result_receipt_preview.v1",
  "content_status": "partial_preview",
  "context_view_limit_bytes": 16384,
  "receipt": {
   "result_id": "tr_7db0168dbeef416fb90e657410001491",
   "total_bytes": 5427,
   "total_lines": 103,
   "omitted_bytes": 0,
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "artifact": {
   "result_id": "tr_7db0168dbeef416fb90e657410001491",
   "page_tool": "read_tool_result_page",
   "page_bytes": 65536
  },
  "content_preview": "{\"tool_outcome\":{\"schema_version\":1,\"tool_name\":\"exec\",\"status\":\"success\",\"exit_code\":0,\"retr\n...[agent-cli tool_result context preview: tool_result_delivery_status=delivered; content_status=partial_preview_not_failure; compatibility_marker=tool_result truncated; omitted_bytes=5062; total_bytes=5248; context_view_limit=512 bytes; context_view_strategy=head_tail_compact; guidance=preview_not_failure_outcome_neutral]...\nres\"],\"command_sha256\":[\"61b4c567737623ddfd919715f7aca90776edf882b77fdd861dcf509d7d74d502\"]}}",
  "stdout": {
   "total_bytes": 4566,
   "total_lines": 103,
   "omitted_bytes": 0,
   "preview": "            text: The text to embed.\n\n        Returns:\n            Embeddings for the text.\n        \"\"\"\n        text = text.replace(\"\\n\", \" \")\n        embedding = self.client.encode(text, **self.encode_kwargs)\n        return embedding.tolist()\n\n\nclass HuggingFaceInstructEmbeddings(BaseModel, Embeddings):\n    \"\"\"Wrapper around sentence_transformers embedding models.\n\n    To use, you should have the ``sentence_transformers``\n    and ``InstructorEmbedding`` python packages installed.\n\n    Example:\n        .. code-block:: python\n\n            from langchain.embeddings import HuggingFaceInstructEmbeddings\n\n            model_name = \"hkunlp/instructor-large\"\n            model_kwargs = {'device': 'cpu'}\n            hf = HuggingFaceInstructEmbeddings(\n                model_name=model_name, model_kwargs=model_kwargs\n            )\n    \"\"\"\n\n    client: Any  #: :meta private:\n    model_name: str = DEFAULT_INSTRUCT_MODEL\n    \"\"\"Model name to use.\"\"\"\n    cache_folder: Optional[str] = None\n    \"\"\"Path to store models. \n    Can be also set by SENTENCE_TRANSFORMERS_HOME environment variable.\"\"\"\n    model_kwargs: Dict[str, Any] = Field(default_factory=dict)\n    \"\"\"Key word arguments to pass to the model.\"\"\"\n    embed_instruction: str = DEFAULT_EMBED_INSTRUCTION\n    \"\"\"Instruction to use for embedding documents.\"\"\"\n    query_instruction: str = DEFAULT_QUERY_INSTRUCTION\n    \"\"\"Instruction to use for embedding query.\"\"\"\n\n    def __init__(self, **kwargs: Any):\n        \"\"\"Initialize the sentence_transformer.\"\"\"\n        super().__init__(**kwargs)\n        try:\n            from InstructorEmbedding import INSTRUCTOR\n\n            self.client = INSTRUCTOR(\n                self.model_name, cache_folder=self.cache_folder, **self.model_kwargs\n            )\n        except ImportError as e:\n            raise ValueError(\"Dependencies for InstructorEmbedding not found.\") from e\n\n    class Config:\n        \"\"\"Configuration for this pydantic object.\"\"\"\n\n        extra = Extra.forbid\n\n    def embed_documents(self, texts: List[str]) -> List[List[float]]:\n        \"\"\"Compute doc embeddings using a HuggingFace instruct model.\n\n        Args:\n            texts: The list of texts to embed.\n\n        Returns:\n            List of embeddings, one for each text.\n        \"\"\"\n        instruction_pairs = [[self.embed_instruction, text] for text in texts]\n        embeddings = self.client.encode(instruction_pairs)\n        return embeddings.tolist()\n\n    def embed_query(self, text: str) -> List[float]:\n        \"\"\"Compute query embeddings using a HuggingFace instruct model.\n\n        Args:\n            text: The text to embed.\n\n        Returns:\n            Embeddings for the text.\n        \"\"\"\n        instruction_pair = [self.query_instruction, text]\n        embedding = self.client.encode([instruction_pair])[0]\n        return embedding.tolist()\nlangchain/vectorstores/pgvector.py:95:class DistanceStrategy(str, enum.Enum):\nlangchain/vectorstores/pgvector.py:101:DEFAULT_DISTANCE_STRATEGY = DistanceStrategy.EUCLIDEAN\nlangchain/vectorstores/pgvector.py:114:    - `distance_strategy` is the distance strategy to use. (default: EUCLIDEAN)\nlangchain/vectorstores/pgvector.py:128:        distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,\nlangchain/vectorstores/pgvector.py:136:        self.distance_strategy = distance_strategy\nlangchain/vectorstores/pgvector.py:319:                    self.distance_strategy(embedding).label(\"distance\"),  # type: ignore\nlangchain/vectorstores/pgvector.py:372:        distance_strategy: DistanceStrategy = DistanceStrategy.COSINE,\nlangchain/vectorstores/pgvector.py:390:            distance_strategy=distance_strategy,\nlangchain/vectorstores/pgvector.py:420:        distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,\nlangchain/vectorstores/pgvector.py:442:            distance_strategy=distance_strategy,\nlangchain/vectorstores/faiss.py:84:        normalize_L2: bool = False,\nlangchain/vectorstores/faiss.py:92:        self._normalize_L2 = normalize_L2\nlangchain/vectorstores/faiss.py:117:        if self._normalize_L2:\nlangchain/vectorstores/faiss.py:118:            faiss.normalize_L2(vector)\nlangchain/vectorstores/faiss.py:196:        if self._normalize_L2:\nlangchain/vectorstores/faiss.py:197:            faiss.normalize_L2(vector)\nlangchain/vectorstores/faiss.py:373:        normalize_L2: bool = False,\nlangchain/vectorstores/faiss.py:379:        if normalize_L2:\nlangchain/vectorstores/faiss.py:380:            faiss.normalize_L2(vector)\nlangchain/vectorstores/faiss.py:395:            normalize_L2=normalize_L2,\n"
  }
 }
}
````

### Turn 3 — thinking

````text
I notice the Instruct embeddings class is missing encode_kwargs — probably a later fix added that parameter to HuggingFaceInstructEmbeddings, so I should check the tests to confirm.
````

### Turn 3 — tool call call_0003 (exec)

````json
{
 "command": "grep -rn \"encode_kwargs\" tests langchain | head"
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
 "stdout": "tests/integration_tests/embeddings/test_huggingface.py:21:    embedding = HuggingFaceEmbeddings(encode_kwargs={\"batch_size\": 16})\nlangchain/embeddings/huggingface.py:39:    encode_kwargs: Dict[str, Any] = Field(default_factory=dict)\nlangchain/embeddings/huggingface.py:73:        embeddings = self.client.encode(texts, **self.encode_kwargs)\nlangchain/embeddings/huggingface.py:86:        embedding = self.client.encode(text, **self.encode_kwargs)\n",
 "device_targets": [],
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [
   "langchain",
   "tests"
  ],
  "command_sha256": [
   "1e9b61b59fb2b0e182cb8415cd49ecbd3dd7568b21accdab9cb1444a685400f1"
  ]
 },
 "duration_ms": 120
}
````

### Turn 4 — assistant text

Add `encode_kwargs` to `HuggingFaceInstructEmbeddings` as well.

### Turn 4 — tool call call_0004 (exec)

````json
{
 "command": "python - <<'EOF'\np='langchain/embeddings/huggingface.py'\ns=open(p).read()\ns=s.replace('''    \"\"\"Key word arguments to pass to the model.\"\"\"\n    embed_instruction''','''    \"\"\"Key word arguments to pass to the model.\"\"\"\n    encode_kwargs: Dict[str, Any] = Field(default_factory=dict)\n    \"\"\"Key word arguments to pass when calling the `encode` method of the model.\"\"\"\n    embed_instruction''',1)\ns=s.replace(\"self.client.encode(instruction_pairs)\",\"self.client.encode(instruction_pairs, **self.encode_kwargs)\")\ns=s.replace(\"self.client.encode([instruction_pair])[0]\",\"self.client.encode([instruction_pair], **self.encode_kwargs)[0]\")\nopen(p,'w').write(s)\nEOF\ngit diff --stat; python -c \"\nfrom langchain.embeddings.huggingface import HuggingFaceInstructEmbeddings as H\nprint(H.__fields__['encode_kwargs'])\""
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
 "stdout": " .dockerignore                       |  6 ----\n Dockerfile                          | 61 +++++++++++++------------------------\n langchain/embeddings/huggingface.py |  6 ++--\n 3 files changed, 26 insertions(+), 47 deletions(-)\nname='encode_kwargs' type=Mapping[str, Any] required=False default_factory='<function dict>'\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 2996,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [],
  "command_sha256": [
   "175ee9acf89e3854259f85e685237f5442d0c8615fea3389c4401478329aacba"
  ]
 }
}
````

### Turn 5 — thinking

````text
Those Dockerfile changes were already there, not something I made—I should check the diff of my own file instead.
````

### Turn 5 — tool call call_0005 (exec)

````json
{
 "command": "git diff langchain/"
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
 "stdout": "diff --git a/langchain/embeddings/huggingface.py b/langchain/embeddings/huggingface.py\nindex 04e0c76e..460ae141 100644\n--- a/langchain/embeddings/huggingface.py\n+++ b/langchain/embeddings/huggingface.py\n@@ -113,6 +113,8 @@ class HuggingFaceInstructEmbeddings(BaseModel, Embeddings):\n     Can be also set by SENTENCE_TRANSFORMERS_HOME environment variable.\"\"\"\n     model_kwargs: Dict[str, Any] = Field(default_factory=dict)\n     \"\"\"Key word arguments to pass to the model.\"\"\"\n+    encode_kwargs: Dict[str, Any] = Field(default_factory=dict)\n+    \"\"\"Key word arguments to pass when calling the `encode` method of the model.\"\"\"\n     embed_instruction: str = DEFAULT_EMBED_INSTRUCTION\n     \"\"\"Instruction to use for embedding documents.\"\"\"\n     query_instruction: str = DEFAULT_QUERY_INSTRUCTION\n@@ -145,7 +147,7 @@ class HuggingFaceInstructEmbeddings(BaseModel, Embeddings):\n             List of embeddings, one for each text.\n         \"\"\"\n         instruction_pairs = [[self.embed_instruction, text] for text in texts]\n-        embeddings = self.client.encode(instruction_pairs)\n+        embeddings = self.client.encode(instruction_pairs, **self.encode_kwargs)\n         return embeddings.tolist()\n \n     def embed_query(self, text: str) -> List[float]:\n@@ -158,5 +160,5 @@ class HuggingFaceInstructEmbeddings(BaseModel, Embeddings):\n             Embeddings for the text.\n         \"\"\"\n         instruction_pair = [self.query_instruction, text]\n-        embedding = self.client.encode([instruction_pair])[0]\n+        embedding = self.client.encode([instruction_pair], **self.encode_kwargs)[0]\n         return embedding.tolist()\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 266,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [],
  "command_sha256": [
   "64d922bc7284b825086773920a48c8ac76f35e5505e02c5938ccdefe7e026fd3"
  ]
 }
}
````

### Turn 6 — thinking

````text
I should quickly verify this with a mock test, since I can't construct it directly without InstructorEmbedding — using construct() with a mocked client should work for a fast check.
````

### Turn 6 — tool call call_0006 (exec)

````json
{
 "command": "python -c \"\nfrom unittest.mock import MagicMock\nimport numpy as np\nfrom langchain.embeddings.huggingface import HuggingFaceInstructEmbeddings as H\nh=H.construct(encode_kwargs={'normalize_embeddings':True}, embed_instruction='e', query_instruction='q')\nh.client=MagicMock(); h.client.encode.return_value=np.array([[1.0,0.0]])\nh.embed_documents(['a']); h.embed_query('b'); print(h.client.encode.call_args_list)\""
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
 "stdout": "[call([['e', 'a']], normalize_embeddings=True),\n call([['q', 'b']], normalize_embeddings=True)]\n",
 "device_targets": [],
 "approval": {
  "requested": true,
  "result": "approved"
 },
 "duration_ms": 4247,
 "completion_evidence": {
  "schema_version": "agent.completion_evidence.tool_result.v1",
  "mutations": [],
  "reads": [],
  "command_sha256": [
   "ada2bcbf86cba239d8b7db7cb553201de6d9cf332e4999f2a7a4705ae905a9e4"
  ]
 }
}
````

### Turn 7 — thinking

````text
I should also check the FAISS distance metric since normalize_L2 already handles that similarity requirement, so this looks like a minimal fix.

I have everything needed to answer, so I'll wrap up with a concise final response.
````

### Turn 7 — assistant text

`HuggingFaceInstructEmbeddings` now takes `encode_kwargs` and passes them to the model's `encode` call, so you can set `normalize_embeddings=True` on it.

You were partly right about `HuggingFaceEmbeddings`. It already had an `encode_kwargs` field that it passes to `encode` for both documents and queries. The instruct version had no such field, so `encode` always ran with its defaults.

What changed, all in `langchain/embeddings/huggingface.py`:
- Added `encode_kwargs: Dict[str, Any] = Field(default_factory=dict)` to `HuggingFaceInstructEmbeddings`.
- `embed_documents` and `embed_query` now pass `**self.encode_kwargs` to `self.client.encode(...)`.

I checked it with a mocked client, because the real Instructor model isn't installed here. Both methods called `encode` with `normalize_embeddings=True`. I didn't run the project's test suite or a real model.

On the distance metric: you can already choose this in some vector stores. FAISS has a `normalize_L2` option, and PGVector has a `distance_strategy` setting (Euclidean or cosine). I didn't change any vector store code.

The worktree also has changes to `.dockerignore` and `Dockerfile` that I didn't make; I left them alone.

### Turn 8 — assistant text

I fixed this by letting `HuggingFaceInstructEmbeddings` pass extra options to the model's `encode` method. `HuggingFaceEmbeddings` already supported this through `encode_kwargs`, so `normalize_embeddings=True` was available there. The instruct variant had no way to pass encode options, so its embeddings could only come out unnormalized.

The change is in `langchain/embeddings/huggingface.py`:
- I added an `encode_kwargs: Dict[str, Any]` field (empty by default) to `HuggingFaceInstructEmbeddings`.
- `embed_documents` and `embed_query` now both pass `**self.encode_kwargs` to `self.client.encode(...)`.

I checked it with a mocked model client, because the real `InstructorEmbedding` package isn't installed here. With `encode_kwargs={'normalize_embeddings': True}`, both document and query embedding passed `normalize_embeddings=True` to `encode`. I didn't run the repo's test suite or a real model.

You can now get normalized embeddings with either class, for example `HuggingFaceEmbeddings(encode_kwargs={'normalize_embeddings': True})`. With normalized vectors, ranking by L2 distance gives the same order as cosine similarity, so the default L2 search works for your case. Some vector stores already let you choose the metric: `FAISS` has `normalize_L2` and `PGVector` has `distance_strategy`. I didn't add a metric setting to `similarity_search` itself.

`Dockerfile` and `.dockerignore` already had uncommitted changes before I started; I left them alone.

## Final answer

I fixed this by letting `HuggingFaceInstructEmbeddings` pass extra options to the model's `encode` method. `HuggingFaceEmbeddings` already supported this through `encode_kwargs`, so `normalize_embeddings=True` was available there. The instruct variant had no way to pass encode options, so its embeddings could only come out unnormalized.

The change is in `langchain/embeddings/huggingface.py`:
- I added an `encode_kwargs: Dict[str, Any]` field (empty by default) to `HuggingFaceInstructEmbeddings`.
- `embed_documents` and `embed_query` now both pass `**self.encode_kwargs` to `self.client.encode(...)`.

I checked it with a mocked model client, because the real `InstructorEmbedding` package isn't installed here. With `encode_kwargs={'normalize_embeddings': True}`, both document and query embedding passed `normalize_embeddings=True` to `encode`. I didn't run the repo's test suite or a real model.

You can now get normalized embeddings with either class, for example `HuggingFaceEmbeddings(encode_kwargs={'normalize_embeddings': True})`. With normalized vectors, ranking by L2 distance gives the same order as cosine similarity, so the default L2 search works for your case. Some vector stores already let you choose the metric: `FAISS` has `normalize_L2` and `PGVector` has `distance_strategy`. I didn't add a metric setting to `similarity_search` itself.

`Dockerfile` and `.dockerignore` already had uncommitted changes before I started; I left them alone.

## Token usage

| turn | input | output | cache_read | cache_write | total |
|---|---|---|---|---|---|
| 1 | 135995 | 2251 | 127810 | 8165 | 138246 |
