from ural import is_url

class Data:
    def __init__(self, claim):
        self.id = claim.get("id")
        self.themes = "|".join(claim.get("themes"))
        self.tags = "|".join(claim.get("tags"))
        self.datePublished = None
        self.url = None
        self.ratingValue = None
        self.rating_alternateName = None

        if claim.get("claim-review") and claim["claim-review"].get("itemReviewed"):
            self.datePublished = claim["claim-review"]["itemReviewed"].get("datePublished")
            self.url = claim["claim-review"]["itemReviewed"]["appearance"].get("url")

        if claim.get("claim-review") and claim["claim-review"].get("reviewRating"):
            self.ratingValue = claim["claim-review"]["reviewRating"].get("ratingValue")
            self.rating_alternateName = claim["claim-review"]["reviewRating"].get("alternateName")

def navigate_json(data:dict) -> list[dict]:
    rows = []
    for claim in data["data"]:
        data = Data(claim)
        if data.url and is_url(data.url):
            rows.append({"id":data.id, "themes":data.themes, "tags":data.tags, "datePublished":data.datePublished, "url":data.url, "ratingValue":data.ratingValue, "rating_alternateName":data.rating_alternateName})
    return rows