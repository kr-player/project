from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.document_loaders import TextLoader
from langchain.document_loaders import DirectoryLoader
from google.colab import drive

# Google 드라이브를 마운트합니다.
drive.mount('/content/drive')

# 사용할 임베딩과 데이터 파일이 위치한 경로를 설정합니다.
HF = HuggingFaceEmbeddings()
fn_dir = "/content/drive/My Drive/Colab Notebooks/data/데이터 저장 폴더 이름"  # 실제 데이터 폴더 경로로 수정해야 합니다.

# 데이터를 로드합니다.
loader = DirectoryLoader(fn_dir, loader_cls=TextLoader)
documents = loader.load()

# 문서를 텍스트 분할기를 사용하여 1000자 단위로 쪼갭니다.
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
docs = text_splitter.split_documents(documents)

# 문서와 임베딩을 사용하여 Chroma 벡터 저장소를 생성하고 유지합니다.
db = Chroma.from_documents(docs, embedding=HF, persist_directory="HF_index_hf")
db.persist()

# 검색할 내용을 작성합니다.
query = " "

# 내용을 검색합니다.
results = db.similarity_search(query)

# 검색 결과를 표시합니다.
for result in results[:2]:
    print("Document:", result['document'])
    print("Similarity Score:", result['score'])
    print("\n")
