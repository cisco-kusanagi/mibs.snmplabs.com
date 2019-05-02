#
# PySNMP MIB module ONEACCESS-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-EVENTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:34:08 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint")
oneAccess, oacMIBModules, oacExpIMEvents = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oneAccess", "oacMIBModules", "oacExpIMEvents")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, IpAddress, NotificationType, TimeTicks, ObjectIdentity, Counter32, Counter64, MibIdentifier, Unsigned32, iso, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "IpAddress", "NotificationType", "TimeTicks", "ObjectIdentity", "Counter32", "Counter64", "MibIdentifier", "Unsigned32", "iso", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
oacEventsMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 6600))
oacEventsMIBModule.setRevisions(('2011-06-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: oacEventsMIBModule.setRevisionsDescriptions(('This MIB module describes ATM Management objects.',))
if mibBuilder.loadTexts: oacEventsMIBModule.setLastUpdated('201106150000Z')
if mibBuilder.loadTexts: oacEventsMIBModule.setOrganization(' OneAccess ')
if mibBuilder.loadTexts: oacEventsMIBModule.setContactInfo('Pascal KESTELOOT Postal: ONE ACCESS 381 Avenue du Gnral de Gaulle 92140 Clamart, France FRANCE Tel: (+33) 01 41 87 70 00 Fax: (+33) 01 41 87 74 00 E-mail: pascal.kesteloot@oneaccess-net.com')
if mibBuilder.loadTexts: oacEventsMIBModule.setDescription('Contact updated')
oacEventsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1))
oacEventsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 2))
oacEventsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3))
oacEventText = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacEventText.setStatus('current')
if mibBuilder.loadTexts: oacEventText.setDescription('Textual representation of the event')
oacEventSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 2), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: oacEventSeverityLevel.setStatus('current')
if mibBuilder.loadTexts: oacEventSeverityLevel.setDescription('Provides the associated severity level used when generating snmp traps. When the device generates a Trap-PDU into a SNMPv2-Trap-PDU, and when it requires a severity level, this variable is inserted before the last varbind.')
oacEventSeverity = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3))
oacEventSeverityAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 1))
oacEventSeverityCritical = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 2))
oacEventSeverityErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 3))
oacEventSeverityWarnings = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 4))
oacEventSeverityNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 5))
oacEventSeverityInformational = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 6))
oacEventSeverityDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 7))
oacEvent = NotificationType((1, 3, 6, 1, 4, 1, 13191) + (0,1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
if mibBuilder.loadTexts: oacEvent.setDescription('Trap generated from Event management')
oacEventsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 1))
oacEventsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 2))
oacEventsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 2, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventsGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacEventsCompliance = oacEventsCompliance.setStatus('current')
if mibBuilder.loadTexts: oacEventsCompliance.setDescription('The compliance statement for agents that support the OA-EVENTS-MIB.')
oacEventsGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 1, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacEventsGeneralGroup = oacEventsGeneralGroup.setStatus('current')
if mibBuilder.loadTexts: oacEventsGeneralGroup.setDescription('This group is mandatory for all Events entities.')
mibBuilder.exportSymbols("ONEACCESS-EVENTS-MIB", oacEventSeverityInformational=oacEventSeverityInformational, oacEventsGroups=oacEventsGroups, oacEventSeverityWarnings=oacEventSeverityWarnings, oacEventsObjects=oacEventsObjects, oacEventsCompliances=oacEventsCompliances, oacEventSeverityCritical=oacEventSeverityCritical, oacEventSeverityLevel=oacEventSeverityLevel, oacEventsMIBModule=oacEventsMIBModule, PYSNMP_MODULE_ID=oacEventsMIBModule, oacEventsConformance=oacEventsConformance, oacEventSeverityNotifications=oacEventSeverityNotifications, oacEventSeverityAlerts=oacEventSeverityAlerts, oacEventsCompliance=oacEventsCompliance, oacEventsGeneralGroup=oacEventsGeneralGroup, oacEvent=oacEvent, oacEventText=oacEventText, oacEventSeverityDebug=oacEventSeverityDebug, oacEventSeverityErrors=oacEventSeverityErrors, oacEventsNotifications=oacEventsNotifications, oacEventSeverity=oacEventSeverity)
