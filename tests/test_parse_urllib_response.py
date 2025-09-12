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


def test_parse_urllib_response_empty_response():
    """Test parsing when response is empty"""
    response = HTTPResponse(body=b'', status=200, preload_content=False)
    response._body = b''

    with pytest.raises(SedaroApiException, match="Empty response cannot be parsed as JSON"):
        parse_urllib_response(response)


def test_parse_urllib_response_plain_text():
    """Test parsing when response is plain text"""
    text_content = b'Internal Server Error'
    response = HTTPResponse(body=text_content, status=500, preload_content=False)
    response._body = text_content

    with pytest.raises(SedaroApiException, match="Failed to parse response as JSON") as e_info:
        parse_urllib_response(response)

    assert 'Internal Server Error' in str(e_info.value)


def test_parse_urllib_response_binary_data():
    """Test parsing when response is binary data"""
    binary_content = b'\x00\x01\x02\x03\xff\xfe'
    response = HTTPResponse(body=binary_content, status=500, preload_content=False)
    response._body = binary_content

    with pytest.raises(SedaroApiException, match="Binary data cannot be parsed as JSON"):
        parse_urllib_response(response)


def test_parse_urllib_response_html():
    """Test parsing when server returns HTML error page"""
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
      <p>This is a mock of an HTML error page.</p>
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

    assert "HTML content detected. This may indicate a proxy, firewall, or server error page." in str(e_info.value)
    assert html_content in str(e_info.value)


def test_parse_urllib_response_long_html():
    """Test HTML truncation for very long HTML content"""
    # Generate HTML longer than 1000 characters
    long_content = "x" * 500  # 500 chars of content
    html_content = f"""<!DOCTYPE html>
<html>
<head><title>Long Page</title></head>
<body>
<div>{''.join(f'<p>Paragraph {i}: {long_content}</p>' for i in range(10))}</div>
</body>
</html>"""

    response = HTTPResponse(body=html_content.encode('utf-8'), status=403, preload_content=False)
    response._body = html_content.encode('utf-8')

    with pytest.raises(SedaroApiException, match="Failed to parse response as JSON") as e_info:
        parse_urllib_response(response)

    error_message = str(e_info.value)
    assert "..." in error_message
    assert "(long html truncated)" in error_message
