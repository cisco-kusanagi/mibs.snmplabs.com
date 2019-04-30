#
# PySNMP MIB module CISCO-SVI-AUTOSTATE-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-SVI-AUTOSTATE-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:56:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
ifIndex, = mibBuilder.importSymbols("IF-MIB", "ifIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
iso, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Counter64, NotificationType, ObjectIdentity, Gauge32, IpAddress, ModuleIdentity, TimeTicks, Counter32, Integer32, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Counter64", "NotificationType", "ObjectIdentity", "Gauge32", "IpAddress", "ModuleIdentity", "TimeTicks", "Counter32", "Integer32", "Bits")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
ciscoSVIAutostateMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 376))
ciscoSVIAutostateMIB.setRevisions(('2004-04-06 00:00',))
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setLastUpdated('200404060000Z')
if mibBuilder.loadTexts: ciscoSVIAutostateMIB.setOrganization('Cisco Systems, Inc.')
ciscoSVIAutostateMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 0))
ciscoSVIAutostateMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1))
ciscoSVIAutostateMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2))
csaGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1))
csaInterface = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2))
csaFeatureEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaFeatureEnable.setStatus('current')
csaTrackedVlansLow = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 2), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansLow.setStatus('current')
csaTrackedVlansHigh = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(0, 256))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaTrackedVlansHigh.setStatus('current')
csaIfConfigTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1), )
if mibBuilder.loadTexts: csaIfConfigTable.setStatus('current')
csaIfConfigEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1), ).setIndexNames((0, "IF-MIB", "ifIndex"))
if mibBuilder.loadTexts: csaIfConfigEntry.setStatus('current')
csaInterfaceMode = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 376, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("normal", 1), ("exclude", 2), ("track", 3)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: csaInterfaceMode.setStatus('current')
csaMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1))
csaMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2))
csaMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 1, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVIAutostateGroup"), ("CISCO-SVI-AUTOSTATE-MIB", "ciscoSVITrackedVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    csaMIBCompliance = csaMIBCompliance.setStatus('current')
ciscoSVIAutostateGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 1)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaFeatureEnable"), ("CISCO-SVI-AUTOSTATE-MIB", "csaInterfaceMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVIAutostateGroup = ciscoSVIAutostateGroup.setStatus('current')
ciscoSVITrackedVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 376, 2, 2, 2)).setObjects(("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansLow"), ("CISCO-SVI-AUTOSTATE-MIB", "csaTrackedVlansHigh"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoSVITrackedVlanGroup = ciscoSVITrackedVlanGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-SVI-AUTOSTATE-MIB", csaMIBCompliance=csaMIBCompliance, ciscoSVIAutostateMIBNotifs=ciscoSVIAutostateMIBNotifs, ciscoSVIAutostateMIBObjects=ciscoSVIAutostateMIBObjects, csaFeatureEnable=csaFeatureEnable, csaMIBCompliances=csaMIBCompliances, csaIfConfigEntry=csaIfConfigEntry, ciscoSVIAutostateMIBConformance=ciscoSVIAutostateMIBConformance, ciscoSVIAutostateMIB=ciscoSVIAutostateMIB, PYSNMP_MODULE_ID=ciscoSVIAutostateMIB, csaTrackedVlansHigh=csaTrackedVlansHigh, csaInterfaceMode=csaInterfaceMode, csaInterface=csaInterface, csaTrackedVlansLow=csaTrackedVlansLow, ciscoSVIAutostateGroup=ciscoSVIAutostateGroup, ciscoSVITrackedVlanGroup=ciscoSVITrackedVlanGroup, csaMIBGroups=csaMIBGroups, csaIfConfigTable=csaIfConfigTable, csaGlobal=csaGlobal)
