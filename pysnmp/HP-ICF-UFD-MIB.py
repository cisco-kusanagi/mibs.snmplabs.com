#
# PySNMP MIB module HP-ICF-UFD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-ICF-UFD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:23:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion")
hpSwitch, = mibBuilder.importSymbols("HP-ICF-OID", "hpSwitch")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
TimeTicks, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn, ObjectIdentity, Counter64, Bits, IpAddress, MibIdentifier, Counter32, iso, Unsigned32, ModuleIdentity, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ObjectIdentity", "Counter64", "Bits", "IpAddress", "MibIdentifier", "Counter32", "iso", "Unsigned32", "ModuleIdentity", "NotificationType")
DisplayString, RowStatus, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "RowStatus", "TextualConvention")
hpicfUfdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74))
hpicfUfdMIB.setRevisions(('2012-04-30 00:00', '2011-05-12 00:00', '2010-02-06 15:39',))
if mibBuilder.loadTexts: hpicfUfdMIB.setLastUpdated('201204300000Z')
if mibBuilder.loadTexts: hpicfUfdMIB.setOrganization('HP Networking')
hpicfUfdNotifications = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0))
hpicfUfdConfigObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1))
hpicfUfdConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3))
class HpUfdTrackEntityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("ufd", 1))

class HpUfdTrackLinksSubtype(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("none", 0), ("portMap", 1), ("lacpKey", 2))

hpicfUfdScalars = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 1))
hpicfUfdAdminStatus = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("enable", 1), ("disable", 2))).clone('disable')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdAdminStatus.setStatus('current')
hpicfUfdNotifyTrackId = MibScalar((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 1, 2), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096))).setMaxAccess("accessiblefornotify")
if mibBuilder.loadTexts: hpicfUfdNotifyTrackId.setStatus('current')
hpicfUfdTrackEntities = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2))
hpicfUfdTrackTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1), )
if mibBuilder.loadTexts: hpicfUfdTrackTable.setStatus('current')
hpicfUfdTrackEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1), ).setIndexNames((0, "HP-ICF-UFD-MIB", "hpicfUfdTrackId"))
if mibBuilder.loadTexts: hpicfUfdTrackEntry.setStatus('current')
hpicfUfdTrackId = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 1), Integer32().subtype(subtypeSpec=ValueRangeConstraint(1, 4096)))
if mibBuilder.loadTexts: hpicfUfdTrackId.setStatus('current')
hpicfUfdTrackEntityType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 2), HpUfdTrackEntityType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdTrackEntityType.setStatus('current')
hpicfUfdLinksToMonitor = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 3), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdLinksToMonitor.setStatus('current')
hpicfUfdLinksToTransition = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 4), OctetString().subtype(subtypeSpec=ValueSizeConstraint(1, 1024))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdLinksToTransition.setStatus('current')
hpicfUfdLinksToMonitorState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("down", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUfdLinksToMonitorState.setStatus('current')
hpicfUfdLinksToTransitionState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("up", 1), ("autoDisabled", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUfdLinksToTransitionState.setStatus('current')
hpicfUfdTrackEntityState = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2))).clone(namedValues=NamedValues(("none", 0), ("ok", 1), ("failed", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUfdTrackEntityState.setStatus('current')
hpicfUfdTrackEntityRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 8), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: hpicfUfdTrackEntityRowStatus.setStatus('current')
hpicfUfdLinksToMonitorType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 9), HpUfdTrackLinksSubtype()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdLinksToMonitorType.setStatus('current')
hpicfUfdLinksToTransitionType = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 1, 1, 10), HpUfdTrackLinksSubtype()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: hpicfUfdLinksToTransitionType.setStatus('current')
hpicfUfdTrackedLinkTable = MibTable((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2), )
if mibBuilder.loadTexts: hpicfUfdTrackedLinkTable.setStatus('current')
hpicfUfdTrackedLinkEntry = MibTableRow((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2, 1), ).setIndexNames((0, "HP-ICF-UFD-MIB", "hpicfUfdTrackId"), (0, "HP-ICF-UFD-MIB", "hpicfUfdIfIndex"))
if mibBuilder.loadTexts: hpicfUfdTrackedLinkEntry.setStatus('current')
hpicfUfdIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2, 1, 1), InterfaceIndex())
if mibBuilder.loadTexts: hpicfUfdIfIndex.setStatus('current')
hpicfUfdLinkRole = MibTableColumn((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 1, 2, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("uplink", 1), ("downlink", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: hpicfUfdLinkRole.setStatus('current')
hpicfUfdNotificationPrefix = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0, 0))
hpicfUfdLtDAutoDisabled = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0, 0, 3)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdNotifyTrackId"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"))
if mibBuilder.loadTexts: hpicfUfdLtDAutoDisabled.setStatus('current')
hpicfUfdLtDAutoEnabled = NotificationType((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 0, 0, 4)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdNotifyTrackId"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"))
if mibBuilder.loadTexts: hpicfUfdLtDAutoEnabled.setStatus('current')
hpicfUfdCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1))
hpicfUfdGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2))
hpicfUfdCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1, 1)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdBaseGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdConfigGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdCompliance = hpicfUfdCompliance.setStatus('deprecated')
hpicfUfdCompliance1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 1, 2)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdBaseGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdConfigGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdNotificationGroup"), ("HP-ICF-UFD-MIB", "hpicfUfdConfigGroup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdCompliance1 = hpicfUfdCompliance1.setStatus('current')
hpicfUfdBaseGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 1)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdAdminStatus"), ("HP-ICF-UFD-MIB", "hpicfUfdNotifyTrackId"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdBaseGroup = hpicfUfdBaseGroup.setStatus('current')
hpicfUfdConfigGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 2)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityType"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitor"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransition"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitorState"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransitionState"), ("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityState"), ("HP-ICF-UFD-MIB", "hpicfUfdTrackEntityRowStatus"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToMonitorType"), ("HP-ICF-UFD-MIB", "hpicfUfdLinksToTransitionType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdConfigGroup = hpicfUfdConfigGroup.setStatus('current')
hpicfUfdNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 3)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdLtDAutoDisabled"), ("HP-ICF-UFD-MIB", "hpicfUfdLtDAutoEnabled"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdNotificationGroup = hpicfUfdNotificationGroup.setStatus('current')
hpicfUfdConfigGroup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 11, 2, 14, 11, 5, 1, 74, 3, 2, 4)).setObjects(("HP-ICF-UFD-MIB", "hpicfUfdLinkRole"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    hpicfUfdConfigGroup1 = hpicfUfdConfigGroup1.setStatus('current')
mibBuilder.exportSymbols("HP-ICF-UFD-MIB", hpicfUfdLinksToTransitionType=hpicfUfdLinksToTransitionType, hpicfUfdTrackedLinkTable=hpicfUfdTrackedLinkTable, hpicfUfdConfigGroup1=hpicfUfdConfigGroup1, hpicfUfdLinksToMonitorState=hpicfUfdLinksToMonitorState, hpicfUfdConformance=hpicfUfdConformance, hpicfUfdConfigObjects=hpicfUfdConfigObjects, HpUfdTrackLinksSubtype=HpUfdTrackLinksSubtype, hpicfUfdLinksToTransition=hpicfUfdLinksToTransition, hpicfUfdBaseGroup=hpicfUfdBaseGroup, hpicfUfdNotificationGroup=hpicfUfdNotificationGroup, hpicfUfdIfIndex=hpicfUfdIfIndex, hpicfUfdTrackEntities=hpicfUfdTrackEntities, hpicfUfdCompliance=hpicfUfdCompliance, hpicfUfdTrackId=hpicfUfdTrackId, hpicfUfdNotifyTrackId=hpicfUfdNotifyTrackId, hpicfUfdLinksToMonitorType=hpicfUfdLinksToMonitorType, hpicfUfdNotificationPrefix=hpicfUfdNotificationPrefix, hpicfUfdTrackEntityState=hpicfUfdTrackEntityState, hpicfUfdLtDAutoDisabled=hpicfUfdLtDAutoDisabled, hpicfUfdMIB=hpicfUfdMIB, HpUfdTrackEntityType=HpUfdTrackEntityType, hpicfUfdScalars=hpicfUfdScalars, hpicfUfdCompliance1=hpicfUfdCompliance1, hpicfUfdLtDAutoEnabled=hpicfUfdLtDAutoEnabled, hpicfUfdNotifications=hpicfUfdNotifications, hpicfUfdTrackTable=hpicfUfdTrackTable, hpicfUfdTrackEntityRowStatus=hpicfUfdTrackEntityRowStatus, hpicfUfdGroups=hpicfUfdGroups, hpicfUfdConfigGroup=hpicfUfdConfigGroup, hpicfUfdTrackedLinkEntry=hpicfUfdTrackedLinkEntry, PYSNMP_MODULE_ID=hpicfUfdMIB, hpicfUfdTrackEntityType=hpicfUfdTrackEntityType, hpicfUfdLinksToMonitor=hpicfUfdLinksToMonitor, hpicfUfdLinksToTransitionState=hpicfUfdLinksToTransitionState, hpicfUfdTrackEntry=hpicfUfdTrackEntry, hpicfUfdAdminStatus=hpicfUfdAdminStatus, hpicfUfdLinkRole=hpicfUfdLinkRole, hpicfUfdCompliances=hpicfUfdCompliances)
