#
# PySNMP MIB module CORIOLIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CORIOLIS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:29:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, TimeTicks, enterprises, NotificationType, Gauge32, MibIdentifier, Unsigned32, Integer32, ObjectIdentity, Bits, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "TimeTicks", "enterprises", "NotificationType", "Gauge32", "MibIdentifier", "Unsigned32", "Integer32", "ObjectIdentity", "Bits", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
coriolisMibs = MibIdentifier((1, 3, 6, 1, 4, 1, 5812))
device = MibIdentifier((1, 3, 6, 1, 4, 1, 5812, 1))
card = MibIdentifier((1, 3, 6, 1, 4, 1, 5812, 2))
port = MibIdentifier((1, 3, 6, 1, 4, 1, 5812, 3))
ring = MibIdentifier((1, 3, 6, 1, 4, 1, 5812, 4))
ne = MibIdentifier((1, 3, 6, 1, 4, 1, 5812, 5))
circuit = MibIdentifier((1, 3, 6, 1, 4, 1, 5812, 6))
routing = MibIdentifier((1, 3, 6, 1, 4, 1, 5812, 7))
interfaces = MibIdentifier((1, 3, 6, 1, 4, 1, 5812, 8))
eventlog = MibIdentifier((1, 3, 6, 1, 4, 1, 5812, 9))
mibBuilder.exportSymbols("CORIOLIS-MIB", routing=routing, interfaces=interfaces, coriolisMibs=coriolisMibs, device=device, port=port, card=card, ne=ne, ring=ring, circuit=circuit, eventlog=eventlog)
