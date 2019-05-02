#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:09:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibIdentifier, ModuleIdentity, TimeTicks, NotificationType, Gauge32, iso, Counter64, ObjectIdentity, IpAddress, Integer32, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, enterprises, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "TimeTicks", "NotificationType", "Gauge32", "iso", "Counter64", "ObjectIdentity", "IpAddress", "Integer32", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "enterprises", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonomaSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 2926))
sonomaSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25))
sonomaATM = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 7))
sonomaLAN = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 5))
sonomaApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 8))
sonomaRouting = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 4))
sonomaBridging = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 3))
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-MIB", sonomaSeries=sonomaSeries, sonomaRouting=sonomaRouting, sonomaApplications=sonomaApplications, sonomaATM=sonomaATM, sonomaLAN=sonomaLAN, sonomaBridging=sonomaBridging, sonomaSystems=sonomaSystems)
