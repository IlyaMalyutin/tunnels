# EXAMPLE:
#
# Tunnels list: tuple of (tunnel_like_ssh, local_port)
# tunnels = [
#     ('ssh -N -p 22 through_ip -L LOCAL_PORT:REMOTE_IP:REMOTE_PORT', 'LOCAL_PORT')
#     ('ssh -N -p 22 10.10.10.10 -L 7676:11.11.11.11:7777', '7676'),  # tunnel1
# ]

# sleep timeout for ping ports
SLEEP = 3  # sec
