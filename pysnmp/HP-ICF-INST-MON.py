#
# PySNMP MIB module HP-ICF-INST-MON (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-INST-MON
# Produced by pysmi-0.3.4 at Mon Apr 29 19:21:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndexOrZero, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
TimeTicks, ObjectIdentity, MibIdentifier, Counter32, Bits, Counter64, NotificationType, Integer32, Gauge32, Unsigned32, IpAddress, iso, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "ObjectIdentity", "MibIdentifier", "Counter32", "Bits", "Counter64", "NotificationType", "Integer32", "Gauge32", "Unsigned32", "IpAddress", "iso", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
TextualConvention, DisplayString, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString", "TruthValue")
hpicfInstMonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35))
hpicfInstMonMIB.setRevisions(('2008-12-04 00:00', '2006-01-23 00:00',))
if mibBuilder.loadTexts: hpicfInstMonMIB.setLastUpdated('200812040000Z')
if mibBuilder.loadTexts: hpicfInstMonMIB.setOrganization('HP Networking')
hpicfInstMonObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1))
hpicfInstMonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2))
hpicfInstMonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1))
hpicfInstMonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 2))
hpicfInstMonLogEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfInstMonLogEnable.setStatus('current')
hpicfInstMonTrapEnable = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 2), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfInstMonTrapEnable.setStatus('current')
hpicfInstMonParameterTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3), )
if mibBuilder.loadTexts: hpicfInstMonParameterTable.setStatus('current')
hpicfInstMonParameterEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1), ).setIndexNames((0, "HP-ICF-INST-MON", "hpicfInstMonInterfaceIndex"), (0, "HP-ICF-INST-MON", "hpicfInstMonParameterIndex"))
if mibBuilder.loadTexts: hpicfInstMonParameterEntry.setStatus('current')
hpicfInstMonInterfaceIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1, 1), InterfaceIndexOrZero())
if mibBuilder.loadTexts: hpicfInstMonInterfaceIndex.setStatus('current')
hpicfInstMonParameterIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 65535)))
if mibBuilder.loadTexts: hpicfInstMonParameterIndex.setStatus('current')
hpicfInstMonParameterName = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 20))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfInstMonParameterName.setStatus('current')
hpicfInstMonParameterThreshold = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 3, 1, 4), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfInstMonParameterThreshold.setStatus('current')
hpicfInstMonNotificationText = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfInstMonNotificationText.setStatus('current')
hpicfInstMonNotification = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 5)).setObjects(("HP-ICF-INST-MON", "hpicfInstMonNotificationText"))
if mibBuilder.loadTexts: hpicfInstMonNotification.setStatus('current')
hpicfInstConfig = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 1, 6), TruthValue().clone('true')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfInstConfig.setStatus('current')
hpicfInstMonNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1, 1)).setObjects(("HP-ICF-INST-MON", "hpicfInstMonNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfInstMonNotificationGroup = hpicfInstMonNotificationGroup.setStatus('current')
hpicfInstMonBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1, 2)).setObjects(("HP-ICF-INST-MON", "hpicfInstMonLogEnable"), ("HP-ICF-INST-MON", "hpicfInstMonTrapEnable"), ("HP-ICF-INST-MON", "hpicfInstMonParameterName"), ("HP-ICF-INST-MON", "hpicfInstMonParameterThreshold"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfInstMonBaseGroup = hpicfInstMonBaseGroup.setStatus('current')
hpicfInstConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1, 3)).setObjects(("HP-ICF-INST-MON", "hpicfInstConfig"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfInstConfigGroup = hpicfInstConfigGroup.setStatus('current')
hpicfInstMonNotifyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 1, 4)).setObjects(("HP-ICF-INST-MON", "hpicfInstMonNotificationText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfInstMonNotifyGroup = hpicfInstMonNotifyGroup.setStatus('current')
hpicfInstMonBaseCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 2, 1)).setObjects(("HP-ICF-INST-MON", "hpicfInstMonBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfInstMonBaseCompliance = hpicfInstMonBaseCompliance.setStatus('current')
hpicfInstConfigCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 2, 2)).setObjects(("HP-ICF-INST-MON", "hpicfInstConfigGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfInstConfigCompliance = hpicfInstConfigCompliance.setStatus('current')
hpicfInstMonNotifyCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 35, 2, 2, 3)).setObjects(("HP-ICF-INST-MON", "hpicfInstMonNotifyGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfInstMonNotifyCompliance = hpicfInstMonNotifyCompliance.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-INST-MON", hpicfInstMonGroups=hpicfInstMonGroups, hpicfInstMonConformance=hpicfInstMonConformance, hpicfInstMonParameterName=hpicfInstMonParameterName, hpicfInstMonTrapEnable=hpicfInstMonTrapEnable, hpicfInstMonNotifyCompliance=hpicfInstMonNotifyCompliance, hpicfInstConfigGroup=hpicfInstConfigGroup, hpicfInstConfigCompliance=hpicfInstConfigCompliance, hpicfInstMonNotificationGroup=hpicfInstMonNotificationGroup, hpicfInstMonParameterIndex=hpicfInstMonParameterIndex, hpicfInstMonLogEnable=hpicfInstMonLogEnable, PYSNMP_MODULE_ID=hpicfInstMonMIB, hpicfInstMonMIB=hpicfInstMonMIB, hpicfInstMonParameterThreshold=hpicfInstMonParameterThreshold, hpicfInstConfig=hpicfInstConfig, hpicfInstMonBaseCompliance=hpicfInstMonBaseCompliance, hpicfInstMonCompliances=hpicfInstMonCompliances, hpicfInstMonInterfaceIndex=hpicfInstMonInterfaceIndex, hpicfInstMonParameterTable=hpicfInstMonParameterTable, hpicfInstMonNotifyGroup=hpicfInstMonNotifyGroup, hpicfInstMonNotificationText=hpicfInstMonNotificationText, hpicfInstMonObjects=hpicfInstMonObjects, hpicfInstMonParameterEntry=hpicfInstMonParameterEntry, hpicfInstMonNotification=hpicfInstMonNotification, hpicfInstMonBaseGroup=hpicfInstMonBaseGroup)
