#
# PySNMP MIB module CISCO-VOIP-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-VOIP-TAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:19:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2MediationContentId, cTap2StreamIndex = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2MediationContentId", "cTap2StreamIndex")
ObjectGroup, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ObjectGroup", "ModuleCompliance", "NotificationGroup")
Counter32, Bits, Unsigned32, Integer32, ModuleIdentity, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, IpAddress, Counter64, ObjectIdentity, iso, Gauge32, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Bits", "Unsigned32", "Integer32", "ModuleIdentity", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "IpAddress", "Counter64", "ObjectIdentity", "iso", "Gauge32", "NotificationType")
DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus")
ciscoVoIpTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 716))
ciscoVoIpTapMIB.setRevisions(('2009-10-01 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoVoIpTapMIB.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setLastUpdated('200910010000Z')
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setContactInfo(' Cisco Systems Customer Service Postal:170 W. Tasman Drive San Jose, CA 95134 USA Tel:+1 800 553-NETS E-mail:cs-li@cisco.com')
if mibBuilder.loadTexts: ciscoVoIpTapMIB.setDescription("This module manages Cisco's intercept feature for Voice over IP (VoIP). This MIB is used along with CISCO-TAP2-MIB to intercept VoIP Control and Data traffic.")
ciscoVoIpTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 0))
ciscoVoIpTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 1))
ciscoVoIpTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2))
cvoiptapStreamEncodePacket = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1))
class CvoipWarrantId(TextualConvention, OctetString):
    description = 'The warrant identifier used by the Mediation Device.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 30)

class CvoipSubscriberId(TextualConvention, OctetString):
    description = 'The subscriber identifier for identifying the endpoint.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 256)

cvoiptapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("usernameOrNumber", 1), ("uri", 2)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cvoiptapStreamCapabilities.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamCapabilities.setDescription("This object identifies what types of intercept streams can be configured on this type of device. This may be dependent on hardware capabilities, software capabilities. The following fields may be supported: tapEnable: set if table entries with cTap2StreamInterceptEnable set to 'false' are used to pre-screen packets for intercept otherwise these entries are ignored. usernameOrNumber: SNMP ifIndex value may be used to select interception of calls to or from a user or phone number may be used to select traffic to be intercepted. uri: Session Initiation Protocol (SIP) Uniform Resource Identifier (URI) may be used to select traffic to be intercepted.")
cvoiptapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2), )
if mibBuilder.loadTexts: cvoiptapStreamTable.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamTable.setDescription("The Intercept Stream VoIP Table lists the streams to be intercepted. To create a VoIP intercept, an entry cvoiptapStreamEntry is created which contains the filter details. An entry cTap2StreamEntry of CISCO-TAP2-MIB is created, which is the common stream information for all kinds of intercepts and type of the specific stream is set to IP in this entry. The same data stream may be required by multiple taps, and one might assume that often the intercepted stream is a small subset of the traffic that could be intercepted. This essentially provides options for call selection. For example, if all traffic to or from a given user is to be intercepted, one would configure an entry which lists the user with approprite tap type. The first index indicates which Mediation Device the intercepted traffic will be diverted to. The second index permits multiple classifiers to be used together, such as having an IP address as source or destination. The value of the second index is that of the stream's counter entry in the cTap2StreamTable. Entries are added to this table via citapStreamStatus in accordance with the RowStatus convention.")
cvoiptapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cvoiptapStreamEntry.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamEntry.setDescription('A stream entry indicates a single data stream to be intercepted to a Mediation Device. Many selected data streams may go to the same application interface, and many application interfaces are supported.')
cvoiptapStreamId = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 1), CvoipWarrantId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamId.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamId.setDescription('This object uniquely identifies this warrant. It has to be unique among all the rows.')
cvoiptapStreamType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 2), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))).clone(namedValues=NamedValues(("pen", 1), ("trace", 2), ("penAndTrace", 3), ("intercept", 4))).clone('intercept')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamType.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamType.setDescription('pen : Pen Register - provides trace of all outgoing calls. Only Call Data is sent. trace : Trace - provides trace of all incoming calls. Only Call Data is sent. penAndTrace : Provides trace of both incoming and outgoing calls. Only Call Data is sent. intercept : Provides both Call Data and Call Content to Commission on Accreditation for Law Enforcement Agencies (CALEA). Intercept is applicable to both originating and terminating calls.')
cvoiptapStreamMatch = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 3), CvoipSubscriberId()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamMatch.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamMatch.setDescription('This field describes the candidate which needs to be tapped.')
cvoiptapStreamMatchType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("usernameOrNumber", 1), ("uri", 2))).clone('usernameOrNumber')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamMatchType.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamMatchType.setDescription("This field specifies the type of information in cvoiptapStreamMatch. A subscriber or intercept candidate can be defined either as username, phone number or Session Initiation Protocol (SIP) Uniform Resource Identifier (URI). 'username' is defined as per RFC-3261. Same value is being used for either username or phone number.")
cvoiptapStreamCCMediationDevice = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 5), Integer32()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamCCMediationDevice.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamCCMediationDevice.setDescription('This object points to a row in Mediation Table which contains the IP address and port number for sending the Call Content intercept information.')
cvoiptapStreamRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 716, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cvoiptapStreamRowStatus.setStatus('current')
if mibBuilder.loadTexts: cvoiptapStreamRowStatus.setDescription("The status of this conceptual row. This object manages creation, modification, and deletion of rows in this table. When any rows must be changed, cvoiptapStreamRowStatus must be first set to 'notInService'. Row will be created when the service provider has to provision a tap for a VoIP endpoint. Row will be deleted when the warrant has expired. Row will be changed when the warrant type has been changed. cTap2StreamTable defined in CISCO-TAP2-MIB goes in conjunction with this row, using the same index.")
ciscoVoIpTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1))
ciscoVoIpTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2))
ciscoVoIpTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 1, 1)).setObjects(("CISCO-VOIP-TAP-MIB", "ciscoVoIpTapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoIpTapMIBCompliance = ciscoVoIpTapMIBCompliance.setStatus('current')
if mibBuilder.loadTexts: ciscoVoIpTapMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco Intercept MIB for VoIP.')
ciscoVoIpTapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 716, 2, 2, 1)).setObjects(("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCapabilities"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamId"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamType"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatch"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamMatchType"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamCCMediationDevice"), ("CISCO-VOIP-TAP-MIB", "cvoiptapStreamRowStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoVoIpTapStreamGroup = ciscoVoIpTapStreamGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoVoIpTapStreamGroup.setDescription('These objects are necessary for a description of VoIP Signaling and Data packets to select for interception.')
mibBuilder.exportSymbols("CISCO-VOIP-TAP-MIB", ciscoVoIpTapMIBGroups=ciscoVoIpTapMIBGroups, ciscoVoIpTapMIB=ciscoVoIpTapMIB, cvoiptapStreamTable=cvoiptapStreamTable, CvoipWarrantId=CvoipWarrantId, cvoiptapStreamCapabilities=cvoiptapStreamCapabilities, ciscoVoIpTapMIBObjects=ciscoVoIpTapMIBObjects, CvoipSubscriberId=CvoipSubscriberId, cvoiptapStreamType=cvoiptapStreamType, ciscoVoIpTapMIBCompliances=ciscoVoIpTapMIBCompliances, ciscoVoIpTapMIBCompliance=ciscoVoIpTapMIBCompliance, cvoiptapStreamId=cvoiptapStreamId, cvoiptapStreamMatch=cvoiptapStreamMatch, ciscoVoIpTapMIBNotifs=ciscoVoIpTapMIBNotifs, cvoiptapStreamRowStatus=cvoiptapStreamRowStatus, cvoiptapStreamMatchType=cvoiptapStreamMatchType, cvoiptapStreamEncodePacket=cvoiptapStreamEncodePacket, cvoiptapStreamCCMediationDevice=cvoiptapStreamCCMediationDevice, PYSNMP_MODULE_ID=ciscoVoIpTapMIB, ciscoVoIpTapStreamGroup=ciscoVoIpTapStreamGroup, cvoiptapStreamEntry=cvoiptapStreamEntry, ciscoVoIpTapMIBConform=ciscoVoIpTapMIBConform)
