#
# PySNMP MIB module CORIOLIS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CORIOLIS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:46:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Integer32, iso, enterprises, ModuleIdentity, ObjectIdentity, Bits, NotificationType, Unsigned32, Counter64, Counter32, Gauge32, IpAddress, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "iso", "enterprises", "ModuleIdentity", "ObjectIdentity", "Bits", "NotificationType", "Unsigned32", "Counter64", "Counter32", "Gauge32", "IpAddress", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
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
mibBuilder.exportSymbols("CORIOLIS-MIB", card=card, eventlog=eventlog, ne=ne, circuit=circuit, routing=routing, device=device, port=port, ring=ring, coriolisMibs=coriolisMibs, interfaces=interfaces)
