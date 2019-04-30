#
# PySNMP MIB module SONOMASYSTEMS-SONOMA-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SONOMASYSTEMS-SONOMA-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:01:17 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Counter64, Gauge32, Counter32, IpAddress, TimeTicks, enterprises, ModuleIdentity, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, MibIdentifier, Integer32, iso, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "Gauge32", "Counter32", "IpAddress", "TimeTicks", "enterprises", "ModuleIdentity", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "MibIdentifier", "Integer32", "iso", "Unsigned32", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
sonomaSystems = MibIdentifier((1, 3, 6, 1, 4, 1, 2926))
sonomaSeries = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25))
sonomaATM = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 7))
sonomaLAN = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 5))
sonomaApplications = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 8))
sonomaRouting = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 4))
sonomaBridging = MibIdentifier((1, 3, 6, 1, 4, 1, 2926, 25, 3))
mibBuilder.exportSymbols("SONOMASYSTEMS-SONOMA-MIB", sonomaRouting=sonomaRouting, sonomaSystems=sonomaSystems, sonomaSeries=sonomaSeries, sonomaLAN=sonomaLAN, sonomaATM=sonomaATM, sonomaApplications=sonomaApplications, sonomaBridging=sonomaBridging)
