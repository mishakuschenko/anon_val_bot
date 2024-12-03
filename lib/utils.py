class ReadText:
    def get_text(self, path: str) -> str:
        with open(path) as file:
            text = file.read()
            return text 
