# EXAMPLE:
#
# Tunnels list: tuple of (tunnel_like_ssh, local_port)
# tunnels = [
#     ('ssh -N -p 22 through_ip -L LOCAL_PORT:REMOTE_IP:REMOTE_PORT', 'LOCAL_PORT')
#     ('ssh -N -p 22 10.10.10.10 -L 7676:11.11.11.11:7777', '7676'),  # tunnel1
# ]

# sleep timeout for ping ports
SLEEP = 3  # sec

# python-logging
logging_conf = {
    'version': 1,
    'formatters': {
        'detailed': {
            'class': 'logging.Formatter',
            'format': '%(asctime)s - %(levelname)s - %(processName)s - %(message)s'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'DEBUG',
            'formatter': 'detailed'
        },
        'file': {
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': 'logs/tunnels.log',
            'when': 'D',
            'interval': 5,
            'backupCount': 5,
            'formatter': 'detailed'
        }
    },
    'loggers': {
        'tunnels': {
            'level': 'DEBUG',
            'handlers': [
                'console',
                'file'
            ],
            'propagate': True,
        },
    }
}
