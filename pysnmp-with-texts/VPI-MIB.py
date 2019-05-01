#
# PySNMP MIB module VPI-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPI-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:35:16 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, Integer32, TimeTicks, Gauge32, ObjectIdentity, Counter32, Counter64, enterprises, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, iso, ModuleIdentity, MibIdentifier, Unsigned32, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Integer32", "TimeTicks", "Gauge32", "ObjectIdentity", "Counter32", "Counter64", "enterprises", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "iso", "ModuleIdentity", "MibIdentifier", "Unsigned32", "IpAddress")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
voiceprint = MibIdentifier((1, 3, 6, 1, 4, 1, 15191))
software = MibIdentifier((1, 3, 6, 1, 4, 1, 15191, 1))
mibBuilder.exportSymbols("VPI-MIB", voiceprint=voiceprint, software=software)
