import sentry_sdk

sentry_sdk.init(
    dsn="https://deb7a6a91a904acfb63bc877d67482c0@o388665.ingest.sentry.io/5225844",
    release="nocode",
    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0,
)

print("starting test application")

try:
	raise NameError('Suspect commit test')
except Exception as e:
	sentry_sdk.capture_exception(e) 
