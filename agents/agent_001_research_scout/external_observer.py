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

        container = item.get(
            "container-title",
            []
        )

        candidates.append({
            "title": title,
            "authors": authors,
            "year": year,
            "doi": item.get("DOI"),
            "type": item.get("type"),
            "journal": (
                container[0]
                if container
                else None
            ),
            "url": item.get("URL"),
            "source": "Crossref"
        })

    return candidates
