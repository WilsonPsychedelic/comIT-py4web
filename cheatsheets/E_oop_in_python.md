# Object-Oriented Programming in Python
### A Beginner-Friendly Guide Using Electronic Devices

---

## Table of Contents

1. [What is Object-Oriented Programming?](#what-is-oop)
2. [Classes and Objects](#classes-and-objects)
3. [The `__init__` Method and Attributes](#the-init-method-and-attributes)
4. [Methods — Teaching Objects to Do Things](#methods)
5. [Encapsulation — Protecting Your Data](#encapsulation)
6. [Inheritance — Building on What Already Exists](#inheritance)
7. [Polymorphism — One Interface, Many Forms](#polymorphism)
8. [Abstraction — Hiding Complexity](#abstraction)
9. [Putting It All Together](#putting-it-all-together)

---

## 1. What is Object-Oriented Programming? <a name="what-is-oop"></a>

Imagine walking into an electronics store. You see phones, tablets, laptops, and massive desktop servers. Each of these is a *different kind of thing*, yet they all share some common traits — they have a screen, a power button, a processor, and they all run software. They are, at their core, **electronic devices**.

**Object-Oriented Programming (OOP)** is a way of writing code that mirrors how we naturally think about the world — in terms of *things* (objects) that have *characteristics* (attributes) and *behaviours* (methods). Instead of writing a long list of instructions, you model your program around objects that interact with each other.

Python is an excellent language for learning OOP because its syntax is clean, readable, and expressive. The four **pillars of OOP** are:

| Pillar | In Plain English |
|---|---|
| **Encapsulation** | Bundling data and behaviour together, and hiding internal details |
| **Inheritance** | A new class can reuse and extend the features of an existing class |
| **Polymorphism** | Different objects can respond to the same action in their own unique way |
| **Abstraction** | Expose only what's necessary; hide the complicated internals |

We'll explore each of these in depth using a family of electronic devices as our guiding example.

---

## 2. Classes and Objects <a name="classes-and-objects"></a>

### What is a Class?

A **class** is a *blueprint* or *template*. Think of it as the design specification for an electronic device. The blueprint itself isn't a real device — it's just the plan. From that one blueprint, you can manufacture as many actual devices as you want.

### What is an Object?

An **object** is a *real, concrete instance* created from a class blueprint. If `ElectronicDevice` is the blueprint, then your personal phone, your work laptop, and the server running a website are all **objects** — each built from that same blueprint, but each existing independently in memory.

```python
# This is how you define a class in Python
class ElectronicDevice:
    pass  # 'pass' means the class is empty for now — we'll fill it in soon
```

```python
# Creating objects (instances) from the class
my_device = ElectronicDevice()
another_device = ElectronicDevice()

print(type(my_device))   # <class '__main__.ElectronicDevice'>
```

The two objects `my_device` and `another_device` are completely independent. Changing one does **not** affect the other — just like buying two identical phones doesn't mean they share your contacts.

---

## 3. The `__init__` Method and Attributes <a name="the-init-method-and-attributes"></a>

### Attributes — The Characteristics of an Object

Every electronic device has characteristics: a brand name, a model, a screen size, whether it's currently powered on, and so on. In OOP, these characteristics are called **attributes** — variables that belong to an object.

### The `__init__` Method — The Constructor

When you manufacture a device, you configure it right away — you set the brand, install the OS, define the battery size. Python uses a special method called `__init__` (short for "initialise") to do exactly this. It runs **automatically** the moment an object is created.

```python
class ElectronicDevice:
    """
    The root blueprint for all electronic devices.
    Every device we create will be based on this class.
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os):
        # 'self' refers to the specific object being created
        self.brand = brand              # e.g., "Apple", "Samsung"
        self.model = model              # e.g., "iPhone 15", "Galaxy S24"
        self.storage_gb = storage_gb    # Internal storage in gigabytes
        self.battery_mah = battery_mah  # Battery capacity in milliamp-hours
        self.os = os                    # Operating system name
        self.is_powered_on = False      # All devices start powered off
        self.battery_level = 100        # Battery starts fully charged (%)

    def __str__(self):
        """
        A special method that defines how the object is represented
        as a human-readable string. Like a name tag for your object.
        """
        return f"{self.brand} {self.model} (OS: {self.os})"
```

> **What is `self`?**
> Think of `self` as the object saying "me". When a phone object calls a method, `self` is how that specific phone refers to its own data. Without `self`, the method wouldn't know *which* device's battery level to check.

```python
# Creating two different ElectronicDevice objects
device_one = ElectronicDevice("Samsung", "Galaxy Tab S9", 256, 8000, "Android")
device_two = ElectronicDevice("Apple", "MacBook Air", 512, 6000, "macOS")

print(device_one)           # Samsung Galaxy Tab S9 (OS: Android)
print(device_two.brand)     # Apple
print(device_one.storage_gb) # 256
```

Each object holds its *own* copy of the data. Changing `device_one.brand` has zero effect on `device_two.brand`.

---

## 4. Methods — Teaching Objects to Do Things <a name="methods"></a>

**Methods** are functions defined inside a class. They define the *behaviours* of an object — the actions it can perform. An electronic device can power on, power off, and charge.

```python
class ElectronicDevice:

    def __init__(self, brand, model, storage_gb, battery_mah, os):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah
        self.os = os
        self.is_powered_on = False
        self.battery_level = 100

    def power_on(self):
        """Powers the device on, but only if there's enough battery."""
        if self.battery_level > 0:
            self.is_powered_on = True
            print(f"{self.brand} {self.model} is now ON. Battery: {self.battery_level}%")
        else:
            print(f"{self.brand} {self.model} cannot power on — battery is dead!")

    def power_off(self):
        """Gracefully shuts the device down."""
        self.is_powered_on = False
        print(f"{self.brand} {self.model} has been powered off.")

    def charge(self, amount):
        """
        Charges the device by a given percentage.
        The battery cannot exceed 100%.
        """
        if amount <= 0:
            print("Charge amount must be a positive number.")
            return
        self.battery_level = min(100, self.battery_level + amount)
        print(f"Charging... Battery is now at {self.battery_level}%")

    def display_info(self):
        """Prints a summary of the device's current status."""
        status = "ON" if self.is_powered_on else "OFF"
        print(f"--- Device Info ---")
        print(f"  Brand   : {self.brand}")
        print(f"  Model   : {self.model}")
        print(f"  OS      : {self.os}")
        print(f"  Storage : {self.storage_gb} GB")
        print(f"  Battery : {self.battery_level}%")
        print(f"  Status  : {status}")
        print(f"-------------------")

    def __str__(self):
        return f"{self.brand} {self.model} (OS: {self.os})"
```

```python
my_device = ElectronicDevice("Google", "Pixel 8", 128, 4575, "Android")

my_device.power_on()       # Google Pixel 8 is now ON. Battery: 100%
my_device.battery_level = 5
my_device.power_off()
my_device.battery_level = 0
my_device.power_on()       # Google Pixel 8 cannot power on — battery is dead!
my_device.charge(30)       # Charging... Battery is now at 30%
my_device.power_on()       # Google Pixel 8 is now ON. Battery: 30%
my_device.display_info()
```

---

## 5. Encapsulation — Protecting Your Data <a name="encapsulation"></a>

**Encapsulation** is the idea of *bundling* related data and behaviour into one unit (the class), and *controlling access* to the internals. Think of the battery in a laptop — you can see the battery percentage, but you can't directly reach in and change the chemical charge level; you interact with it through a proper charging port.

In Python, we signal that an attribute is **private** (internal use only) by prefixing it with a double underscore `__`. Python will then "mangle" the name to make it harder to access accidentally from outside the class.

```python
class ElectronicDevice:

    def __init__(self, brand, model, storage_gb, battery_mah, os):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah
        self.os = os
        self.is_powered_on = False
        self.__battery_level = 100  # PRIVATE — use the methods below to interact with it

    @property
    def battery_level(self):
        """A 'getter' — safely reads the private battery level."""
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value):
        """
        A 'setter' — safely updates the private battery level,
        but only within the valid range of 0 to 100.
        """
        if 0 <= value <= 100:
            self.__battery_level = value
        else:
            print(f"Invalid battery level: {value}. Must be between 0 and 100.")

    def charge(self, amount):
        self.battery_level = min(100, self.__battery_level + amount)
        print(f"Battery charged to {self.__battery_level}%")
```

```python
laptop = ElectronicDevice("Dell", "XPS 15", 1000, 86000, "Windows 11")

# Correct way — through the property setter (validates the value)
laptop.battery_level = 75
print(laptop.battery_level)   # 75

# Attempting an invalid value — the setter catches it
laptop.battery_level = 150    # Invalid battery level: 150. Must be between 0 and 100.
print(laptop.battery_level)   # Still 75 — protected!

# Trying to access the private attribute directly will raise an AttributeError
# laptop.__battery_level  ← This would fail!
```

> **Why does this matter?**
> Without encapsulation, any part of your code could accidentally set `battery_level = 9999`, breaking the logic of your entire application. Encapsulation acts like a security guard — all changes must go through the front door (the setter), where rules can be enforced.

---

## 6. Inheritance — Building on What Already Exists <a name="inheritance"></a>

**Inheritance** is one of the most powerful concepts in OOP. It allows a new class (called a **child class** or **subclass**) to inherit all the attributes and methods of an existing class (called the **parent class** or **superclass**), and then *extend or override* that functionality.

Think of it this way: a `Phone` is a kind of `ElectronicDevice`. It has everything a generic device has — a brand, a battery, power controls — **plus** phone-specific things like a phone number and the ability to make calls. Instead of rewriting everything from scratch, `Phone` simply *inherits* from `ElectronicDevice` and adds what's unique to it.

```
ElectronicDevice (Root / Parent class)
├── Phone
├── Tablet
├── Laptop
├── Desktop
└── Server
```

### The `super()` Function

When a child class defines its own `__init__`, it usually needs to call the parent's `__init__` first to set up the shared attributes. The `super()` function is how Python lets you call the parent class's methods from inside the child class.

```python
class Phone(ElectronicDevice):
    """
    A Phone is a mobile ElectronicDevice.
    It inherits everything from ElectronicDevice and adds
    phone-specific features: a phone number and call functionality.
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os, phone_number, is_5g):
        # Call the parent's __init__ to set up the shared attributes
        super().__init__(brand, model, storage_gb, battery_mah, os)
        # Now add the Phone-specific attributes
        self.phone_number = phone_number
        self.is_5g = is_5g
        self.call_log = []   # An empty list to track call history

    def make_call(self, number):
        """Makes a phone call to the given number."""
        if not self.is_powered_on:
            print("Cannot make a call — the phone is powered off!")
            return
        print(f"📞 Calling {number} from {self.phone_number}...")
        self.call_log.append({"to": number, "type": "outgoing"})

    def receive_call(self, number):
        """Receives an incoming call."""
        if not self.is_powered_on:
            print(f"Missed call from {number} — phone is off.")
            return
        print(f"📲 Incoming call from {number}!")
        self.call_log.append({"from": number, "type": "incoming"})

    def show_call_log(self):
        """Displays the call history."""
        if not self.call_log:
            print("No calls yet.")
            return
        print("--- Call Log ---")
        for entry in self.call_log:
            if entry["type"] == "outgoing":
                print(f"  ↗ Outgoing to: {entry['to']}")
            else:
                print(f"  ↙ Incoming from: {entry['from']}")
        print("----------------")
```

```python
class Tablet(ElectronicDevice):
    """
    A Tablet is a touch-screen ElectronicDevice.
    Larger than a phone but more portable than a laptop.
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os, screen_size_inches, has_stylus):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.screen_size_inches = screen_size_inches
        self.has_stylus = has_stylus
        self.installed_apps = []

    def install_app(self, app_name):
        """Installs an app onto the tablet."""
        if app_name in self.installed_apps:
            print(f"'{app_name}' is already installed.")
        else:
            self.installed_apps.append(app_name)
            print(f"✅ '{app_name}' installed successfully.")

    def launch_app(self, app_name):
        """Launches an installed app."""
        if not self.is_powered_on:
            print("Power on the tablet first!")
            return
        if app_name in self.installed_apps:
            print(f"🚀 Launching '{app_name}'...")
        else:
            print(f"'{app_name}' is not installed. Install it first.")
```

```python
class Laptop(ElectronicDevice):
    """A portable personal computer with a physical keyboard."""

    def __init__(self, brand, model, storage_gb, battery_mah, os, ram_gb, cpu_model, is_touchscreen):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.ram_gb = ram_gb
        self.cpu_model = cpu_model
        self.is_touchscreen = is_touchscreen
        self.open_applications = []

    def open_application(self, app_name):
        """Opens an application on the laptop."""
        if not self.is_powered_on:
            print("Boot the laptop first!")
            return
        self.open_applications.append(app_name)
        print(f"💻 '{app_name}' is now running.")

    def close_application(self, app_name):
        """Closes a running application."""
        if app_name in self.open_applications:
            self.open_applications.remove(app_name)
            print(f"'{app_name}' has been closed.")
        else:
            print(f"'{app_name}' is not currently running.")

    def display_info(self):
        """Override the parent display to add laptop-specific info."""
        super().display_info()   # Call the parent version first
        print(f"  RAM     : {self.ram_gb} GB")
        print(f"  CPU     : {self.cpu_model}")
        print(f"  Running : {', '.join(self.open_applications) or 'Nothing'}")
        print(f"-------------------")
```

```python
class Desktop(ElectronicDevice):
    """A stationary personal computer with high performance potential."""

    def __init__(self, brand, model, storage_gb, battery_mah, os, ram_gb, gpu_model, num_monitors):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.ram_gb = ram_gb
        self.gpu_model = gpu_model
        self.num_monitors = num_monitors

    def connect_monitor(self):
        """Simulates plugging in an additional monitor."""
        self.num_monitors += 1
        print(f"Monitor connected. Total monitors: {self.num_monitors}")
```

```python
class Server(ElectronicDevice):
    """
    A Server is a high-performance ElectronicDevice designed to run
    continuously and serve data or applications to other devices.
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os, ip_address, max_connections, rack_unit):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.ip_address = ip_address
        self.max_connections = max_connections
        self.rack_unit = rack_unit          # Physical size in rack units
        self.active_connections = 0
        self.uptime_hours = 0

    def accept_connection(self):
        """Handles an incoming client connection."""
        if self.active_connections < self.max_connections:
            self.active_connections += 1
            print(f"Connection accepted. Active connections: {self.active_connections}/{self.max_connections}")
        else:
            print("⚠️ Connection refused — server is at maximum capacity!")

    def drop_connection(self):
        """Drops an active client connection."""
        if self.active_connections > 0:
            self.active_connections -= 1
            print(f"Connection dropped. Active: {self.active_connections}/{self.max_connections}")

    def report_status(self):
        """Prints a server health report."""
        load_percent = (self.active_connections / self.max_connections) * 100
        print(f"🖥️  Server Status: {self.ip_address}")
        print(f"   Uptime   : {self.uptime_hours} hours")
        print(f"   Load     : {load_percent:.1f}% ({self.active_connections}/{self.max_connections})")
        print(f"   Battery  : {self.battery_level}%")
```

### Inheritance in Action — Example 1: Phone

```python
iphone = Phone("Apple", "iPhone 15 Pro", 256, 3274, "iOS", "+1-555-0100", is_5g=True)

iphone.power_on()                  # Apple iPhone 15 Pro is now ON. Battery: 100%
iphone.make_call("+1-555-0199")    # 📞 Calling +1-555-0199 from +1-555-0100...
iphone.receive_call("+1-555-0200") # 📲 Incoming call from +1-555-0200!
iphone.show_call_log()
# --- Call Log ---
#   ↗ Outgoing to: +1-555-0199
#   ↙ Incoming from: +1-555-0200
# ----------------

iphone.charge(0)                   # Charge amount must be a positive number.
iphone.battery_level = 40
iphone.charge(20)                  # Charging... Battery is now at 60%
iphone.display_info()              # Uses the inherited method from ElectronicDevice
```

Notice that `iphone` can call `display_info()` and `charge()` even though those methods are defined in `ElectronicDevice`, not in `Phone`. That's the power of inheritance — the child class gets everything the parent has, for free.

### Inheritance in Action — Example 2: Server

```python
web_server = Server(
    brand="Dell",
    model="PowerEdge R750",
    storage_gb=10000,
    battery_mah=0,       # Servers are typically plugged in — no battery needed
    os="Ubuntu Server 22.04",
    ip_address="192.168.1.10",
    max_connections=500,
    rack_unit=2
)

web_server.power_on()
web_server.uptime_hours = 2000

# Simulate incoming traffic
for _ in range(3):
    web_server.accept_connection()

web_server.report_status()
# 🖥️  Server Status: 192.168.1.10
#    Uptime   : 2000 hours
#    Load     : 0.6% (3/500)
#    Battery  : 100%

web_server.drop_connection()
web_server.report_status()
```

---

## 7. Polymorphism — One Interface, Many Forms <a name="polymorphism"></a>

The word *polymorphism* comes from Greek, meaning "many forms". In OOP, it refers to the ability of **different objects to respond to the same method call in their own unique way**.

Imagine you have a list of electronic devices — a phone, a tablet, and a laptop. You want to call `display_info()` on each of them. Even though `Laptop` overrides `display_info()` to show extra details, you don't need to write different code for each type. You just call the same method, and each object does the right thing.

### Method Overriding

When a child class redefines a method that already exists in the parent class, it is **overriding** that method. The child's version takes precedence when called on a child object.

```python
class Phone(ElectronicDevice):
    # ... (previous code) ...

    def display_info(self):
        """Phone overrides display_info to add phone-specific details."""
        super().display_info()  # Still shows the base info
        print(f"  Phone # : {self.phone_number}")
        print(f"  5G      : {'Yes' if self.is_5g else 'No'}")
        print(f"-------------------")


class Server(ElectronicDevice):
    # ... (previous code) ...

    def display_info(self):
        """Server overrides display_info to show connection stats."""
        super().display_info()
        print(f"  IP Addr : {self.ip_address}")
        print(f"  Conns   : {self.active_connections}/{self.max_connections}")
        print(f"-------------------")
```

### Polymorphism in Action

```python
galaxy = Phone("Samsung", "Galaxy S24", 256, 4000, "Android", "+44-7700-000001", is_5g=True)
ipad = Tablet("Apple", "iPad Pro 12.9", 512, 10758, "iPadOS", screen_size_inches=12.9, has_stylus=True)
dell_server = Server("Dell", "PowerEdge R640", 8000, 0, "CentOS", "10.0.0.5", 1000, 1)

galaxy.power_on()
ipad.power_on()
dell_server.power_on()

# A list of different device types — treated uniformly
devices = [galaxy, ipad, dell_server]

# Same method call, different behaviour for each object
for device in devices:
    device.display_info()
    print()
```

Each object responds to `display_info()` in its own way — the phone shows its phone number, the server shows its IP and connections, and the tablet uses the default inherited version. **The calling code doesn't need to know what type each object is.** This is polymorphism at work.

---

## 8. Abstraction — Hiding Complexity <a name="abstraction"></a>

**Abstraction** means exposing only *what is necessary* to the outside world, and hiding the complex, messy internals. When you press the power button on your laptop, you don't need to understand the electrical sequences, firmware checks, or BIOS initialisation steps — you just press the button and it turns on.

In Python, we can enforce abstraction using **Abstract Base Classes (ABCs)**. An abstract class defines a *contract*: any class that inherits from it **must** implement the specified methods. The abstract class itself cannot be instantiated directly.

```python
from abc import ABC, abstractmethod

class ElectronicDevice(ABC):
    """
    An abstract base class for all electronic devices.
    
    By making this abstract, we ensure that every concrete device class
    (Phone, Tablet, Laptop, etc.) MUST implement the 'connect_to_network'
    method in its own way, because each device type connects differently.
    """

    def __init__(self, brand, model, storage_gb, battery_mah, os):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah
        self.os = os
        self.is_powered_on = False
        self.__battery_level = 100

    @abstractmethod
    def connect_to_network(self):
        """
        Every device must be able to connect to a network,
        but the HOW is up to each specific device type.
        """
        pass  # No implementation here — child classes MUST provide one

    def power_on(self):
        self.is_powered_on = True
        print(f"{self.brand} {self.model} is now ON.")

    @property
    def battery_level(self):
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value):
        if 0 <= value <= 100:
            self.__battery_level = value
```

```python
class Phone(ElectronicDevice):
    def __init__(self, brand, model, storage_gb, battery_mah, os, phone_number, is_5g):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.phone_number = phone_number
        self.is_5g = is_5g

    def connect_to_network(self):
        """Phones connect via cellular (4G/5G) or Wi-Fi."""
        network_type = "5G" if self.is_5g else "4G LTE"
        print(f"📶 {self.brand} {self.model} connected via {network_type} cellular network.")


class Server(ElectronicDevice):
    def __init__(self, brand, model, storage_gb, battery_mah, os, ip_address, max_connections, rack_unit):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.ip_address = ip_address
        self.max_connections = max_connections
        self.rack_unit = rack_unit
        self.active_connections = 0

    def connect_to_network(self):
        """Servers connect via hardwired Ethernet at high speeds."""
        print(f"🔌 {self.brand} {self.model} connected via 10GbE Ethernet. Static IP: {self.ip_address}")
```

```python
# You CANNOT instantiate an abstract class directly:
# device = ElectronicDevice(...)  ← This would raise a TypeError!

# But you CAN instantiate the concrete subclasses:
my_phone = Phone("OnePlus", "12", 256, 5400, "Android", "+1-555-9000", is_5g=True)
my_server = Server("HP", "ProLiant DL380", 20000, 0, "RHEL 9", "172.16.0.1", 2000, 2)

my_phone.connect_to_network()
# 📶 OnePlus 12 connected via 5G cellular network.

my_server.connect_to_network()
# 🔌 HP ProLiant DL380 connected via 10GbE Ethernet. Static IP: 172.16.0.1
```

> **The benefit of abstraction:** You can write code that works with *any* `ElectronicDevice` and call `connect_to_network()` without caring about the details. The abstraction guarantees that the method will always exist, and that each device will handle it appropriately.

---

## 9. Putting It All Together <a name="putting-it-all-together"></a>

Here is a complete, cohesive example that brings all four pillars together in one flowing demonstration:

```python
from abc import ABC, abstractmethod

# ─────────────────────────────────────────
# ROOT CLASS (Abstract Base)
# ─────────────────────────────────────────
class ElectronicDevice(ABC):

    def __init__(self, brand, model, storage_gb, battery_mah, os):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_mah = battery_mah
        self.os = os
        self.is_powered_on = False
        self.__battery_level = 100      # Encapsulated

    @property
    def battery_level(self):
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value):
        if 0 <= value <= 100:
            self.__battery_level = value
        else:
            print(f"⚠️ Invalid battery value: {value}")

    def power_on(self):
        if self.__battery_level > 0:
            self.is_powered_on = True
            print(f"✅ {self} powered ON. Battery: {self.__battery_level}%")
        else:
            print(f"❌ {self} cannot start — battery empty!")

    def power_off(self):
        self.is_powered_on = False
        print(f"🔴 {self} powered OFF.")

    def charge(self, amount):
        self.battery_level = min(100, self.__battery_level + amount)
        print(f"🔋 {self.brand} {self.model} battery: {self.__battery_level}%")

    @abstractmethod                     # Abstraction
    def connect_to_network(self):
        pass

    def display_info(self):
        print(f"\n{'='*40}")
        print(f"  {self.brand} {self.model}")
        print(f"  OS      : {self.os}")
        print(f"  Storage : {self.storage_gb} GB")
        print(f"  Battery : {self.__battery_level}%")
        print(f"  Power   : {'ON' if self.is_powered_on else 'OFF'}")

    def __str__(self):
        return f"{self.brand} {self.model}"


# ─────────────────────────────────────────
# CHILD CLASSES (Inheritance)
# ─────────────────────────────────────────
class Phone(ElectronicDevice):
    def __init__(self, brand, model, storage_gb, battery_mah, os, phone_number, is_5g):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.phone_number = phone_number
        self.is_5g = is_5g

    def connect_to_network(self):       # Polymorphism
        net = "5G" if self.is_5g else "4G LTE"
        print(f"📶 {self} online via {net}")

    def display_info(self):             # Polymorphism
        super().display_info()
        print(f"  Phone # : {self.phone_number}")
        print(f"  5G      : {'Yes' if self.is_5g else 'No'}")
        print(f"{'='*40}\n")


class Laptop(ElectronicDevice):
    def __init__(self, brand, model, storage_gb, battery_mah, os, ram_gb, cpu_model):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.ram_gb = ram_gb
        self.cpu_model = cpu_model
        self.open_apps = []

    def connect_to_network(self):       # Polymorphism
        print(f"📡 {self} online via Wi-Fi 6E")

    def open_application(self, app):
        if self.is_powered_on:
            self.open_apps.append(app)
            print(f"💻 Running: {app}")
        else:
            print("Power on the laptop first!")

    def display_info(self):             # Polymorphism
        super().display_info()
        print(f"  RAM     : {self.ram_gb} GB")
        print(f"  CPU     : {self.cpu_model}")
        print(f"  Apps    : {', '.join(self.open_apps) or 'None'}")
        print(f"{'='*40}\n")


class Server(ElectronicDevice):
    def __init__(self, brand, model, storage_gb, battery_mah, os, ip_address, max_connections):
        super().__init__(brand, model, storage_gb, battery_mah, os)
        self.ip_address = ip_address
        self.max_connections = max_connections
        self.active_connections = 0

    def connect_to_network(self):       # Polymorphism
        print(f"🔌 {self} online via 10GbE Ethernet. IP: {self.ip_address}")

    def accept_connection(self):
        if self.active_connections < self.max_connections:
            self.active_connections += 1
            print(f"Connection #{self.active_connections} accepted.")
        else:
            print("Server at max capacity!")

    def display_info(self):             # Polymorphism
        super().display_info()
        print(f"  IP Addr : {self.ip_address}")
        print(f"  Load    : {self.active_connections}/{self.max_connections}")
        print(f"{'='*40}\n")


# ─────────────────────────────────────────
# DEMONSTRATION
# ─────────────────────────────────────────
if __name__ == "__main__":
    # Create our device fleet
    pixel = Phone("Google", "Pixel 8 Pro", 128, 5050, "Android 14", "+1-555-7777", is_5g=True)
    macbook = Laptop("Apple", "MacBook Pro 14", 1000, 69600, "macOS Sonoma", ram_gb=32, cpu_model="M3 Pro")
    blade = Server("Dell", "PowerEdge R750", 12000, 0, "Ubuntu 22.04", "192.168.0.50", max_connections=1000)

    all_devices = [pixel, macbook, blade]

    # Power everything on and connect to the network
    for device in all_devices:
        device.power_on()
        device.connect_to_network()     # Polymorphism — each device connects differently!

    print("\n--- Simulating usage ---\n")

    pixel.battery_level = 20
    pixel.charge(50)

    macbook.open_application("VS Code")
    macbook.open_application("Chrome")

    for _ in range(5):
        blade.accept_connection()

    print("\n--- Final Device Reports ---")
    for device in all_devices:
        device.display_info()           # Polymorphism — each shows its own details!
```

---

## Summary of Key Concepts

| Concept | What It Means | In Our Example |
|---|---|---|
| **Class** | A blueprint for creating objects | `ElectronicDevice` is the root blueprint |
| **Object** | A concrete instance of a class | `pixel`, `macbook`, `blade` are objects |
| **Attribute** | Data stored on an object | `brand`, `model`, `battery_level` |
| **Method** | A function belonging to a class | `power_on()`, `charge()`, `connect_to_network()` |
| **`__init__`** | Constructor — runs when an object is created | Sets `brand`, `model`, etc. on creation |
| **Encapsulation** | Protecting internal data with access controls | `__battery_level` is private; accessed via `@property` |
| **Inheritance** | Child class extends parent class | `Phone`, `Laptop`, `Server` all extend `ElectronicDevice` |
| **Polymorphism** | Same method, different behaviour per class | `connect_to_network()` and `display_info()` behave differently for each device |
| **Abstraction** | Enforcing a contract; hiding complexity | `ABC` forces subclasses to implement `connect_to_network()` |
| **`super()`** | Calls the parent class's version of a method | `Phone.__init__` calls `super().__init__()` to initialise shared attributes |

---

*Happy coding — and remember, every great program is just a well-designed collection of objects working together!* 🚀
