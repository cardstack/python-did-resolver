from did_resolver import Resolver


def get_resolver():
    def resolve(did, _1, _2):
        return {
            "didResolutionMetadata": {"contentType": "application/did+ld+json"},
            "didDocument": {
                "@context": "https://w3id.org/did/v1",
                "id": did,
                "verificationMethod": [
                    {
                        "id": "owner",
                        "controller": "1234",
                        "type": "xyz",
                    },
                ],
            },
            "didDocumentMetadata": {},
        }

    return {"cardstack": resolve}


example_did = "did:cardstack:1pWMyKj3qfgbTtdBuaWSGUeN70913f2bde84cb36"
print(Resolver(get_resolver()).resolve(example_did))
