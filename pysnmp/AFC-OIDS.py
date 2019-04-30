#
# PySNMP MIB module AFC-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AFC-OIDS
# Produced by pysmi-0.3.4 at Mon Apr 29 17:00:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Integer32, NotificationType, IpAddress, iso, Counter32, Gauge32, enterprises, ObjectIdentity, MibIdentifier, Counter64, ModuleIdentity, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Integer32", "NotificationType", "IpAddress", "iso", "Counter32", "Gauge32", "enterprises", "ObjectIdentity", "MibIdentifier", "Counter64", "ModuleIdentity", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
afc = MibIdentifier((1, 3, 6, 1, 4, 1, 2067))
afcProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1))
umc = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 1))
umcCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 1, 1))
umc1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 1, 2))
afcEms = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 2))
afcEmsPlatformSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 2, 1))
afcEmsOV = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 2, 1, 1))
mibBuilder.exportSymbols("AFC-OIDS", afcEmsPlatformSpecific=afcEmsPlatformSpecific, umc=umc, afcEmsOV=afcEmsOV, umcCommon=umcCommon, umc1000=umc1000, afc=afc, afcEms=afcEms, afcProducts=afcProducts)
