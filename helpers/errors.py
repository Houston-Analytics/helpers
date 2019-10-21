"""
Exceptions

@author Arttu Manninen <arttu@kaktus.cc>
"""

class InvalidArguments(Exception):
    """ Invalid arguments exception """

class SecretsManagerError(Exception):
    """ SecretsManagerException """


class DatabaseError(Exception):
    """ Generic database error """

class DuplicateError(DatabaseError):
    """ Duplicate error """


class HTTPError(Exception):
    """ HTTP/1.1 Errors """
    status_code = 500


class SuccessResponseException(HTTPError):
    """ HTTP/1.1 200 Success response exceptions """
    status_code = 200

class OKException(SuccessResponseException):
    """ OK """
    status_code = 200

class CreatedException(SuccessResponseException):
    """ Created """
    status_code = 201

class AcceptedException(SuccessResponseException):
    """ Accepted """
    status_code = 202

class NonAuthoritativeInformationException(SuccessResponseException):
    """ Non-Authoritative Information """
    status_code = 203

class NoContentException(SuccessResponseException):
    """ No Content """
    status_code = 204

class ResetContentException(SuccessResponseException):
    """ Reset Content """
    status_code = 205

class PartialContentException(SuccessResponseException):
    """ Partial Content """
    status_code = 206


class RedirectionException(HTTPError):
    """ HTTP/1.1 300 Redirection exceptions """
    status_code = 300

class MultipleChoicesException(RedirectionException):
    """ Multiple Choices """
    status_code = 300

class MovedPermanentlyException(RedirectionException):
    """ Moved Permanently """
    status_code = 301

class FoundException(RedirectionException):
    """ Found """
    status_code = 302

class SeeOtherException(RedirectionException):
    """ See Other """
    status_code = 303

class NotModifiedException(RedirectionException):
    """ Not Modified """
    status_code = 304

class TemporaryRedirectException(RedirectionException):
    """ Temporary Redirect """
    status_code = 307

class PermanentRedirectException(RedirectionException):
    """ Permanent Redirect """
    status_code = 308


class ClientError(HTTPError):
    """ HTTP/1.1 400 Client errors """
    status_code = 400

class BadRequestError(ClientError):
    """ Bad Request """
    status_code = 400

class UnauthorizedError(ClientError):
    """ Unauthorized """
    status_code = 401

class PaymentRequiredError(ClientError):
    """ Payment Required """
    status_code = 402

class ForbiddenError(ClientError):
    """ Forbidden """
    status_code = 403

class NotFoundError(ClientError):
    """ Not Found """
    status_code = 404

class MethodNotAllowedError(ClientError):
    """ Method Not Allowed """
    status_code = 405

class NotAcceptableError(ClientError):
    """ Not Acceptable """
    status_code = 406

class ProxyAuthenticationRequiredError(ClientError):
    """ Proxy Authentication Required """
    status_code = 407

class RequestTimeoutError(ClientError):
    """ Request Timeout """
    status_code = 408

class ConflictError(ClientError):
    """ Conflict """
    status_code = 409

class GoneError(ClientError):
    """ Gone """
    status_code = 410

class LengthRequiredError(ClientError):
    """ Length Required """
    status_code = 411

class PreconditionFailedError(ClientError):
    """ Precondition Failed """
    status_code = 412

class PayloadTooLargeError(ClientError):
    """ Payload Too Large """
    status_code = 413

class URITooLongError(ClientError):
    """ URI Too Long """
    status_code = 414

class UnsupportedMediaTypeError(ClientError):
    """ Unsupported Media Type """
    status_code = 415

class RangeNotSatisfiableError(ClientError):
    """ Range Not Satisfiable """
    status_code = 416

class ExpectationFailedError(ClientError):
    """ Expectation Failed """
    status_code = 417

class UnprocessableEntityError(ClientError):
    """ Unprocessable Entity """
    status_code = 422

class TooEarlyError(ClientError):
    """ Too Early """
    status_code = 425

class UpgradeRequiredError(ClientError):
    """ Upgrade Required """
    status_code = 426

class PreconditionRequiredError(ClientError):
    """ Precondition Required """
    status_code = 428

class TooManyRequestsError(ClientError):
    """ Too Many Requests """
    status_code = 429

class RequestHeaderFieldsTooLargeError(ClientError):
    """ Request Header Fields Too Large """
    status_code = 431

class UnavailableForLegalReasonsError(ClientError):
    """ Unavailable For Legal Reasons """
    status_code = 451


class ServerError(HTTPError):
    """ HTTP/1.1 500 Server errors """
    status_code = 500

class InternalServerError(ServerError):
    """ Internal Server Error """
    status_code = 500

class ServerInitialized(InternalServerError):
    """ ServerInitialized exception """

class ImplementationMissing(ServerError):
    """ Not Implemented """
    status_code = 501

class BadGatewayError(ServerError):
    """ Bad Gateway """
    status_code = 502

class ServiceUnavailableError(ServerError):
    """ Service Unavailable """
    status_code = 503

class GatewayTimeoutError(ServerError):
    """ Gateway Timeout """
    status_code = 504

class HTTPVersionNotSupportedError(ServerError):
    """ HTTP Version Not Supported """
    status_code = 505

class NetworkAuthenticationRequiredError(ServerError):
    """ Network Authentication Required """
    status_code = 511
