#
# PySNMP MIB module ONEACCESS-PING-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-PING-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:25:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
pingCtlTestName, pingCtlOwnerIndex = mibBuilder.importSymbols("DISMAN-PING-MIB", "pingCtlTestName", "pingCtlOwnerIndex")
oacMIBModules, oneAccess, oacExpIMPing = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oacMIBModules", "oneAccess", "oacExpIMPing")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
NotificationType, iso, Counter32, mib_2, Unsigned32, Bits, Counter64, Integer32, IpAddress, ObjectIdentity, Gauge32, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "iso", "Counter32", "mib-2", "Unsigned32", "Bits", "Counter64", "Integer32", "IpAddress", "ObjectIdentity", "Gauge32", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacPingMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 6601))
oacPingMIBModule.setRevisions(('2011-06-15 00:00', '2010-07-08 00:01',))
if mibBuilder.loadTexts: oacPingMIBModule.setLastUpdated('201106150000Z')
if mibBuilder.loadTexts: oacPingMIBModule.setOrganization(' OneAccess ')
oacPingNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 0))
oacPingObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1))
oacPingConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2))
oacPingResultsTable = MibTable((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3), )
if mibBuilder.loadTexts: oacPingResultsTable.setStatus('current')
oacPingResultsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1), ).setIndexNames((0, "DISMAN-PING-MIB", "pingCtlOwnerIndex"), (0, "DISMAN-PING-MIB", "pingCtlTestName"))
if mibBuilder.loadTexts: oacPingResultsEntry.setStatus('current')
oacPingJitterSamples = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 1), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacPingJitterSamples.setStatus('current')
oacPingResultsMinJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 2), Unsigned32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacPingResultsMinJitter.setStatus('current')
oacPingResultsMaxJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 3), Unsigned32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacPingResultsMaxJitter.setStatus('current')
oacPingResultsAverageJitter = MibTableColumn((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 1, 3, 1, 4), Unsigned32()).setUnits('microseconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: oacPingResultsAverageJitter.setStatus('current')
oacPingCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 1))
oacPingGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 2))
oacPingCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 1, 1)).setObjects(("ONEACCESS-PING-MIB", "oacPingGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacPingCompliance = oacPingCompliance.setStatus('current')
oacPingGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 3, 2, 2, 1)).setObjects(("ONEACCESS-PING-MIB", "oacPingJitterSamples"), ("ONEACCESS-PING-MIB", "oacPingResultsMinJitter"), ("ONEACCESS-PING-MIB", "oacPingResultsMaxJitter"), ("ONEACCESS-PING-MIB", "oacPingResultsAverageJitter"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacPingGroup = oacPingGroup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-PING-MIB", oacPingResultsMaxJitter=oacPingResultsMaxJitter, oacPingResultsTable=oacPingResultsTable, oacPingJitterSamples=oacPingJitterSamples, PYSNMP_MODULE_ID=oacPingMIBModule, oacPingGroups=oacPingGroups, oacPingGroup=oacPingGroup, oacPingNotifications=oacPingNotifications, oacPingResultsAverageJitter=oacPingResultsAverageJitter, oacPingResultsEntry=oacPingResultsEntry, oacPingResultsMinJitter=oacPingResultsMinJitter, oacPingMIBModule=oacPingMIBModule, oacPingConformance=oacPingConformance, oacPingCompliances=oacPingCompliances, oacPingObjects=oacPingObjects, oacPingCompliance=oacPingCompliance)
