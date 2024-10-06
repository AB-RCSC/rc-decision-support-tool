from notebook.base.handlers import IPythonHandler

# Define the custom handler to capture and return the user's IP address
class IPHandler(IPythonHandler):
    def get(self):
        # Retrieve user's IP from headers (if behind a reverse proxy) or fallback to remote IP
        user_ip = self.request.headers.get("X-Real-IP", self.request.remote_ip)
        self.write(f"User IP is: {user_ip}")

# Function to load the extension and register the IPHandler
def load_jupyter_server_extension(nb_server_app):
    # Get the web application
    web_app = nb_server_app.web_app
    # Define the host pattern (allowing all hosts)
    host_pattern = '.*$'
    # Define the route for the handler
    route_pattern = '/get-ip'
    # Register the IPHandler at the defined route
    web_app.add_handlers(host_pattern, [(route_pattern, IPHandler)])
