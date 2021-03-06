#
# PySNMP MIB module APH323-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/APH323-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:23:24 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
acmepacketMgmt, = mibBuilder.importSymbols("ACMEPACKET-SMI", "acmepacketMgmt")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ValueRangeConstraint")
InetAddressPrefixLength, InetVersion, InetAddressType, InetAddress, InetZoneIndex = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetVersion", "InetAddressType", "InetAddress", "InetZoneIndex")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
Integer32, Counter32, IpAddress, Gauge32, ObjectIdentity, MibIdentifier, Bits, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, TimeTicks, NotificationType, Counter64, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Integer32", "Counter32", "IpAddress", "Gauge32", "ObjectIdentity", "MibIdentifier", "Bits", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "TimeTicks", "NotificationType", "Counter64", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
apH323Module = ModuleIdentity((1, 3, 6, 1, 4, 1, 9148, 3, 10))
apH323Module.setRevisions(('2012-07-16 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: apH323Module.setRevisionsDescriptions(('Updated contact info.',))
if mibBuilder.loadTexts: apH323Module.setLastUpdated('201207160000Z')
if mibBuilder.loadTexts: apH323Module.setOrganization('Acme Packet, Inc')
if mibBuilder.loadTexts: apH323Module.setContactInfo(' Customer Service Postal: Acme Packet, Inc 100 Crosby Drive Bedford, MA 01730 US Tel: 1-781-328-4400 E-mail: support@acmepacket.com')
if mibBuilder.loadTexts: apH323Module.setDescription(' The H323 MIB for Acme Packet, now includes statistical data for H323 entities.')
apH323MIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1))
apH323NotificationObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 2))
apH323NotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 3))
apH323Conformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4))
apH323Notifications = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 3, 0))
apH323Groups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 1))
apH323NotificationGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 2))
apH323StackTable = MibTable((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1), )
if mibBuilder.loadTexts: apH323StackTable.setStatus('current')
if mibBuilder.loadTexts: apH323StackTable.setDescription('h323 stack table')
apH323StackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1, 1), ).setIndexNames((1, "APH323-MIB", "apH323StackName"))
if mibBuilder.loadTexts: apH323StackEntry.setStatus('current')
if mibBuilder.loadTexts: apH323StackEntry.setDescription('A h323 stack entry')
apH323StackName = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1, 1, 1), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(1, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: apH323StackName.setStatus('current')
if mibBuilder.loadTexts: apH323StackName.setDescription('configured h323 stack name')
apH323StackCurrentCalls = MibTableColumn((1, 3, 6, 1, 4, 1, 9148, 3, 10, 1, 1, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: apH323StackCurrentCalls.setStatus('current')
if mibBuilder.loadTexts: apH323StackCurrentCalls.setDescription('Number of current calls.')
apH323StackMaxCalls = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 10, 2, 1), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apH323StackMaxCalls.setStatus('current')
if mibBuilder.loadTexts: apH323StackMaxCalls.setDescription('Number of max calls.')
apH323StackMaxCallsThreshold = MibScalar((1, 3, 6, 1, 4, 1, 9148, 3, 10, 2, 2), Unsigned32()).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: apH323StackMaxCallsThreshold.setStatus('current')
if mibBuilder.loadTexts: apH323StackMaxCallsThreshold.setDescription('Threshold value is the percentage of max calls.')
apH323StackMaxCallThresholdTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 10, 3, 0, 1)).setObjects(("APH323-MIB", "apH323StackName"), ("APH323-MIB", "apH323StackMaxCalls"), ("APH323-MIB", "apH323StackMaxCallsThreshold"), ("APH323-MIB", "apH323StackCurrentCalls"))
if mibBuilder.loadTexts: apH323StackMaxCallThresholdTrap.setStatus('current')
if mibBuilder.loadTexts: apH323StackMaxCallThresholdTrap.setDescription('This trap is sent if the number of h323 calls increases percentage of the max-calls threshold ')
apH323StackMaxCallThresholdClearTrap = NotificationType((1, 3, 6, 1, 4, 1, 9148, 3, 10, 3, 0, 2)).setObjects(("APH323-MIB", "apH323StackName"), ("APH323-MIB", "apH323StackMaxCalls"), ("APH323-MIB", "apH323StackMaxCallsThreshold"), ("APH323-MIB", "apH323StackCurrentCalls"))
if mibBuilder.loadTexts: apH323StackMaxCallThresholdClearTrap.setStatus('current')
if mibBuilder.loadTexts: apH323StackMaxCallThresholdClearTrap.setDescription('This trap is sent if the number of h323 calls decreases to below the lowest max-calls threshold')
apH323StackObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 1, 1)).setObjects(("APH323-MIB", "apH323StackName"), ("APH323-MIB", "apH323StackCurrentCalls"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackObjectsGroup = apH323StackObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: apH323StackObjectsGroup.setDescription('A collection of objects providing h323 stack information')
apH323StackNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9148, 3, 10, 4, 2, 1)).setObjects(("APH323-MIB", "apH323StackMaxCallThresholdTrap"), ("APH323-MIB", "apH323StackMaxCallThresholdClearTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    apH323StackNotificationsGroup = apH323StackNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: apH323StackNotificationsGroup.setDescription('A collection of h323 stack notifications')
mibBuilder.exportSymbols("APH323-MIB", apH323StackTable=apH323StackTable, apH323StackName=apH323StackName, apH323StackNotificationsGroup=apH323StackNotificationsGroup, apH323StackCurrentCalls=apH323StackCurrentCalls, apH323Conformance=apH323Conformance, apH323StackMaxCallsThreshold=apH323StackMaxCallsThreshold, apH323StackMaxCallThresholdTrap=apH323StackMaxCallThresholdTrap, apH323NotificationObjects=apH323NotificationObjects, apH323StackEntry=apH323StackEntry, apH323MIBObjects=apH323MIBObjects, apH323Module=apH323Module, apH323NotificationGroups=apH323NotificationGroups, apH323StackMaxCallThresholdClearTrap=apH323StackMaxCallThresholdClearTrap, apH323StackObjectsGroup=apH323StackObjectsGroup, apH323Groups=apH323Groups, PYSNMP_MODULE_ID=apH323Module, apH323NotificationPrefix=apH323NotificationPrefix, apH323StackMaxCalls=apH323StackMaxCalls, apH323Notifications=apH323Notifications)
