from src.graph.rag_graph import app

if __name__ == "__main__":
    q = input("Enter your research question: ")
    result = app.invoke({"question": q})
    print("\nANSWER:\n", result["answer"])