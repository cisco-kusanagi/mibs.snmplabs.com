#
# PySNMP MIB module ARISTA-TEST-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ARISTA-TEST-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:09:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
aristaMibs, = mibBuilder.importSymbols("ARISTA-SMI-MIB", "aristaMibs")
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ZeroBasedCounter32, = mibBuilder.importSymbols("RMON2-MIB", "ZeroBasedCounter32")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
Counter32, Bits, ObjectIdentity, Counter64, MibIdentifier, Gauge32, NotificationType, ModuleIdentity, iso, TimeTicks, IpAddress, Unsigned32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "ObjectIdentity", "Counter64", "MibIdentifier", "Gauge32", "NotificationType", "ModuleIdentity", "iso", "TimeTicks", "IpAddress", "Unsigned32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
aristaTestMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 30065, 3, 3))
aristaTestMIB.setRevisions(('2014-08-15 00:00', '2011-03-31 13:00', '2010-12-01 00:00',))
if mibBuilder.loadTexts: aristaTestMIB.setLastUpdated('201408150000Z')
if mibBuilder.loadTexts: aristaTestMIB.setOrganization('Arista Networks, Inc.')
aristaTestNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0))
aristaTestObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1))
aristaTestConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2))
aristaTestNotificationCounter = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 1), ZeroBasedCounter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaTestNotificationCounter.setStatus('current')
aristaTestNotificationComment = MibScalar((1, 3, 6, 1, 4, 1, 30065, 3, 3, 1, 2), DisplayString().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readonly")
if mibBuilder.loadTexts: aristaTestNotificationComment.setStatus('current')
aristaTestNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0))
aristaTestNotification = NotificationType((1, 3, 6, 1, 4, 1, 30065, 3, 3, 0, 0, 1)).setObjects(("ARISTA-TEST-MIB", "aristaTestNotificationCounter"), ("ARISTA-TEST-MIB", "aristaTestNotificationComment"))
if mibBuilder.loadTexts: aristaTestNotification.setStatus('current')
aristaTestCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1))
aristaTestGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2))
aristaTestCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 1, 1)).setObjects(("ARISTA-TEST-MIB", "aristaTestObjectsGroup"), ("ARISTA-TEST-MIB", "aristaTestNotificationsGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaTestCompliance = aristaTestCompliance.setStatus('current')
aristaTestObjectsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 1)).setObjects(("ARISTA-TEST-MIB", "aristaTestNotificationCounter"), ("ARISTA-TEST-MIB", "aristaTestNotificationComment"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaTestObjectsGroup = aristaTestObjectsGroup.setStatus('current')
aristaTestNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 30065, 3, 3, 2, 2, 2)).setObjects(("ARISTA-TEST-MIB", "aristaTestNotification"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    aristaTestNotificationsGroup = aristaTestNotificationsGroup.setStatus('current')
mibBuilder.exportSymbols("ARISTA-TEST-MIB", aristaTestNotification=aristaTestNotification, aristaTestNotifications=aristaTestNotifications, aristaTestNotificationCounter=aristaTestNotificationCounter, aristaTestMIB=aristaTestMIB, PYSNMP_MODULE_ID=aristaTestMIB, aristaTestNotificationPrefix=aristaTestNotificationPrefix, aristaTestGroups=aristaTestGroups, aristaTestObjectsGroup=aristaTestObjectsGroup, aristaTestCompliance=aristaTestCompliance, aristaTestObjects=aristaTestObjects, aristaTestConformance=aristaTestConformance, aristaTestNotificationsGroup=aristaTestNotificationsGroup, aristaTestNotificationComment=aristaTestNotificationComment, aristaTestCompliances=aristaTestCompliances)
