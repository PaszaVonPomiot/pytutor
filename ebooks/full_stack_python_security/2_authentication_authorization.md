# Authentication and Authorization

## HTTP Session Management

The server assigns a session id and sends it in a cookie:

```http
Set-Cookie: sessionid=<cookie-value>
```

The browser sends cookies back with later requests:

```http
Cookie: sessionid=<cookie-value>; key=value;
```

Session sniffing means stealing a valid session id after login.

## Cookie Attributes

- `Secure`: only sent over HTTPS
- `Domain`: must match the server domain rules
- `Path`: request path must match
- `Max-Age` / `Expires`: persistent cookies
- No `Max-Age`: session cookie
- `HttpOnly`: unavailable to JavaScript
- `SameSite`: controls cross-site sending behavior

### `SameSite`

- `Strict`: only same-site requests
- `Lax`: same-site and some top-level navigation
- `None`: cross-site allowed, must also use `Secure`

```http
Set-Cookie: <cookie-name>=<cookie-value>
Set-Cookie: <cookie-name>=<cookie-value>; Expires=<date>
Set-Cookie: <cookie-name>=<cookie-value>; Max-Age=<number>
Set-Cookie: <cookie-name>=<cookie-value>; Domain=<domain-value>
Set-Cookie: <cookie-name>=<cookie-value>; Path=<path-value>
Set-Cookie: <cookie-name>=<cookie-value>; Secure
Set-Cookie: <cookie-name>=<cookie-value>; HttpOnly
Set-Cookie: <cookie-name>=<cookie-value>; SameSite=Strict
Set-Cookie: <cookie-name>=<cookie-value>; SameSite=Lax
Set-Cookie: <cookie-name>=<cookie-value>; SameSite=None; Secure
Set-Cookie: <cookie-name>=<cookie-value>; Domain=<domain-value>; Secure; HttpOnly
```

Cookies are commonly used for:

- Session management
- Personalization
- Tracking

## Django Sessions

Set cookies manually with `HttpResponse`:

```python
from django.http import HttpResponse

response = HttpResponse()
response.set_cookie(
    "cookie-name",
    "cookie-value",
    secure=True,
    domain="alice.com",
    max_age=42,
)
```

Use `request.session` to manage session data:

```python
request.session["name"] = "Alice"
name = request.session.get("name", "Bob")
request.session["name"] = "Charlie"
del request.session["name"]
```

- `SESSION_SERIALIZER` can be `JSONSerializer` or `PickleSerializer`
- `SESSION_ENGINE` defines storage, for example database-backed sessions
- Django uses `SECRET_KEY` for keyed hashing, not encryption

## User Authentication

- `django-registration` can handle registration workflows
- Django provides built-in class-based views such as `LoginView`
- Require login with:

```python
@login_required
LoginRequiredMixin
```

Test authentication with:

```python
from django.contrib.auth import get_user_model
from django.test import TestCase
```

## Password Management

- Use built-in views such as `PasswordChangeView`
- Use `AUTH_PASSWORD_VALIDATORS` for password rules

### Custom Validator

```python
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


class PassphraseValidator:
    def __init__(self, dictionary_file="/usr/share/dict/words"):
        self.min_words = 4
        with open(dictionary_file) as f:
            self.words = set(word.strip() for word in f)

    def get_help_text(self):
        return _("Your password must contain %s words" % self.min_words)

    def validate(self, password, user=None):
        tokens = password.split(" ")

        if len(tokens) < self.min_words:
            too_short = _("This password needs %s words" % self.min_words)
            raise ValidationError(too_short, code="too_short")

        if not all(token in self.words for token in tokens):
            not_passphrase = _("This password is not a passphrase")
            raise ValidationError(not_passphrase, code="not_passphrase")
```

## Authorization

### Application-Level Authorization

- Django uses the built-in `Permission` model
- Users can have zero or more permissions
- Permissions can be default or custom
- Django creates default CRUD permissions for each model during migrations
- Custom permissions can be added in a model `Meta` class

```python
class AuthenticatedMessage(Model):
    message = CharField(max_length=100)
    mac = CharField(max_length=64)

    class Meta:
        permissions = [
            ("send_authenticatedmessage", "Can send msgs"),
            ("receive_authenticatedmessage", "Can receive msgs"),
        ]
```

## OAuth 2

Placeholder for later notes.
