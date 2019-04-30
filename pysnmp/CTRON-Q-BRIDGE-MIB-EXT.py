#
# PySNMP MIB module CTRON-Q-BRIDGE-MIB-EXT (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CTRON-Q-BRIDGE-MIB-EXT
# Produced by pysmi-0.3.4 at Mon Apr 29 18:14:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
dot1dBasePort, dot1dBasePortEntry = mibBuilder.importSymbols("BRIDGE-MIB", "dot1dBasePort", "dot1dBasePortEntry")
ctVlanExt, = mibBuilder.importSymbols("CTRON-MIB-NAMES", "ctVlanExt")
EnabledStatus, = mibBuilder.importSymbols("P-BRIDGE-MIB", "EnabledStatus")
dot1qVlanIndex, dot1qFdbId, dot1qVlanCurrentEntry, PortList, VlanIndex, dot1qTpFdbAddress = mibBuilder.importSymbols("Q-BRIDGE-MIB", "dot1qVlanIndex", "dot1qFdbId", "dot1qVlanCurrentEntry", "PortList", "VlanIndex", "dot1qTpFdbAddress")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
TimeTicks, Counter64, Unsigned32, Counter32, ObjectIdentity, IpAddress, Bits, iso, Integer32, Gauge32, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "TimeTicks", "Counter64", "Unsigned32", "Counter32", "ObjectIdentity", "IpAddress", "Bits", "iso", "Integer32", "Gauge32", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "ModuleIdentity")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ctQBridgeMibExt = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7))
ctQBridgeMibExt.setRevisions(('2007-02-16 17:44', '2005-01-21 17:17', '2004-06-04 12:41', '2003-12-15 20:53', '2002-07-26 20:45', '2002-07-19 14:12', '2001-04-16 18:16', '2001-01-10 13:29', '1999-10-06 08:12',))
if mibBuilder.loadTexts: ctQBridgeMibExt.setLastUpdated('200702161744Z')
if mibBuilder.loadTexts: ctQBridgeMibExt.setOrganization('Enterasys Networks, Inc.')
ctQBridgeMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1))
ctDot1qPortVlanExtTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1), )
if mibBuilder.loadTexts: ctDot1qPortVlanExtTable.setStatus('current')
ctDot1qPortVlanEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1), )
dot1dBasePortEntry.registerAugmentions(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEntry"))
ctDot1qPortVlanEntry.setIndexNames(*dot1dBasePortEntry.getIndexNames())
if mibBuilder.loadTexts: ctDot1qPortVlanEntry.setStatus('current')
ctDot1qPortDefaultForwardMode = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("forwardNoFrames", 1), ("forwardAllFramesAsTagged", 2), ("forwardAllFramesAsUntagged", 3))).clone('forwardNoFrames')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qPortDefaultForwardMode.setStatus('current')
ctDot1qPortDiscardTagged = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qPortDiscardTagged.setStatus('current')
ctDot1qPortReplaceTCI = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 1, 1, 3), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qPortReplaceTCI.setStatus('current')
ctDot1qVlanDynamicEgressTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2), )
if mibBuilder.loadTexts: ctDot1qVlanDynamicEgressTable.setStatus('current')
ctDot1qVlanDynamicEgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2, 1), ).setIndexNames((0, "CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanDynamicEgressIndex"))
if mibBuilder.loadTexts: ctDot1qVlanDynamicEgressEntry.setStatus('current')
ctDot1qVlanDynamicEgressIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2, 1, 1), VlanIndex())
if mibBuilder.loadTexts: ctDot1qVlanDynamicEgressIndex.setStatus('current')
ctDot1qVlanDynamicEgressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 2, 1, 2), EnabledStatus().clone('disabled')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qVlanDynamicEgressStatus.setStatus('current')
ctDot1qVlanCurrentExtTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 3), )
if mibBuilder.loadTexts: ctDot1qVlanCurrentExtTable.setStatus('current')
ctDot1qVlanCurrentEntryExt = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 3, 1), )
dot1qVlanCurrentEntry.registerAugmentions(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanCurrentEntryExt"))
ctDot1qVlanCurrentEntryExt.setIndexNames(*dot1qVlanCurrentEntry.getIndexNames())
if mibBuilder.loadTexts: ctDot1qVlanCurrentEntryExt.setStatus('current')
ctDot1qVlanForbidEgressPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 3, 1, 1), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDot1qVlanForbidEgressPorts.setStatus('current')
ctDot1qPortVlanEgressTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4), )
if mibBuilder.loadTexts: ctDot1qPortVlanEgressTable.setStatus('current')
ctDot1qPortVlanEgressEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4, 1), ).setIndexNames((0, "BRIDGE-MIB", "dot1dBasePort"), (0, "Q-BRIDGE-MIB", "dot1qVlanIndex"))
if mibBuilder.loadTexts: ctDot1qPortVlanEgressEntry.setStatus('current')
ctDot1qPortVlanEgressStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("other", 1), ("static", 2), ("gvrp", 3), ("ctDynamicEgress", 4), ("etsysPolicyProfile", 5), ("ctPortDefFwdMode", 6), ("rfc3580VlanTunnelAttribute", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDot1qPortVlanEgressStatus.setStatus('current')
ctDot1qPortVlanEgressType = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 4, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("tagged", 1), ("untagged", 2), ("forbidden", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: ctDot1qPortVlanEgressType.setStatus('current')
ctDot1qTpFdbExtTable = MibTable((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 5), )
if mibBuilder.loadTexts: ctDot1qTpFdbExtTable.setStatus('current')
ctDot1qTpFdbExtEntry = MibTableRow((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 5, 1), ).setIndexNames((0, "Q-BRIDGE-MIB", "dot1qFdbId"), (0, "Q-BRIDGE-MIB", "dot1qTpFdbAddress"))
if mibBuilder.loadTexts: ctDot1qTpFdbExtEntry.setStatus('current')
ctDot1qTpFdbRemoveAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 1, 5, 1, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: ctDot1qTpFdbRemoveAddress.setStatus('current')
ctQBridgeConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2))
ctQBridgeGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1))
ctQBridgeCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2))
ctQBridgePortGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 1)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortDefaultForwardMode"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgePortGroup = ctQBridgePortGroup.setStatus('deprecated')
ctQBridgeVlanGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 2)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanDynamicEgressStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgeVlanGroup = ctQBridgeVlanGroup.setStatus('current')
ctQBridgePortGroup2 = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 3)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortDefaultForwardMode"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortDiscardTagged"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgePortGroup2 = ctQBridgePortGroup2.setStatus('current')
ctQBridgeVlanCurrentForbidGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 4)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qVlanForbidEgressPorts"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgeVlanCurrentForbidGroup = ctQBridgeVlanCurrentForbidGroup.setStatus('current')
ctQBridgePortReplaceTCIGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 5)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortReplaceTCI"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgePortReplaceTCIGroup = ctQBridgePortReplaceTCIGroup.setStatus('current')
ctQBridgePortVlanEgressGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 6)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEgressStatus"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qPortVlanEgressType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgePortVlanEgressGroup = ctQBridgePortVlanEgressGroup.setStatus('current')
ctQBridgeTpFdbTableExtGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 1, 7)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctDot1qTpFdbRemoveAddress"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctQBridgeTpFdbTableExtGroup = ctQBridgeTpFdbTableExtGroup.setStatus('current')
ctDot1qVlan = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 1)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortGroup"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeVlanGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qVlan = ctDot1qVlan.setStatus('deprecated')
ctDot1qVlan2 = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 2)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeVlanGroup"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortGroup2"), ("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortReplaceTCIGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qVlan2 = ctDot1qVlan2.setStatus('current')
ctDot1qVlanCurentCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 3)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeVlanCurrentForbidGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qVlanCurentCompliance = ctDot1qVlanCurentCompliance.setStatus('current')
ctDot1qPortVlanEgressCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 4)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgePortVlanEgressGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qPortVlanEgressCompliance = ctDot1qPortVlanEgressCompliance.setStatus('current')
ctDot1qTpFdbTableExtCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 52, 4, 1, 2, 16, 7, 2, 2, 5)).setObjects(("CTRON-Q-BRIDGE-MIB-EXT", "ctQBridgeTpFdbTableExtGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ctDot1qTpFdbTableExtCompliance = ctDot1qTpFdbTableExtCompliance.setStatus('current')
mibBuilder.exportSymbols("CTRON-Q-BRIDGE-MIB-EXT", ctQBridgeConformance=ctQBridgeConformance, ctQBridgePortGroup2=ctQBridgePortGroup2, ctDot1qVlanCurentCompliance=ctDot1qVlanCurentCompliance, ctDot1qVlanCurrentEntryExt=ctDot1qVlanCurrentEntryExt, ctDot1qVlan=ctDot1qVlan, ctDot1qVlanForbidEgressPorts=ctDot1qVlanForbidEgressPorts, ctDot1qPortVlanEntry=ctDot1qPortVlanEntry, PYSNMP_MODULE_ID=ctQBridgeMibExt, ctQBridgePortReplaceTCIGroup=ctQBridgePortReplaceTCIGroup, ctDot1qPortVlanExtTable=ctDot1qPortVlanExtTable, ctQBridgePortVlanEgressGroup=ctQBridgePortVlanEgressGroup, ctDot1qPortVlanEgressType=ctDot1qPortVlanEgressType, ctQBridgeVlanGroup=ctQBridgeVlanGroup, ctDot1qVlanDynamicEgressEntry=ctDot1qVlanDynamicEgressEntry, ctDot1qTpFdbExtEntry=ctDot1qTpFdbExtEntry, ctDot1qVlanDynamicEgressTable=ctDot1qVlanDynamicEgressTable, ctDot1qTpFdbRemoveAddress=ctDot1qTpFdbRemoveAddress, ctDot1qPortVlanEgressEntry=ctDot1qPortVlanEgressEntry, ctDot1qPortDiscardTagged=ctDot1qPortDiscardTagged, ctQBridgeMIBObjects=ctQBridgeMIBObjects, ctQBridgeGroups=ctQBridgeGroups, ctDot1qVlan2=ctDot1qVlan2, ctDot1qPortVlanEgressCompliance=ctDot1qPortVlanEgressCompliance, ctDot1qVlanDynamicEgressIndex=ctDot1qVlanDynamicEgressIndex, ctQBridgeMibExt=ctQBridgeMibExt, ctDot1qPortReplaceTCI=ctDot1qPortReplaceTCI, ctQBridgeTpFdbTableExtGroup=ctQBridgeTpFdbTableExtGroup, ctQBridgePortGroup=ctQBridgePortGroup, ctDot1qTpFdbExtTable=ctDot1qTpFdbExtTable, ctDot1qTpFdbTableExtCompliance=ctDot1qTpFdbTableExtCompliance, ctDot1qVlanDynamicEgressStatus=ctDot1qVlanDynamicEgressStatus, ctQBridgeCompliances=ctQBridgeCompliances, ctDot1qPortVlanEgressStatus=ctDot1qPortVlanEgressStatus, ctQBridgeVlanCurrentForbidGroup=ctQBridgeVlanCurrentForbidGroup, ctDot1qPortDefaultForwardMode=ctDot1qPortDefaultForwardMode, ctDot1qVlanCurrentExtTable=ctDot1qVlanCurrentExtTable, ctDot1qPortVlanEgressTable=ctDot1qPortVlanEgressTable)
