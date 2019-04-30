#
# PySNMP MIB module TPLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:16:41 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, TimeTicks, Bits, iso, ObjectIdentity, MibIdentifier, enterprises, IpAddress, Counter32, Counter64, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "TimeTicks", "Bits", "iso", "ObjectIdentity", "MibIdentifier", "enterprises", "IpAddress", "Counter32", "Counter64", "Integer32", "Unsigned32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplink = MibIdentifier((1, 3, 6, 1, 4, 1, 11863))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 1))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 2))
wireless = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 3))
adsl = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 4))
tplinkProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 11863, 5))
if mibBuilder.loadTexts: tplinkProducts.setStatus('current')
tplinkMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 11863, 6))
if mibBuilder.loadTexts: tplinkMgmt.setStatus('current')
mibBuilder.exportSymbols("TPLINK-MIB", tplinkMgmt=tplinkMgmt, switch=switch, adsl=adsl, tplinkProducts=tplinkProducts, router=router, wireless=wireless, tplink=tplink)
