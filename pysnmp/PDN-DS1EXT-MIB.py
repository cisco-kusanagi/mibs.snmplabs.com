#
# PySNMP MIB module PDN-DS1EXT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-DS1EXT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ent_ds1, = mibBuilder.importSymbols("PDN-HEADER-MIB", "ent-ds1")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, iso, Counter32, ModuleIdentity, TimeTicks, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, Counter64, Unsigned32, IpAddress, ObjectIdentity, MibIdentifier = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "iso", "Counter32", "ModuleIdentity", "TimeTicks", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "Counter64", "Unsigned32", "IpAddress", "ObjectIdentity", "MibIdentifier")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
pdnDs1Ext = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5))
if mibBuilder.loadTexts: pdnDs1Ext.setLastUpdated('200204050000Z')
if mibBuilder.loadTexts: pdnDs1Ext.setOrganization('Paradyne Corp MIB Working Group')
pdnDs1ExtObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1))
pdnDs1ExtConfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1), )
if mibBuilder.loadTexts: pdnDs1ExtConfTable.setStatus('current')
pdnDs1ExtConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: pdnDs1ExtConfEntry.setStatus('current')
pdnDs1ExtConfLineLengthType = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("shortHaul", 1), ("longHaul", 2))).clone('longHaul')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfLineLengthType.setStatus('current')
pdnDs1ExtConfLineLength = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))).clone(namedValues=NamedValues(("feet000To133", 1), ("feet134To266", 2), ("feet267To399", 3), ("feet400To533", 4), ("feet534To655", 5))).clone('feet000To133')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfLineLength.setStatus('current')
pdnDs1ExtConfLineBuildOut = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dB0Pnt0", 1), ("dB7Pnt5", 2), ("dB15Pnt0", 3), ("dB22Pnt5", 4))).clone('dB0Pnt0')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfLineBuildOut.setStatus('current')
pdnDs1ExtConfConnector = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("bnc", 1), ("rj48", 2))).clone('rj48')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: pdnDs1ExtConfConnector.setStatus('current')
pdnDs1ExtConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2))
pdnDs1ExtGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1))
pdnDs1ExtCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2))
pdnDs1ExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2, 1)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtT1ConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtCompliance = pdnDs1ExtCompliance.setStatus('current')
pdnDs1ExtG703Compliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 2, 2)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtE1ConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtG703Compliance = pdnDs1ExtG703Compliance.setStatus('current')
pdnDs1ExtT1ConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1, 1)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLengthType"), ("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLength"), ("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineBuildOut"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtT1ConfigGroup = pdnDs1ExtT1ConfigGroup.setStatus('current')
pdnDs1ExtE1ConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 6, 5, 5, 2, 1, 2)).setObjects(("PDN-DS1EXT-MIB", "pdnDs1ExtConfLineLengthType"), ("PDN-DS1EXT-MIB", "pdnDs1ExtConfConnector"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnDs1ExtE1ConfigGroup = pdnDs1ExtE1ConfigGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-DS1EXT-MIB", pdnDs1ExtConformance=pdnDs1ExtConformance, pdnDs1Ext=pdnDs1Ext, pdnDs1ExtCompliance=pdnDs1ExtCompliance, pdnDs1ExtE1ConfigGroup=pdnDs1ExtE1ConfigGroup, pdnDs1ExtG703Compliance=pdnDs1ExtG703Compliance, pdnDs1ExtT1ConfigGroup=pdnDs1ExtT1ConfigGroup, pdnDs1ExtConfTable=pdnDs1ExtConfTable, pdnDs1ExtConfLineLength=pdnDs1ExtConfLineLength, pdnDs1ExtGroups=pdnDs1ExtGroups, PYSNMP_MODULE_ID=pdnDs1Ext, pdnDs1ExtObjects=pdnDs1ExtObjects, pdnDs1ExtCompliances=pdnDs1ExtCompliances, pdnDs1ExtConfLineBuildOut=pdnDs1ExtConfLineBuildOut, pdnDs1ExtConfConnector=pdnDs1ExtConfConnector, pdnDs1ExtConfLineLengthType=pdnDs1ExtConfLineLengthType, pdnDs1ExtConfEntry=pdnDs1ExtConfEntry)
