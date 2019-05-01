#
# PySNMP MIB module CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:18:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint")
ciscoWan, = mibBuilder.importSymbols("CISCOWAN-SMI", "ciscoWan")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, Counter64, Counter32, IpAddress, Unsigned32, MibIdentifier, NotificationType, Integer32, TimeTicks, Bits, iso, ModuleIdentity, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "Counter64", "Counter32", "IpAddress", "Unsigned32", "MibIdentifier", "NotificationType", "Integer32", "TimeTicks", "Bits", "iso", "ModuleIdentity", "ObjectIdentity")
TextualConvention, RowStatus, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "RowStatus", "DisplayString")
ciscoWanPersistentXgcpEventsMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 351, 150, 18))
ciscoWanPersistentXgcpEventsMIB.setRevisions(('2003-10-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setRevisionsDescriptions(('Update descriptions in the MIB. ',))
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setLastUpdated('200310200000Z')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-voice@cisco.com')
if mibBuilder.loadTexts: ciscoWanPersistentXgcpEventsMIB.setDescription('The MIB module for managing CA(Call Agent) events. ')
ciscoWanPersistentXgcpEventsMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1))
persistentXgcpEvents = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1))
persistentXgcpEventsTable = MibTable((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1), )
if mibBuilder.loadTexts: persistentXgcpEventsTable.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsTable.setDescription('The persistentXgcpEventsTable contains configuration information about xGCP events which involve a persistent notification request. ')
persistentXgcpEventsEntry = MibTableRow((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventNum"))
if mibBuilder.loadTexts: persistentXgcpEventsEntry.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsEntry.setDescription("An entry in the persistentXgcpEventsTable. Each entry consists of persistentXgcpEventNum - Index to the persistentXgcpEventsTable. persistentXgcpEventName - Name of the xGCP event that needs persistent notification to the call agent for example 't/hd'. persistentXgcpEventRowStatus -This indicates whether an xGCP event is added in this entry or not. This table is not created implicitly. The user can add xGCP event or delete an xGCP event. ")
persistentXgcpEventNum = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 16)))
if mibBuilder.loadTexts: persistentXgcpEventNum.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventNum.setDescription('This object is a index to persistentXgcpEventsTable. ')
persistentXgcpEventName = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 64))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventName.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventName.setDescription("This object holds the name of the event for example 't/hd' or 't/hu'. ")
persistentXgcpEventRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 351, 150, 18, 1, 1, 1, 1, 3), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: persistentXgcpEventRowStatus.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventRowStatus.setDescription("This object allows to add or delete an entry. Modifying an entry is not allowed. An entry may be created using the 'createAndGo' option. When the row is successfully created, the RowStatus would be set to 'active' by the agent. An entry may be deleted by setting the RowStatus to 'destroy'. Other options such as `CreateAndWait', 'notInService', 'notReady' will not be used. For creating an entry the persistentXgcpEventNum and persistentXgcpEventName must be provided. This object tells call control whether or not a particular xGCP event is added or not, based on this the call control module will decide whether or not to notify (NTFY) call agent when a particular xGCP event is received, without waiting for CA to request for that event. ")
persistentXgcpEventsMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2))
persistentXgcpEventsMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1))
persistentXgcpEventsMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2))
persistentXgcpEventsMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 1, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventsMIBGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBCompliance = persistentXgcpEventsMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsMIBCompliance.setDescription(' The complaince statement for persistent Xgcp events which implement persistentXgcpEvents MIB.')
persistentXgcpEventsMIBGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 351, 150, 18, 2, 2, 1)).setObjects(("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventName"), ("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", "persistentXgcpEventRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    persistentXgcpEventsMIBGroup = persistentXgcpEventsMIBGroup.setStatus('current')
if mibBuilder.loadTexts: persistentXgcpEventsMIBGroup.setDescription('This group contains objects related to configuration of persistent xGCP events. ')
mibBuilder.exportSymbols("CISCO-WAN-PERSISTENT-XGCP-EVENTS-MIB", persistentXgcpEventRowStatus=persistentXgcpEventRowStatus, persistentXgcpEventsMIBGroup=persistentXgcpEventsMIBGroup, persistentXgcpEventsMIBCompliances=persistentXgcpEventsMIBCompliances, persistentXgcpEventsMIBGroups=persistentXgcpEventsMIBGroups, ciscoWanPersistentXgcpEventsMIBObjects=ciscoWanPersistentXgcpEventsMIBObjects, persistentXgcpEventsTable=persistentXgcpEventsTable, persistentXgcpEventsMIBCompliance=persistentXgcpEventsMIBCompliance, PYSNMP_MODULE_ID=ciscoWanPersistentXgcpEventsMIB, persistentXgcpEventsMIBConformance=persistentXgcpEventsMIBConformance, persistentXgcpEventsEntry=persistentXgcpEventsEntry, ciscoWanPersistentXgcpEventsMIB=ciscoWanPersistentXgcpEventsMIB, persistentXgcpEventName=persistentXgcpEventName, persistentXgcpEvents=persistentXgcpEvents, persistentXgcpEventNum=persistentXgcpEventNum)
