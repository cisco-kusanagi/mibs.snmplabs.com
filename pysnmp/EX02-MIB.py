#
# PySNMP MIB module EX02-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/EX02-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:52:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, ModuleIdentity, Gauge32, MibIdentifier, iso, TimeTicks, Integer32, experimental, Unsigned32, Counter64, NotificationType, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "ModuleIdentity", "Gauge32", "MibIdentifier", "iso", "TimeTicks", "Integer32", "experimental", "Unsigned32", "Counter64", "NotificationType", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ex01Module = ModuleIdentity((1, 3, 6, 1, 3, 1194))
if mibBuilder.loadTexts: ex01Module.setLastUpdated('9602010000Z')
if mibBuilder.loadTexts: ex01Module.setOrganization('MIB Testers')
ex01Test = MibIdentifier((1, 3, 6, 1, 3, 1195))
aTable = MibTable((1, 3, 6, 1, 3, 1195, 1), )
if mibBuilder.loadTexts: aTable.setStatus('current')
aEntry = MibTableRow((1, 3, 6, 1, 3, 1195, 1, 1), ).setIndexNames((0, "EX02-MIB", "aIndex"))
if mibBuilder.loadTexts: aEntry.setStatus('current')
aIndex = MibTableColumn((1, 3, 6, 1, 3, 1195, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("red", 1), ("green", 2), ("blue", 3))))
if mibBuilder.loadTexts: aIndex.setStatus('current')
aOct1 = MibTableColumn((1, 3, 6, 1, 3, 1195, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)).clone('a default value')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aOct1.setStatus('current')
aOct2 = MibTableColumn((1, 3, 6, 1, 3, 1195, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 16)).clone(hexValue="0a23bc")).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aOct2.setStatus('current')
aInt1 = MibTableColumn((1, 3, 6, 1, 3, 1195, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 10)).clone(5)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: aInt1.setStatus('current')
oG = ObjectGroup((1, 3, 6, 1, 3, 1194, 1)).setObjects(("EX02-MIB", "aOct1"), ("EX02-MIB", "aOct2"), ("EX02-MIB", "aInt1"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oG = oG.setStatus('current')
mibBuilder.exportSymbols("EX02-MIB", PYSNMP_MODULE_ID=ex01Module, aOct1=aOct1, aOct2=aOct2, aEntry=aEntry, aTable=aTable, oG=oG, aInt1=aInt1, ex01Test=ex01Test, ex01Module=ex01Module, aIndex=aIndex)
