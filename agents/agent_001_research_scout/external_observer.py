import requests


CROSSREF_URL = "https://api.crossref.org/works"


def search_crossref(query, rows=5):
    params = {
        "query.bibliographic": query,
        "rows": rows,
        "select": "DOI,title,author,published,container-title,type,URL"
    }

    headers = {
        "User-Agent": "Wizards-Forge-GRS-001/0.4"
    }

    response = requests.get(
        CROSSREF_URL,
        params=params,
        headers=headers,
        timeout=20
    )

    response.raise_for_status()

    items = response.json()["message"]["items"]

    candidates = []

    for item in items:
        title_list = item.get("title", [])
        title = title_list[0] if title_list else "Untitled"

        authors = []

        for author in item.get("author", []):
            given = author.get("given", "")
            family = author.get("family", "")
            name = f"{given} {family}".strip()

            if name:
                authors.append(name)

        date_parts = (
            item.get("published", {})
            .get("date-parts", [[]])
        )

        year = None

        if date_parts and date_parts[0]:
            year = date_parts[0][0]

        journal_list = item.get(
            "container-title",
            []
        )

        journal = (
            journal_list[0]
            if journal_list
            else None
        )

        doi = item.get("DOI")
        url = item.get("URL")

        author_text = (
            ", ".join(authors)
            if authors
            else "Unknown author"
        )

        citation_parts = [
            author_text,
            f"({year})" if year else None,
            title,
            journal,
            f"DOI: {doi}" if doi else url
        ]

        citation = ". ".join(
            str(part)
            for part in citation_parts
            if part
        )

        candidates.append({
            "title": title,

            "source_type": "scholarly_work",

            "citation": citation,

            "relevance_summary":
                "Candidate scholarly work retrieved "
                "through Crossref in response to the "
                "submitted research mission. Relevance "
                "requires human or model-directed review.",

            "confidence": 0.75,

            "authors": authors,
            "year": year,
            "doi": doi,
            "journal": journal,
            "url": url,

            "observation_source": "Crossref",

            "raw_source_type": item.get("type")
        })

    return candidates
