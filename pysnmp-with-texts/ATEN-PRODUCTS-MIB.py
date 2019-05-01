#
# PySNMP MIB module ATEN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATEN-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:30:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
atenProducts, = mibBuilder.importSymbols("ATEN-SMI", "atenProducts")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, iso, Integer32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ObjectIdentity, NotificationType, TimeTicks, Counter32, Unsigned32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "iso", "Integer32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ObjectIdentity", "NotificationType", "TimeTicks", "Counter32", "Unsigned32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
public = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 1))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 2))
overip = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3))
kvm = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 4))
video = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 5))
usb = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 6))
firewire = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 7))
kvmoverip = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 1))
poweroverip = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 2))
serialoverip = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3))
pn9108 = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 2, 1))
sn0116a = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 1))
sn3101 = MibIdentifier((1, 3, 6, 1, 4, 1, 21317, 1, 3, 3, 2))
mibBuilder.exportSymbols("ATEN-PRODUCTS-MIB", usb=usb, overip=overip, sn3101=sn3101, sn0116a=sn0116a, poweroverip=poweroverip, video=video, public=public, pn9108=pn9108, software=software, firewire=firewire, kvmoverip=kvmoverip, kvm=kvm, serialoverip=serialoverip)
