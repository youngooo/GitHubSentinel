class ReportGenerator:
    def __init__(self, update_retriever):
        self.update_retriever = update_retriever

    def generate_report(self):
        updates = self.update_retriever.fetch_updates()
        return f"Generated report with updates: {updates}"
