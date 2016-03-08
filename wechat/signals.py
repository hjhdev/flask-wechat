#encoding:utf8

from flask.signals import Namespace

__all__ = ["verify_failed", "verify_received", "verify_successed", 
    "message_error", "message_received", "response_error", "response_sent"]

signals = Namespace()

verify_received = signals.signal("verify_received")
verify_successed = signals.signal("verify_successed")
verify_failed = signals.signal("verify_failed")

message_received = signals.signal("message_received")
message_error = signals.signal("message_error")
response_error = signals.signal("response_error")
response_sent = signals.signal("response_sent")