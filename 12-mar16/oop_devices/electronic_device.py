"""
electronic_device.py
────────────────────
The ROOT class for all electronic devices.

This module defines the abstract base class `ElectronicDevice`.
Every concept in this OOP guide (encapsulation, inheritance,
polymorphism, abstraction) builds on top of this foundation.
"""

from abc import ABC, abstractmethod


# ══════════════════════════════════════════════════════════════════
#  ROOT / PARENT CLASS
# ══════════════════════════════════════════════════════════════════

class ElectronicDevice(ABC):
    """
    Abstract base class — the shared blueprint for every electronic device.

    ABSTRACTION in action:
      - This class is marked ABC (Abstract Base Class).
      - It declares connect_to_network() as @abstractmethod.
      - That means Python will REFUSE to let you create an ElectronicDevice
        directly; every subclass MUST provide its own connect_to_network().

    ENCAPSULATION in action:
      - battery_level is stored as a private attribute (__battery_level).
      - All reads/writes go through the @property getter and setter,
        which enforce the 0–100 range rule.
    """

    # ------------------------------------------------------------------
    #  Constructor  (__init__)
    # ------------------------------------------------------------------
    def __init__(self, brand, model, storage_gb, battery_mah, os):
        # Public attributes — visible and readable by anyone
        self.brand        = brand         # e.g. "Apple", "Samsung"
        self.model        = model         # e.g. "iPhone 15", "Galaxy S24"
        self.storage_gb   = storage_gb    # Internal storage in GB
        self.battery_mah  = battery_mah   # Physical battery capacity (mAh)
        self.os           = os            # Operating system name
        self.is_powered_on = False        # Devices always start OFF

        # Private attribute — the leading __ hides it from outside code
        self.__battery_level = 100        # Battery starts fully charged

    # ------------------------------------------------------------------
    #  ENCAPSULATION — @property getter & setter for battery_level
    # ------------------------------------------------------------------
    @property
    def battery_level(self):
        """Read the battery level safely (getter)."""
        return self.__battery_level

    @battery_level.setter
    def battery_level(self, value):
        """
        Write the battery level safely (setter).
        Rejects any value outside 0–100, protecting internal state.
        """
        if 0 <= value <= 100:
            self.__battery_level = value
        else:
            print(f"  ⚠️  Invalid battery value '{value}' — must be 0 to 100. No change made.")

    # ------------------------------------------------------------------
    #  Shared METHODS — inherited by every subclass for free
    # ------------------------------------------------------------------
    def power_on(self):
        """Powers the device on — only if the battery isn't dead."""
        if self.__battery_level > 0:
            self.is_powered_on = True
            print(f"  ✅  {self.brand} {self.model} powered ON  "
                  f"(battery: {self.__battery_level}%)")
        else:
            print(f"  ❌  {self.brand} {self.model} cannot start — battery is empty!")

    def power_off(self):
        """Gracefully shuts the device down."""
        self.is_powered_on = False
        print(f"  🔴  {self.brand} {self.model} powered OFF.")

    def charge(self, amount):
        """
        Charges the device by `amount` percent.
        The battery is capped at 100% — no over-charging!
        """
        if amount <= 0:
            print("  ⚠️  Charge amount must be a positive number.")
            return
        new_level = min(100, self.__battery_level + amount)
        self.battery_level = new_level
        print(f"  🔋  Charging {self.brand} {self.model}... battery now at {self.__battery_level}%")

    def display_info(self):
        """
        Prints a status card for the device.
        Subclasses call super().display_info() and then add their own lines.
        """
        status = "ON ✅" if self.is_powered_on else "OFF 🔴"
        print(f"  {'─'*36}")
        print(f"  {'Device:':10} {self.brand} {self.model}")
        print(f"  {'OS:':10} {self.os}")
        print(f"  {'Storage:':10} {self.storage_gb} GB")
        print(f"  {'Battery:':10} {self.__battery_level}%")
        print(f"  {'Status:':10} {status}")

    # ------------------------------------------------------------------
    #  ABSTRACTION — abstract method; subclasses MUST implement this
    # ------------------------------------------------------------------
    @abstractmethod
    def connect_to_network(self):
        """
        Every device must be able to connect to a network.
        HOW it connects (cellular, Wi-Fi, Ethernet…) is left to each
        subclass to define — that's the contract enforced by abstraction.
        """
        pass  # No body here on purpose

    # ------------------------------------------------------------------
    #  __str__ — human-readable label for print() and f-strings
    # ------------------------------------------------------------------
    def __str__(self):
        return f"{self.brand} {self.model} [{self.os}]"
