#
# PySNMP MIB module CISCOWORKS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCOWORKS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 18:08:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ciscoworks, = mibBuilder.importSymbols("CISCO-SMI", "ciscoworks")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
sysUpTime, = mibBuilder.importSymbols("SNMPv2-MIB", "sysUpTime")
Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Bits, MibIdentifier, ModuleIdentity, Counter64, TimeTicks, ObjectIdentity, iso, IpAddress, Gauge32, Unsigned32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Bits", "MibIdentifier", "ModuleIdentity", "Counter64", "TimeTicks", "ObjectIdentity", "iso", "IpAddress", "Gauge32", "Unsigned32", "NotificationType")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cwLogMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 14, 1))
cwLogMIB.setRevisions(('2003-02-18 00:00', '1995-04-02 00:00',))
if mibBuilder.loadTexts: cwLogMIB.setLastUpdated('200302180000Z')
if mibBuilder.loadTexts: cwLogMIB.setOrganization('Cisco Systems, Inc.')
cwLog = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 1))
cwTrapsPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 2))
cwMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3))
cwLogDate = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(15, 15)).setFixedLength(15)).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogDate.setStatus('current')
cwLogSource = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("other", 1), ("ciscoworks", 2), ("device", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogSource.setStatus('current')
cwLogApp = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 3), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogApp.setStatus('current')
cwLogMsg = MibScalar((1, 3, 6, 1, 4, 1, 9, 14, 1, 1, 4), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cwLogMsg.setStatus('current')
cwTraps = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0))
cwAppLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 1)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogApp"), ("CISCOWORKS-MIB", "cwLogMsg"))
if mibBuilder.loadTexts: cwAppLogTrap.setStatus('current')
cwDevLogTrap = NotificationType((1, 3, 6, 1, 4, 1, 9, 14, 1, 2, 0, 2)).setObjects(("SNMPv2-MIB", "sysUpTime"), ("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogMsg"))
if mibBuilder.loadTexts: cwDevLogTrap.setStatus('current')
ciscoCwMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1))
ciscoCwMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2))
ciscoCwMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 1, 1)).setObjects(("CISCOWORKS-MIB", "ciscoCwObjectsGroup"), ("CISCOWORKS-MIB", "ciscoCwNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwMIBCompliance = ciscoCwMIBCompliance.setStatus('current')
ciscoCwObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 7)).setObjects(("CISCOWORKS-MIB", "cwLogDate"), ("CISCOWORKS-MIB", "cwLogSource"), ("CISCOWORKS-MIB", "cwLogApp"), ("CISCOWORKS-MIB", "cwLogMsg"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwObjectsGroup = ciscoCwObjectsGroup.setStatus('current')
ciscoCwNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 14, 1, 3, 2, 12)).setObjects(("CISCOWORKS-MIB", "cwAppLogTrap"), ("CISCOWORKS-MIB", "cwDevLogTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoCwNotificationsGroup = ciscoCwNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("CISCOWORKS-MIB", cwTraps=cwTraps, cwDevLogTrap=cwDevLogTrap, ciscoCwMIBGroups=ciscoCwMIBGroups, cwLogApp=cwLogApp, cwAppLogTrap=cwAppLogTrap, ciscoCwMIBCompliances=ciscoCwMIBCompliances, ciscoCwObjectsGroup=ciscoCwObjectsGroup, cwLogMsg=cwLogMsg, cwMIBConform=cwMIBConform, cwLogMIB=cwLogMIB, ciscoCwMIBCompliance=ciscoCwMIBCompliance, PYSNMP_MODULE_ID=cwLogMIB, cwLogDate=cwLogDate, ciscoCwNotificationsGroup=ciscoCwNotificationsGroup, cwLog=cwLog, cwTrapsPrefix=cwTrapsPrefix, cwLogSource=cwLogSource)
