class Formatter:
    def to_uppercase(self, text: str) -> str:
        return text.upper()

    def to_lowercase(self, text: str) -> str:
        return text.lower()

    def to_title_case(self, text: str) -> str:
        return text.title()

    def truncate(self, text: str, max_length: int) -> str:
        if len(text) <= max_length:
            return text
        return text[:max_length] + "..."
