#
# PySNMP MIB module SUN-CLUSTER-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/SUN-CLUSTER-EVENTS-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 21:04:15 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, SingleValueConstraint, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "SingleValueConstraint", "ValueRangeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, Bits, Integer32, iso, ObjectIdentity, IpAddress, Counter32, TimeTicks, MibIdentifier, Gauge32, NotificationType, ModuleIdentity, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "Bits", "Integer32", "iso", "ObjectIdentity", "IpAddress", "Counter32", "TimeTicks", "MibIdentifier", "Gauge32", "NotificationType", "ModuleIdentity", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
sunClusterEventsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 42, 2, 80, 2))
sunClusterEventsMIB.setRevisions(('1902-11-30 00:00',))
if mibBuilder.loadTexts: sunClusterEventsMIB.setLastUpdated('0211300000Z')
if mibBuilder.loadTexts: sunClusterEventsMIB.setOrganization('Sun Microsystems')
sun = MibIdentifier((1, 3, 6, 1, 4, 1, 42))
prod = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2))
suncluster = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 80))
scEventsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1))
scEventsMIBNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 2))
class ScEventTableCount(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(20, 32767)

class ScEventIndex(TextualConvention, Integer32):
    status = 'current'

class ScClusterId(DisplayString):
    status = 'current'

class ScClusterName(DisplayString):
    status = 'current'

class ScNodeName(DisplayString):
    status = 'current'

class ScEventVersion(TextualConvention, Integer32):
    status = 'current'

class ScEventClassName(DisplayString):
    status = 'current'

class ScEventSubclassName(DisplayString):
    status = 'current'

class ScEventSeverity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("clEventSevInfo", 0), ("clEventSevWarning", 1), ("clEventSevError", 2), ("clEventSevCritical", 3), ("clEventSevFatal", 4))

class ScEventInitiator(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("clEventInitUnknown", 0), ("clEventInitSystem", 1), ("clEventInitOperator", 2), ("clEventInitAgent", 3))

class ScEventPublisher(DisplayString):
    status = 'current'

class ScEventPid(TextualConvention, Counter64):
    status = 'current'

class ScTimeStamp(TextualConvention, Counter64):
    status = 'current'

class ScEventData(DisplayString):
    status = 'current'

class ScEventAttributeName(DisplayString):
    status = 'current'

class ScEventAttributeValue(DisplayString):
    status = 'current'

escEventTableCount = MibScalar((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 1), ScEventTableCount()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: escEventTableCount.setStatus('current')
escEventsTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2), )
if mibBuilder.loadTexts: escEventsTable.setStatus('current')
escEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1), ).setIndexNames((0, "SUN-CLUSTER-EVENTS-MIB", "eventIndex"))
if mibBuilder.loadTexts: escEventsEntry.setStatus('current')
eventIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 1), ScEventIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventIndex.setStatus('current')
eventClusterId = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 2), ScClusterId()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClusterId.setStatus('current')
eventClusterName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 3), ScClusterName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClusterName.setStatus('current')
eventNodeName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 4), ScNodeName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventNodeName.setStatus('current')
eventVersion = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 5), ScEventVersion()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventVersion.setStatus('current')
eventClassName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 6), ScEventClassName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventClassName.setStatus('current')
eventSubclassName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 7), ScEventSubclassName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSubclassName.setStatus('current')
eventSeverity = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 8), ScEventSeverity()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSeverity.setStatus('current')
eventInitiator = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 9), ScEventInitiator()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventInitiator.setStatus('current')
eventPublisher = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 10), ScEventPublisher()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPublisher.setStatus('current')
eventSeqNo = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 11), Counter64()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventSeqNo.setStatus('current')
eventPid = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 12), ScEventPid()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventPid.setStatus('current')
eventTimeStamp = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 13), ScTimeStamp()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventTimeStamp.setStatus('current')
eventData = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 2, 1, 14), ScEventData()).setMaxAccess("readonly")
if mibBuilder.loadTexts: eventData.setStatus('current')
escEventsAttributesTable = MibTable((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3), )
if mibBuilder.loadTexts: escEventsAttributesTable.setStatus('current')
escEventsAttributesEntry = MibTableRow((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1), ).setIndexNames((0, "SUN-CLUSTER-EVENTS-MIB", "eventIndex"), (0, "SUN-CLUSTER-EVENTS-MIB", "attributeName"))
if mibBuilder.loadTexts: escEventsAttributesEntry.setStatus('current')
attributeName = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1, 1), ScEventAttributeName())
if mibBuilder.loadTexts: attributeName.setStatus('current')
attributeValue = MibTableColumn((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 1, 3, 1, 2), ScEventAttributeValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: attributeValue.setStatus('current')
escNewEvents = NotificationType((1, 3, 6, 1, 4, 1, 42, 2, 80, 2, 2, 1)).setObjects(("SUN-CLUSTER-EVENTS-MIB", "eventIndex"), ("SUN-CLUSTER-EVENTS-MIB", "eventClusterId"), ("SUN-CLUSTER-EVENTS-MIB", "eventClusterName"), ("SUN-CLUSTER-EVENTS-MIB", "eventNodeName"), ("SUN-CLUSTER-EVENTS-MIB", "eventVersion"), ("SUN-CLUSTER-EVENTS-MIB", "eventClassName"), ("SUN-CLUSTER-EVENTS-MIB", "eventSubclassName"), ("SUN-CLUSTER-EVENTS-MIB", "eventSeverity"), ("SUN-CLUSTER-EVENTS-MIB", "eventInitiator"), ("SUN-CLUSTER-EVENTS-MIB", "eventPublisher"), ("SUN-CLUSTER-EVENTS-MIB", "eventSeqNo"), ("SUN-CLUSTER-EVENTS-MIB", "eventPid"), ("SUN-CLUSTER-EVENTS-MIB", "eventTimeStamp"), ("SUN-CLUSTER-EVENTS-MIB", "eventData"))
if mibBuilder.loadTexts: escNewEvents.setStatus('current')
mibBuilder.exportSymbols("SUN-CLUSTER-EVENTS-MIB", ScEventData=ScEventData, ScEventSubclassName=ScEventSubclassName, eventClusterName=eventClusterName, escEventsAttributesTable=escEventsAttributesTable, eventClusterId=eventClusterId, eventInitiator=eventInitiator, prod=prod, escEventTableCount=escEventTableCount, escEventsAttributesEntry=escEventsAttributesEntry, eventPublisher=eventPublisher, escEventsTable=escEventsTable, ScEventIndex=ScEventIndex, ScEventAttributeValue=ScEventAttributeValue, scEventsMIBObjects=scEventsMIBObjects, eventNodeName=eventNodeName, ScEventAttributeName=ScEventAttributeName, attributeName=attributeName, escEventsEntry=escEventsEntry, eventSeqNo=eventSeqNo, ScTimeStamp=ScTimeStamp, attributeValue=attributeValue, eventVersion=eventVersion, eventSubclassName=eventSubclassName, ScEventInitiator=ScEventInitiator, ScEventClassName=ScEventClassName, escNewEvents=escNewEvents, PYSNMP_MODULE_ID=sunClusterEventsMIB, scEventsMIBNotifications=scEventsMIBNotifications, ScNodeName=ScNodeName, eventTimeStamp=eventTimeStamp, ScEventSeverity=ScEventSeverity, eventIndex=eventIndex, ScEventPublisher=ScEventPublisher, eventSeverity=eventSeverity, eventData=eventData, eventPid=eventPid, suncluster=suncluster, ScEventPid=ScEventPid, sunClusterEventsMIB=sunClusterEventsMIB, ScClusterId=ScClusterId, sun=sun, ScEventTableCount=ScEventTableCount, ScClusterName=ScClusterName, eventClassName=eventClassName, ScEventVersion=ScEventVersion)
