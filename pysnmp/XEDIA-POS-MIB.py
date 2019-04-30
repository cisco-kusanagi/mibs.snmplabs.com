#
# PySNMP MIB module XEDIA-POS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-POS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:36:32 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, MibIdentifier, ObjectIdentity, ModuleIdentity, Bits, Counter32, iso, Counter64, Unsigned32, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "MibIdentifier", "ObjectIdentity", "ModuleIdentity", "Bits", "Counter32", "iso", "Counter64", "Unsigned32", "Integer32", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaPosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 39))
if mibBuilder.loadTexts: xediaPosMIB.setLastUpdated('9801142155Z')
if mibBuilder.loadTexts: xediaPosMIB.setOrganization('Xedia Corp.')
xPosTables = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 39, 1))
xPosConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 39, 2))
xPosInterfaceConfTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 39, 1, 1), )
if mibBuilder.loadTexts: xPosInterfaceConfTable.setStatus('current')
xPosInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 39, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xPosInterfaceConfEntry.setStatus('current')
xPosConfigCrcMode = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 39, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc16", 1), ("crc32", 2))).clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xPosConfigCrcMode.setStatus('current')
xPosCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 1))
xPosGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 2))
xPosCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 1, 1)).setObjects(("XEDIA-POS-MIB", "xPosAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xPosCompliance = xPosCompliance.setStatus('current')
xPosAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 2, 1)).setObjects(("XEDIA-POS-MIB", "xPosConfigCrcMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xPosAllGroup = xPosAllGroup.setStatus('current')
mibBuilder.exportSymbols("XEDIA-POS-MIB", xPosAllGroup=xPosAllGroup, xediaPosMIB=xediaPosMIB, xPosConformance=xPosConformance, xPosConfigCrcMode=xPosConfigCrcMode, xPosCompliances=xPosCompliances, xPosGroups=xPosGroups, PYSNMP_MODULE_ID=xediaPosMIB, xPosCompliance=xPosCompliance, xPosInterfaceConfEntry=xPosInterfaceConfEntry, xPosInterfaceConfTable=xPosInterfaceConfTable, xPosTables=xPosTables)
