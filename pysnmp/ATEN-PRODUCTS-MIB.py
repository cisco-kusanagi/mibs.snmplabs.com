#
# PySNMP MIB module ATEN-PRODUCTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ATEN-PRODUCTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:14:51 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion")
atenProducts, = mibBuilder.importSymbols("ATEN-SMI", "atenProducts")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, MibIdentifier, ObjectIdentity, Counter64, Gauge32, Bits, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter32, iso, NotificationType, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "MibIdentifier", "ObjectIdentity", "Counter64", "Gauge32", "Bits", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter32", "iso", "NotificationType", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
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
mibBuilder.exportSymbols("ATEN-PRODUCTS-MIB", public=public, software=software, firewire=firewire, video=video, sn0116a=sn0116a, pn9108=pn9108, usb=usb, kvmoverip=kvmoverip, serialoverip=serialoverip, kvm=kvm, poweroverip=poweroverip, sn3101=sn3101, overip=overip)
