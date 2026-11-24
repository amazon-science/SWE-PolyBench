# Instance: langchain-ai__langchain-5450

- Final resolved (evaluator, logs/langchain-ai__langchain-5450_result.json): True
- Run state: DONE
- One attempt. Duration 111.9 s, turns 9, actor cost $0.2128436, container commands 1
- Actor: Claude Code 2.1.280, model claude-opus-5-5, effort high; tools Bash, Read, Write, Edit, Glob, Grep; no MCP; no hooks; network: model API only

## Instruction (the only task input; problem statement as given by the dataset)

```
<uploaded_files>
/work/langchain-ai__langchain-5450/repo
</uploaded_files>
I've uploaded a Python code repository in the directory /work/langchain-ai__langchain-5450/repo. Consider the following issue description:

<issue_description>
Embeddings normalization and similarity metric
I am new to using Langchain and attempting to make it work with a locally running LLM (Alpaca) and Embeddings model (Sentence Transformer). When configuring the sentence transformer model with `HuggingFaceEmbeddings` no arguments can be passed to the encode method of the model, specifically `normalize_embeddings=True`. Neither can I specify the distance metric that I want to use in the `similarity_search` method irrespective of what vector store I am using. So it seems to me I can only create unnormalized embeddings with huggingface models and only use L2 distance as the similarity metric by default. Whereas I want to use the cosine similarity metric or have normalized embeddings and then use the dot product/L2 distance.

If I am wrong here can someone point me in the right direction. If not are there any plans to implement this?

</issue_description>

Can you help me implement the necessary changes to the repository so that the requirements specified in the <issue_description> are met?
I've already taken care of all changes to any of the test files described in the <issue_description>. This means you DON'T have to modify the testing logic or any of the tests in any way!
Your task is to make the minimal changes to non-test files in the /work/langchain-ai__langchain-5450/repo directory to ensure the <issue_description> is satisfied.

The repository's environment (its toolchain, build tools and installed dependencies) lives in a Linux container, not on this machine. Run every command that needs that environment through /work/langchain-ai__langchain-5450/bin/envrun, which executes one shell command inside the container with the working directory at the repository root (the same files, mounted there at /testbed). Example:
  /work/langchain-ai__langchain-5450/bin/envrun 'git status --short && ls'
Edits you make under /work/langchain-ai__langchain-5450/repo are visible inside the container immediately. The container has no network access, so use the build tools' offline modes where they have one.

Follow these steps to resolve the issue:
1. As a first step, explore the repo to find and read the code relevant to the <issue_description>.
2. Create a script or a small test to reproduce the error and execute it with envrun, to confirm the error.
3. Edit the source code of the repo to resolve the issue.
4. Rerun your reproduction and confirm that the error is fixed.
5. Think about edge cases and make sure your fix handles them as well; run the existing tests closest to the code you changed.
6. Delete any scripts or files you created only for reproduction or checking, so that only the fix remains in the repository.

```

## Trajectory

_session start: model claude-opus-5-5, tools ['Bash', 'Edit', 'Glob', 'Grep', 'Read', 'Write'], MCP servers []_

**tool call: Bash**

```bash
cat langchain/embeddings/huggingface.py && ls tests/*/embeddings/ && grep -rn "encode_kwargs\|normalize" tests/ | head
```

tool result:

```
"""Wrapper around HuggingFace embedding models."""
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Extra, Field

from langchain.embeddings.base import Embeddings

DEFAULT_MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
DEFAULT_INSTRUCT_MODEL = "hkunlp/instructor-large"
DEFAULT_EMBED_INSTRUCTION = "Represent the document for retrieval: "
DEFAULT_QUERY_INSTRUCTION = (
    "Represent the question for retrieving supporting documents: "
)


class HuggingFaceEmbeddings(BaseModel, Embeddings):
    """Wrapper around sentence_transformers embedding models.

    To use, you should have the ``sentence_transformers`` python package installed.

    Example:
        .. code-block:: python

            from langchain.embeddings import HuggingFaceEmbeddings

            model_name = "sentence-transformers/all-mpnet-base-v2"
            model_kwargs = {'device': 'cpu'}
            hf = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)
    """

    client: Any  #: :meta private:
    model_name: str = DEFAULT_MODEL_NAME
    """Model name to use."""
    cache_folder: Optional[str] = None
    """Path to store models. 
    Can be also set by SENTENCE_TRANSFORMERS_HOME environment variable."""
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Key word arguments to pass to the model."""
    encode_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Key word arguments to pass when calling the `encode` method of the model."""

    def __init__(self, **kwargs: Any):
        """Initialize the sentence_transformer."""
        super().__init__(**kwargs)
        try:
            import sentence_transformers

        except ImportError as exc:
            raise ImportError(
                "Could not import sentence_transformers python package. "
                "Please install it with `pip install sentence_transformers`."
            ) from exc

        self.client = sentence_transformers.SentenceTransformer(
            self.model_name, cache_folder=self.cache_folder, **self.model_kwargs
        )

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Compute doc embeddings using a HuggingFace transformer model.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        texts = list(map(lambda x: x.replace("\n", " "), texts))
        embeddings = self.client.encode(texts, **self.encode_kwargs)
        return embeddings.tolist()

    def embed_query(self, text: str) -> List[float]:
        """Compute query embeddings using a HuggingFace transformer model.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        text = text.replace("\n", " ")
        embedding = self.client.encode(text, **self.encode_kwargs)
        return embedding.tolist()


class HuggingFaceInstructEmbeddings(BaseModel, Embeddings):
    """Wrapper around sentence_transformers embedding models.

    To use, you should have the ``sentence_transformers``
    and ``InstructorEmbedding`` python packages installed.

    Example:
        .. code-block:: python

            from langchain.embeddings import HuggingFaceInstructEmbeddings

            model_name = "hkunlp/instructor-large"
            model_kwargs = {'device': 'cpu'}
            hf = HuggingFaceInstructEmbeddings(
                model_name=model_name, model_kwargs=model_kwargs
            )
    """

    client: Any  #: :meta private:
    model_name: str = DEFAULT_INSTRUCT_MODEL
    """Model name to use."""
    cache_folder: Optional[str] = None
    """Path to store models. 
    Can be also set by SENTENCE_TRANSFORMERS_HOME environment variable."""
    model_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Key word arguments to pass to the model."""
    embed_instruction: str = DEFAULT_EMBED_INSTRUCTION
    """Instruction to use for embedding documents."""
    query_instruction: str = DEFAULT_QUERY_INSTRUCTION
    """Instruction to use for embedding query."""

    def __init__(self, **kwargs: Any):
        """Initialize the sentence_transformer."""
        super().__init__(**kwargs)
        try:
            from InstructorEmbedding import INSTRUCTOR

            self.client = INSTRUCTOR(
                self.model_name, cache_folder=self.cache_folder, **self.model_kwargs
            )
        except ImportError as e:
            raise ValueError("Dependencies for InstructorEmbedding not found.") from e

    class Config:
        """Configuration for this pydantic object."""

        extra = Extra.forbid

    def embed_documents(self, texts: List[str]) -> List[List[float]]:
        """Compute doc embeddings using a HuggingFace instruct model.

        Args:
            texts: The list of texts to embed.

        Returns:
            List of embeddings, one for each text.
        """
        instruction_pairs = [[self.embed_instruction, text] for text in texts]
        embeddings = self.client.encode(instruction_pairs)
        return embeddings.tolist()

    def embed_query(self, text: str) -> List[float]:
        """Compute query embeddings using a HuggingFace instruct model.

        Args:
            text: The text to embed.

        Returns:
            Embeddings for the text.
        """
        instruction_pair = [self.query_instruction, text]
        embedding = self.client.encode([instruction_pair])[0]
        return embedding.tolist()
__init__.py
test_cohere.py
test_elasticsearch.py
test_google_palm.py
test_huggingface.py
test_huggingface_hub.py
test_jina.py
test_llamacpp.py
test_modelscope_hub.py
test_mosaicml.py
test_openai.py
test_self_hosted.py
test_sentence_transformer.py
test_tensorflow_hub.py
test_vertexai.py
tests/unit_tests/retrievers/test_time_weighted_retriever.py:95:        """Return docs an
[... 1018 more characters not shown]
```

**tool call: Bash**

```bash
cat tests/integration_tests/embeddings/test_huggingface.py
```

tool result:

```
"""Test huggingface embeddings."""

from langchain.embeddings.huggingface import (
    HuggingFaceEmbeddings,
    HuggingFaceInstructEmbeddings,
)


def test_huggingface_embedding_documents() -> None:
    """Test huggingface embeddings."""
    documents = ["foo bar"]
    embedding = HuggingFaceEmbeddings()
    output = embedding.embed_documents(documents)
    assert len(output) == 1
    assert len(output[0]) == 768


def test_huggingface_embedding_query() -> None:
    """Test huggingface embeddings."""
    document = "foo bar"
    embedding = HuggingFaceEmbeddings(encode_kwargs={"batch_size": 16})
    output = embedding.embed_query(document)
    assert len(output) == 768


def test_huggingface_instructor_embedding_documents() -> None:
    """Test huggingface embeddings."""
    documents = ["foo bar"]
    embedding = HuggingFaceInstructEmbeddings()
    output = embedding.embed_documents(documents)
    assert len(output) == 1
    assert len(output[0]) == 768


def test_huggingface_instructor_embedding_query() -> None:
    """Test huggingface embeddings."""
    query = "foo bar"
    embedding = HuggingFaceInstructEmbeddings()
    output = embedding.embed_query(query)
    assert len(output) == 768
```

**tool call: Bash**

```bash
git log --oneline | head -3; git status; grep -rn "distance_strategy\|DistanceStrategy\|encode_kwargs" --include=*.py . | grep -v "^./langchain/embeddings/huggingface.py" | head -30
```

tool result:

```
64b4165c bump 185 (#5442)
9d658aaa Add more code splitters (go, rst, js, java, cpp, scala, ruby, php, swift, rust) (#5171)
a61b7f7e adding MongoDBAtlasVectorSearch (#5338)
On branch main
Changes not staged for commit:
  (use "git add/rm <file>..." to update what will be committed)
  (use "git restore <file>..." to discard changes in working directory)
	deleted:    .dockerignore
	modified:   Dockerfile

no changes added to commit (use "git add" and/or "git commit -a")
(eval):1: no matches found: --include=*.py
```

**tool call: Grep**

```json
{
 "pattern": "distance_strategy|DistanceStrategy|encode_kwargs",
 "output_mode": "content"
}
```

tool result:

```
langchain/embeddings/huggingface.py:39:    encode_kwargs: Dict[str, Any] = Field(default_factory=dict)
langchain/embeddings/huggingface.py:73:        embeddings = self.client.encode(texts, **self.encode_kwargs)
langchain/embeddings/huggingface.py:86:        embedding = self.client.encode(text, **self.encode_kwargs)
langchain/vectorstores/pgvector.py:95:class DistanceStrategy(str, enum.Enum):
langchain/vectorstores/pgvector.py:101:DEFAULT_DISTANCE_STRATEGY = DistanceStrategy.EUCLIDEAN
langchain/vectorstores/pgvector.py:114:    - `distance_strategy` is the distance strategy to use. (default: EUCLIDEAN)
langchain/vectorstores/pgvector.py:128:        distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,
langchain/vectorstores/pgvector.py:136:        self.distance_strategy = distance_strategy
langchain/vectorstores/pgvector.py:319:                    self.distance_strategy(embedding).label("distance"),  # type: ignore
langchain/vectorstores/pgvector.py:372:        distance_strategy: DistanceStrategy = DistanceStrategy.COSINE,
langchain/vectorstores/pgvector.py:390:            distance_strategy=distance_strategy,
langchain/vectorstores/pgvector.py:420:        distance_strategy: DistanceStrategy = DEFAULT_DISTANCE_STRATEGY,
langchain/vectorstores/pgvector.py:442:            distance_strategy=distance_strategy,
tests/integration_tests/embeddings/test_huggingface.py:21:    embedding = HuggingFaceEmbeddings(encode_kwargs={"batch_size": 16})
docs/modules/indexes/vectorstores/examples/pgvector.ipynb:253:    "    distance_strategy=DistanceStrategy.COSINE,\n",
docs/modules/indexes/vectorstores/examples/pgvector.ipynb:277:    "    distance_strategy=DistanceStrategy.COSINE\n",
```

**tool call: Bash**

```bash
grep -n "metadata\|relevance\|cosine" tests/integration_tests/vectorstores/test_chroma.py | head -30; grep -n "def \|collection" langchain/vectorstores/chroma.py | head -60
```

tool result:

```
30:def test_chroma_with_metadatas() -> None:
33:    metadatas = [{"page": str(i)} for i in range(len(texts))]
38:        metadatas=metadatas,
41:    assert output == [Document(page_content="foo", metadata={"page": "0"})]
44:def test_chroma_with_metadatas_with_scores() -> None:
47:    metadatas = [{"page": str(i)} for i in range(len(texts))]
52:        metadatas=metadatas,
55:    assert output == [(Document(page_content="foo", metadata={"page": "0"}), 0.0)]
59:    """Test end to end construction and search with metadata filtering."""
61:    metadatas = [{"first_letter": "{}".format(text[0])} for text in texts]
66:        metadatas=metadatas,
69:    assert output == [Document(page_content="far", metadata={"first_letter": "f"})]
71:    assert output == [Document(page_content="bar", metadata={"first_letter": "b"})]
75:    """Test end to end construction and scored search with metadata filtering."""
77:    metadatas = [{"first_letter": "{}".format(text[0])} for text in texts]
82:        metadatas=metadatas,
88:        (Document(page_content="far", metadata={"first_letter": "f"}), 0.0)
94:        (Document(page_content="bar", metadata={"first_letter": "b"}), 1.0)
137:    output = docsearch.max_marginal_relevance_search("foo", k=1)
149:    output = docsearch.max_marginal_relevance_search_by_vector(embedded_query, k=1)
172:    # Create an instance of Document with initial content and metadata
173:    original_doc = Document(page_content=initial_content, metadata={"page": "0"})
187:    updated_doc = Document(page_content=updated_content, metadata={"page": "0"})
196:    assert output == [Document(page_content=updated_content, metadata={"page": "0"})]
24:def _results_to_docs(results: Any) -> List[Document]:
28:def _results_to_docs_and_scores(results: Any) -> List[Tuple[Document, float]]:
58:    def __init__(
60:        collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
64:        collection_metadata: Optional[Dict] = None,
93:        self._collection = self._client.get_or_create_collection(
94:            name=collection_name,
98:            metadata=collection_metadata,
102:    def __query_collection(
110:        """Query the chroma collection."""
121:                return self._collection.query(
130:                    f"Chroma collection {self._collection.name} "
134:            f"No documents found for Chroma collection {self._collection.name}"
137:    def add_texts(
160:        self._collection.add(
165:    def similarity_search(
185:    def similarity_search_by_vector(
200:        results = self.__query_collection(
205:    def similarity_search_with_score(
224:            results = self.__query_collection(
229:            results = self.__query_collection(
235:    def max_marginal_relevance_search_by_vector(
260:        results = self.__query_collection(
278:    def max_marginal_relevance_search(
313:    def delete_collection(self) -> None:
314:        """Delete the collection."""
315:        self._client.delete_collection(self._collection.name)
317:    def get(self, include: Optional[List[str]] = None) -> Dict[str, Any]:
318:        """Gets the collection.
325:            return self._collection.get(include=include)
327:            return self._collection.get()
329:    def persist(self) -> None:
330:        """Persist the collection.
338:                "creation to persist the collection."
342:    def update_document(self, document_id: str, document: Document) -> None:
343:        """Update a document in the collection.
357:        self._collection.update(
365:    def from_texts(
371:        collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
379:        If a persist_directory is specified, the collection will be persisted there.
383:            texts (List[str]): List of texts to add to the collection.
384:            collection_name (str): Name of the collection to create.
385:            persist_directory (Optional[str]): Directory to persist the collection.
394:        chroma_collection = cls(
395:            collection_name=collection_name,
401:        chroma_collection.add_texts(texts=texts, metadatas=metadatas, ids=ids)
402:        return chroma_collection
405:    def from_documents(
410:        collection_name: str = _LANGCHAIN_DEFAULT_COLLECTION_NAME,
418:        If a persist_directory is specified, the collection will be persisted there.
422:            collection_name (str): Name of the collection to create.
423:            persist_directory (Optional[str]): Directory to persist the collection.
438:            collection_name=collection_name,
```

**tool call: Bash**

```bash
cat langchain/embeddings/sentence_transformer.py; grep -n "encode\|kwargs" langchain/embeddings/self_hosted_hugging_face.py
```

tool result:

```
"""Wrapper around sentence transformer embedding models."""
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

SentenceTransformerEmbeddings = HuggingFaceEmbeddings
18:def _embed_documents(client: Any, *args: Any, **kwargs: Any) -> List[List[float]]:
24:    return client.encode(*args, **kwargs)
89:    load_fn_kwargs: Optional[dict] = None
94:    def __init__(self, **kwargs: Any):
96:        load_fn_kwargs = kwargs.pop("load_fn_kwargs", {})
97:        load_fn_kwargs["model_id"] = load_fn_kwargs.get("model_id", DEFAULT_MODEL_NAME)
98:        load_fn_kwargs["instruct"] = load_fn_kwargs.get("instruct", False)
99:        load_fn_kwargs["device"] = load_fn_kwargs.get("device", 0)
100:        super().__init__(load_fn_kwargs=load_fn_kwargs, **kwargs)
133:    def __init__(self, **kwargs: Any):
135:        load_fn_kwargs = kwargs.pop("load_fn_kwargs", {})
136:        load_fn_kwargs["model_id"] = load_fn_kwargs.get(
139:        load_fn_kwargs["instruct"] = load_fn_kwargs.get("instruct", True)
140:        load_fn_kwargs["device"] = load_fn_kwargs.get("device", 0)
141:        super().__init__(load_fn_kwargs=load_fn_kwargs, **kwargs)
```

**assistant:** `HuggingFaceEmbeddings` already supports `encode_kwargs`. `HuggingFaceInstructEmbeddings` doesn't, so you can't pass `normalize_embeddings=True` to it. I'll add the same option there.

**tool call: Bash**

```bash
python3 - <<'EOF'
p='langchain/embeddings/huggingface.py'
s=open(p).read()
s=s.replace('''    """Key word arguments to pass to the model."""
    embed_instruction: str''','''    """Key word arguments to pass to the model."""
    encode_kwargs: Dict[str, Any] = Field(default_factory=dict)
    """Key word arguments to pass when calling the `encode` method of the model."""
    embed_instruction: str''')
s=s.replace("self.client.encode(instruction_pairs)","self.client.encode(instruction_pairs, **self.encode_kwargs)")
s=s.replace("self.client.encode([instruction_pair])[0]","self.client.encode([instruction_pair], **self.encode_kwargs)[0]")
s=s.replace('''            model_kwargs = {'device': 'cpu'}
            hf = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)''','''            model_kwargs = {'device': 'cpu'}
            encode_kwargs = {'normalize_embeddings': False}
            hf = HuggingFaceEmbeddings(
                model_name=model_name,
                model_kwargs=model_kwargs,
                encode_kwargs=encode_kwargs
            )''')
s=s.replace('''            model_kwargs = {'device': 'cpu'}
            hf = HuggingFaceInstructEmbeddings(
                model_name=model_name, model_kwargs=model_kwargs
            )''','''            model_kwargs = {'device': 'cpu'}
            encode_kwargs = {'normalize_embeddings': True}
            hf = HuggingFaceInstructEmbeddings(
                model_name=model_name,
                model_kwargs=model_kwargs,
                encode_kwargs=encode_kwargs
            )''')
open(p,'w').write(s)
EOF
git diff langchain
```

tool result:

```
diff --git a/langchain/embeddings/huggingface.py b/langchain/embeddings/huggingface.py
index 04e0c76e..4420484f 100644
--- a/langchain/embeddings/huggingface.py
+++ b/langchain/embeddings/huggingface.py
@@ -25,7 +25,12 @@ class HuggingFaceEmbeddings(BaseModel, Embeddings):
 
             model_name = "sentence-transformers/all-mpnet-base-v2"
             model_kwargs = {'device': 'cpu'}
-            hf = HuggingFaceEmbeddings(model_name=model_name, model_kwargs=model_kwargs)
+            encode_kwargs = {'normalize_embeddings': False}
+            hf = HuggingFaceEmbeddings(
+                model_name=model_name,
+                model_kwargs=model_kwargs,
+                encode_kwargs=encode_kwargs
+            )
     """
 
     client: Any  #: :meta private:
@@ -100,8 +105,11 @@ class HuggingFaceInstructEmbeddings(BaseModel, Embeddings):
 
             model_name = "hkunlp/instructor-large"
             model_kwargs = {'device': 'cpu'}
+            encode_kwargs = {'normalize_embeddings': True}
             hf = HuggingFaceInstructEmbeddings(
-                model_name=model_name, model_kwargs=model_kwargs
+                model_name=model_name,
+                model_kwargs=model_kwargs,
+                encode_kwargs=encode_kwargs
             )
     """
 
@@ -113,6 +121,8 @@ class HuggingFaceInstructEmbeddings(BaseModel, Embeddings):
     Can be also set by SENTENCE_TRANSFORMERS_HOME environment variable."""
     model_kwargs: Dict[str, Any] = Field(default_factory=dict)
     """Key word arguments to pass to the model."""
+    encode_kwargs: Dict[str, Any] = Field(default_factory=dict)
+    """Key word arguments to pass when calling the `encode` method of the model."""
     embed_instruction: str = DEFAULT_EMBED_INSTRUCTION
     """Instruction to use for embedding documents."""
     query_instruction: str = DEFAULT_QUERY_INSTRUCTION
@@ -145,7 +155,7 @@ class HuggingFaceInstructEmbeddings(BaseModel, Embeddings):
             List of embeddings, one for each text.
         """
         instruction_pairs = [[self.embed_instruction, text] for text in texts]
-        embeddings = self.client.encode(instruction_pairs)
+        embeddings = self.client.encode(instruction_pairs, **self.encode_kwargs)
         return embeddings.tolist()
 
     def embed_query(self, text: str) -> List[float]:
@@ -158,5 +168,5 @@ class HuggingFaceInstructEmbeddings(BaseModel, Embeddings):
             Embeddings for the text.
         """
         instruction_pair = [self.query_instruction, text]
-        embedding = self.client.encode([instruction_pair])[0]
+        embedding = self.client.encode([instruction_pair], **self.encode_kwargs)[0]
         return embedding.tolist()
```

**assistant:** Now verifying with mocked clients, because the container has no network and can't download models:

**tool call: Bash**

```bash
cat > /tmp/x.py 2>/dev/null; /work/langchain-ai__langchain-5450/bin/envrun 'python - <<EOF
import sys, types, numpy as np
calls=[]
class M:
    def __init__(self,*a,**k): pass
    def encode(self,x,**kw):
        calls.append(kw); return np.zeros((len(x),3)) if isinstance(x,list) else np.zeros(3)
st=types.ModuleType("sentence_transformers"); st.SentenceTransformer=M; sys.modules["sentence_transformers"]=st
ie=types.ModuleType("InstructorEmbedding"); ie.INSTRUCTOR=M; sys.modules["InstructorEmbedding"]=ie
from langchain.embeddings import HuggingFaceEmbeddings, HuggingFaceInstructEmbeddings
for cls in (HuggingFaceEmbeddings, HuggingFaceInstructEmbeddings):
    e=cls(encode_kwargs={"normalize_embeddings":True}); e.embed_documents(["a"]); e.embed_query("a")
    cls().embed_query("a")
print(calls)
EOF
ruff langchain/embeddings/huggingface.py && black --check langchain/embeddings/huggingface.py && mypy langchain/embeddings/huggingface.py 2>&1 | tail -1'
```

tool result:

```
(eval):1: operation not permitted: /tmp/x.py
[{'normalize_embeddings': True}, {'normalize_embeddings': True}, {}, {'normalize_embeddings': True}, {'normalize_embeddings': True}, {}]
All done! ✨ 🍰 ✨
1 file would be left unchanged.
Success: no issues found in 1 source file
```

**assistant:** Both HuggingFace embedding classes now accept `encode_kwargs`, which are passed straight to the model's `encode` call. So `encode_kwargs={"normalize_embeddings": True}` gives you normalized embeddings.

**What was already there:**
- **`HuggingFaceEmbeddings`** (also exported as `SentenceTransformerEmbeddings`) already had `encode_kwargs` and used it in both `embed_documents` and `embed_query`. For this class, the issue was already fixed in the repo.
- **Picking a distance metric** is already possible in some vector stores: `PGVector` takes `distance_strategy` (Euclidean, cosine or inner product), and `Chroma` takes `collection_metadata`, e.g. `{"hnsw:space": "cosine"}`. There's no single option that works for every store.

**What I changed** (only `langchain/embeddings/huggingface.py`):
- **`HuggingFaceInstructEmbeddings`** couldn't take extra `encode` arguments at all; passing `encode_kwargs` raised an error. I added the same `encode_kwargs` field and passed it to `encode` in `embed_documents` and `embed_query`.
- I updated both class docstrings to show how to use `encode_kwargs`.

**Testing:**
- The container has no network access, so it couldn't download real models and I couldn't run the integration tests in `tests/integration_tests/embeddings/test_huggingface.py`.
- Instead I ran a script with stand-in model classes. For both classes, `{"normalize_embeddings": True}` reached `encode` for documents and queries, and nothing extra was passed when `encode_kwargs` was left out.
- `ruff`, `black --check` and `mypy` pass on the changed file.

I didn't add any files to the repo; the check script ran inline. The pre-existing edits to `Dockerfile` and `.dockerignore` are untouched.

_session end: success, turns 9, is_error False_

## Container commands (task container, no network; broker log)

- `rc=0` 77.31 s: python - <<EOF import sys, types, numpy as np calls=[] class M:     def __init__(self,*a,**k): pass     def encode(self,x,**kw):         calls.append(kw); return np.zeros((len(x),3)) if isinstance(x,list) else np.zeros(3) st=types.ModuleType("sentence_transformers"); st.SentenceTransformer=M; sys.modules["sentence_transformers"]=st ie=types.ModuleType("InstructorEmbedding"); ie.INSTRUCTOR=M; sys.modules["InstructorEmbedding"]=ie from langchain.embeddings import HuggingFaceEmbeddings, HuggingFaceInstructEmbeddings for cls in (HuggingFaceEmbeddings, HuggingFaceInstructEmbeddings):     e=cls(enco
