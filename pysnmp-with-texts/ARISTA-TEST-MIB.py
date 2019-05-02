#
# PySNMP MIB module ARISTA-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-TEST-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:25:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint")
ZeroBasedCounter32, = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
ObjectGroup, NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "NotificationGroup", "ModuleCompliance")
Counter64, MibIdentifier, Integer32, NotificationType, ObjectIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, Unsigned32, Gauge32, TimeTicks, Counter32, IpAddress, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Counter64", "MibIdentifier", "Integer32", "NotificationType", "ObjectIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "Unsigned32", "Gauge32", "TimeTicks", "Counter32", "IpAddress", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
aristaTestMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 3))
aristaTestMIB.setRevisions(('2014-08-15 00:00', '2011-03-31 13:00', '2010-12-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: aristaTestMIB.setRevisionsDescriptions(('Updated postal and e-mail addresses', 'Updated postal address and telephone', 'Initial revision.',))
if mibBuilder.loadTexts: aristaTestMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaTestMIB.setOrganization('Arista Networks, Inc.')
if mibBuilder.loadTexts: aristaTestMIB.setContactInfo('Arista Networks, Inc. Postal: 5453 Great America Parkway Santa Clara, CA 9505 Tel: +1 408 547-5500 E-mail: snmp@arista.com')
if mibBuilder.loadTexts: aristaTestMIB.setDescription('Arista Test MIB.')
aristaTestNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0))
aristaTestObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1))
aristaTestConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2))
aristaTestNotificationCounter = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 1), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaTestNotificationCounter.setStatus('current')
if mibBuilder.loadTexts: aristaTestNotificationCounter.setDescription('Notifications counter - the number of times this notification has been sent.')
aristaTestNotificationComment = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaTestNotificationComment.setStatus('current')
if mibBuilder.loadTexts: aristaTestNotificationComment.setDescription('Notification comment specified by the user executing the test command.')
aristaTestNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0))
aristaTestNotification = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0, 1)).setObjects(("ARISTA-TEST-MIB", "aristaTestNotificationCounter"), ("ARISTA-TEST-MIB", "aristaTestNotificationComment"))
if mibBuilder.loadTexts: aristaTestNotification.setStatus('current')
if mibBuilder.loadTexts: aristaTestNotification.setDescription('Arista test notification. This notification is triggered whenever the user executes the -test snmp notification- Cli command.')
aristaTestCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1))
aristaTestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2))
aristaTestCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1, 1)).setObjects(("ARISTA-TEST-MIB", "aristaTestObjectsGroup"), ("ARISTA-TEST-MIB", "aristaTestNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaTestCompliance = aristaTestCompliance.setStatus('current')
if mibBuilder.loadTexts: aristaTestCompliance.setDescription('The compliance statement for SNMP entities which implement the ARISTA TEST MIB.')
aristaTestObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 1)).setObjects(("ARISTA-TEST-MIB", "aristaTestNotificationCounter"), ("ARISTA-TEST-MIB", "aristaTestNotificationComment"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaTestObjectsGroup = aristaTestObjectsGroup.setStatus('current')
if mibBuilder.loadTexts: aristaTestObjectsGroup.setDescription('The collection of objects in the ARISTA TEST MIB.')
aristaTestNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 2)).setObjects(("ARISTA-TEST-MIB", "aristaTestNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaTestNotificationsGroup = aristaTestNotificationsGroup.setStatus('current')
if mibBuilder.loadTexts: aristaTestNotificationsGroup.setDescription('The collection of notifications in the ARISTA TEST MIB.')
mibBuilder.exportSymbols("ARISTA-TEST-MIB", aristaTestNotificationsGroup=aristaTestNotificationsGroup, aristaTestCompliance=aristaTestCompliance, aristaTestNotificationComment=aristaTestNotificationComment, aristaTestMIB=aristaTestMIB, aristaTestNotificationPrefix=aristaTestNotificationPrefix, aristaTestObjectsGroup=aristaTestObjectsGroup, aristaTestGroups=aristaTestGroups, PYSNMP_MODULE_ID=aristaTestMIB, aristaTestNotifications=aristaTestNotifications, aristaTestObjects=aristaTestObjects, aristaTestNotificationCounter=aristaTestNotificationCounter, aristaTestNotification=aristaTestNotification, aristaTestConformance=aristaTestConformance, aristaTestCompliances=aristaTestCompliances)
