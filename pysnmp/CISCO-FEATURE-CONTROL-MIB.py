#
# PySNMP MIB module CISCO-FEATURE-CONTROL-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-FEATURE-CONTROL-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:41:19 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
MibIdentifier, ModuleIdentity, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType, Counter64, ObjectIdentity, Counter32, Unsigned32, Integer32, TimeTicks, iso, Bits, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "ModuleIdentity", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType", "Counter64", "ObjectIdentity", "Counter32", "Unsigned32", "Integer32", "TimeTicks", "iso", "Bits", "IpAddress")
DisplayString, TruthValue, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TruthValue", "TextualConvention")
ciscoFeatureCtrlMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 377))
ciscoFeatureCtrlMIB.setRevisions(('2016-11-16 00:00', '2016-10-25 00:00', '2016-03-11 00:00', '2015-10-09 00:00', '2014-12-24 00:00', '2014-04-09 00:00', '2013-07-29 00:00', '2013-05-28 00:00', '2012-03-22 00:00', '2011-06-09 00:00', '2009-08-11 00:00', '2008-12-05 00:00', '2008-06-27 00:00', '2008-06-12 00:00', '2008-03-13 00:00', '2007-05-04 00:00', '2007-01-22 00:00', '2005-12-27 00:00', '2004-12-28 00:00', '2004-07-06 00:00', '2003-11-22 00:00',))
if mibBuilder.loadTexts: ciscoFeatureCtrlMIB.setLastUpdated('201611160000Z')
if mibBuilder.loadTexts: ciscoFeatureCtrlMIB.setOrganization('Cisco Systems, Inc.')
ciscoFeatureCtrlMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 377, 0))
ciscoFeatureCtrlMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 377, 1))
ciscoFeatureCtrlMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 377, 2))
cfcFeature = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1))
cfcNotifControl = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 2))
class CiscoOptionalFeature(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 134, 135, 136, 137, 138, 139, 140, 141, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 200, 264, 9875))
    namedValues = NamedValues(("ivr", 1), ("fcip", 2), ("fcsp", 3), ("ficon", 4), ("iscsi", 5), ("tacacs", 6), ("qosManager", 7), ("portSecurity", 8), ("fabricBinding", 9), ("iscsiInterfaceVsanMembership", 10), ("ike", 11), ("isns", 12), ("ipSec", 13), ("portTracker", 14), ("scheduler", 15), ("npiv", 16), ("sanExtTuner", 17), ("dpvm", 18), ("extenedCredit", 19), ("cloudDiscovery", 20), ("isis", 21), ("ospf", 22), ("ospfV3", 23), ("rip", 24), ("bgp", 25), ("pim", 26), ("igmp", 27), ("msdp", 28), ("pim6", 29), ("eigrp", 30), ("sdv", 31), ("cluster", 32), ("sme", 33), ("lacp", 34), ("amt", 35), ("dot1x", 36), ("npv", 37), ("l2nac", 38), ("glbp", 39), ("dhcpSnooping", 40), ("hsrp", 41), ("svi", 42), ("vmm", 43), ("pvlan", 44), ("tunnelManager", 45), ("ethPortSec", 46), ("lisp", 47), ("trustSec", 48), ("copp", 49), ("udld", 50), ("mcecm", 51), ("pbr", 52), ("nfm", 53), ("isapi", 54), ("vrrp", 55), ("netSift", 56), ("isisL2", 57), ("cimServer", 58), ("otv", 59), ("sanTap", 60), ("nasb", 61), ("dmm", 62), ("u2rib", 63), ("isisOtv", 64), ("orib", 65), ("fcoe", 66), ("siaServiceBroker", 67), ("evfp", 68), ("vtp", 69), ("splitter", 70), ("sfm", 71), ("ioa", 72), ("telnetServer", 73), ("sshServer", 74), ("httpServer", 75), ("wccp", 76), ("siaSve", 77), ("xcvrFreq", 78), ("assocMgr", 79), ("lldp", 80), ("rsvp", 81), ("ldp", 82), ("te", 83), ("mplsOam", 84), ("l2vpn", 85), ("drap", 86), ("bfd", 87), ("bfdApp", 88), ("fex", 89), ("pong", 90), ("rtp", 91), ("ldap", 92), ("privilege", 93), ("oim", 94), ("mplsMgr", 95), ("ulib", 96), ("scp", 97), ("sftp", 98), ("l3vpn", 99), ("mvpn", 101), ("ipPool", 102), ("uufb", 103), ("umfb", 104), ("ethernetNpv", 105), ("wccpClient", 106), ("scadaGw", 107), ("poe", 108), ("flexlink", 109), ("niv", 110), ("vem", 111), ("ewise", 112), ("onep", 113), ("slaS", 114), ("slaR", 115), ("rise", 116), ("pppManager", 117), ("itronMcastAgent", 118), ("vsmAggregation", 119), ("segmentation", 120), ("vrrpv3", 121), ("vTracker", 122), ("fdmi", 123), ("cmm", 124), ("ntp", 125), ("fabricAccess", 126), ("nat", 127), ("vlanVnSeg", 128), ("bulkStat", 129), ("bbu", 130), ("vnSegment", 131), ("evb", 132), ("ngMvpn", 134), ("hmm", 135), ("vxlan", 136), ("mvrp", 137), ("evmed", 138), ("nSegMgr", 139), ("vff", 140), ("sol", 141), ("nxapi", 143), ("itd", 144), ("vmTracker", 145), ("xosFeatureTest", 146), ("xosMIFeatureTest", 147), ("nxschema", 148), ("mplsStatic", 149), ("imp", 150), ("evc", 151), ("ptp", 152), ("bashShell", 153), ("nxdb", 154), ("ngoam", 155), ("mld", 156), ("evpn", 157), ("smartChannel", 158), ("openFlow", 159), ("mplsSegmentRouting", 160), ("analytics", 161), ("ipp", 162), ("licenseSmart", 163), ("pmn", 164), ("dpt", 165), ("ngmvpn", 166), ("dciTunnelInterop", 167), ("fabricTelemetry", 168), ("plb", 169), ("vmis", 170), ("ldbmgr", 171), ("icam", 172), ("catena", 173), ("licensePlr", 174), ("poap", 200), ("sflow", 264), ("elo", 9875))

class CiscoOptionalFeatureSet(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 7, 8))
    namedValues = NamedValues(("fcoe", 1), ("l2mp", 2), ("fex", 3), ("mpls", 4), ("fabric", 7), ("fcoenpv", 8))

class CiscoFeatureAction(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("noOp", 1), ("enable", 2), ("disable", 3), ("install", 4), ("uninstall", 5), ("allow", 6), ("disallow", 7))

class CiscoFeatureStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("enabled", 2), ("disabled", 3), ("installed", 4), ("uninstalled", 5), ("enabledNotRunning", 6))

class CiscoFeatureActionResult(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("actionSuccess", 2), ("actionFailed", 3), ("actionInProgress", 4))

cfcFeatureCtrlTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1), )
if mibBuilder.loadTexts: cfcFeatureCtrlTable.setStatus('deprecated')
cfcFeatureCtrlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1), ).setIndexNames((0, "CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlIndex"))
if mibBuilder.loadTexts: cfcFeatureCtrlEntry.setStatus('deprecated')
cfcFeatureCtrlIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 1), CiscoOptionalFeature())
if mibBuilder.loadTexts: cfcFeatureCtrlIndex.setStatus('deprecated')
cfcFeatureCtrlName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 2), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlName.setStatus('deprecated')
cfcFeatureCtrlAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 3), CiscoFeatureAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcFeatureCtrlAction.setStatus('deprecated')
cfcFeatureCtrlLastAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 4), CiscoFeatureAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlLastAction.setStatus('deprecated')
cfcFeatureCtrlLastActionResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 5), CiscoFeatureActionResult()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlLastActionResult.setStatus('deprecated')
cfcFeatureCtrlLastFailureReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlLastFailureReason.setStatus('deprecated')
cfcFeatureCtrlOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 7), CiscoFeatureStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlOpStatus.setStatus('deprecated')
cfcFeatureCtrlOpStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 1, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlOpStatusReason.setStatus('deprecated')
cfcFeatureCtrl2Table = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2), )
if mibBuilder.loadTexts: cfcFeatureCtrl2Table.setStatus('current')
cfcFeatureCtrl2Entry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlIndex2"), (0, "CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlInstanceNum2"))
if mibBuilder.loadTexts: cfcFeatureCtrl2Entry.setStatus('current')
cfcFeatureCtrlIndex2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 1), CiscoOptionalFeature())
if mibBuilder.loadTexts: cfcFeatureCtrlIndex2.setStatus('current')
cfcFeatureCtrlInstanceNum2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 2), Unsigned32())
if mibBuilder.loadTexts: cfcFeatureCtrlInstanceNum2.setStatus('current')
cfcFeatureCtrlName2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 3), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(1, 32))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlName2.setStatus('current')
cfcFeatureCtrlAction2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 4), CiscoFeatureAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcFeatureCtrlAction2.setStatus('current')
cfcFeatureCtrlLastAction2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 5), CiscoFeatureAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlLastAction2.setStatus('current')
cfcFeatureCtrlLastActionResult2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 6), CiscoFeatureActionResult()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlLastActionResult2.setStatus('current')
cfcFeatureCtrlLastFailureReason2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 7), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlLastFailureReason2.setStatus('current')
cfcFeatureCtrlOpStatus2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 8), CiscoFeatureStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlOpStatus2.setStatus('current')
cfcFeatureCtrlOpStatusReason2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 9), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureCtrlOpStatusReason2.setStatus('current')
cfcFeatureCtrlTag2 = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 2, 1, 10), SnmpAdminString().subtype(subtypeSpec=ValueSizeConstraint(0, 32))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcFeatureCtrlTag2.setStatus('current')
cfcFeatureSetTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3), )
if mibBuilder.loadTexts: cfcFeatureSetTable.setStatus('current')
cfcFeatureSetEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1), ).setIndexNames((0, "CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetIndex"))
if mibBuilder.loadTexts: cfcFeatureSetEntry.setStatus('current')
cfcFeatureSetIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 1), CiscoOptionalFeatureSet())
if mibBuilder.loadTexts: cfcFeatureSetIndex.setStatus('current')
cfcFeatureSetName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 2), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureSetName.setStatus('current')
cfcFeatureSetAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 3), CiscoFeatureAction()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcFeatureSetAction.setStatus('current')
cfcFeatureSetLastAction = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 4), CiscoFeatureAction()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureSetLastAction.setStatus('current')
cfcFeatureSetLastActionResult = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 5), CiscoFeatureActionResult()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureSetLastActionResult.setStatus('current')
cfcFeatureSetLastFailureReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 6), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureSetLastFailureReason.setStatus('current')
cfcFeatureSetOpStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 7), CiscoFeatureStatus()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureSetOpStatus.setStatus('current')
cfcFeatureSetOpStatusReason = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 1, 3, 1, 8), SnmpAdminString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: cfcFeatureSetOpStatusReason.setStatus('current')
cfcFeatureSetNotifEnable = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 377, 1, 2, 1), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: cfcFeatureSetNotifEnable.setStatus('current')
ciscoFeatureOpStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 377, 0, 1)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatus"))
if mibBuilder.loadTexts: ciscoFeatureOpStatusChange.setStatus('deprecated')
ciscoFeatOpStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 377, 0, 2)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatus2"))
if mibBuilder.loadTexts: ciscoFeatOpStatusChange.setStatus('current')
ciscoFeatureSetOpStatusChange = NotificationType((1, 3, 6, 1, 4, 1, 9, 9, 377, 0, 3)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetOpStatus"))
if mibBuilder.loadTexts: ciscoFeatureSetOpStatusChange.setStatus('current')
ciscoFeatureCtrlMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 1))
ciscoFeatureCtrlMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2))
ciscoFeatureCtrlMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 1, 1)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureGroup"), ("CISCO-FEATURE-CONTROL-MIB", "cfcNotificationGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFeatureCtrlMIBCompliance = ciscoFeatureCtrlMIBCompliance.setStatus('deprecated')
ciscoFeatureCtrlMIBComplianceRev = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 1, 2)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureGroupRev"), ("CISCO-FEATURE-CONTROL-MIB", "cfcNotificationGroupRev"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFeatureCtrlMIBComplianceRev = ciscoFeatureCtrlMIBComplianceRev.setStatus('deprecated')
ciscoFeatureSetCtrlMIBComplianceRev1 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 1, 3)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetGroup"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetNotificationCtrlGroup"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetNotificationGroup"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureGroupRev"), ("CISCO-FEATURE-CONTROL-MIB", "cfcNotificationGroupRev"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoFeatureSetCtrlMIBComplianceRev1 = ciscoFeatureSetCtrlMIBComplianceRev1.setStatus('current')
cfcFeatureGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 1)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlName"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlAction"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastAction"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastActionResult"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastFailureReason"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatus"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatusReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFeatureGroup = cfcFeatureGroup.setStatus('deprecated')
cfcNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 2)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "ciscoFeatureOpStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcNotificationGroup = cfcNotificationGroup.setStatus('deprecated')
cfcFeatureGroupRev = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 3)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlName2"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlTag2"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlAction2"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastAction2"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastActionResult2"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlLastFailureReason2"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatus2"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureCtrlOpStatusReason2"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFeatureGroupRev = cfcFeatureGroupRev.setStatus('current')
cfcNotificationGroupRev = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 4)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "ciscoFeatOpStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcNotificationGroupRev = cfcNotificationGroupRev.setStatus('current')
cfcFeatureSetGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 5)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetName"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetAction"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetLastAction"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetLastActionResult"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetLastFailureReason"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetOpStatus"), ("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetOpStatusReason"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFeatureSetGroup = cfcFeatureSetGroup.setStatus('current')
cfcFeatureSetNotificationCtrlGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 6)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "cfcFeatureSetNotifEnable"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFeatureSetNotificationCtrlGroup = cfcFeatureSetNotificationCtrlGroup.setStatus('current')
cfcFeatureSetNotificationGroup = NotificationGroup((1, 3, 6, 1, 4, 1, 9, 9, 377, 2, 2, 7)).setObjects(("CISCO-FEATURE-CONTROL-MIB", "ciscoFeatureSetOpStatusChange"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    cfcFeatureSetNotificationGroup = cfcFeatureSetNotificationGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-FEATURE-CONTROL-MIB", cfcFeatureGroupRev=cfcFeatureGroupRev, CiscoOptionalFeature=CiscoOptionalFeature, CiscoOptionalFeatureSet=CiscoOptionalFeatureSet, cfcFeatureCtrlTable=cfcFeatureCtrlTable, ciscoFeatureOpStatusChange=ciscoFeatureOpStatusChange, cfcFeatureCtrlTag2=cfcFeatureCtrlTag2, cfcFeatureCtrlIndex=cfcFeatureCtrlIndex, cfcFeatureSetName=cfcFeatureSetName, ciscoFeatureCtrlMIBNotifs=ciscoFeatureCtrlMIBNotifs, PYSNMP_MODULE_ID=ciscoFeatureCtrlMIB, ciscoFeatOpStatusChange=ciscoFeatOpStatusChange, ciscoFeatureCtrlMIBCompliance=ciscoFeatureCtrlMIBCompliance, ciscoFeatureCtrlMIB=ciscoFeatureCtrlMIB, cfcNotifControl=cfcNotifControl, cfcFeatureCtrlAction=cfcFeatureCtrlAction, cfcFeatureCtrlEntry=cfcFeatureCtrlEntry, cfcFeatureSetLastActionResult=cfcFeatureSetLastActionResult, ciscoFeatureCtrlMIBGroups=ciscoFeatureCtrlMIBGroups, CiscoFeatureAction=CiscoFeatureAction, cfcFeatureSetNotificationCtrlGroup=cfcFeatureSetNotificationCtrlGroup, ciscoFeatureSetCtrlMIBComplianceRev1=ciscoFeatureSetCtrlMIBComplianceRev1, cfcFeatureCtrlInstanceNum2=cfcFeatureCtrlInstanceNum2, cfcFeatureCtrlLastActionResult2=cfcFeatureCtrlLastActionResult2, cfcFeatureCtrlLastActionResult=cfcFeatureCtrlLastActionResult, cfcFeatureCtrlOpStatus=cfcFeatureCtrlOpStatus, cfcFeatureSetOpStatusReason=cfcFeatureSetOpStatusReason, CiscoFeatureStatus=CiscoFeatureStatus, cfcFeatureSetLastFailureReason=cfcFeatureSetLastFailureReason, cfcFeatureSetNotificationGroup=cfcFeatureSetNotificationGroup, ciscoFeatureCtrlMIBConformance=ciscoFeatureCtrlMIBConformance, CiscoFeatureActionResult=CiscoFeatureActionResult, cfcFeatureCtrlAction2=cfcFeatureCtrlAction2, cfcFeatureGroup=cfcFeatureGroup, cfcFeatureCtrlOpStatusReason=cfcFeatureCtrlOpStatusReason, cfcFeatureCtrlOpStatus2=cfcFeatureCtrlOpStatus2, cfcFeatureCtrlLastFailureReason2=cfcFeatureCtrlLastFailureReason2, cfcFeatureCtrl2Table=cfcFeatureCtrl2Table, cfcFeatureCtrlName=cfcFeatureCtrlName, cfcFeatureSetOpStatus=cfcFeatureSetOpStatus, cfcFeatureSetLastAction=cfcFeatureSetLastAction, ciscoFeatureCtrlMIBComplianceRev=ciscoFeatureCtrlMIBComplianceRev, cfcFeature=cfcFeature, cfcNotificationGroupRev=cfcNotificationGroupRev, cfcFeatureCtrl2Entry=cfcFeatureCtrl2Entry, cfcFeatureCtrlOpStatusReason2=cfcFeatureCtrlOpStatusReason2, cfcFeatureCtrlName2=cfcFeatureCtrlName2, cfcFeatureSetEntry=cfcFeatureSetEntry, cfcFeatureSetTable=cfcFeatureSetTable, cfcFeatureCtrlLastAction2=cfcFeatureCtrlLastAction2, ciscoFeatureSetOpStatusChange=ciscoFeatureSetOpStatusChange, ciscoFeatureCtrlMIBCompliances=ciscoFeatureCtrlMIBCompliances, cfcFeatureSetAction=cfcFeatureSetAction, cfcFeatureSetNotifEnable=cfcFeatureSetNotifEnable, cfcFeatureSetGroup=cfcFeatureSetGroup, cfcFeatureSetIndex=cfcFeatureSetIndex, cfcNotificationGroup=cfcNotificationGroup, cfcFeatureCtrlLastAction=cfcFeatureCtrlLastAction, cfcFeatureCtrlLastFailureReason=cfcFeatureCtrlLastFailureReason, cfcFeatureCtrlIndex2=cfcFeatureCtrlIndex2, ciscoFeatureCtrlMIBObjects=ciscoFeatureCtrlMIBObjects)
