# Feel free to cleanup this file by removing comments, once you have memorised them ;)

%define device sirius
%define vendor xiaomi

# Manufacturer and device name to be shown in UI
%define vendor_pretty Xiaomi
%define device_pretty MI 8 SE

# See ../droid-hal-version/droid-hal-device.inc for similar macros:
%define have_vibrator_native 1
%define have_led 1

%include droid-hal-version/droid-hal-version.inc

# IMPORTANT if you want to comment out any macros in your .spec, delete the %
# sign, otherwise they will remain defined! E.g.:
#define some_macro "I'll not be defined because I don't have % in front"

