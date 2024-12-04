class ReadText:
    def get_text(self, path: str) -> str:
        with open(path) as file:
            text = file.read()
            return text 

mas_of_id = []
def tme_url(id):
    mas_of_id.append(id)
    return "https://t.me/anon_message_ru_bot?start=" + str(id)
