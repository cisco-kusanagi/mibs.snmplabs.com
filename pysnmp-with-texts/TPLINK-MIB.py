#
# PySNMP MIB module TPLINK-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TPLINK-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:24:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
TimeTicks, Bits, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, ModuleIdentity, enterprises, Unsigned32, MibIdentifier, ObjectIdentity, Gauge32, IpAddress, Integer32, iso, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Bits", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "ModuleIdentity", "enterprises", "Unsigned32", "MibIdentifier", "ObjectIdentity", "Gauge32", "IpAddress", "Integer32", "iso", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
tplink = MibIdentifier((1, 3, 6, 1, 4, 1, 11863))
switch = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 1))
router = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 2))
wireless = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 3))
adsl = MibIdentifier((1, 3, 6, 1, 4, 1, 11863, 4))
tplinkProducts = ObjectIdentity((1, 3, 6, 1, 4, 1, 11863, 5))
if mibBuilder.loadTexts: tplinkProducts.setStatus('current')
if mibBuilder.loadTexts: tplinkProducts.setDescription('tplinkProducts is the root OBJECT IDENTIFIER from which sysObjectID values are assigned. Actual values are defined in TPLINK-PRODUCTS-MIB.')
tplinkMgmt = ObjectIdentity((1, 3, 6, 1, 4, 1, 11863, 6))
if mibBuilder.loadTexts: tplinkMgmt.setStatus('current')
if mibBuilder.loadTexts: tplinkMgmt.setDescription('tplinkMgmt is the main subtree for new mib development.')
mibBuilder.exportSymbols("TPLINK-MIB", wireless=wireless, router=router, tplinkMgmt=tplinkMgmt, adsl=adsl, tplinkProducts=tplinkProducts, switch=switch, tplink=tplink)
