#
# PySNMP MIB module ASCEND-MIBBGP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/ASCEND-MIBBGP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:26:42 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
configuration, = mibBuilder.importSymbols("ASCEND-MIB", "configuration")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Bits, Unsigned32, ObjectIdentity, MibIdentifier, TimeTicks, Counter32, Integer32, IpAddress, NotificationType, Counter64, iso, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Bits", "Unsigned32", "ObjectIdentity", "MibIdentifier", "TimeTicks", "Counter32", "Integer32", "IpAddress", "NotificationType", "Counter64", "iso", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class DisplayString(OctetString):
    pass

mibmibProfBgpGlobal = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 57))
mibmibProfBgpPolicy = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 60))
mibmibProfBgpSummary = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 59))
mibmibProfBgpPeer = MibIdentifier((1, 3, 6, 1, 4, 1, 529, 23, 58))
mibmibProfBgpGlobalTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 57, 1), )
if mibBuilder.loadTexts: mibmibProfBgpGlobalTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpGlobalTable.setDescription('A list of mibmibProfBgpGlobal profile entries.')
mibmibProfBgpGlobalEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1), ).setIndexNames((0, "ASCEND-MIBBGP-MIB", "mibProfBgpGlobal-Index-o"))
if mibBuilder.loadTexts: mibmibProfBgpGlobalEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpGlobalEntry.setDescription('A mibmibProfBgpGlobal entry containing objects that maps to the parameters of mibmibProfBgpGlobal profile.')
mibProfBgpGlobal_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 1), Integer32()).setLabel("mibProfBgpGlobal-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfBgpGlobal_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_Index_o.setDescription('')
mibProfBgpGlobal_Enable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfBgpGlobal-Enable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_Enable.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_Enable.setDescription('Enable/Disable BGP on the box')
mibProfBgpGlobal_AutonomousSystem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 3), Integer32()).setLabel("mibProfBgpGlobal-AutonomousSystem").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_AutonomousSystem.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_AutonomousSystem.setDescription('Local Autonomous System number.')
mibProfBgpGlobal_Id = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 4), IpAddress()).setLabel("mibProfBgpGlobal-Id").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_Id.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_Id.setDescription('Local BGP router id.')
mibProfBgpGlobal_ConnectRetryInterval = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 5), Integer32()).setLabel("mibProfBgpGlobal-ConnectRetryInterval").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_ConnectRetryInterval.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_ConnectRetryInterval.setDescription('The connection retry interval in seconds.')
mibProfBgpGlobal_KeepaliveTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 6), Integer32()).setLabel("mibProfBgpGlobal-KeepaliveTime").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_KeepaliveTime.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_KeepaliveTime.setDescription('The keep alive time interval in seconds.')
mibProfBgpGlobal_HoldTime = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 7), Integer32()).setLabel("mibProfBgpGlobal-HoldTime").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_HoldTime.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_HoldTime.setDescription('The hold time interval in seconds.')
mibProfBgpGlobal_SubAs = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 16), Integer32()).setLabel("mibProfBgpGlobal-SubAs").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_SubAs.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_SubAs.setDescription('If non-zero, AS number within a confederation.')
mibProfBgpGlobal_ClusterId = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 9), IpAddress()).setLabel("mibProfBgpGlobal-ClusterId").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_ClusterId.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_ClusterId.setDescription('Cluster Identifier.')
mibProfBgpGlobal_IgpLockstep = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 10), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfBgpGlobal-IgpLockstep").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_IgpLockstep.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_IgpLockstep.setDescription('Enable/Disable BGP igp-lockstep')
mibProfBgpGlobal_MaxMultiPaths = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 13), Integer32()).setLabel("mibProfBgpGlobal-MaxMultiPaths").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_MaxMultiPaths.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_MaxMultiPaths.setDescription('Maximum number of equal cost paths installed in the routing table')
mibProfBgpGlobal_StaticRouteRedistPolicy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 14), DisplayString()).setLabel("mibProfBgpGlobal-StaticRouteRedistPolicy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_StaticRouteRedistPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_StaticRouteRedistPolicy.setDescription('BGP-POLICY profile to be used for static route redistribution policy')
mibProfBgpGlobal_ConnRouteRedistPolicy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 15), DisplayString()).setLabel("mibProfBgpGlobal-ConnRouteRedistPolicy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_ConnRouteRedistPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_ConnRouteRedistPolicy.setDescription('BGP-POLICY profile to be used for connected routes redistribution policy')
mibProfBgpGlobal_LocalPrefDefault = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 17), Integer32()).setLabel("mibProfBgpGlobal-LocalPrefDefault").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_LocalPrefDefault.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_LocalPrefDefault.setDescription('Default Local Preference.')
mibProfBgpGlobal_AlwaysCompareMed = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 18), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfBgpGlobal-AlwaysCompareMed").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_AlwaysCompareMed.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_AlwaysCompareMed.setDescription("Enable/Disable BGP to compare MED from different AS's")
mibProfBgpGlobal_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 57, 1, 1, 11), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfBgpGlobal-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpGlobal_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpGlobal_Action_o.setDescription('')
mibmibProfBgpPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 60, 1), )
if mibBuilder.loadTexts: mibmibProfBgpPolicyTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpPolicyTable.setDescription('A list of mibmibProfBgpPolicy profile entries.')
mibmibProfBgpPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 60, 1, 1), ).setIndexNames((0, "ASCEND-MIBBGP-MIB", "mibProfBgpPolicy-Name"))
if mibBuilder.loadTexts: mibmibProfBgpPolicyEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpPolicyEntry.setDescription('A mibmibProfBgpPolicy entry containing objects that maps to the parameters of mibmibProfBgpPolicy profile.')
mibProfBgpPolicy_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 60, 1, 1, 1), DisplayString()).setLabel("mibProfBgpPolicy-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfBgpPolicy_Name.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPolicy_Name.setDescription('The name of the BGP Policy.')
mibProfBgpPolicy_NextPolicy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 60, 1, 1, 3), DisplayString()).setLabel("mibProfBgpPolicy-NextPolicy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPolicy_NextPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPolicy_NextPolicy.setDescription('The name of the next BGP policy to scan for rules')
mibProfBgpPolicy_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 60, 1, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfBgpPolicy-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPolicy_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPolicy_Action_o.setDescription('')
mibmibProfBgpPolicy_RuleTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 60, 2), ).setLabel("mibmibProfBgpPolicy-RuleTable")
if mibBuilder.loadTexts: mibmibProfBgpPolicy_RuleTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpPolicy_RuleTable.setDescription('A list of mibmibProfBgpPolicy__rule profile entries.')
mibmibProfBgpPolicy_RuleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 60, 2, 1), ).setLabel("mibmibProfBgpPolicy-RuleEntry").setIndexNames((0, "ASCEND-MIBBGP-MIB", "mibProfBgpPolicy-Rule-Name"), (0, "ASCEND-MIBBGP-MIB", "mibProfBgpPolicy-Rule-Index-o"))
if mibBuilder.loadTexts: mibmibProfBgpPolicy_RuleEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpPolicy_RuleEntry.setDescription('A mibmibProfBgpPolicy__rule entry containing objects that maps to the parameters of mibmibProfBgpPolicy__rule profile.')
mibProfBgpPolicy_Rule_Name = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 60, 2, 1, 1), DisplayString()).setLabel("mibProfBgpPolicy-Rule-Name").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfBgpPolicy_Rule_Name.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPolicy_Rule_Name.setDescription('')
mibProfBgpPolicy_Rule_Index_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 60, 2, 1, 2), Integer32()).setLabel("mibProfBgpPolicy-Rule-Index-o").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfBgpPolicy_Rule_Index_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPolicy_Rule_Index_o.setDescription('')
mibProfBgpPolicy_Rule = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 60, 2, 1, 3), DisplayString()).setLabel("mibProfBgpPolicy-Rule").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPolicy_Rule.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPolicy_Rule.setDescription('The rule of the BGP Policy.')
mibmibProfBgpSummaryTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 59, 1), )
if mibBuilder.loadTexts: mibmibProfBgpSummaryTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpSummaryTable.setDescription('A list of mibmibProfBgpSummary profile entries.')
mibmibProfBgpSummaryEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1), ).setIndexNames((0, "ASCEND-MIBBGP-MIB", "mibProfBgpSummary-Prefix-IpAddress"), (0, "ASCEND-MIBBGP-MIB", "mibProfBgpSummary-Prefix-Netmask"))
if mibBuilder.loadTexts: mibmibProfBgpSummaryEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpSummaryEntry.setDescription('A mibmibProfBgpSummary entry containing objects that maps to the parameters of mibmibProfBgpSummary profile.')
mibProfBgpSummary_Prefix_IpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 8), IpAddress()).setLabel("mibProfBgpSummary-Prefix-IpAddress").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfBgpSummary_Prefix_IpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpSummary_Prefix_IpAddress.setDescription('An IP address.')
mibProfBgpSummary_Prefix_Netmask = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 11), IpAddress()).setLabel("mibProfBgpSummary-Prefix-Netmask").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfBgpSummary_Prefix_Netmask.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpSummary_Prefix_Netmask.setDescription('The netmask')
mibProfBgpSummary_Enable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfBgpSummary-Enable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpSummary_Enable.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpSummary_Enable.setDescription('Enable/Disable Bgp-Summarization')
mibProfBgpSummary_SummarizationPolicy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 12), DisplayString()).setLabel("mibProfBgpSummary-SummarizationPolicy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpSummary_SummarizationPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpSummary_SummarizationPolicy.setDescription('BGP-POLICY profile to be used for summarization policy')
mibProfBgpSummary_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 59, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfBgpSummary-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpSummary_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpSummary_Action_o.setDescription('')
mibmibProfBgpPeerTable = MibTable((1, 3, 6, 1, 4, 1, 529, 23, 58, 1), )
if mibBuilder.loadTexts: mibmibProfBgpPeerTable.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpPeerTable.setDescription('A list of mibmibProfBgpPeer profile entries.')
mibmibProfBgpPeerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1), ).setIndexNames((0, "ASCEND-MIBBGP-MIB", "mibProfBgpPeer-PeerName"))
if mibBuilder.loadTexts: mibmibProfBgpPeerEntry.setStatus('mandatory')
if mibBuilder.loadTexts: mibmibProfBgpPeerEntry.setDescription('A mibmibProfBgpPeer entry containing objects that maps to the parameters of mibmibProfBgpPeer profile.')
mibProfBgpPeer_PeerName = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 14), DisplayString()).setLabel("mibProfBgpPeer-PeerName").setMaxAccess("readonly")
if mibBuilder.loadTexts: mibProfBgpPeer_PeerName.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_PeerName.setDescription('Name of bgp peer')
mibProfBgpPeer_Enable = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfBgpPeer-Enable").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_Enable.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_Enable.setDescription('Enable/Disable Bgp-peer')
mibProfBgpPeer_PeerIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 15), IpAddress()).setLabel("mibProfBgpPeer-PeerIpAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_PeerIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_PeerIpAddress.setDescription('The IP address of the BGP Peer.')
mibProfBgpPeer_MyIpAddress = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 16), IpAddress()).setLabel("mibProfBgpPeer-MyIpAddress").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_MyIpAddress.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_MyIpAddress.setDescription('The IP address of the Local BGP Peer.')
mibProfBgpPeer_AutonomousSystem = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 3), Integer32()).setLabel("mibProfBgpPeer-AutonomousSystem").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_AutonomousSystem.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_AutonomousSystem.setDescription('Autonomous System number of the BGP Peer.')
mibProfBgpPeer_AlwaysNextHop = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 6), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfBgpPeer-AlwaysNextHop").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_AlwaysNextHop.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_AlwaysNextHop.setDescription('Always use local IP address as the next hop in update packets.')
mibProfBgpPeer_RouteReflectorClient = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfBgpPeer-RouteReflectorClient").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_RouteReflectorClient.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_RouteReflectorClient.setDescription('Enable/Disable Bgp Peer as route refelector client')
mibProfBgpPeer_ConfederationMember = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("no", 1), ("yes", 2)))).setLabel("mibProfBgpPeer-ConfederationMember").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_ConfederationMember.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_ConfederationMember.setDescription('Is this peer a member of our confederation ?')
mibProfBgpPeer_DefaultGatewayMetric = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 17), Integer32()).setLabel("mibProfBgpPeer-DefaultGatewayMetric").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_DefaultGatewayMetric.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_DefaultGatewayMetric.setDescription('Metric to use when injecting this peer as gateway to default (0.0.0.0/0) route.')
mibProfBgpPeer_AcceptPolicy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 10), DisplayString()).setLabel("mibProfBgpPeer-AcceptPolicy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_AcceptPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_AcceptPolicy.setDescription('BGP-POLICY profile to be used for accept policy')
mibProfBgpPeer_InjectPolicy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 11), DisplayString()).setLabel("mibProfBgpPeer-InjectPolicy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_InjectPolicy.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_InjectPolicy.setDescription('BGP-POLICY profile to be used for inject policy')
mibProfBgpPeer_AdvertisePolicy = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 12), DisplayString()).setLabel("mibProfBgpPeer-AdvertisePolicy").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_AdvertisePolicy.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_AdvertisePolicy.setDescription('BGP-POLICY profile to be used for advertise policy')
mibProfBgpPeer_Action_o = MibScalar((1, 3, 6, 1, 4, 1, 529, 23, 58, 1, 1, 13), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("noAction", 1), ("createProfile", 2), ("deleteProfile", 3)))).setLabel("mibProfBgpPeer-Action-o").setMaxAccess("readwrite")
if mibBuilder.loadTexts: mibProfBgpPeer_Action_o.setStatus('mandatory')
if mibBuilder.loadTexts: mibProfBgpPeer_Action_o.setDescription('')
mibBuilder.exportSymbols("ASCEND-MIBBGP-MIB", mibProfBgpPolicy_Name=mibProfBgpPolicy_Name, mibProfBgpPeer_Enable=mibProfBgpPeer_Enable, mibmibProfBgpSummary=mibmibProfBgpSummary, mibProfBgpGlobal_SubAs=mibProfBgpGlobal_SubAs, mibProfBgpPolicy_Rule_Name=mibProfBgpPolicy_Rule_Name, mibmibProfBgpPeer=mibmibProfBgpPeer, mibmibProfBgpGlobalTable=mibmibProfBgpGlobalTable, mibProfBgpGlobal_IgpLockstep=mibProfBgpGlobal_IgpLockstep, mibProfBgpGlobal_Action_o=mibProfBgpGlobal_Action_o, mibmibProfBgpSummaryTable=mibmibProfBgpSummaryTable, mibProfBgpGlobal_StaticRouteRedistPolicy=mibProfBgpGlobal_StaticRouteRedistPolicy, mibProfBgpPeer_PeerIpAddress=mibProfBgpPeer_PeerIpAddress, mibmibProfBgpPolicyTable=mibmibProfBgpPolicyTable, mibmibProfBgpPolicy=mibmibProfBgpPolicy, mibProfBgpGlobal_AlwaysCompareMed=mibProfBgpGlobal_AlwaysCompareMed, mibProfBgpPolicy_NextPolicy=mibProfBgpPolicy_NextPolicy, mibProfBgpGlobal_Id=mibProfBgpGlobal_Id, mibProfBgpSummary_SummarizationPolicy=mibProfBgpSummary_SummarizationPolicy, mibmibProfBgpPeerTable=mibmibProfBgpPeerTable, mibmibProfBgpGlobalEntry=mibmibProfBgpGlobalEntry, mibProfBgpPeer_PeerName=mibProfBgpPeer_PeerName, mibProfBgpPeer_RouteReflectorClient=mibProfBgpPeer_RouteReflectorClient, mibProfBgpPeer_AutonomousSystem=mibProfBgpPeer_AutonomousSystem, mibProfBgpSummary_Enable=mibProfBgpSummary_Enable, mibProfBgpPeer_ConfederationMember=mibProfBgpPeer_ConfederationMember, mibProfBgpSummary_Action_o=mibProfBgpSummary_Action_o, mibmibProfBgpPolicyEntry=mibmibProfBgpPolicyEntry, mibProfBgpGlobal_KeepaliveTime=mibProfBgpGlobal_KeepaliveTime, mibProfBgpPeer_AlwaysNextHop=mibProfBgpPeer_AlwaysNextHop, mibProfBgpGlobal_Index_o=mibProfBgpGlobal_Index_o, mibProfBgpPeer_AdvertisePolicy=mibProfBgpPeer_AdvertisePolicy, mibProfBgpGlobal_HoldTime=mibProfBgpGlobal_HoldTime, mibProfBgpPeer_Action_o=mibProfBgpPeer_Action_o, mibmibProfBgpPeerEntry=mibmibProfBgpPeerEntry, DisplayString=DisplayString, mibmibProfBgpGlobal=mibmibProfBgpGlobal, mibProfBgpPolicy_Action_o=mibProfBgpPolicy_Action_o, mibProfBgpPeer_MyIpAddress=mibProfBgpPeer_MyIpAddress, mibProfBgpGlobal_Enable=mibProfBgpGlobal_Enable, mibProfBgpGlobal_ConnRouteRedistPolicy=mibProfBgpGlobal_ConnRouteRedistPolicy, mibmibProfBgpPolicy_RuleTable=mibmibProfBgpPolicy_RuleTable, mibProfBgpPolicy_Rule=mibProfBgpPolicy_Rule, mibProfBgpSummary_Prefix_IpAddress=mibProfBgpSummary_Prefix_IpAddress, mibProfBgpGlobal_MaxMultiPaths=mibProfBgpGlobal_MaxMultiPaths, mibProfBgpPeer_DefaultGatewayMetric=mibProfBgpPeer_DefaultGatewayMetric, mibProfBgpGlobal_AutonomousSystem=mibProfBgpGlobal_AutonomousSystem, mibProfBgpGlobal_LocalPrefDefault=mibProfBgpGlobal_LocalPrefDefault, mibProfBgpPeer_AcceptPolicy=mibProfBgpPeer_AcceptPolicy, mibProfBgpPolicy_Rule_Index_o=mibProfBgpPolicy_Rule_Index_o, mibProfBgpGlobal_ConnectRetryInterval=mibProfBgpGlobal_ConnectRetryInterval, mibProfBgpGlobal_ClusterId=mibProfBgpGlobal_ClusterId, mibmibProfBgpSummaryEntry=mibmibProfBgpSummaryEntry, mibProfBgpSummary_Prefix_Netmask=mibProfBgpSummary_Prefix_Netmask, mibmibProfBgpPolicy_RuleEntry=mibmibProfBgpPolicy_RuleEntry, mibProfBgpPeer_InjectPolicy=mibProfBgpPeer_InjectPolicy)
