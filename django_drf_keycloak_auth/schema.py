from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.plumbing import build_bearer_security_scheme_object

from django_drf_keycloak_auth.keycloak_utils import KEYCLOAK_REALM, KEYCLOAK_SERVER_URL


class KeycloakBearerScheme(OpenApiAuthenticationExtension):

    target_class = "django_drf_keycloak_auth.authentication.KeycloakAuthentication"
    name = "KeycloakBearer"

    def get_security_definition(self, auto_schema):
        return build_bearer_security_scheme_object(
            header_name="Authorization",
            token_prefix="Bearer",
        )


class KeycloakOAuth2Scheme(OpenApiAuthenticationExtension):

    target_class = "django_drf_keycloak_auth.authentication.KeycloakAuthentication"
    name = "KeycloakOAuth2"

    def get_security_definition(self, auto_schema):
        return {
            "type": "oauth2",
            "flows": {
                # Use the authorizationCode flow
                "authorizationCode": {
                    "authorizationUrl": f"{KEYCLOAK_SERVER_URL}/auth/realms/{KEYCLOAK_REALM}/protocol/openid-connect/auth",
                    "tokenUrl": f"{KEYCLOAK_SERVER_URL}/auth/realms/{KEYCLOAK_REALM}/protocol/openid-connect/token",
                    "scopes": {
                        "openid": "OpenID connect scope",
                        "profile": "Access user profile",
                        "email": "Access user email",
                    },
                }
            },
        }
