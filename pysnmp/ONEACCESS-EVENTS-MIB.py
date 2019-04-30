#
# PySNMP MIB module ONEACCESS-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ONEACCESS-EVENTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:24:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueRangeConstraint")
oneAccess, oacExpIMEvents, oacMIBModules = mibBuilder.importSymbols("ONEACCESS-GLOBAL-REG", "oneAccess", "oacExpIMEvents", "oacMIBModules")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
Gauge32, ObjectIdentity, Counter32, Unsigned32, Integer32, Counter64, NotificationType, ModuleIdentity, TimeTicks, iso, IpAddress, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "Counter32", "Unsigned32", "Integer32", "Counter64", "NotificationType", "ModuleIdentity", "TimeTicks", "iso", "IpAddress", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
oacEventsMIBModule = ModuleIdentity((1, 3, 6, 1, 4, 1, 13191, 1, 100, 6600))
oacEventsMIBModule.setRevisions(('2011-06-15 00:00',))
if mibBuilder.loadTexts: oacEventsMIBModule.setLastUpdated('201106150000Z')
if mibBuilder.loadTexts: oacEventsMIBModule.setOrganization(' OneAccess ')
oacEventsObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1))
oacEventsNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 2))
oacEventsConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3))
oacEventText = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 1), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: oacEventText.setStatus('current')
oacEventSeverityLevel = MibScalar((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 2), ObjectIdentifier()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: oacEventSeverityLevel.setStatus('current')
oacEventSeverity = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3))
oacEventSeverityAlerts = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 1))
oacEventSeverityCritical = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 2))
oacEventSeverityErrors = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 3))
oacEventSeverityWarnings = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 4))
oacEventSeverityNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 5))
oacEventSeverityInformational = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 6))
oacEventSeverityDebug = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 1, 3, 7))
oacEvent = NotificationType((1, 3, 6, 1, 4, 1, 13191) + (0,1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
oacEventsGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 1))
oacEventsCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 2))
oacEventsCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 2, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventsGeneralGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacEventsCompliance = oacEventsCompliance.setStatus('current')
oacEventsGeneralGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 13191, 10, 3, 4, 2, 3, 1, 1)).setObjects(("ONEACCESS-EVENTS-MIB", "oacEventText"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    oacEventsGeneralGroup = oacEventsGeneralGroup.setStatus('current')
mibBuilder.exportSymbols("ONEACCESS-EVENTS-MIB", oacEvent=oacEvent, oacEventSeverity=oacEventSeverity, oacEventSeverityDebug=oacEventSeverityDebug, oacEventsNotifications=oacEventsNotifications, oacEventSeverityErrors=oacEventSeverityErrors, oacEventSeverityLevel=oacEventSeverityLevel, oacEventSeverityNotifications=oacEventSeverityNotifications, oacEventsGeneralGroup=oacEventsGeneralGroup, oacEventSeverityWarnings=oacEventSeverityWarnings, oacEventsConformance=oacEventsConformance, oacEventsMIBModule=oacEventsMIBModule, oacEventsCompliance=oacEventsCompliance, oacEventSeverityCritical=oacEventSeverityCritical, oacEventsObjects=oacEventsObjects, PYSNMP_MODULE_ID=oacEventsMIBModule, oacEventSeverityInformational=oacEventSeverityInformational, oacEventSeverityAlerts=oacEventSeverityAlerts, oacEventText=oacEventText, oacEventsGroups=oacEventsGroups, oacEventsCompliances=oacEventsCompliances)
