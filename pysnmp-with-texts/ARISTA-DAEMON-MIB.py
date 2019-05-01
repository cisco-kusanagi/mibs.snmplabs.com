#
# PySNMP MIB module ARISTA-DAEMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-DAEMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:24:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Gauge32, Counter32, Bits, Counter64, ObjectIdentity, Integer32, MibIdentifier, Unsigned32, NotificationType, iso, IpAddress, TimeTicks, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "Counter32", "Bits", "Counter64", "ObjectIdentity", "Integer32", "MibIdentifier", "Unsigned32", "NotificationType", "iso", "IpAddress", "TimeTicks", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue")
aristaDaemonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 17))
aristaDaemonMIB.setRevisions(('2015-04-27 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaDaemonMIB.setRevisionsDescriptions(('Initial version of this MIB.',))
if mibBuilder.loadTexts: aristaDaemonMIB.setLastUpdated('201504270000Z')
if mibBuilder.loadTexts: aristaDaemonMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaDaemonMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 95054 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaDaemonMIB.setDescription('The MIB module for managing the state of custom agents for Arista EOS.')
class AgentName(TextualConvention, OctetString):
    description = 'A custom agent name (as a string).'
    status = 'current'
    displayHint = '32a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 32)

class AgentAttributeKey(TextualConvention, OctetString):
    description = 'A custom attribute of an agent (as a string).'
    status = 'current'
    displayHint = '64a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class AgentAttributeValue(TextualConvention, OctetString):
    description = 'A value of a custom attribute of an agent (as a string).'
    status = 'current'
    displayHint = '10240a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 10240)

aristaDaemonConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1))
aristaDaemonStatus = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2))
aristaDaemonEnabledTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1), )
if mibBuilder.loadTexts: aristaDaemonEnabledTable.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonEnabledTable.setDescription('A table that contains the enabled configurations for custom daemons.')
aristaDaemonEnabledEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1, 1), ).setIndexNames((0, "ARISTA-DAEMON-MIB", "aristaDaemonEnabledAgentName"))
if mibBuilder.loadTexts: aristaDaemonEnabledEntry.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonEnabledEntry.setDescription('The enabled configuration of a daemon.')
aristaDaemonEnabledAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1, 1, 1), AgentName())
if mibBuilder.loadTexts: aristaDaemonEnabledAgentName.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonEnabledAgentName.setDescription('The name of the agent.')
aristaDaemonEnabled = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDaemonEnabled.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonEnabled.setDescription("This attribute has value 'true(1)' if the agent is enabled and value 'false(2)' if it is disabled.")
aristaDaemonOptionTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2), )
if mibBuilder.loadTexts: aristaDaemonOptionTable.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonOptionTable.setDescription('A table that contains user-configured options for daemons.')
aristaDaemonOptionEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1), ).setIndexNames((0, "ARISTA-DAEMON-MIB", "aristaDaemonOptionAgentName"), (0, "ARISTA-DAEMON-MIB", "aristaDaemonOptionKey"))
if mibBuilder.loadTexts: aristaDaemonOptionEntry.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonOptionEntry.setDescription('A user-configured daemon option entry.')
aristaDaemonOptionAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1, 1), AgentName())
if mibBuilder.loadTexts: aristaDaemonOptionAgentName.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonOptionAgentName.setDescription('The name of the agent.')
aristaDaemonOptionKey = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1, 2), AgentAttributeKey())
if mibBuilder.loadTexts: aristaDaemonOptionKey.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonOptionKey.setDescription('The name of a user-configured option.')
aristaDaemonOptionValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 1, 2, 1, 3), AgentAttributeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDaemonOptionValue.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonOptionValue.setDescription('The value of a user-configured option.')
aristaDaemonRunningTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1), )
if mibBuilder.loadTexts: aristaDaemonRunningTable.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonRunningTable.setDescription('A table that contains the running statuses for custom daemons.')
aristaDaemonRunningEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1, 1), ).setIndexNames((0, "ARISTA-DAEMON-MIB", "aristaDaemonRunningAgentName"))
if mibBuilder.loadTexts: aristaDaemonRunningEntry.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonRunningEntry.setDescription('The running status of a daemon.')
aristaDaemonRunningAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1, 1, 1), AgentName())
if mibBuilder.loadTexts: aristaDaemonRunningAgentName.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonRunningAgentName.setDescription('The name of the agent.')
aristaDaemonRunning = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 1, 1, 2), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDaemonRunning.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonRunning.setDescription("This attribute has value 'true(1)' if the agent is running and value 'false(2)' if it is not running.")
aristaDaemonDataTable = MibTable((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2), )
if mibBuilder.loadTexts: aristaDaemonDataTable.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonDataTable.setDescription('A table that contains status data for daemons.')
aristaDaemonDataEntry = MibTableRow((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1), ).setIndexNames((0, "ARISTA-DAEMON-MIB", "aristaDaemonDataAgentName"), (0, "ARISTA-DAEMON-MIB", "aristaDaemonDataKey"))
if mibBuilder.loadTexts: aristaDaemonDataEntry.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonDataEntry.setDescription('A daemon data entry about its status.')
aristaDaemonDataAgentName = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1, 1), AgentName())
if mibBuilder.loadTexts: aristaDaemonDataAgentName.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonDataAgentName.setDescription('The name of the agent.')
aristaDaemonDataKey = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1, 2), AgentAttributeKey())
if mibBuilder.loadTexts: aristaDaemonDataKey.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonDataKey.setDescription('The name of a status data entry.')
aristaDaemonDataValue = MibTableColumn((1, 3, 6, 1, 4, 1, 30065, 3, 17, 2, 2, 1, 3), AgentAttributeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaDaemonDataValue.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonDataValue.setDescription('The value of a status data.')
aristaDaemonConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3))
aristaDaemonGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 1))
aristaDaemonCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 2))
aristaDaemonBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 1, 1)).setObjects(("ARISTA-DAEMON-MIB", "aristaDaemonEnabled"), ("ARISTA-DAEMON-MIB", "aristaDaemonOptionValue"), ("ARISTA-DAEMON-MIB", "aristaDaemonRunning"), ("ARISTA-DAEMON-MIB", "aristaDaemonDataValue"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaDaemonBaseGroup = aristaDaemonBaseGroup.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonBaseGroup.setDescription('A collection of objects providing information about the custom agent.')
aristaDaemonCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 17, 3, 2, 1)).setObjects(("ARISTA-DAEMON-MIB", "aristaDaemonBaseGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaDaemonCompliance = aristaDaemonCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaDaemonCompliance.setDescription('The compliance statement for Arista switches that support EOS SDK custom agents.')
mibBuilder.exportSymbols("ARISTA-DAEMON-MIB", aristaDaemonDataKey=aristaDaemonDataKey, AgentName=AgentName, PYSNMP_MODULE_ID=aristaDaemonMIB, aristaDaemonDataEntry=aristaDaemonDataEntry, aristaDaemonGroups=aristaDaemonGroups, AgentAttributeValue=AgentAttributeValue, aristaDaemonRunningTable=aristaDaemonRunningTable, aristaDaemonRunningAgentName=aristaDaemonRunningAgentName, aristaDaemonMIB=aristaDaemonMIB, aristaDaemonConfig=aristaDaemonConfig, aristaDaemonOptionTable=aristaDaemonOptionTable, aristaDaemonStatus=aristaDaemonStatus, aristaDaemonRunning=aristaDaemonRunning, aristaDaemonDataAgentName=aristaDaemonDataAgentName, aristaDaemonBaseGroup=aristaDaemonBaseGroup, aristaDaemonConformance=aristaDaemonConformance, AgentAttributeKey=AgentAttributeKey, aristaDaemonEnabled=aristaDaemonEnabled, aristaDaemonRunningEntry=aristaDaemonRunningEntry, aristaDaemonOptionValue=aristaDaemonOptionValue, aristaDaemonOptionEntry=aristaDaemonOptionEntry, aristaDaemonOptionAgentName=aristaDaemonOptionAgentName, aristaDaemonEnabledEntry=aristaDaemonEnabledEntry, aristaDaemonCompliances=aristaDaemonCompliances, aristaDaemonCompliance=aristaDaemonCompliance, aristaDaemonDataValue=aristaDaemonDataValue, aristaDaemonDataTable=aristaDaemonDataTable, aristaDaemonEnabledTable=aristaDaemonEnabledTable, aristaDaemonOptionKey=aristaDaemonOptionKey, aristaDaemonEnabledAgentName=aristaDaemonEnabledAgentName)
