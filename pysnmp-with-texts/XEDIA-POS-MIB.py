#
# PySNMP MIB module XEDIA-POS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/XEDIA-POS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 15:43:01 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Bits, Gauge32, TimeTicks, iso, Counter32, NotificationType, Unsigned32, MibIdentifier, Counter64, ObjectIdentity, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Gauge32", "TimeTicks", "iso", "Counter32", "NotificationType", "Unsigned32", "MibIdentifier", "Counter64", "ObjectIdentity", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "ModuleIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
xediaMibs, = mibBuilder.importSymbols("XEDIA-REG", "xediaMibs")
xediaPosMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 838, 3, 39))
if mibBuilder.loadTexts: xediaPosMIB.setLastUpdated('9801142155Z')
if mibBuilder.loadTexts: xediaPosMIB.setOrganization('Xedia Corp.')
if mibBuilder.loadTexts: xediaPosMIB.setContactInfo('support@xedia.com')
if mibBuilder.loadTexts: xediaPosMIB.setDescription('This module defines additional objects for management of PoS links in Xedia devices, above and beyond what is defined in the standard SONET MIB.')
xPosTables = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 39, 1))
xPosConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 39, 2))
xPosInterfaceConfTable = MibTable((1, 3, 6, 1, 4, 1, 838, 3, 39, 1, 1), )
if mibBuilder.loadTexts: xPosInterfaceConfTable.setStatus('current')
if mibBuilder.loadTexts: xPosInterfaceConfTable.setDescription('The Xedia POS Interface Configuration Table contains extensions to the POS Interface Configuration Table, one entry per POS interface.')
xPosInterfaceConfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 838, 3, 39, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: xPosInterfaceConfEntry.setStatus('current')
if mibBuilder.loadTexts: xPosInterfaceConfEntry.setDescription('An entry in the Xedia POS Interface Configuration Table.')
xPosConfigCrcMode = MibTableColumn((1, 3, 6, 1, 4, 1, 838, 3, 39, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("crc16", 1), ("crc32", 2))).clone('crc32')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xPosConfigCrcMode.setStatus('current')
if mibBuilder.loadTexts: xPosConfigCrcMode.setDescription('The configured CRC mode of the interface.')
xPosCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 1))
xPosGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 2))
xPosCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 1, 1)).setObjects(("XEDIA-POS-MIB", "xPosAllGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xPosCompliance = xPosCompliance.setStatus('current')
if mibBuilder.loadTexts: xPosCompliance.setDescription('The compliance statement for all agents that support this MIB. A compliant agent implements all objects defined in this MIB.')
xPosAllGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 838, 3, 39, 2, 2, 1)).setObjects(("XEDIA-POS-MIB", "xPosConfigCrcMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    xPosAllGroup = xPosAllGroup.setStatus('current')
if mibBuilder.loadTexts: xPosAllGroup.setDescription('The set of all accessible objects in this MIB.')
mibBuilder.exportSymbols("XEDIA-POS-MIB", xPosInterfaceConfEntry=xPosInterfaceConfEntry, xediaPosMIB=xediaPosMIB, xPosGroups=xPosGroups, xPosConfigCrcMode=xPosConfigCrcMode, xPosCompliances=xPosCompliances, xPosCompliance=xPosCompliance, xPosAllGroup=xPosAllGroup, xPosConformance=xPosConformance, xPosTables=xPosTables, xPosInterfaceConfTable=xPosInterfaceConfTable, PYSNMP_MODULE_ID=xediaPosMIB)
