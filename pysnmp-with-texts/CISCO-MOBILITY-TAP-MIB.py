#
# PySNMP MIB module CISCO-MOBILITY-TAP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MOBILITY-TAP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:07:50 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ciscoMgmt, = mibBuilder.importSymbols("CISCO-SMI", "ciscoMgmt")
cTap2StreamIndex, cTap2MediationContentId = mibBuilder.importSymbols("CISCO-TAP2-MIB", "cTap2StreamIndex", "cTap2MediationContentId")
ModuleCompliance, ObjectGroup, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "ObjectGroup", "NotificationGroup")
Unsigned32, iso, TimeTicks, ModuleIdentity, Counter32, IpAddress, NotificationType, ObjectIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "iso", "TimeTicks", "ModuleIdentity", "Counter32", "IpAddress", "NotificationType", "ObjectIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "Gauge32")
TruthValue, TextualConvention, StorageType, DisplayString, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "TextualConvention", "StorageType", "DisplayString", "RowStatus")
ciscoMobilityTapMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 9, 672))
ciscoMobilityTapMIB.setRevisions(('2010-06-16 00:00', '2010-04-15 00:00', '2008-08-05 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMobilityTapMIB.setRevisionsDescriptions(('Added a new textual convention: CmtapLawfulInterceptID. Added following three objects to cmtapStreamTable. cmtapStreamLIIdentifier. cmtapStreamLocationInfo. cmtapStreamInterceptType. Added the following new MODULE-COMPLIANCE. ciscoMobilityTapMIBComplianceRev01. Added the following new OBJECT-GROUP. ciscoMobilityTapStreamGroupSup1.', "Added enumeration 'servedMdn' for mtapStreamCapabilities object and CmtapSubscriberIDType.", 'Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setLastUpdated('201006160000Z')
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setContactInfo('Cisco Systems Customer Service Postal:170 W. Tasman Drive San Jose, CA 95134 USA Tel:+1 800 553-NETS E-mail:cs-li@cisco.com')
if mibBuilder.loadTexts: ciscoMobilityTapMIB.setDescription("This module manages Cisco's intercept feature for Mobility Gateway Products. This MIB is used along with CISCO-TAP2-MIB MIB to intercept Mobility Gateway traffic. CISCO-TAP2-MIB MIB along with specific filter MIBs like this MIB replace the CISCO-TAP-MIB MIB. To create a Mobility intercept, an entry cmtapStreamEntry is created which contains the filter details. An entry cTap2StreamEntry of CISCO-TAP2-MIB is created which is the common stream information for all kinds of intercepts and type of the specific stream is set to 'mobility' in this entry.")
ciscoMobilityTapMIBNotifs = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 0))
ciscoMobilityTapMIBObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 1))
ciscoMobilityTapMIBConform = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2))
cmtapStreamGroup = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1))
class CmtapLawfulInterceptID(TextualConvention, OctetString):
    description = 'An octet string containing the Lawful Intercept Identifier (LIID)assigned to the intercepted target by a law enforcement agency defined by Communications Assistance for Law Enforcement Act (CALEA).'
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 256)

class CmtapSubscriberIDType(TextualConvention, Integer32):
    description = "A value that represents the type of address that is used to identify a subscriber. The following types are currently supported: unknown: The Subscriber's identifier type is not known. msid: A Mobile Subscriber Identity (MSID). imsi: An International Mobile Subscriber Identity(IMSI) number. nai: A Network Access Identifier (NAI). esn: An Electronic Serial Number (ESN). servedMdn: Served Mdn(mobile directory number) is a vendor specific attribute. It is similar to the class IETF attribute. Refer to RFC 2865 for vendor specific attribute format. Example:dsg-mdn."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("unknown", 1), ("msid", 2), ("imsi", 3), ("nai", 4), ("esn", 5), ("servedMdn", 6))

class CmtapSubscriberID(TextualConvention, OctetString):
    description = "An octet string containing a subscriber's identification, preferably in human-readable form. A CmtapStreamSubscriberID value is always interpreted within the context of an CmtapStreamSubscriberIDType value. Every usage of the CmtapStreamSubscriberID textual convention is required to specify the identity that corresponds to a CmtapStreamSubscriberIDType object."
    status = 'current'
    displayHint = '256a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 256)

cmtapStreamCapabilities = MibScalar((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 1), Bits().clone(namedValues=NamedValues(("tapEnable", 0), ("interface", 1), ("calledSubscriberID", 2), ("nonvolatileStorage", 3), ("msid", 4), ("imsi", 5), ("nai", 6), ("esn", 7), ("servedMdn", 8)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: cmtapStreamCapabilities.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamCapabilities.setDescription("This object indicates the Mobility Gateway intercept features that are implemented by this device and are manageable through this MIB. tapEnable: set if table entries with cTap2StreamInterceptEnable set to 'false' are used to pre-screen packets for intercept; otherwise these entries are ignored. interface: SNMP ifIndex Value may be used to select interception of all data crossing an interface or set of interfaces. nonvolatileStorage: The cmTapStreamTable supports the ability to store rows in nonvolatile memory. calledSubscriberID: The cmtapStreamCalledSubscriberID can be used to specify intercepts. Otherwise, this field is disabled. msid: A Mobile Subscriber Identity (MSID) can be used in the ID strings to specify intercepts. imsi: An International Mobile Subscriber Identity (IMSI) number can be used ID strings to specify intercepts. nai: A Network Access Identifier (NAI) can be used in the ID strings to specify intercepts. esn: An Electronic Serial Number (ESN) can be used in the ID strings to specify intercepts. servedMdn: Vendor specific attribute Served-Mobile Directory Number(MDN) can be used in the ID strings to specify intercepts.")
cmtapStreamTable = MibTable((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2), )
if mibBuilder.loadTexts: cmtapStreamTable.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamTable.setDescription('The Mobility Stream Table lists the data streams to be intercepted. The same data stream may be required by multiple taps. This essentially provides options for packet selection, only some of which might be used. For example, if all the traffic to or from a subscriber is to be intercepted, one would configure an entry listing SubscriberID along with the SubscriberIDType corresponding to the stream that one wishes to intercept. The first index indicates which Mediation Device the intercepted traffic will be diverted to. The second index, which indicates the specific intercept stream, permits multiple classifiers to be used together. For example, an IP stream and a Mobility stream could both be listed in their respective tables, yet still correspond to the same Mediation Device entry. Entries are added to this table via cmtapStreamStatus in accordance with the RowStatus convention.')
cmtapStreamEntry = MibTableRow((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1), ).setIndexNames((0, "CISCO-TAP2-MIB", "cTap2MediationContentId"), (0, "CISCO-TAP2-MIB", "cTap2StreamIndex"))
if mibBuilder.loadTexts: cmtapStreamEntry.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamEntry.setDescription('A stream entry indicates a single data stream to be intercepted to a Mediation Device. Many selected data streams may go to the same application interface and many application interfaces are supported.')
cmtapStreamCalledSubscriberIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 1), CmtapSubscriberIDType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberIDType.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberIDType.setDescription('Identifies the type of address that is stored in the cmtapStreamCalledSubscriberID string.')
cmtapStreamCalledSubscriberID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 2), CmtapSubscriberID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberID.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamCalledSubscriberID.setDescription('A string used to identify the party being contacted. The type of this identification is determined by the cmtapStreamCalledSubscriberIDType object.')
cmtapStreamSubscriberIDType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 3), CmtapSubscriberIDType().clone('unknown')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamSubscriberIDType.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamSubscriberIDType.setDescription('Identifies the type of address that is stored in the cmtapStreamSubscriberID string.')
cmtapStreamSubscriberID = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 4), CmtapSubscriberID()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamSubscriberID.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamSubscriberID.setDescription('A string used to identify the subscriber to tap. The type of this indentification is determined by the cmtapStreamSubscriberIDType object.')
cmtapStreamStorageType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 5), StorageType().clone('volatile')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamStorageType.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamStorageType.setDescription("This object specifies the storage type of this conceptual row. If it is set to 'nonVolatile', this entry can be saved into non-volatile memory.")
cmtapStreamStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 6), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamStatus.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamStatus.setDescription("The status of this conceptual row. This object manages creation, modification, and deletion of rows in this table. When any field must be changed, cmtapStreamStatus must be first set to 'notInService'.")
cmtapStreamLIIdentifier = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 7), CmtapLawfulInterceptID().clone('not set')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamLIIdentifier.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamLIIdentifier.setDescription('This object is an identifier assigned by a Law Enforcement Agency (LEA) to facilitate LI operations as defined in 3GPP TS 33.108 v8.7.0 standards document.')
cmtapStreamLocationInfo = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 8), TruthValue().clone('true')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamLocationInfo.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamLocationInfo.setDescription('This object indicates, if the userLocationInfo object should be included in the Intercept Related Information (IRI) messages sent by the gateway to mediation gateway(s) for interception taps. The userLocationInfo is defined as part of the IRI messages in 3GPP 33.108 v8.7.0 standards document.')
cmtapStreamInterceptType = MibTableColumn((1, 3, 6, 1, 4, 1, 9, 9, 672, 1, 1, 2, 1, 9), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("ccOnly", 1), ("iriOnly", 2), ("both", 3))).clone('both')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: cmtapStreamInterceptType.setStatus('current')
if mibBuilder.loadTexts: cmtapStreamInterceptType.setDescription('This object indicates the intercept type of the tapped stream. The tap can be provisioned to intercept control messages (IRI) from the tapped stream, the payload (CC) messages from the tapped stream or both. The format of these messages in defined in 3GPP TS 33.108 v8.7.0 standards document. ccOnly(1) - Content of communication interception only. iriOnly(2) - Intercept Related Information only. both(3) - Intercept both: CC and IRI.')
ciscoMobilityTapMIBCompliances = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1))
ciscoMobilityTapMIBGroups = MibIdentifier((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2))
ciscoMobilityTapMIBCompliance = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 1)).setObjects(("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapCapabilityGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroup"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapMIBCompliance = ciscoMobilityTapMIBCompliance.setStatus('deprecated')
if mibBuilder.loadTexts: ciscoMobilityTapMIBCompliance.setDescription('The compliance statement for entities which implement the Cisco Intercept MIB for Mobility Gateways')
ciscoMobilityTapMIBComplianceRev01 = ModuleCompliance((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 1, 2)).setObjects(("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapCapabilityGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroup"), ("CISCO-MOBILITY-TAP-MIB", "ciscoMobilityTapStreamGroupSup1"))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapMIBComplianceRev01 = ciscoMobilityTapMIBComplianceRev01.setStatus('current')
if mibBuilder.loadTexts: ciscoMobilityTapMIBComplianceRev01.setDescription('The compliance statement for entities which implement the Cisco Intercept MIB for Mobility Gateways.')
ciscoMobilityTapCapabilityGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 1)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCapabilities"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapCapabilityGroup = ciscoMobilityTapCapabilityGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoMobilityTapCapabilityGroup.setDescription('A collection of objects which provide Mobility Gateway capabilities for the system.')
ciscoMobilityTapStreamGroup = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 2)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberIDType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamCalledSubscriberID"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberIDType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamSubscriberID"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStorageType"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamStatus"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapStreamGroup = ciscoMobilityTapStreamGroup.setStatus('current')
if mibBuilder.loadTexts: ciscoMobilityTapStreamGroup.setDescription('A collection of objects which provide information about the stream from which we wish to intercept packets.')
ciscoMobilityTapStreamGroupSup1 = ObjectGroup((1, 3, 6, 1, 4, 1, 9, 9, 672, 2, 2, 3)).setObjects(("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLIIdentifier"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamLocationInfo"), ("CISCO-MOBILITY-TAP-MIB", "cmtapStreamInterceptType"))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMobilityTapStreamGroupSup1 = ciscoMobilityTapStreamGroupSup1.setStatus('current')
if mibBuilder.loadTexts: ciscoMobilityTapStreamGroupSup1.setDescription('A collection of objects which provide additional information about the stream from which we wish to intercept packets.')
mibBuilder.exportSymbols("CISCO-MOBILITY-TAP-MIB", cmtapStreamInterceptType=cmtapStreamInterceptType, ciscoMobilityTapMIBConform=ciscoMobilityTapMIBConform, CmtapLawfulInterceptID=CmtapLawfulInterceptID, cmtapStreamStorageType=cmtapStreamStorageType, cmtapStreamGroup=cmtapStreamGroup, cmtapStreamCalledSubscriberIDType=cmtapStreamCalledSubscriberIDType, ciscoMobilityTapMIBNotifs=ciscoMobilityTapMIBNotifs, cmtapStreamCalledSubscriberID=cmtapStreamCalledSubscriberID, CmtapSubscriberID=CmtapSubscriberID, ciscoMobilityTapMIBComplianceRev01=ciscoMobilityTapMIBComplianceRev01, cmtapStreamTable=cmtapStreamTable, cmtapStreamSubscriberID=cmtapStreamSubscriberID, cmtapStreamEntry=cmtapStreamEntry, PYSNMP_MODULE_ID=ciscoMobilityTapMIB, ciscoMobilityTapStreamGroupSup1=ciscoMobilityTapStreamGroupSup1, cmtapStreamLocationInfo=cmtapStreamLocationInfo, cmtapStreamLIIdentifier=cmtapStreamLIIdentifier, ciscoMobilityTapStreamGroup=ciscoMobilityTapStreamGroup, ciscoMobilityTapMIBGroups=ciscoMobilityTapMIBGroups, cmtapStreamSubscriberIDType=cmtapStreamSubscriberIDType, cmtapStreamStatus=cmtapStreamStatus, ciscoMobilityTapMIBCompliance=ciscoMobilityTapMIBCompliance, ciscoMobilityTapMIB=ciscoMobilityTapMIB, ciscoMobilityTapMIBCompliances=ciscoMobilityTapMIBCompliances, cmtapStreamCapabilities=cmtapStreamCapabilities, ciscoMobilityTapCapabilityGroup=ciscoMobilityTapCapabilityGroup, CmtapSubscriberIDType=CmtapSubscriberIDType, ciscoMobilityTapMIBObjects=ciscoMobilityTapMIBObjects)
