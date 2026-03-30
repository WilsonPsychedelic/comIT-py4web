"""
main.py
───────
OOP in Python — Interactive Terminal Tour

Run this file to walk through each OOP concept step-by-step,
with discovery print statements explaining what is happening
at every stage and why it matters.

Usage:
  python main.py
"""

from electronic_device import ElectronicDevice
from devices import Phone, Tablet, Laptop, Desktop, Server


# ──────────────────────────────────────────────────────────────────
#  HELPER: pretty section banner
# ──────────────────────────────────────────────────────────────────

def banner(title, subtitle=""):
    width = 60
    print("\n" + "═" * width)
    print(f"  {title}")
    if subtitle:
        print(f"  {subtitle}")
    print("═" * width)


def section(label):
    print(f"\n  ┄┄ {label} ┄┄")


# ══════════════════════════════════════════════════════════════════
#  CHAPTER 1 — Classes and Objects
# ══════════════════════════════════════════════════════════════════

def chapter_1_classes_and_objects():
    banner("CHAPTER 1 — Classes and Objects",
           "Blueprint vs. real thing")

    print("""
  A CLASS is the blueprint.  An OBJECT is the real device built
  from that blueprint.  You can stamp out as many objects as you
  like from a single class — each one is independent in memory.
    """)

    section("DISCOVERY: What type is a Phone object?")
    pixel = Phone("Google", "Pixel 8 Pro", 128, 5050, "Android 14",
                  "+1-555-0001", is_5g=True)
    iphone = Phone("Apple", "iPhone 15 Pro", 256, 3274, "iOS 17",
                   "+1-555-0002", is_5g=True)

    print(f"  type(pixel)  → {type(pixel)}")
    print(f"  type(iphone) → {type(iphone)}")

    section("DISCOVERY: Are two Phone objects the same object in memory?")
    print(f"  pixel is iphone → {pixel is iphone}")
    print("  ✔  They are DIFFERENT objects — changing one won't affect the other.")

    section("DISCOVERY: Both are instances of Phone AND ElectronicDevice")
    print(f"  isinstance(pixel,  Phone)           → {isinstance(pixel,  Phone)}")
    print(f"  isinstance(pixel,  ElectronicDevice)→ {isinstance(pixel,  ElectronicDevice)}")
    print("  ✔  Phone inherits from ElectronicDevice, so pixel qualifies as BOTH.")

    section("DISCOVERY: Can we instantiate the abstract root class directly?")
    print("  Trying: ElectronicDevice('X', 'Y', 0, 0, 'Z')  ...")
    try:
        bad = ElectronicDevice("X", "Y", 0, 0, "Z")
    except TypeError as e:
        print(f"  ❌  TypeError raised! → {e}")
    print("  ✔  Good — abstract classes cannot be created on their own.")


# ══════════════════════════════════════════════════════════════════
#  CHAPTER 2 — The __init__ Method and Attributes
# ══════════════════════════════════════════════════════════════════

def chapter_2_init_and_attributes():
    banner("CHAPTER 2 — __init__ and Attributes",
           "Configuring a device at birth")

    print("""
  __init__ is the CONSTRUCTOR — it runs the moment an object is
  created and stamps the object's unique data (attributes) onto it.
  'self' is Python's way of saying "this specific object".
    """)

    section("DISCOVERY: Attributes set by __init__")
    laptop = Laptop("Apple", "MacBook Pro 14", 1000, 69600,
                    "macOS Sonoma", ram_gb=32, cpu_model="M3 Pro",
                    is_touchscreen=False)
    print(f"  laptop.brand        = '{laptop.brand}'")
    print(f"  laptop.model        = '{laptop.model}'")
    print(f"  laptop.os           = '{laptop.os}'")
    print(f"  laptop.storage_gb   = {laptop.storage_gb}")
    print(f"  laptop.ram_gb       = {laptop.ram_gb}")
    print(f"  laptop.cpu_model    = '{laptop.cpu_model}'")
    print(f"  laptop.is_powered_on= {laptop.is_powered_on}  ← always starts OFF")
    print(f"  laptop.battery_level= {laptop.battery_level}%  ← always starts full")

    section("DISCOVERY: __str__ gives a clean label for print()")
    print(f"  str(laptop) → '{laptop}'")
    print("  ✔  This comes from the __str__ method defined on ElectronicDevice.")

    section("DISCOVERY: Each object holds its OWN copy of attributes")
    tablet = Tablet("Apple", "iPad Pro 12.9", 512, 10758, "iPadOS 17",
                    screen_size_inches=12.9, has_stylus=True)
    laptop.brand = "Dell"           # Change brand on laptop only
    print(f"  After: laptop.brand = '{laptop.brand}'")
    print(f"  tablet.brand is still: '{tablet.brand}'  ← untouched ✔")


# ══════════════════════════════════════════════════════════════════
#  CHAPTER 3 — Methods
# ══════════════════════════════════════════════════════════════════

def chapter_3_methods():
    banner("CHAPTER 3 — Methods",
           "Teaching objects to act")

    print("""
  Methods are functions that live inside a class.
  They define what an object can DO — its behaviours.
  Every method receives 'self' so it can read/change its own data.
    """)

    section("DISCOVERY: power_on() checks battery before starting")
    device = Desktop("Dell", "OptiPlex 7090", 512, 0, "Windows 11",
                     ram_gb=16, gpu_model="Intel UHD 770", num_monitors=2)
    device.power_on()                        # Should work — battery = 100%

    section("DISCOVERY: power_on() refuses if battery is 0%")
    device.battery_level = 0
    device.power_off()
    device.power_on()                        # Should refuse

    section("DISCOVERY: charge() caps at 100%")
    print(f"  Battery before charge: {device.battery_level}%")
    device.charge(60)
    print(f"  After charge(60):      {device.battery_level}%")
    device.charge(999)                       # Should cap at 100
    print(f"  After charge(999):     {device.battery_level}%  ← capped at 100!")

    section("DISCOVERY: display_info() gives a full status snapshot")
    device.power_on()
    device.display_info()


# ══════════════════════════════════════════════════════════════════
#  CHAPTER 4 — Encapsulation
# ══════════════════════════════════════════════════════════════════

def chapter_4_encapsulation():
    banner("CHAPTER 4 — Encapsulation",
           "Protecting data behind a controlled interface")

    print("""
  Encapsulation means BUNDLING data + behaviour inside a class,
  and HIDING the internals so outside code can't corrupt them.

  In Python:
    __attribute   (double underscore prefix) = private
    @property     getter  = safe read access
    @property setter      = safe write access with validation
    """)

    server = Server("Dell", "PowerEdge R750", 12000, 0,
                    "Ubuntu 22.04", "192.168.0.10", max_connections=500)

    section("DISCOVERY: battery_level is a @property (getter)")
    print(f"  server.battery_level  → {server.battery_level}%")
    print("  ✔  We read it like a regular attribute, but a method ran behind the scenes.")

    section("DISCOVERY: The setter validates values before applying them")
    print(f"  Setting battery_level = 75 ...")
    server.battery_level = 75
    print(f"  server.battery_level  → {server.battery_level}%  ✔")

    print(f"\n  Setting battery_level = 200 (invalid) ...")
    server.battery_level = 200
    print(f"  server.battery_level  → {server.battery_level}%  ✔  (unchanged — setter blocked it!)")

    print(f"\n  Setting battery_level = -10 (invalid) ...")
    server.battery_level = -10
    print(f"  server.battery_level  → {server.battery_level}%  ✔  (unchanged again!)")

    section("DISCOVERY: The private attribute is name-mangled by Python")
    print("  Trying: server.__battery_level  ...")
    try:
        val = server.__battery_level
    except AttributeError as e:
        print(f"  ❌  AttributeError → {e}")
    print("  ✔  Python hides it as '_ElectronicDevice__battery_level' to prevent accidents.")
    print(f"  Actual mangled name: server._ElectronicDevice__battery_level "
          f"= {server._ElectronicDevice__battery_level}%")
    print("     (You CAN access it this way, but doing so breaks encapsulation on purpose.)")


# ══════════════════════════════════════════════════════════════════
#  CHAPTER 5 — Inheritance
# ══════════════════════════════════════════════════════════════════

def chapter_5_inheritance():
    banner("CHAPTER 5 — Inheritance",
           "Child classes reuse everything the parent has")

    print("""
  Inheritance lets a CHILD class extend a PARENT class.
  The child gets ALL of the parent's attributes and methods,
  then adds its own specialised ones on top.

  Keyword: super() — calls the parent's version of a method.
    """)

    # ── Example 1: Phone inherits from ElectronicDevice ───────────────
    section("EXAMPLE 1 — Phone uses inherited methods it didn't define itself")
    samsung = Phone("Samsung", "Galaxy S24 Ultra", 512, 5000,
                    "Android 14", "+44-7700-111222", is_5g=True)

    print("  Calling power_on() — defined in ElectronicDevice, NOT in Phone:")
    samsung.power_on()

    print("\n  Calling charge() — also inherited from ElectronicDevice:")
    samsung.battery_level = 30
    samsung.charge(40)

    print("\n  Now calling make_call() — defined ONLY in Phone:")
    samsung.make_call("+44-7700-999000")

    print("\n  And receive_call() — also Phone-only:")
    samsung.receive_call("+44-7700-888111")

    samsung.show_call_log()

    # ── Example 2: Server inherits and extends ─────────────────────────
    section("EXAMPLE 2 — Server inherits everything and adds its own methods")
    hp_server = Server("HP", "ProLiant DL380", 20000, 0,
                       "RHEL 9", "10.0.0.5", max_connections=1000, rack_unit=2)

    print("  power_on() — inherited:")
    hp_server.power_on()

    print("\n  accept_connection() — Server-only:")
    hp_server.uptime_hours = 4380   # Half a year of uptime
    for _ in range(4):
        hp_server.accept_connection()

    print("\n  drop_connection() — Server-only:")
    hp_server.drop_connection()

    print("\n  report_status() — Server-only:")
    hp_server.report_status()

    # ── Checking the inheritance chain ────────────────────────────────
    section("DISCOVERY: Inspect the inheritance chain with __mro__")
    print("  Phone.__mro__:")
    for cls in Phone.__mro__:
        print(f"    → {cls}")
    print("\n  Server.__mro__:")
    for cls in Server.__mro__:
        print(f"    → {cls}")
    print("  ✔  Every class ultimately traces back to Python's built-in 'object'.")


# ══════════════════════════════════════════════════════════════════
#  CHAPTER 6 — Polymorphism
# ══════════════════════════════════════════════════════════════════

def chapter_6_polymorphism():
    banner("CHAPTER 6 — Polymorphism",
           "Same message — each object responds in its own way")

    print("""
  Polymorphism (Greek: 'many forms') means different object types
  can all respond to the SAME method call — but each does so in
  its own unique way.

  The calling code doesn't need to know WHICH type it's dealing
  with.  It just calls the method and trusts each object to do
  the right thing.
    """)

    # Build one of each device type
    pixel   = Phone("Google",   "Pixel 8 Pro",      128,   5050, "Android 14",
                    "+1-555-0001", is_5g=True)
    ipad    = Tablet("Apple",   "iPad Pro 11",       256,   7538, "iPadOS 17",
                    screen_size_inches=11.0, has_stylus=True)
    xps     = Laptop("Dell",    "XPS 15",            512,  86000, "Windows 11",
                    ram_gb=32, cpu_model="Intel Core i9-13900H", is_touchscreen=True)
    imac    = Desktop("Apple",  "iMac 24",          1000,      0, "macOS Sonoma",
                    ram_gb=24, gpu_model="Apple M3", num_monitors=1)
    r750    = Server("Dell",    "PowerEdge R750",  12000,      0, "Ubuntu 22.04",
                    ip_address="192.168.1.50", max_connections=500, rack_unit=2)

    fleet = [pixel, ipad, xps, imac, r750]

    section("DISCOVERY: Power on all devices with the SAME loop")
    for device in fleet:
        device.power_on()

    section("DISCOVERY: connect_to_network() — same call, 5 different behaviours")
    print("  Each device type connects differently — this is polymorphism!")
    print()
    for device in fleet:
        device.connect_to_network()

    section("DISCOVERY: display_info() — same call, each shows its own fields")
    print("  Notice how Phone, Tablet, Laptop, Desktop, and Server each add")
    print("  their own lines after the shared base info:\n")
    for device in fleet:
        device.display_info()

    section("DISCOVERY: isinstance() lets us branch logic when needed")
    for device in fleet:
        if isinstance(device, Phone):
            print(f"  {device.model} is a Phone → testing make_call()...")
            device.make_call("+1-555-9999")
        elif isinstance(device, Server):
            print(f"  {device.model} is a Server → testing accept_connection()...")
            device.accept_connection()
        else:
            print(f"  {device.model} is a {type(device).__name__} — no extra action.")


# ══════════════════════════════════════════════════════════════════
#  CHAPTER 7 — Abstraction
# ══════════════════════════════════════════════════════════════════

def chapter_7_abstraction():
    banner("CHAPTER 7 — Abstraction",
           "Enforce a contract; hide the messy details")

    print("""
  Abstraction means:
    1. Expose ONLY the interface a caller needs.
    2. Hide the internal complexity behind clean method names.
    3. Use Abstract Base Classes (ABC) to FORCE subclasses to
       implement critical methods — breaking the rule raises
       a TypeError at class definition time.

  In our code, connect_to_network() is declared @abstractmethod.
  Every device MUST implement it, or Python won't let you create
  objects of that class.
    """)

    section("DISCOVERY: What happens if a subclass forgets an abstract method?")
    print("  Defining an incomplete class that skips connect_to_network() ...")
    print()

    try:
        # Dynamically define a broken subclass to show the error
        broken_code = """
class BrokenDevice(ElectronicDevice):
    def __init__(self):
        super().__init__('X', 'Y', 0, 0, 'Z')
    # Forgot to implement connect_to_network() !

b = BrokenDevice()   # ← this line raises TypeError
"""
        print("  Code being attempted:")
        for line in broken_code.strip().split("\n"):
            print(f"    {line}")
        print()

        # Actually execute it
        exec(broken_code, {"ElectronicDevice": ElectronicDevice})

    except TypeError as e:
        print(f"  ❌  TypeError raised! → {e}")
    print("  ✔  Python enforced the contract. BrokenDevice never came to life.")

    section("DISCOVERY: The abstract method guarantees a uniform interface")
    print("  Even though each device implements connect_to_network() differently,")
    print("  callers can always count on it existing.  Here's proof:\n")

    devices = [
        Phone("Nokia",  "G60",          128,  4500, "Android 12", "+358-40-000", is_5g=False),
        Laptop("Lenovo","ThinkPad X1",  512, 57000, "Windows 11",
               ram_gb=16, cpu_model="Intel Core i7-1365U"),
        Server("IBM",   "System x3650", 4000,    0, "AIX 7.3",
               "10.10.0.1", max_connections=200),
    ]

    for d in devices:
        d.power_on()
        d.connect_to_network()       # Works on all — abstraction guarantees it
        d.power_off()
        print()


# ══════════════════════════════════════════════════════════════════
#  CHAPTER 8 — Putting It All Together
# ══════════════════════════════════════════════════════════════════

def chapter_8_full_simulation():
    banner("CHAPTER 8 — Full Simulation",
           "All four pillars working together")

    print("""
  Let's run a realistic simulation using the complete device fleet.
  Every concept from this guide plays a role:

    • Classes & Objects    — we create five distinct device instances
    • __init__             — each device is configured at creation
    • Methods              — behaviours drive the simulation
    • Encapsulation        — battery is protected; setters validate
    • Inheritance          — all devices share the root class features
    • Polymorphism         — one loop handles every device type
    • Abstraction          — connect_to_network() is guaranteed to exist
    """)

    # ── Create the fleet ───────────────────────────────────────────────
    section("Building the device fleet")
    pixel   = Phone("Google", "Pixel 9 Pro",      256,  5050, "Android 15",
                    "+1-555-8000", is_5g=True)
    ipad    = Tablet("Apple",  "iPad Pro M4",      512,  10758, "iPadOS 18",
                    screen_size_inches=13.0, has_stylus=True)
    macbook = Laptop("Apple",  "MacBook Pro M4",  1000,  69600, "macOS Sequoia",
                    ram_gb=32, cpu_model="Apple M4 Pro")
    studio  = Desktop("Apple", "Mac Studio M4",  2000,      0, "macOS Sequoia",
                     ram_gb=64, gpu_model="Apple M4 Max", num_monitors=3)
    r760    = Server("Dell",   "PowerEdge R760", 24000,      0, "Ubuntu 24.04",
                    ip_address="10.0.0.1", max_connections=2000, rack_unit=2)

    fleet = [pixel, ipad, macbook, studio, r760]
    print(f"  Fleet assembled: {len(fleet)} devices created.")

    # ── Power everything on and connect ────────────────────────────────
    section("Powering on and connecting all devices (Inheritance + Polymorphism)")
    for device in fleet:
        device.power_on()
        device.connect_to_network()

    # ── Simulate real use ──────────────────────────────────────────────
    section("Simulating real-world usage")

    print("\n  [ Phone — making and receiving calls ]")
    pixel.make_call("+1-555-1234")
    pixel.receive_call("+1-555-5678")
    pixel.show_call_log()

    print("\n  [ Tablet — installing and launching apps ]")
    ipad.install_app("Procreate")
    ipad.install_app("Notability")
    ipad.install_app("Procreate")    # Duplicate — should warn
    ipad.launch_app("Procreate")
    ipad.launch_app("GarageBand")   # Not installed — should warn

    print("\n  [ Laptop — opening and closing apps ]")
    macbook.open_application("VS Code")
    macbook.open_application("Docker")
    macbook.open_application("Slack")
    macbook.close_application("Docker")

    print("\n  [ Desktop — adding monitors ]")
    studio.connect_monitor()         # 3 → 4
    studio.connect_monitor()         # 4 → 5

    print("\n  [ Server — handling connections ]")
    r760.uptime_hours = 8760         # One full year of uptime
    for i in range(6):
        r760.accept_connection()
    r760.drop_connection()
    r760.report_status()

    # ── Battery drain and recharge ─────────────────────────────────────
    section("Draining and recharging (Encapsulation in action)")
    print("\n  Draining pixel battery to 8%...")
    pixel.battery_level = 8
    pixel.charge(72)

    print("\n  Trying to set macbook battery to 150% (invalid)...")
    macbook.battery_level = 150
    print(f"  macbook.battery_level is still: {macbook.battery_level}%  ✔")

    # ── Final status report ────────────────────────────────────────────
    section("Final device status report (Polymorphism — one loop, all types)")
    print()
    for device in fleet:
        device.display_info()

    print("\n  🎉  Simulation complete — all four OOP pillars demonstrated!\n")


# ══════════════════════════════════════════════════════════════════
#  ENTRY POINT
# ══════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    banner("OOP IN PYTHON — A TERMINAL TOUR",
           "Follow along chapter by chapter")

    print("""
  This tour walks you through the four pillars of Object-Oriented
  Programming using a family of electronic devices as the example.

  Files in this project:
    electronic_device.py  — Root abstract base class
    devices.py            — Phone, Tablet, Laptop, Desktop, Server
    main.py               — This file (chapters + discoveries)
    """)

    chapter_1_classes_and_objects()
    chapter_2_init_and_attributes()
    chapter_3_methods()
    chapter_4_encapsulation()
    chapter_5_inheritance()
    chapter_6_polymorphism()
    chapter_7_abstraction()
    chapter_8_full_simulation()

    banner("END OF TOUR",
           "Happy coding! Every great program is just well-designed objects. 🚀")
