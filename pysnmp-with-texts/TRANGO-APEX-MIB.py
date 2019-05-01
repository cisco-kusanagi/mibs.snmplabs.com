#
# PySNMP MIB module TRANGO-APEX-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRANGO-APEX-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:26:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, ModuleIdentity, Counter32, enterprises, iso, TimeTicks, Counter64, Gauge32, MibIdentifier, NotificationType, Bits, ObjectIdentity, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "ModuleIdentity", "Counter32", "enterprises", "iso", "TimeTicks", "Counter64", "Gauge32", "MibIdentifier", "NotificationType", "Bits", "ObjectIdentity", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
trango = MibIdentifier((1, 3, 6, 1, 4, 1, 5454))
tbw = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1))
apex = MibIdentifier((1, 3, 6, 1, 4, 1, 5454, 1, 60))
mibBuilder.exportSymbols("TRANGO-APEX-MIB", trango=trango, tbw=tbw, apex=apex)
