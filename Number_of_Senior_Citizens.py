def countSeniors(self, details: List[str]) -> int:
    return sum(1 if int(passenger[11:13]) > 60 else 0 for passenger in details)