def parse_urls(input_text):
    if not input_text:
        return []

    urls = [url.strip() for url in input_text.replace(",", "\n").split("\n") if url.strip()]
    return list(set(urls))
