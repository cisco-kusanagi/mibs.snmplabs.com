#
# PySNMP MIB module CISCO-ADMISSION-POLICY-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ADMISSION-POLICY-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:32:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
InterfaceIndex, = mibBuilder.importSymbols("IF-MIB", "InterfaceIndex")
InetAddressType, InetAddress = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressType", "InetAddress")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
IpAddress, TimeTicks, Counter32, MibIdentifier, iso, Counter64, ObjectIdentity, Integer32, Gauge32, NotificationType, Unsigned32, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "TimeTicks", "Counter32", "MibIdentifier", "iso", "Counter64", "ObjectIdentity", "Integer32", "Gauge32", "NotificationType", "Unsigned32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Bits")
TextualConvention, MacAddress, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "MacAddress", "DisplayString")
ciscoAdmissionPolicyMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 653))
ciscoAdmissionPolicyMIB.setRevisions(('2008-06-11 00:00',))
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setLastUpdated('200806110000Z')
if mibBuilder.loadTexts: ciscoAdmissionPolicyMIB.setOrganization('Cisco Systems, Inc.')
class CapSessionId(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 64)

class CapQosPolicy(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapAclName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapURLString(TextualConvention, OctetString):
    reference = 'Uniform Resource Locators. RFC 1738.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class CapPolicyState(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("notApplicable", 1), ("success", 2), ("failure", 3), ("inProgress", 4), ("ipWait", 5))

ciscoAdmissionPolicyMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 0))
ciscoAdmissionPolicyMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 1))
ciscoAdmissionPolicyMIBConformance = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2))
capSessions = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1))
capTotalSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 1), Counter32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capTotalSessions.setStatus('current')
capActiveSessions = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 2), Gauge32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capActiveSessions.setStatus('current')
capSidSessionInfoTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3), )
if mibBuilder.loadTexts: capSidSessionInfoTable.setStatus('current')
capSidSessionInfoEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1), ).setIndexNames((1, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"))
if mibBuilder.loadTexts: capSidSessionInfoEntry.setStatus('current')
capSidSessionIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 1), CapSessionId())
if mibBuilder.loadTexts: capSidSessionIndex.setStatus('current')
capSidSessionIfIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 2), InterfaceIndex()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionIfIndex.setStatus('current')
capSidSessionMacAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 3), MacAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionMacAddress.setStatus('current')
capSidSessionAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 4), InetAddressType()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionAddressType.setStatus('current')
capSidSessionAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 5), InetAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionAddress.setStatus('current')
capSidSessionFeatureType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 3, 1, 6), Bits().clone(namedValues=NamedValues(("dot1x", 0), ("mab", 1), ("eou", 2), ("authProxy", 3)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSessionFeatureType.setStatus('current')
capSidSessionPolicyTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4), )
if mibBuilder.loadTexts: capSidSessionPolicyTable.setStatus('current')
capSidSessionPolicyEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1), ).setIndexNames((0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionIndex"), (0, "CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyIndex"))
if mibBuilder.loadTexts: capSidSessionPolicyEntry.setStatus('current')
capSidSessionPolicyIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 1), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("dot1x", 1), ("mab", 2), ("eou", 3), ("authProxy", 4))))
if mibBuilder.loadTexts: capSidSessionPolicyIndex.setStatus('current')
capSidIngressQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 2), CapQosPolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidIngressQosPolicy.setStatus('current')
capSidIngressQosPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 3), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidIngressQosPolicyState.setStatus('current')
capSidEgressQosPolicy = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 4), CapQosPolicy()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidEgressQosPolicy.setStatus('current')
capSidEgressQosPolicyState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 5), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidEgressQosPolicyState.setStatus('current')
capSidDownloadableAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 6), CapAclName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidDownloadableAclName.setStatus('current')
capSidDownloadableAclState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 7), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidDownloadableAclState.setStatus('current')
capSidUrlRedirectAclName = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 8), CapAclName()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidUrlRedirectAclName.setStatus('current')
capSidUrlRedirectAclState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 9), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidUrlRedirectAclState.setStatus('current')
capSidRedirectUrlString = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 10), CapURLString()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidRedirectUrlString.setStatus('current')
capSidRedirectUrlStringState = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 11), CapPolicyState()).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidRedirectUrlStringState.setStatus('current')
capSidSecurityGroupTag = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 653, 1, 1, 4, 1, 12), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(-1, -1), ValueRangeConstraint(0, 65535), ))).setMaxAccess("readonly")
if mibBuilder.loadTexts: capSidSecurityGroupTag.setStatus('current')
ciscoAdmissionPolicyMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1))
ciscoAdmissionPolicyMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2))
ciscoAdmissionPolicyMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 1, 1)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSessionStatisticsGroup"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionPolicyGroup"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionInfoGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoAdmissionPolicyMIBCompliance = ciscoAdmissionPolicyMIBCompliance.setStatus('current')
capSessionStatisticsGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 1)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capTotalSessions"), ("CISCO-ADMISSION-POLICY-MIB", "capActiveSessions"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSessionStatisticsGroup = capSessionStatisticsGroup.setStatus('current')
capSidSessionInfoGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 2)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddressType"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionAddress"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionIfIndex"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionMacAddress"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSessionFeatureType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSidSessionInfoGroup = capSidSessionInfoGroup.setStatus('current')
capSidSessionPolicyGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 653, 2, 2, 3)).setObjects(("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicy"), ("CISCO-ADMISSION-POLICY-MIB", "capSidIngressQosPolicyState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicy"), ("CISCO-ADMISSION-POLICY-MIB", "capSidEgressQosPolicyState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclName"), ("CISCO-ADMISSION-POLICY-MIB", "capSidDownloadableAclState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlString"), ("CISCO-ADMISSION-POLICY-MIB", "capSidRedirectUrlStringState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclName"), ("CISCO-ADMISSION-POLICY-MIB", "capSidUrlRedirectAclState"), ("CISCO-ADMISSION-POLICY-MIB", "capSidSecurityGroupTag"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    capSidSessionPolicyGroup = capSidSessionPolicyGroup.setStatus('current')
mibBuilder.exportSymbols("CISCO-ADMISSION-POLICY-MIB", ciscoAdmissionPolicyMIBGroups=ciscoAdmissionPolicyMIBGroups, ciscoAdmissionPolicyMIBObjects=ciscoAdmissionPolicyMIBObjects, capSidSessionFeatureType=capSidSessionFeatureType, capSidIngressQosPolicyState=capSidIngressQosPolicyState, capSidSessionIndex=capSidSessionIndex, capSidEgressQosPolicyState=capSidEgressQosPolicyState, capSidSecurityGroupTag=capSidSecurityGroupTag, capSidIngressQosPolicy=capSidIngressQosPolicy, ciscoAdmissionPolicyMIBNotifs=ciscoAdmissionPolicyMIBNotifs, capSidUrlRedirectAclName=capSidUrlRedirectAclName, capSidSessionInfoEntry=capSidSessionInfoEntry, CapURLString=CapURLString, PYSNMP_MODULE_ID=ciscoAdmissionPolicyMIB, capSidSessionIfIndex=capSidSessionIfIndex, ciscoAdmissionPolicyMIBCompliances=ciscoAdmissionPolicyMIBCompliances, capSidSessionInfoTable=capSidSessionInfoTable, capSidSessionPolicyEntry=capSidSessionPolicyEntry, CapSessionId=CapSessionId, capSidUrlRedirectAclState=capSidUrlRedirectAclState, capSessions=capSessions, ciscoAdmissionPolicyMIBConformance=ciscoAdmissionPolicyMIBConformance, capSidSessionPolicyIndex=capSidSessionPolicyIndex, capSidSessionInfoGroup=capSidSessionInfoGroup, capSidSessionAddress=capSidSessionAddress, capSessionStatisticsGroup=capSessionStatisticsGroup, capSidDownloadableAclState=capSidDownloadableAclState, ciscoAdmissionPolicyMIBCompliance=ciscoAdmissionPolicyMIBCompliance, capSidEgressQosPolicy=capSidEgressQosPolicy, capActiveSessions=capActiveSessions, CapPolicyState=CapPolicyState, capSidSessionAddressType=capSidSessionAddressType, capSidRedirectUrlStringState=capSidRedirectUrlStringState, capSidDownloadableAclName=capSidDownloadableAclName, ciscoAdmissionPolicyMIB=ciscoAdmissionPolicyMIB, capSidRedirectUrlString=capSidRedirectUrlString, CapQosPolicy=CapQosPolicy, capSidSessionPolicyGroup=capSidSessionPolicyGroup, capTotalSessions=capTotalSessions, capSidSessionPolicyTable=capSidSessionPolicyTable, capSidSessionMacAddress=capSidSessionMacAddress, CapAclName=CapAclName)
