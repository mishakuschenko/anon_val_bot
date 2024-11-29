class ReadText:
    def get_text(self, path: str) -> str:
        try:
            with open(path) as file:
                text = file.read()
                return text 
        except FileNotFoundError:
            return False
