import chromadb
import os
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex, StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings

Settings.embed_model = HuggingFaceEmbedding(model_name="BAAI/bge-m3")
Settings.text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=50)
Settings.llm = None

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
WIKI_PATH = os.path.join(BASE_DIR, "wiki_ti")
CHROMA_PATH = os.path.join(BASE_DIR, "chroma_db_wiki_ti_m3")

print("Cargando paginas wiki...")
documents = SimpleDirectoryReader(
    input_dir=WIKI_PATH,
    required_exts=[".md"],
    exclude=["index.md", "log.md"]
).load_data()
print(f"Paginas cargadas: {len(documents)}")

print("Indexando en ChromaDB con BGE-M3...")
chroma_client = chromadb.PersistentClient(path=CHROMA_PATH)

existing = [c.name for c in chroma_client.list_collections()]
if "wiki_ti_m3" in existing:
    chroma_client.delete_collection("wiki_ti_m3")

chroma_collection = chroma_client.get_or_create_collection("wiki_ti_m3")
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
    show_progress=True
)

print(f"Indexacion completada. Chunks de 512 tokens, overlap 50. Base de datos guardada en: {CHROMA_PATH}")