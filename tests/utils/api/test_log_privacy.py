import json
import logging

from utils.api.structured_logging import StructuredFormatter


def test_structured_credentials_are_redacted_without_mutating_input():
    fields = {
        "headers": {"Authorization": "private-fixture"},
        "items": [{"refresh_token": "private-fixture", "page": 2}],
    }
    record = logging.LogRecord("test", logging.INFO, "", 1, "Request", (), None)
    record.extra_fields = fields
    rendered = StructuredFormatter().format(record)
    assert "private-fixture" not in rendered
    assert json.loads(rendered)["items"][0]["page"] == 2
    assert fields["headers"]["Authorization"] == "private-fixture"
