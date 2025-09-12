from unittest.mock import Mock, patch

import pytest
from urllib3.response import HTTPResponse

from sedaro.exceptions import SedaroApiException
from sedaro.utils import parse_urllib_response


def test_parse_urllib_response_orjson():
    """Test successful orjson parsing"""
    response = Mock()
    response.data = b'{"key": "value"}'

    result = parse_urllib_response(response)

    assert result == {"key": "value"}


def test_parse_urllib_response_json_fallback():
    """Test json fallback when orjson fails"""
    response = Mock()
    response.data = b'{"foo": "bar"}'

    # Mock orjson.loads to fail, forcing json fallback
    with patch('sedaro.utils.orjson.loads', side_effect=Exception("orjson failed")):
        result = parse_urllib_response(response)

    assert result == {"foo": "bar"}


def test_parse_urllib_response_firewall_html():
    """Test parsing when firewall returns HTML error page"""
    html_content = """<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Access Denied</title>
  </head>
  <body>
    <div>
      <h1>Access Denied</h1>
      <p>Your request was blocked by the security system.</p>
      <p>This is a mock of a firewall-generated HTML error page.</p>
    </div>
  </body>
</html>"""

    # Create actual HTTPResponse with HTML content
    response = HTTPResponse(body=html_content.encode('utf-8'), status=403, preload_content=False)
    response._body = html_content.encode('utf-8')

    # This will fail as expected since the function expects JSON
    with pytest.raises(
        SedaroApiException,
        match="Failed to parse response as JSON"
    ) as e_info:
        parse_urllib_response(response)

        assert html_content in str(e_info.value)
