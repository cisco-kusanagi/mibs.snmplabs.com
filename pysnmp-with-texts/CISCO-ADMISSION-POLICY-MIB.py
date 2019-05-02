#
# PySNMP MIB module CISCO-ADMISSION-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ADMISSION-POLICY-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:50:00 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddress, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddress", "InetAddressType")
ModuleCompliance, NotificationGroup, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup", "ObjectGroup")
iso, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, ModuleIdentity, Unsigned32, TimeTicks, Counter64, Integer32, IpAddress, Gauge32, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "ModuleIdentity", "Unsigned32", "TimeTicks", "Counter64", "Integer32", "IpAddress", "Gauge32", "Counter32", "ObjectIdentity")
MacAddress, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "MacAddress", "TextualConvention", "DisplayString")
ciscoAdmissionPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 653))
ciscoAdmissionPolicyMIB.setRevisions(('2008-06-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setLastUpdated('200806110000Z')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setDescription('This MIB module defines managed objects that facilitate the management of policies upon host(s) admission to a network. The information available through this MIB includes: o Statistics information such as number of total and active sessions. o Session information such as IP and MAC address of host, client type, and session state. o QoS and Security policy applied to host traffic upon host admission to a network. The following terms are used throughout this MIB: QoS (Quality of Service) is the method which attempts to ensure that the network requirements of different applications can be met by giving preferential forwarding treatment to some traffic. ACL (Access Control List) which contains filters used to identify traffic flows with certain characteristics. Downloadable ACL is a set of filters, configured on the RADIUS server which are downloaded during authorization phase of admission features like dot1x, authProxy, etc. SGT (Security Group Tag) is a unique 16 bits value assigned to every security group and used by network devices to enforce network policies. URL: Universal Resource Locator. URL-Redirect ACL is used for URL redirection feature. Any ingress HTTP from the host that matches the ACL content is subjected to redirection to the URL address specified by the URL-Redirect string. URL redirect string is the URL to which HTTP traffic to the host would be redirected.')
class CapSessionId(TextualConvention, OctetString):
    description = 'An octet string describes an unique session identification.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class CapQosPolicy(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form, describes a QoS policy.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapAclName(TextualConvention, OctetString):
    description = 'An octet string, preferably in human-readable form, describes the name of an ACL.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapURLString(TextualConvention, OctetString):
    reference = 'Uniform Resource Locators. RFC 1738.'
    description = "This textual convention defines the URL string. The Universal Resource Locator (URL). The URL strings are compact string representation for a resource available via internet. This is the address location of the page to load. The string should represent a fully qualifying string with the format 'protocol:/server/page'. In general the string should point to any value that can be saved/loaded. Any limitation for the URL must be defined as part of the description of any object which uses this syntax. The description of any object which uses this syntax must specifically describe the meaning of zero length value."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapPolicyState(TextualConvention, Integer32):
    description = "This textual convention indicates the current state of a policy applied to host traffic. 'notApplicable' indicates that the policy is not applicable. 'success' indicates that the policy is applied successfully. 'failure' indicates that the policy is failed to apply. 'inProgress' indicates that the policy application is in progress. 'ipWait' indicates that the policy is waiting for IP address assignment. "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notApplicable", 1), ("success", 2), ("failure", 3), ("inProgress", 4), ("ipWait", 5))

ciscoAdmissionPolicyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 0))
ciscoAdmissionPolicyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 1))
ciscoAdmissionPolicyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2))
capSessions = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1))
capTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTotalSessions.setStatus('current')
if mibBuilder.loadTexts: capTotalSessions.setDescription('This object indicates the total numbers of sessions created in the device since the last system reset.')
capActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capActiveSessions.setStatus('current')
if mibBuilder.loadTexts: capActiveSessions.setDescription('This object indicates the currently active sessions in the device.')
capSidSessionInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3), )
if mibBuilder.loadTexts: capSidSessionInfoTable.setStatus('current')
if mibBuilder.loadTexts: capSidSessionInfoTable.setDescription('This table lists admission policy sessions based on unique session identifier. An entry is created by the agent when an admission policy session has successfully registered to the system. An entry is deleted by the agent upon de-registration of the admission policy session with system.')
capSidSessionInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1), ).setIndexNames((1, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"))
if mibBuilder.loadTexts: capSidSessionInfoEntry.setStatus('current')
if mibBuilder.loadTexts: capSidSessionInfoEntry.setDescription('Each row contains the management information of a particular active session based on unique session identifier.')
capSidSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 1), CapSessionId())
if mibBuilder.loadTexts: capSidSessionIndex.setStatus('current')
if mibBuilder.loadTexts: capSidSessionIndex.setDescription('This object uniquely identifies a session.')
capSidSessionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionIfIndex.setStatus('current')
if mibBuilder.loadTexts: capSidSessionIfIndex.setDescription('This object indicates the ifIndex value of the interface on which the session is established.')
capSidSessionMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionMacAddress.setStatus('current')
if mibBuilder.loadTexts: capSidSessionMacAddress.setDescription('This object indicates the MAC address of the host.')
capSidSessionAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionAddressType.setStatus('current')
if mibBuilder.loadTexts: capSidSessionAddressType.setDescription('This object indicates the type of Internet address assigned for the host.')
capSidSessionAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionAddress.setStatus('current')
if mibBuilder.loadTexts: capSidSessionAddress.setDescription('This object indicates the Internet address assigned for the host. The type of this address is determined by the value of capSidSessionAddressType object.')
capSidSessionFeatureType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 6), Bits().clone(namedValues=NamedValues(("dot1x", 0), ("mab", 1), ("eou", 2), ("authProxy", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionFeatureType.setStatus('current')
if mibBuilder.loadTexts: capSidSessionFeatureType.setDescription("This object indicates the admission features associated with the session. 'dot1x' indicates that the admission feature is 802.1x feature. 'mab' indicates that the admission feature is Mac Authentication Bypass feature. 'eou' indicates that the admission feature is Extensible Authentication Protocol over UDP feature. 'authProxy' indicates that the admission feature is Authentication Proxy feature.")
capSidSessionPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4), )
if mibBuilder.loadTexts: capSidSessionPolicyTable.setStatus('current')
if mibBuilder.loadTexts: capSidSessionPolicyTable.setDescription('This table lists the policies that will be enforced per session per admission feature. The session in this table should have a corresponding entry in capSidSessionInfoTable.')
capSidSessionPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"), (0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyIndex"))
if mibBuilder.loadTexts: capSidSessionPolicyEntry.setStatus('current')
if mibBuilder.loadTexts: capSidSessionPolicyEntry.setDescription('Each row contains the management information of a particular admission feature of a session.')
capSidSessionPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dot1x", 1), ("mab", 2), ("eou", 3), ("authProxy", 4))))
if mibBuilder.loadTexts: capSidSessionPolicyIndex.setStatus('current')
if mibBuilder.loadTexts: capSidSessionPolicyIndex.setDescription("This object indicates the admission feature which a host is subjected to in a session. 'dot1x' indicates that the admission feature is 802.1x feature. 'mab' indicates that the admission feature is Mac Authentication Bypass feature. 'eou' indicates that the admission feature is Extensible Authentication Protocol over UDP feature. 'authProxy' indicates that the admission feature is Authentication Proxy feature.")
capSidIngressQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 2), CapQosPolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidIngressQosPolicy.setStatus('current')
if mibBuilder.loadTexts: capSidIngressQosPolicy.setDescription('This object indicates the name of an existing QoS policy which will be applied to incoming traffic in this session. An empty string indicates that no such policy is applied.')
capSidIngressQosPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 3), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidIngressQosPolicyState.setStatus('current')
if mibBuilder.loadTexts: capSidIngressQosPolicyState.setDescription('This object indicates the current state of the QoS policy which will be applied to incoming traffic in this session.')
capSidEgressQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 4), CapQosPolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidEgressQosPolicy.setStatus('current')
if mibBuilder.loadTexts: capSidEgressQosPolicy.setDescription('This object indicates the name of an existing QoS policy which will be applied to outgoing traffic in this session. An empty string indicates that no such policy is applied.')
capSidEgressQosPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 5), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidEgressQosPolicyState.setStatus('current')
if mibBuilder.loadTexts: capSidEgressQosPolicyState.setDescription('This object indicates the current state of the QoS policy which will be applied to outgoing traffic in this session.')
capSidDownloadableAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 6), CapAclName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidDownloadableAclName.setStatus('current')
if mibBuilder.loadTexts: capSidDownloadableAclName.setDescription('This object indicates the name of a Downloadable ACL which will be applied to the host traffic. An empty string indicates that no such ACL is applied.')
capSidDownloadableAclState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 7), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidDownloadableAclState.setStatus('current')
if mibBuilder.loadTexts: capSidDownloadableAclState.setDescription('This object indicates the state of this session downloadable ACL policy.')
capSidUrlRedirectAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 8), CapAclName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidUrlRedirectAclName.setStatus('current')
if mibBuilder.loadTexts: capSidUrlRedirectAclName.setDescription('This object indicates the ACL name that redirected traffic from the host will be subjected to. An empty string indicates that no such ACL is applied.')
capSidUrlRedirectAclState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 9), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidUrlRedirectAclState.setStatus('current')
if mibBuilder.loadTexts: capSidUrlRedirectAclState.setDescription('This object indicates the state of this session URL-Redirect ACL policy.')
capSidRedirectUrlString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 10), CapURLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidRedirectUrlString.setStatus('current')
if mibBuilder.loadTexts: capSidRedirectUrlString.setDescription('This object indicates the URL that traffic from the host will be redirected to. An empty string indicates that no such URL is applied.')
capSidRedirectUrlStringState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 11), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidRedirectUrlStringState.setStatus('current')
if mibBuilder.loadTexts: capSidRedirectUrlStringState.setDescription('This object indicates the state of this session URL-Redirect string policy.')
capSidSecurityGroupTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSecurityGroupTag.setStatus('current')
if mibBuilder.loadTexts: capSidSecurityGroupTag.setDescription('This object indicates the SGT value assigned to the host that initiated this session. Value of -1 indicates that there is no SGT value assigned.')
ciscoAdmissionPolicyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1))
ciscoAdmissionPolicyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2))
ciscoAdmissionPolicyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1, 1)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSessionStatisticsGroup"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyGroup"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAdmissionPolicyMIBCompliance = ciscoAdmissionPolicyMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIBCompliance.setDescription('The compliance statement for the CISCO-ADMISSION-POLICY-MIB')
capSessionStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 1)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capTotalSessions"), ("CISCO-ADMISSION-POLICY-MIB", "capActiveSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSessionStatisticsGroup = capSessionStatisticsGroup.setStatus('current')
if mibBuilder.loadTexts: capSessionStatisticsGroup.setDescription('A collection of object which provides session statistics information in the device.')
capSidSessionInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 2)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddressType"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddress"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionIfIndex"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionMacAddress"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionFeatureType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSidSessionInfoGroup = capSidSessionInfoGroup.setStatus('current')
if mibBuilder.loadTexts: capSidSessionInfoGroup.setDescription('A collection of objects which provides managed information of a session based on unique session identifier.')
capSidSessionPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 3)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicy"), ("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicyState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicy"), ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicyState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclName"), ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlString"), ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlStringState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclName"), ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSecurityGroupTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSidSessionPolicyGroup = capSidSessionPolicyGroup.setStatus('current')
if mibBuilder.loadTexts: capSidSessionPolicyGroup.setDescription('A collection of objects which provides policy information in a session based on unique session identifier.')
mibBuilder.exportSymbols("CISCO-ADMISSION-POLICY-MIB", CapSessionId=CapSessionId, capSidEgressQosPolicy=capSidEgressQosPolicy, ciscoAdmissionPolicyMIB=ciscoAdmissionPolicyMIB, ciscoAdmissionPolicyMIBCompliances=ciscoAdmissionPolicyMIBCompliances, CapAclName=CapAclName, capSidUrlRedirectAclName=capSidUrlRedirectAclName, capSidSessionPolicyIndex=capSidSessionPolicyIndex, capTotalSessions=capTotalSessions, capSidSessionPolicyEntry=capSidSessionPolicyEntry, PYSNMP_MODULE_ID=ciscoAdmissionPolicyMIB, capSidRedirectUrlString=capSidRedirectUrlString, ciscoAdmissionPolicyMIBConformance=ciscoAdmissionPolicyMIBConformance, ciscoAdmissionPolicyMIBNotifs=ciscoAdmissionPolicyMIBNotifs, capActiveSessions=capActiveSessions, capSidSessionInfoEntry=capSidSessionInfoEntry, capSidSessionAddressType=capSidSessionAddressType, capSidSessionPolicyGroup=capSidSessionPolicyGroup, capSessions=capSessions, capSidSessionInfoTable=capSidSessionInfoTable, capSidEgressQosPolicyState=capSidEgressQosPolicyState, capSidSessionFeatureType=capSidSessionFeatureType, capSidUrlRedirectAclState=capSidUrlRedirectAclState, CapURLString=CapURLString, capSidSessionInfoGroup=capSidSessionInfoGroup, capSidIngressQosPolicyState=capSidIngressQosPolicyState, capSidIngressQosPolicy=capSidIngressQosPolicy, CapQosPolicy=CapQosPolicy, capSidSessionMacAddress=capSidSessionMacAddress, capSidSessionIfIndex=capSidSessionIfIndex, ciscoAdmissionPolicyMIBObjects=ciscoAdmissionPolicyMIBObjects, capSidSessionPolicyTable=capSidSessionPolicyTable, ciscoAdmissionPolicyMIBCompliance=ciscoAdmissionPolicyMIBCompliance, capSidSessionAddress=capSidSessionAddress, capSidSessionIndex=capSidSessionIndex, capSidDownloadableAclState=capSidDownloadableAclState, capSidDownloadableAclName=capSidDownloadableAclName, CapPolicyState=CapPolicyState, capSessionStatisticsGroup=capSessionStatisticsGroup, capSidRedirectUrlStringState=capSidRedirectUrlStringState, capSidSecurityGroupTag=capSidSecurityGroupTag, ciscoAdmissionPolicyMIBGroups=ciscoAdmissionPolicyMIBGroups)
