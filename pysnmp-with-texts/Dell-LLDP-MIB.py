#
# PySNMP MIB module Dell-LLDP-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/Dell-LLDP-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:56:10 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ValueSizeConstraint")
Dscp, = mibBuilder.importSymbols("DIFFSERV-DSCP-TC", "Dscp")
rndErrorSeverity, rndErrorDesc = mibBuilder.importSymbols("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity", "rndErrorDesc")
rnd, rndNotifications = mibBuilder.importSymbols("Dell-MIB", "rnd", "rndNotifications")
AddressFamilyNumbers, = mibBuilder.importSymbols("IANA-ADDRESS-FAMILY-NUMBERS-MIB", "AddressFamilyNumbers")
LldpXMedCapabilities, = mibBuilder.importSymbols("LLDP-EXT-MED-MIB", "LldpXMedCapabilities")
lldpRemTimeMark, LldpManAddress, LldpPortNumber, lldpRemLocalPortNum, LldpPortList, lldpRemIndex = mibBuilder.importSymbols("LLDP-MIB", "lldpRemTimeMark", "LldpManAddress", "LldpPortNumber", "lldpRemLocalPortNum", "LldpPortList", "lldpRemIndex")
PortList, = mibBuilder.importSymbols("Q-BRIDGE-MIB", "PortList")
NotificationGroup, ObjectGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ObjectGroup", "ModuleCompliance")
IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, NotificationType, iso, MibIdentifier, Bits, TimeTicks, Gauge32, ModuleIdentity, Counter32, ObjectIdentity, Counter64, Unsigned32 = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "NotificationType", "iso", "MibIdentifier", "Bits", "TimeTicks", "Gauge32", "ModuleIdentity", "Counter32", "ObjectIdentity", "Counter64", "Unsigned32")
TruthValue, RowStatus, TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "RowStatus", "TextualConvention", "DisplayString")
rlLldp = ModuleIdentity((1, 3, 6, 1, 4, 1, 89, 110))
rlLldp.setRevisions(('2005-06-20 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rlLldp.setRevisionsDescriptions(('Initial revision.',))
if mibBuilder.loadTexts: rlLldp.setLastUpdated('200506200000Z')
if mibBuilder.loadTexts: rlLldp.setOrganization('Dell')
if mibBuilder.loadTexts: rlLldp.setContactInfo('www.dell.com')
if mibBuilder.loadTexts: rlLldp.setDescription('This private MIB module adds MIBs to LLDP (Link Layer Discovery Protocol).')
rlLldpObjects = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 110, 1))
rlLldpConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 110, 1, 1))
rlLldpXMedConfig = MibIdentifier((1, 3, 6, 1, 4, 1, 89, 110, 1, 2))
class PolicyNumber(TextualConvention, Integer32):
    description = 'Policy Number in the Media Policy Container. Policy numbers should be in the range of 1 and 32768 since 8 policies can be configured for each particular port and the number of ports range is 1 to 4096.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 32768)

class PolicyContainerAppType(TextualConvention, Integer32):
    description = 'The media type that defines the primary function of the application for the policy advertised by an endpoint. A value of voice(1) indicates that the media type defining a primary function of the application for the policy advertised on the local port is voice. A value of voiceSignaling(3) indicates that the media type defining a primary function of the application for the policy advertised on the local port is voice signaling. A value of guestVoice(4) indicates that the media type Defining a primary function of the application for the policy advertised on the local port is guest voice. A value of guestVoiceSignaling(5) indicates that the media type defining a primary function of the application for the policy advertised on the local port is guest voice signaling. A value of softPhoneVoice(6) indicates that the media type Defining a primary function of the application for the policy advertised on the local port is softphone voice. A value of videoConferencing(7) indicates that the media type defining a primary function of the application for the policy advertised on the local port is voice. A value of streamingVideo(8) indicates that the media type defining a primary function of the application for the policy advertised on the local port is streaming video. A value of videoSignaling(2) indicates that the media type defining a primary function of the application for the policy advertised on the local port is video signaling.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("unknown", 0), ("voice", 1), ("voiceSignaling", 2), ("guestVoice", 3), ("guestVoiceSignaling", 4), ("softPhoneVoice", 5), ("videoconferencing", 6), ("streamingVideo", 7), ("videoSignaling", 8))

class PolicyAppVoiceUpdateMode(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("manual", 0), ("auto", 1))

rlLldpEnabled = MibScalar((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 1), TruthValue()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpEnabled.setStatus('current')
if mibBuilder.loadTexts: rlLldpEnabled.setDescription("Setting this variable to 'true' will globally enable the LLDP feature (both transmit and receive functionalities). Setting this variable to 'false' will globally disable the LLDP feature. Thus, the administratively desired status of a local port is determined by both this variable and the MIB lldpPortConfigAdminStatus.")
rlLldpClearRx = MibScalar((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 2), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpClearRx.setReference('')
if mibBuilder.loadTexts: rlLldpClearRx.setStatus('current')
if mibBuilder.loadTexts: rlLldpClearRx.setDescription('A set of ports that are identified by a PortList, in which each port is represented as a bit. Clears the Rx information about the remote agents accordingly to the specified PortList. The default value for rlLldpClearRx object is an empty binary string, which means no ports are specified to be cleared from the Rx Info. This object behaviors as an event (write-only) than reading this object always results in an Empty Port List of length zero.')
rlLldpDuMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2))).clone(namedValues=NamedValues(("filtering", 1), ("flooding", 2))).clone('filtering')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpDuMode.setReference('Dell LLDP System Specifications')
if mibBuilder.loadTexts: rlLldpDuMode.setStatus('current')
if mibBuilder.loadTexts: rlLldpDuMode.setDescription("Action with LLDPDU upon globally disabled LLDP. If the associated rlLldpDuMode object has a value of 'filtering(1)', then received frames are containing LLDPDU will be dropped. If the associated rlLldpDuMode object has a value of 'flooding(2)', then received frames are containing LLDPDU will flood all active ports.")
rlLldpAutoAdvLocPortManAddrTable = MibTable((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 4), )
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortManAddrTable.setReference('Dell LLDP')
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortManAddrTable.setStatus('current')
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortManAddrTable.setDescription('This table contains automaticaly selected management address, advertised on the local port.')
rlLldpAutoAdvLocPortManAddrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 4, 1), ).setIndexNames((0, "Dell-LLDP-MIB", "rlLldpAutoAdvLocPortNum"))
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortManAddrEntry.setStatus('current')
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortManAddrEntry.setDescription("Information about a local port, which advertises the Management address automatically. Entry also included an interface number, on which the Management address is assigned. Each management address should have distinct 'management address type' (rlLldpAutoAdvManAddrSubtype) and 'management address' (rlLldpAutoAdvManAddr).")
rlLldpAutoAdvLocPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 4, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortNum.setStatus('current')
if mibBuilder.loadTexts: rlLldpAutoAdvLocPortNum.setDescription('The index value used to identify the port component (contained in the local chassis with the LLDP agent) associated with this entry. The value of this object is used as a port index to the rlLldpAutoAdvLocPortManAddrTable.')
rlLldpAutoAdvManAddrOwnerIfId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 4, 1, 2), Integer32()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpAutoAdvManAddrOwnerIfId.setStatus('current')
if mibBuilder.loadTexts: rlLldpAutoAdvManAddrOwnerIfId.setDescription("The integer value is used to identify the interface number (port, trunk or vlan). The management address, automatically advertised from associated 'rlLldpAutoAdvLocPortNum'local port is assigned to mentioned 'rlLldpAutoAdvManAddrOwnerIfId' interface. In case of 0 the management address is automatically calculated without care to the ifIndex it was defined on.")
rlLldpAutoAdvManAddrNone = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 4, 1, 3), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpAutoAdvManAddrNone.setStatus('current')
if mibBuilder.loadTexts: rlLldpAutoAdvManAddrNone.setDescription("A value of 'true' indicates that the any management address hasn't advertised by the local port. Moreover, the configuration of automatic management address advertisment is disabled. A value of 'false' indicates that the configuration of automatic management address advertisment is enabled.")
rlLldpAutoAdvManAddrSubtype = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 4, 1, 4), AddressFamilyNumbers()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpAutoAdvManAddrSubtype.setStatus('current')
if mibBuilder.loadTexts: rlLldpAutoAdvManAddrSubtype.setDescription("The type of management address identifier encoding used in the associated 'rlLldpAutoAdvManAddr' object.")
rlLldpAutoAdvManAddr = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 4, 1, 5), LldpManAddress()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpAutoAdvManAddr.setStatus('current')
if mibBuilder.loadTexts: rlLldpAutoAdvManAddr.setDescription("The string value used to identify the management address is automaticaly advertised by local port, and assigned on the associated 'rlLldpAutoAdvManAddrOwnerIfId' interface.")
rlLldpAutoAdvPortsStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 4, 1, 6), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpAutoAdvPortsStatus.setStatus('current')
if mibBuilder.loadTexts: rlLldpAutoAdvPortsStatus.setDescription('The row status variable, used according to row installation and removal conventions.')
rlLldpXMedLocMediaPolicyContainerTable = MibTable((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1), )
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerTable.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerTable.setDescription('This table contains one row per policy number of media policy container configuration.')
rlLldpXMedLocMediaPolicyContainerEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1), ).setIndexNames((0, "Dell-LLDP-MIB", "rlLldpXMedLocMediaPolicyContainerIndex"))
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerEntry.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerEntry.setDescription('Configuration of a particular policy in the media policy container.')
rlLldpXMedLocMediaPolicyContainerIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1, 1), PolicyNumber())
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerIndex.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerIndex.setDescription('The index value used to identify the Media Policy associated with this entry. The value of this object is used as a policy number index to the rlLldpXMedLocMediaPolicyContainerTable.')
rlLldpXMedLocMediaPolicyContainerAppType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1, 2), PolicyContainerAppType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerAppType.setReference('ANSI/TIA-1057, Section 10.2.3.1')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerAppType.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerAppType.setDescription('The media type that defines the primary function of the application for the policy advertised by an endpoint.')
rlLldpXMedLocMediaPolicyContainerVlanID = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4094), ValueRangeConstraint(4095, 4095), ))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerVlanID.setReference(' ANSI/TIA-1057, Section 10.2.3.5')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerVlanID.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerVlanID.setDescription('An extension of the VLAN Identifier for the port, as defined in IEEE 802.1P-1998. A value of 1 through 4094 is used to define a valid PVID. A value of 0 shall be used if the device is using priority tagged frames, meaning that only the 802.1p priority level is significant and the default VID of the ingress port is being used instead. A value of 4095 is reserved for implementation use.')
rlLldpXMedLocMediaPolicyContainerPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1, 4), Integer32().subtype(subtypeSpec=ValueRangeConstraint(0, 7))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerPriority.setReference(' ANSI/TIA-1057, Section 10.2.3.6 ')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerPriority.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerPriority.setDescription('This object contains the value of the 802.1p priority which is associated with the given port on the local system.')
rlLldpXMedLocMediaPolicyContainerDscp = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1, 5), Dscp()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerDscp.setReference(' ANSI/TIA-1057, Section 10.2.3.7')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerDscp.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerDscp.setDescription('This object contains the value of the Differentiated Service Code Point (DSCP) as defined in IETF RFC 2474 and RFC 2475 which is associated with the given port on the local system.')
rlLldpXMedLocMediaPolicyContainerUnknown = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1, 6), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerUnknown.setReference(' ANSI/TIA-1057, Section 10.2.3.2')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerUnknown.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerUnknown.setDescription("A value of 'true' indicates that the network policy for the specified application type is currently unknown. In this case, the VLAN ID, the layer 2 priority and the DSCP value fields are ignored. A value of 'false' indicates that this network policy is defined ")
rlLldpXMedLocMediaPolicyContainerTagged = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1, 7), TruthValue().clone('false')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerTagged.setReference(' ANSI/TIA-1057, Section 10.2.3.3')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerTagged.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerTagged.setDescription("A value of 'true' indicates that the application is using a tagged VLAN. A value of 'false' indicates that for the specific application the device either is using an untagged VLAN or does not support port based VLAN operation. In this case, both the VLAN ID and the Layer 2 priority fields are ignored and only the DSCP value has relevance ")
rlLldpXMedLocMediaPolicyContainerPorts = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1, 8), PortList().clone(hexValue="")).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerPorts.setReference('IEEE 802.1AB-2004 10.2.1.1')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerPorts.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerPorts.setDescription('A set of ports that are identified by a PortList, in which each port is represented as a bit. The local Media Policy Number will be associated with (or attached to) the ports specified at the rlLldpXMedLocMediaPolicyContainerPorts. The default value for rlLldpXMedLocMediaPolicyContainerPorts object is empty binary string, which means no ports are specified for advertising indicated management address instance.')
rlLldpXMedLocMediaPolicyContainerRowStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 2, 1, 1, 9), RowStatus()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerRowStatus.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedLocMediaPolicyContainerRowStatus.setDescription('The row status variable, used according to row installation and removal conventions.')
rlLldpTLVsTxOverloadingTable = MibTable((1, 3, 6, 1, 4, 1, 89, 110, 1, 3), )
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingTable.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingTable.setDescription('A table that show the which of the LLDP TLVs are not transmitted on individual ports due to insufficient room in the frame and the size of each TLV.')
rlLldpTLVsTxOverloadingEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 110, 1, 3, 1), ).setIndexNames((0, "Dell-LLDP-MIB", "rlLldpTxOverloadingPortNum"), (0, "Dell-LLDP-MIB", "rlLldpTxOverloadingIndex"))
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingEntry.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingEntry.setDescription('LLDP TX overloading information that shows the transmission of TLVs on LLDP transmission capable ports.')
rlLldpTxOverloadingPortNum = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 3, 1, 1), LldpPortNumber())
if mibBuilder.loadTexts: rlLldpTxOverloadingPortNum.setStatus('current')
if mibBuilder.loadTexts: rlLldpTxOverloadingPortNum.setDescription(' The value of this object is used as a port index to the TLVs TX overloading Table .')
rlLldpTxOverloadingIndex = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 3, 1, 2), Unsigned32())
if mibBuilder.loadTexts: rlLldpTxOverloadingIndex.setStatus('current')
if mibBuilder.loadTexts: rlLldpTxOverloadingIndex.setDescription('The sequence number of the group into sent LLDP PPDU starting from 1.')
rlLldpTxOverloadingGroupId = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))).clone(namedValues=NamedValues(("mandatory", 1), ("optional", 2), ("medCap", 3), ("medLocation", 4), ("medNetPolicy", 5), ("medPoe", 6), ("medInventory", 7), ("xDot3", 8), ("xDot1", 9), ("dcbx", 10)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTxOverloadingGroupId.setStatus('current')
if mibBuilder.loadTexts: rlLldpTxOverloadingGroupId.setDescription('Defines the TLVs groups. A value of mandatory(1) defines LLDP mandatory TLVs group A value of optinal(2) defines LLDP optional TLVs group A value of medCap(3) defines LLDP MED - Capabilities group A value of medLocation(4) defines LLDP MED - Location group A value of medNetPolicy(5) defines LLDP MED - Network Policy group A value of medPoe(6) defines LLDP MED - Extended Power via MDI group A value of medInventory(7) defines LLDP MED - Inventory group A value of Xdot3(8) defines 802.3 TLVs group A value of Xdot1(9) defines 802.1 TLVs group ')
rlLldpTLVsTxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 3, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxSize.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxSize.setDescription(' The size of the TLV in Bytes.')
rlLldpTLVsTxGroupOverloading = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 3, 1, 5), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxGroupOverloading.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxGroupOverloading.setDescription('Boolean Flag, When TRUE indicating that LLDP TLVs were overloaded and the value of left size is negative')
rlLldpTLVsTxLeftSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 3, 1, 6), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxLeftSize.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxLeftSize.setDescription(' The size in Bytes of the available space left in the LLDPDU after adding the TLVs group. In case the Overloading Flag is TRUE, there not enough space in the LLDPDU for the TLVs group and this is the size of the additional scpace that required for the TLVs group')
rlLldpTLVsTxOverloadingSizeTable = MibTable((1, 3, 6, 1, 4, 1, 89, 110, 1, 4), )
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingSizeTable.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingSizeTable.setDescription('A table that show the total size of the all TLVs and the LLDPDU free size .')
rlLldpTLVsTxOverloadingSizeEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 110, 1, 4, 1), ).setIndexNames((0, "Dell-LLDP-MIB", "rlLldpTxOverloadingPortNum"))
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingSizeEntry.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingSizeEntry.setDescription('LLDP TX overloading information')
rlLldpTotalTLVsTxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 4, 1, 2), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTotalTLVsTxSize.setStatus('current')
if mibBuilder.loadTexts: rlLldpTotalTLVsTxSize.setDescription(' The Total size of all TLVs group in Bytes.')
rlLldpTLVsTxOverloading = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 4, 1, 3), TruthValue()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxOverloading.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxOverloading.setDescription('Boolean Flag, When TRUE indicating that LLDP TLVs group were overloaded and the value of left size is negative')
rlLldpLeftTLVsTxSize = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 4, 1, 4), Unsigned32()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpLeftTLVsTxSize.setStatus('current')
if mibBuilder.loadTexts: rlLldpLeftTLVsTxSize.setDescription(' The size in Bytes of the available space left in the LLDPDU after adding all TLVs group. In case the Overloading Flag is TRUE, there not enough space in the LLDPDU for all the TLVs group and this is the size of the additional scpace that required for all the TLVs group')
rlLldpTLVsTxOverloadingPorts = MibScalar((1, 3, 6, 1, 4, 1, 89, 110, 1, 5), PortList()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingPorts.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingPorts.setDescription('Port list that represent the overloading state of each port')
rlLldpTLVsTxOverloadingStateEnterTrap = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 209)).setObjects(("Dell-DEVICEPARAMS-MIB", "rndErrorDesc"), ("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingStateEnterTrap.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingStateEnterTrap.setDescription('Informational trap indicating that the port has entered the overloading state.')
rlLldpTLVsTxOverloadingStateExitTrap = NotificationType((1, 3, 6, 1, 4, 1, 89, 0, 210)).setObjects(("Dell-DEVICEPARAMS-MIB", "rndErrorDesc"), ("Dell-DEVICEPARAMS-MIB", "rndErrorSeverity"))
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingStateExitTrap.setStatus('current')
if mibBuilder.loadTexts: rlLldpTLVsTxOverloadingStateExitTrap.setDescription('Informational trap indicating that the port is no longer in the overloading state..')
rlLldpXMedNetPolVoiceUpdateMode = MibScalar((1, 3, 6, 1, 4, 1, 89, 110, 1, 7), PolicyAppVoiceUpdateMode()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpXMedNetPolVoiceUpdateMode.setStatus('current')
if mibBuilder.loadTexts: rlLldpXMedNetPolVoiceUpdateMode.setDescription('')
rlLldpRemTtlTable = MibTable((1, 3, 6, 1, 4, 1, 89, 110, 1, 8), )
if mibBuilder.loadTexts: rlLldpRemTtlTable.setStatus('current')
if mibBuilder.loadTexts: rlLldpRemTtlTable.setDescription('This table contains the remote device Time To Live LLDP TLV.')
rlLldpRemTtlEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 110, 1, 8, 1), ).setIndexNames((0, "LLDP-MIB", "lldpRemTimeMark"), (0, "LLDP-MIB", "lldpRemLocalPortNum"), (0, "LLDP-MIB", "lldpRemIndex"))
if mibBuilder.loadTexts: rlLldpRemTtlEntry.setStatus('current')
if mibBuilder.loadTexts: rlLldpRemTtlEntry.setDescription('LLDP Time To TTL remove TLV. This uses the key as defind in lldpRemTable of the LLDP-MIB.')
rlLldpRemTtl = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 110, 1, 8, 1, 1), Unsigned32()).setUnits('seconds').setMaxAccess("readonly")
if mibBuilder.loadTexts: rlLldpRemTtl.setStatus('current')
if mibBuilder.loadTexts: rlLldpRemTtl.setDescription('This object contains the remote device Time To Live LLDP TLV.')
rlLldpChassisIdSubtype = MibScalar((1, 3, 6, 1, 4, 1, 89, 110, 1, 1, 5), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(4, 7))).clone(namedValues=NamedValues(("macAddress", 4), ("local", 7))).clone('macAddress')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: rlLldpChassisIdSubtype.setReference('IEEE 802.1AB-2004 9.5.2.2')
if mibBuilder.loadTexts: rlLldpChassisIdSubtype.setStatus('current')
if mibBuilder.loadTexts: rlLldpChassisIdSubtype.setDescription('The type of encoding used to identify the chassis associated with the local system.')
mibBuilder.exportSymbols("Dell-LLDP-MIB", rlLldpAutoAdvManAddrNone=rlLldpAutoAdvManAddrNone, rlLldpXMedLocMediaPolicyContainerIndex=rlLldpXMedLocMediaPolicyContainerIndex, rlLldpAutoAdvLocPortNum=rlLldpAutoAdvLocPortNum, rlLldpTLVsTxOverloading=rlLldpTLVsTxOverloading, rlLldpRemTtlEntry=rlLldpRemTtlEntry, rlLldpAutoAdvLocPortManAddrEntry=rlLldpAutoAdvLocPortManAddrEntry, PolicyNumber=PolicyNumber, rlLldpAutoAdvPortsStatus=rlLldpAutoAdvPortsStatus, rlLldpTLVsTxOverloadingSizeTable=rlLldpTLVsTxOverloadingSizeTable, PolicyContainerAppType=PolicyContainerAppType, rlLldpXMedLocMediaPolicyContainerRowStatus=rlLldpXMedLocMediaPolicyContainerRowStatus, rlLldpXMedLocMediaPolicyContainerEntry=rlLldpXMedLocMediaPolicyContainerEntry, rlLldpTLVsTxLeftSize=rlLldpTLVsTxLeftSize, rlLldpXMedLocMediaPolicyContainerPriority=rlLldpXMedLocMediaPolicyContainerPriority, rlLldpXMedLocMediaPolicyContainerDscp=rlLldpXMedLocMediaPolicyContainerDscp, rlLldpAutoAdvManAddrOwnerIfId=rlLldpAutoAdvManAddrOwnerIfId, rlLldpTLVsTxOverloadingStateExitTrap=rlLldpTLVsTxOverloadingStateExitTrap, rlLldpXMedLocMediaPolicyContainerTable=rlLldpXMedLocMediaPolicyContainerTable, rlLldpXMedNetPolVoiceUpdateMode=rlLldpXMedNetPolVoiceUpdateMode, rlLldpTLVsTxOverloadingPorts=rlLldpTLVsTxOverloadingPorts, rlLldpXMedLocMediaPolicyContainerPorts=rlLldpXMedLocMediaPolicyContainerPorts, PYSNMP_MODULE_ID=rlLldp, rlLldp=rlLldp, rlLldpEnabled=rlLldpEnabled, rlLldpLeftTLVsTxSize=rlLldpLeftTLVsTxSize, rlLldpAutoAdvManAddr=rlLldpAutoAdvManAddr, rlLldpTLVsTxOverloadingStateEnterTrap=rlLldpTLVsTxOverloadingStateEnterTrap, rlLldpXMedConfig=rlLldpXMedConfig, rlLldpXMedLocMediaPolicyContainerTagged=rlLldpXMedLocMediaPolicyContainerTagged, rlLldpObjects=rlLldpObjects, rlLldpConfig=rlLldpConfig, rlLldpChassisIdSubtype=rlLldpChassisIdSubtype, rlLldpTLVsTxOverloadingSizeEntry=rlLldpTLVsTxOverloadingSizeEntry, rlLldpRemTtlTable=rlLldpRemTtlTable, rlLldpTLVsTxGroupOverloading=rlLldpTLVsTxGroupOverloading, rlLldpTxOverloadingGroupId=rlLldpTxOverloadingGroupId, rlLldpTotalTLVsTxSize=rlLldpTotalTLVsTxSize, rlLldpClearRx=rlLldpClearRx, rlLldpRemTtl=rlLldpRemTtl, rlLldpXMedLocMediaPolicyContainerAppType=rlLldpXMedLocMediaPolicyContainerAppType, rlLldpTLVsTxSize=rlLldpTLVsTxSize, rlLldpXMedLocMediaPolicyContainerVlanID=rlLldpXMedLocMediaPolicyContainerVlanID, rlLldpXMedLocMediaPolicyContainerUnknown=rlLldpXMedLocMediaPolicyContainerUnknown, rlLldpTLVsTxOverloadingEntry=rlLldpTLVsTxOverloadingEntry, rlLldpTxOverloadingIndex=rlLldpTxOverloadingIndex, rlLldpTLVsTxOverloadingTable=rlLldpTLVsTxOverloadingTable, rlLldpAutoAdvManAddrSubtype=rlLldpAutoAdvManAddrSubtype, rlLldpAutoAdvLocPortManAddrTable=rlLldpAutoAdvLocPortManAddrTable, rlLldpDuMode=rlLldpDuMode, PolicyAppVoiceUpdateMode=PolicyAppVoiceUpdateMode, rlLldpTxOverloadingPortNum=rlLldpTxOverloadingPortNum)
