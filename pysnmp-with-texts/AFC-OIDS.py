#
# PySNMP MIB module AFC-OIDS (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AFC-OIDS
# Produced by pysmi-0.3.4 at Wed May  1 11:15:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Gauge32, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Bits, Unsigned32, Counter64, MibIdentifier, iso, IpAddress, ObjectIdentity, TimeTicks, ModuleIdentity, Integer32, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Bits", "Unsigned32", "Counter64", "MibIdentifier", "iso", "IpAddress", "ObjectIdentity", "TimeTicks", "ModuleIdentity", "Integer32", "Counter32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
afc = MibIdentifier((1, 3, 6, 1, 4, 1, 2067))
afcProducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1))
umc = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 1))
umcCommon = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 1, 1))
umc1000 = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 1, 2))
afcEms = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 2))
afcEmsPlatformSpecific = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 2, 1))
afcEmsOV = MibIdentifier((1, 3, 6, 1, 4, 1, 2067, 1, 2, 1, 1))
mibBuilder.exportSymbols("AFC-OIDS", umc=umc, afcEmsOV=afcEmsOV, umcCommon=umcCommon, afcEmsPlatformSpecific=afcEmsPlatformSpecific, afcProducts=afcProducts, afc=afc, umc1000=umc1000, afcEms=afcEms)
