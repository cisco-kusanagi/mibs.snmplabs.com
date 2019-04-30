#
# PySNMP MIB module MTSALLSTREAM-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MTSALLSTREAM-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:05:59 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, MibIdentifier, TimeTicks, NotificationType, ObjectIdentity, Bits, Integer32, ModuleIdentity, IpAddress, iso, Counter32, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "MibIdentifier", "TimeTicks", "NotificationType", "ObjectIdentity", "Bits", "Integer32", "ModuleIdentity", "IpAddress", "iso", "Counter32", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
mtsallstream = ModuleIdentity((1, 3, 6, 1, 4, 1, 23398))
if mibBuilder.loadTexts: mtsallstream.setLastUpdated('200505240000Z')
if mibBuilder.loadTexts: mtsallstream.setOrganization('MTS Allstream')
allstreamObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 1))
allstreamMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 2))
allstreamCICEventEntities = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 1, 1))
cicEventID = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 1), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 4294967295))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicEventID.setStatus('current')
cicNode = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 2), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicNode.setStatus('current')
cicEventMessage = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 3), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicEventMessage.setStatus('current')
cicEventSeverity = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicEventSeverity.setStatus('current')
cicEventTrapReason = MibScalar((1, 3, 6, 1, 4, 1, 23398, 1, 1, 5), DisplayString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cicEventTrapReason.setStatus('current')
allstreamNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 1, 20))
allstreamForwardCICEventTrap = NotificationType((1, 3, 6, 1, 4, 1, 23398, 1, 20, 1)).setObjects(("MTSALLSTREAM-MIB", "cicEventID"), ("MTSALLSTREAM-MIB", "cicNode"), ("MTSALLSTREAM-MIB", "cicEventMessage"), ("MTSALLSTREAM-MIB", "cicEventSeverity"), ("MTSALLSTREAM-MIB", "cicEventTrapReason"))
if mibBuilder.loadTexts: allstreamForwardCICEventTrap.setStatus('current')
allstreamCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 2, 1))
allstreamGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 23398, 2, 2))
allstreamBasicCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 23398, 2, 1, 1)).setObjects(("MTSALLSTREAM-MIB", "allstreamNotificationsGroup"), ("MTSALLSTREAM-MIB", "allstreamObjectGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    allstreamBasicCompliance = allstreamBasicCompliance.setStatus('current')
allstreamNotificationsGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 23398, 2, 2, 1)).setObjects(("MTSALLSTREAM-MIB", "allstreamForwardCICEventTrap"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    allstreamNotificationsGroup = allstreamNotificationsGroup.setStatus('current')
allstreamObjectGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 23398, 2, 2, 2)).setObjects(("MTSALLSTREAM-MIB", "cicEventID"), ("MTSALLSTREAM-MIB", "cicNode"), ("MTSALLSTREAM-MIB", "cicEventMessage"), ("MTSALLSTREAM-MIB", "cicEventSeverity"), ("MTSALLSTREAM-MIB", "cicEventTrapReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    allstreamObjectGroup = allstreamObjectGroup.setStatus('current')
mibBuilder.exportSymbols("MTSALLSTREAM-MIB", allstreamNotifications=allstreamNotifications, cicEventID=cicEventID, allstreamBasicCompliance=allstreamBasicCompliance, allstreamGroups=allstreamGroups, PYSNMP_MODULE_ID=mtsallstream, mtsallstream=mtsallstream, allstreamObjects=allstreamObjects, cicNode=cicNode, cicEventMessage=cicEventMessage, allstreamNotificationsGroup=allstreamNotificationsGroup, cicEventTrapReason=cicEventTrapReason, allstreamCompliances=allstreamCompliances, allstreamForwardCICEventTrap=allstreamForwardCICEventTrap, allstreamCICEventEntities=allstreamCICEventEntities, allstreamMIBConformance=allstreamMIBConformance, allstreamObjectGroup=allstreamObjectGroup, cicEventSeverity=cicEventSeverity)
