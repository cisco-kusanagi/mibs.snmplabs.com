#
# PySNMP MIB module PDN-ATM-BRIDGE-IWF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PDN-ATM-BRIDGE-IWF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:29:03 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
pdn_common, = mibBuilder.importSymbols("PDN-HEADER-MIB", "pdn-common")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
NotificationType, Gauge32, iso, Unsigned32, Counter64, ObjectIdentity, MibIdentifier, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, TimeTicks, Counter32, ModuleIdentity, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "iso", "Unsigned32", "Counter64", "ObjectIdentity", "MibIdentifier", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "TimeTicks", "Counter32", "ModuleIdentity", "IpAddress")
TextualConvention, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "RowStatus")
pdnAtmBridgeIwfMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43))
pdnAtmBridgeIwfMIB.setRevisions(('2003-04-24 00:00', '2003-03-24 00:00', '2003-03-17 00:00',))
if mibBuilder.loadTexts: pdnAtmBridgeIwfMIB.setLastUpdated('200303240000Z')
if mibBuilder.loadTexts: pdnAtmBridgeIwfMIB.setOrganization('Paradyne Networks MIB Working Group Other information about group editing the MIB')
pdnAtmBridgeIwfNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 0))
pdnAtmBridgeIwfObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1))
pdnAtmBridgeIwfConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2))
pdnAtmBridgeIwfTable = MibTable((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1), )
if mibBuilder.loadTexts: pdnAtmBridgeIwfTable.setStatus('current')
pdnAtmBridgeIwfEntry = MibTableRow((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"), (0, "PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfVclVpi"), (0, "PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfVclVci"))
if mibBuilder.loadTexts: pdnAtmBridgeIwfEntry.setStatus('current')
pdnAtmBridgeIwfVclVpi = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4095)))
if mibBuilder.loadTexts: pdnAtmBridgeIwfVclVpi.setStatus('current')
pdnAtmBridgeIwfVclVci = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 2), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)))
if mibBuilder.loadTexts: pdnAtmBridgeIwfVclVci.setStatus('current')
pdnAtmBridgeIwfRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 3), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnAtmBridgeIwfRowStatus.setStatus('current')
pdnAtmBridgeIwfDot1dBasePort = MibTableColumn((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 1, 1, 1, 4), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535))).setMaxAccess("readcreate")
if mibBuilder.loadTexts: pdnAtmBridgeIwfDot1dBasePort.setStatus('current')
pdnAtmBridgeIwfCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 1))
pdnAtmBridgeIwfGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 2))
pdnAtmBridgeIwfMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 1, 1)).setObjects(("PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnAtmBridgeIwfMIBCompliance = pdnAtmBridgeIwfMIBCompliance.setStatus('current')
pdnAtmBridgeIwfGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 1795, 2, 24, 2, 43, 2, 2, 1)).setObjects(("PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfRowStatus"), ("PDN-ATM-BRIDGE-IWF-MIB", "pdnAtmBridgeIwfDot1dBasePort"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    pdnAtmBridgeIwfGroup = pdnAtmBridgeIwfGroup.setStatus('current')
mibBuilder.exportSymbols("PDN-ATM-BRIDGE-IWF-MIB", pdnAtmBridgeIwfConformance=pdnAtmBridgeIwfConformance, pdnAtmBridgeIwfRowStatus=pdnAtmBridgeIwfRowStatus, pdnAtmBridgeIwfObjects=pdnAtmBridgeIwfObjects, pdnAtmBridgeIwfMIBCompliance=pdnAtmBridgeIwfMIBCompliance, pdnAtmBridgeIwfNotifications=pdnAtmBridgeIwfNotifications, pdnAtmBridgeIwfGroups=pdnAtmBridgeIwfGroups, pdnAtmBridgeIwfDot1dBasePort=pdnAtmBridgeIwfDot1dBasePort, pdnAtmBridgeIwfVclVpi=pdnAtmBridgeIwfVclVpi, pdnAtmBridgeIwfCompliances=pdnAtmBridgeIwfCompliances, pdnAtmBridgeIwfEntry=pdnAtmBridgeIwfEntry, pdnAtmBridgeIwfVclVci=pdnAtmBridgeIwfVclVci, pdnAtmBridgeIwfTable=pdnAtmBridgeIwfTable, PYSNMP_MODULE_ID=pdnAtmBridgeIwfMIB, pdnAtmBridgeIwfGroup=pdnAtmBridgeIwfGroup, pdnAtmBridgeIwfMIB=pdnAtmBridgeIwfMIB)
