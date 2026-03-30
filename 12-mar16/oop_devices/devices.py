"""
devices.py
──────────
All five concrete device classes that INHERIT from ElectronicDevice.

INHERITANCE:  Phone, Tablet, Laptop, Desktop, Server all extend the
              root class, reusing its attributes and methods, then
              adding their own specialised behaviour.

POLYMORPHISM: Every class overrides connect_to_network() and
              display_info() in its own way — same method name,
              different behaviour depending on the object type.
"""

from electronic_device import ElectronicDevice


# ══════════════════════════════════════════════════════════════════
#  1.  PHONE
# ══════════════════════════════════════════════════════════════════

class Phone(ElectronicDevice):
    """
    A mobile phone — the most portable member of the device family.

    Extra attributes:
      phone_number  — the SIM card number
      is_5g         — whether the phone supports 5G networks
      call_log      — list of past calls (outgoing and incoming)
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os,
                 phone_number, is_5g):
        # Call the parent constructor to set up the shared attributes
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.phone_number = phone_number
        self.is_5g        = is_5g
        self.call_log     = []   # Starts empty — no call history yet

    # ── Polymorphism: Phone's own version of connect_to_network ───────
    def connect_to_network(self):
        network = "5G" if self.is_5g else "4G LTE"
        print(f"  📶  {self.brand} {self.model} connected via {network} cellular.")

    # ── Phone-specific methods ─────────────────────────────────────────
    def make_call(self, number):
        """Dial a number. The phone must be powered on first."""
        if not self.is_powered_on:
            print(f"  📵  Can't call — {self.model} is powered off!")
            return
        print(f"  📞  Calling {number} from {self.phone_number}...")
        self.call_log.append({"to": number, "type": "outgoing"})

    def receive_call(self, number):
        """Simulate an incoming call."""
        if not self.is_powered_on:
            print(f"  📵  Missed call from {number} — {self.model} is off.")
            return
        print(f"  📲  Incoming call from {number}!")
        self.call_log.append({"from": number, "type": "incoming"})

    def show_call_log(self):
        """Display the full call history."""
        if not self.call_log:
            print("  📋  No calls recorded yet.")
            return
        print(f"  📋  Call log for {self.phone_number}:")
        for entry in self.call_log:
            if entry["type"] == "outgoing":
                print(f"       ↗  Outgoing → {entry['to']}")
            else:
                print(f"       ↙  Incoming ← {entry['from']}")

    # ── Polymorphism: Phone's own version of display_info ─────────────
    def display_info(self):
        super().display_info()          # Print the shared base info first
        print(f"  {'Phone #:':10} {self.phone_number}")
        print(f"  {'5G:':10} {'Yes ✅' if self.is_5g else 'No ❌'}")
        print(f"  {'─'*36}")


# ══════════════════════════════════════════════════════════════════
#  2.  TABLET
# ══════════════════════════════════════════════════════════════════

class Tablet(ElectronicDevice):
    """
    A touch-screen tablet — larger than a phone, more portable than a laptop.

    Extra attributes:
      screen_size_inches — diagonal screen measurement
      has_stylus         — whether a stylus / pen is supported
      installed_apps     — list of apps installed on the device
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os,
                 screen_size_inches, has_stylus):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.screen_size_inches = screen_size_inches
        self.has_stylus         = has_stylus
        self.installed_apps     = []

    # ── Polymorphism ──────────────────────────────────────────────────
    def connect_to_network(self):
        print(f"  📡  {self.brand} {self.model} connected via Wi-Fi 6.")

    # ── Tablet-specific methods ────────────────────────────────────────
    def install_app(self, app_name):
        """Install an app (if it isn't already installed)."""
        if app_name in self.installed_apps:
            print(f"  ℹ️   '{app_name}' is already installed.")
        else:
            self.installed_apps.append(app_name)
            print(f"  ✅  '{app_name}' installed successfully.")

    def launch_app(self, app_name):
        """Launch an installed app (device must be on)."""
        if not self.is_powered_on:
            print(f"  ⚠️   Power on the tablet first!")
            return
        if app_name in self.installed_apps:
            print(f"  🚀  Launching '{app_name}'...")
        else:
            print(f"  ❌  '{app_name}' is not installed. Install it first.")

    # ── Polymorphism ──────────────────────────────────────────────────
    def display_info(self):
        super().display_info()
        print(f"  {'Screen:':10} {self.screen_size_inches}\"")
        print(f"  {'Stylus:':10} {'Yes ✅' if self.has_stylus else 'No ❌'}")
        print(f"  {'Apps:':10} {', '.join(self.installed_apps) or 'None'}")
        print(f"  {'─'*36}")


# ══════════════════════════════════════════════════════════════════
#  3.  LAPTOP
# ══════════════════════════════════════════════════════════════════

class Laptop(ElectronicDevice):
    """
    A portable personal computer with a built-in keyboard and trackpad.

    Extra attributes:
      ram_gb        — RAM installed (GB)
      cpu_model     — Processor name/model
      is_touchscreen — Whether the display supports touch input
      open_apps     — List of currently running applications
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os,
                 ram_gb, cpu_model, is_touchscreen=False):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.ram_gb         = ram_gb
        self.cpu_model      = cpu_model
        self.is_touchscreen = is_touchscreen
        self.open_apps      = []

    # ── Polymorphism ──────────────────────────────────────────────────
    def connect_to_network(self):
        print(f"  📡  {self.brand} {self.model} connected via Wi-Fi 6E.")

    # ── Laptop-specific methods ────────────────────────────────────────
    def open_application(self, app_name):
        """Launch an application (laptop must be powered on)."""
        if not self.is_powered_on:
            print(f"  ⚠️   Boot the laptop first!")
            return
        self.open_apps.append(app_name)
        print(f"  💻  '{app_name}' is now running.")

    def close_application(self, app_name):
        """Close a running application."""
        if app_name in self.open_apps:
            self.open_apps.remove(app_name)
            print(f"  ✅  '{app_name}' has been closed.")
        else:
            print(f"  ℹ️   '{app_name}' is not currently running.")

    # ── Polymorphism ──────────────────────────────────────────────────
    def display_info(self):
        super().display_info()
        print(f"  {'RAM:':10} {self.ram_gb} GB")
        print(f"  {'CPU:':10} {self.cpu_model}")
        print(f"  {'Touch:':10} {'Yes ✅' if self.is_touchscreen else 'No ❌'}")
        print(f"  {'Running:':10} {', '.join(self.open_apps) or 'Nothing open'}")
        print(f"  {'─'*36}")


# ══════════════════════════════════════════════════════════════════
#  4.  DESKTOP
# ══════════════════════════════════════════════════════════════════

class Desktop(ElectronicDevice):
    """
    A stationary, high-performance personal computer.

    Extra attributes:
      ram_gb       — RAM installed (GB)
      gpu_model    — Graphics card name/model
      num_monitors — Number of displays currently connected
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os,
                 ram_gb, gpu_model, num_monitors=1):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.ram_gb      = ram_gb
        self.gpu_model   = gpu_model
        self.num_monitors = num_monitors

    # ── Polymorphism ──────────────────────────────────────────────────
    def connect_to_network(self):
        print(f"  🔌  {self.brand} {self.model} connected via Gigabit Ethernet.")

    # ── Desktop-specific methods ───────────────────────────────────────
    def connect_monitor(self):
        """Plug in an additional display."""
        self.num_monitors += 1
        print(f"  🖥️   Monitor connected. Total displays: {self.num_monitors}")

    def disconnect_monitor(self):
        """Unplug a display (minimum 1 must remain)."""
        if self.num_monitors > 1:
            self.num_monitors -= 1
            print(f"  🖥️   Monitor disconnected. Total displays: {self.num_monitors}")
        else:
            print(f"  ⚠️   Cannot disconnect — at least one monitor must stay connected.")

    # ── Polymorphism ──────────────────────────────────────────────────
    def display_info(self):
        super().display_info()
        print(f"  {'RAM:':10} {self.ram_gb} GB")
        print(f"  {'GPU:':10} {self.gpu_model}")
        print(f"  {'Monitors:':10} {self.num_monitors}")
        print(f"  {'─'*36}")


# ══════════════════════════════════════════════════════════════════
#  5.  SERVER
# ══════════════════════════════════════════════════════════════════

class Server(ElectronicDevice):
    """
    A rack-mounted server designed to run 24/7 and serve other devices.

    Extra attributes:
      ip_address        — Static IP address on the network
      max_connections   — Maximum simultaneous client connections
      rack_unit         — Physical height in rack units (U)
      active_connections — Current live connection count
      uptime_hours      — Hours the server has been running continuously
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os,
                 ip_address, max_connections, rack_unit=1):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.ip_address         = ip_address
        self.max_connections    = max_connections
        self.rack_unit          = rack_unit
        self.active_connections = 0
        self.uptime_hours       = 0

    # ── Polymorphism ──────────────────────────────────────────────────
    def connect_to_network(self):
        print(f"  🔌  {self.brand} {self.model} connected via "
              f"10GbE Ethernet  |  Static IP: {self.ip_address}")

    # ── Server-specific methods ────────────────────────────────────────
    def accept_connection(self):
        """Accept one new client connection."""
        if self.active_connections < self.max_connections:
            self.active_connections += 1
            print(f"  🟢  Connection #{self.active_connections} accepted "
                  f"({self.active_connections}/{self.max_connections} slots used)")
        else:
            print(f"  🔴  Connection refused — server at max capacity "
                  f"({self.max_connections}/{self.max_connections})!")

    def drop_connection(self):
        """Drop one active connection."""
        if self.active_connections > 0:
            self.active_connections -= 1
            print(f"  ⬇️   Connection dropped. "
                  f"Active: {self.active_connections}/{self.max_connections}")
        else:
            print(f"  ℹ️   No active connections to drop.")

    def report_status(self):
        """Print a health summary for the server."""
        load = (self.active_connections / self.max_connections) * 100
        bar_filled  = int(load / 5)          # 20-char bar
        bar_empty   = 20 - bar_filled
        bar         = "█" * bar_filled + "░" * bar_empty
        print(f"\n  ┌─ Server Health Report ──────────────────┐")
        print(f"  │  IP      : {self.ip_address:<29}│")
        print(f"  │  Uptime  : {self.uptime_hours} hrs{' '*(25 - len(str(self.uptime_hours)))}│")
        print(f"  │  Load    : [{bar}] {load:5.1f}%│")
        print(f"  │  Conns   : {self.active_connections}/{self.max_connections}"
              f"{' '*(29 - len(f'{self.active_connections}/{self.max_connections}'))}│")
        print(f"  │  Battery : {self.battery_level}%"
              f"{' '*(28 - len(str(self.battery_level)))}│")
        print(f"  └─────────────────────────────────────────┘")

    # ── Polymorphism ──────────────────────────────────────────────────
    def display_info(self):
        super().display_info()
        print(f"  {'IP:':10} {self.ip_address}")
        print(f"  {'Rack U:':10} {self.rack_unit}U")
        print(f"  {'Conns:':10} {self.active_connections}/{self.max_connections}")
        print(f"  {'Uptime:':10} {self.uptime_hours} hrs")
        print(f"  {'─'*36}")
