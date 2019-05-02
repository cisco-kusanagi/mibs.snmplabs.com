#
# PySNMP MIB module ASCEND-WAN-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-WAN-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
advancedAgent, = mibBuilder.importSymbols("ASCEND-MIB", "advancedAgent")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, MibIdentifier, iso, Bits, Counter64, ModuleIdentity, ObjectIdentity, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "MibIdentifier", "iso", "Bits", "Counter64", "ModuleIdentity", "ObjectIdentity", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
wanTypeAny = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 1))
wanTypeT1 = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 2))
wanTypeE1 = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 3))
wanTypeDpnss = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 4))
wanTypeBri = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 5))
wanTypeS562 = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 6))
wanTypeS564 = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 7))
wanTypeSdsl = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 8))
wanTypeAdslCap = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 9))
wanTypeAdslDmt = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 10))
wanTypeHdsl2 = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 4, 12))
mibBuilder.exportSymbols("ASCEND-WAN-MIB", wanTypeBri=wanTypeBri, wanTypeDpnss=wanTypeDpnss, wanTypeSdsl=wanTypeSdsl, wanTypeS564=wanTypeS564, wanTypeS562=wanTypeS562, wanTypeHdsl2=wanTypeHdsl2, wanTypeE1=wanTypeE1, wanTypeAdslCap=wanTypeAdslCap, wanTypeAdslDmt=wanTypeAdslDmt, wanTypeAny=wanTypeAny, wanTypeT1=wanTypeT1)
