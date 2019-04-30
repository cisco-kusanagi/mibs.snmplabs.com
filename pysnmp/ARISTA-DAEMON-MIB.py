#
# PySNMP MIB module ARISTA-DAEMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-DAEMON-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
iso, TimeTicks, NotificationType, Counter32, ModuleIdentity, IpAddress, Counter64, Bits, MibIdentifier, Gauge32, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "TimeTicks", "NotificationType", "Counter32", "ModuleIdentity", "IpAddress", "Counter64", "Bits", "MibIdentifier", "Gauge32", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Unsigned32")
TruthValue, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "DisplayString")
aristaDaemonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 17))
aristaDaemonMIB.setRevisions(('2015-04-27 00:00',))
if mibBuilder.loadTexts: aristaDaemonMIB.setLastUpdated('201504270000Z')
if mibBuilder.loadTexts: aristaDaemonMIB.setOrganization('Arista Networks, Inc.')
class AgentName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class AgentAttributeKey(TextualConvention, OctetString):
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class AgentAttributeValue(TextualConvention, OctetString):
    status = 'current'
    displayHint = '10240a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 10240)

aristaDaemonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1))
aristaDaemonStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2))
aristaDaemonEnabledTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1), )
if mibBuilder.loadTexts: aristaDaemonEnabledTable.setStatus('current')
aristaDaemonEnabledEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1, 1), ).setIndexNames((0, "ARISTA-DAEMON-MIB", "aristaDaemonEnabledAgentName"))
if mibBuilder.loadTexts: aristaDaemonEnabledEntry.setStatus('current')
aristaDaemonEnabledAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1, 1, 1), AgentName())
if mibBuilder.loadTexts: aristaDaemonEnabledAgentName.setStatus('current')
aristaDaemonEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDaemonEnabled.setStatus('current')
aristaDaemonOptionTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2), )
if mibBuilder.loadTexts: aristaDaemonOptionTable.setStatus('current')
aristaDaemonOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1), ).setIndexNames((0, "ARISTA-DAEMON-MIB", "aristaDaemonOptionAgentName"), (0, "ARISTA-DAEMON-MIB", "aristaDaemonOptionKey"))
if mibBuilder.loadTexts: aristaDaemonOptionEntry.setStatus('current')
aristaDaemonOptionAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1, 1), AgentName())
if mibBuilder.loadTexts: aristaDaemonOptionAgentName.setStatus('current')
aristaDaemonOptionKey = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1, 2), AgentAttributeKey())
if mibBuilder.loadTexts: aristaDaemonOptionKey.setStatus('current')
aristaDaemonOptionValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1, 3), AgentAttributeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDaemonOptionValue.setStatus('current')
aristaDaemonRunningTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1), )
if mibBuilder.loadTexts: aristaDaemonRunningTable.setStatus('current')
aristaDaemonRunningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1, 1), ).setIndexNames((0, "ARISTA-DAEMON-MIB", "aristaDaemonRunningAgentName"))
if mibBuilder.loadTexts: aristaDaemonRunningEntry.setStatus('current')
aristaDaemonRunningAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1, 1, 1), AgentName())
if mibBuilder.loadTexts: aristaDaemonRunningAgentName.setStatus('current')
aristaDaemonRunning = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDaemonRunning.setStatus('current')
aristaDaemonDataTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2), )
if mibBuilder.loadTexts: aristaDaemonDataTable.setStatus('current')
aristaDaemonDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1), ).setIndexNames((0, "ARISTA-DAEMON-MIB", "aristaDaemonDataAgentName"), (0, "ARISTA-DAEMON-MIB", "aristaDaemonDataKey"))
if mibBuilder.loadTexts: aristaDaemonDataEntry.setStatus('current')
aristaDaemonDataAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1, 1), AgentName())
if mibBuilder.loadTexts: aristaDaemonDataAgentName.setStatus('current')
aristaDaemonDataKey = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1, 2), AgentAttributeKey())
if mibBuilder.loadTexts: aristaDaemonDataKey.setStatus('current')
aristaDaemonDataValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1, 3), AgentAttributeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDaemonDataValue.setStatus('current')
aristaDaemonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3))
aristaDaemonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 1))
aristaDaemonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 2))
aristaDaemonBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 1, 1)).setObjects(("ARISTA-DAEMON-MIB", "aristaDaemonEnabled"), ("ARISTA-DAEMON-MIB", "aristaDaemonOptionValue"), ("ARISTA-DAEMON-MIB", "aristaDaemonRunning"), ("ARISTA-DAEMON-MIB", "aristaDaemonDataValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaDaemonBaseGroup = aristaDaemonBaseGroup.setStatus('current')
aristaDaemonCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 2, 1)).setObjects(("ARISTA-DAEMON-MIB", "aristaDaemonBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaDaemonCompliance = aristaDaemonCompliance.setStatus('current')
mibBuilder.exportSymbols("ARISTA-DAEMON-MIB", AgentAttributeValue=AgentAttributeValue, AgentAttributeKey=AgentAttributeKey, aristaDaemonRunningAgentName=aristaDaemonRunningAgentName, aristaDaemonEnabled=aristaDaemonEnabled, aristaDaemonEnabledTable=aristaDaemonEnabledTable, aristaDaemonDataValue=aristaDaemonDataValue, AgentName=AgentName, aristaDaemonConformance=aristaDaemonConformance, aristaDaemonOptionKey=aristaDaemonOptionKey, aristaDaemonMIB=aristaDaemonMIB, aristaDaemonOptionValue=aristaDaemonOptionValue, aristaDaemonEnabledEntry=aristaDaemonEnabledEntry, aristaDaemonDataAgentName=aristaDaemonDataAgentName, aristaDaemonBaseGroup=aristaDaemonBaseGroup, aristaDaemonEnabledAgentName=aristaDaemonEnabledAgentName, aristaDaemonDataEntry=aristaDaemonDataEntry, aristaDaemonOptionAgentName=aristaDaemonOptionAgentName, aristaDaemonGroups=aristaDaemonGroups, aristaDaemonDataKey=aristaDaemonDataKey, aristaDaemonOptionEntry=aristaDaemonOptionEntry, PYSNMP_MODULE_ID=aristaDaemonMIB, aristaDaemonConfig=aristaDaemonConfig, aristaDaemonCompliance=aristaDaemonCompliance, aristaDaemonStatus=aristaDaemonStatus, aristaDaemonDataTable=aristaDaemonDataTable, aristaDaemonOptionTable=aristaDaemonOptionTable, aristaDaemonRunning=aristaDaemonRunning, aristaDaemonRunningTable=aristaDaemonRunningTable, aristaDaemonCompliances=aristaDaemonCompliances, aristaDaemonRunningEntry=aristaDaemonRunningEntry)
