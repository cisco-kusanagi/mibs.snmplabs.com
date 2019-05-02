#
# PySNMP MIB module AVAYA-WLAN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/AVAYA-WLAN-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:32:23 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint")
SnmpAdminString, = mibBuilder.importSymbols("SNMP-FRAMEWORK-MIB", "SnmpAdminString")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Unsigned32, ObjectIdentity, MibIdentifier, Counter64, NotificationType, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, Bits, ModuleIdentity, Counter32, Integer32, IpAddress, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Counter64", "NotificationType", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "Bits", "ModuleIdentity", "Counter32", "Integer32", "IpAddress", "Gauge32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
avayaWlanMibs, = mibBuilder.importSymbols("SYNOPTICS-ROOT-MIB", "avayaWlanMibs")
avayaWlanTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 7, 1))
avayaWlanTcMib.setRevisions(('2011-12-15 00:00', '2011-11-21 00:00', '2011-10-11 00:00', '2011-07-23 00:00', '2011-01-07 00:00', '2010-06-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: avayaWlanTcMib.setRevisionsDescriptions(('v5: Following new TCs are added for MobSw notifications: AvWlanMobVlanRole AvWlanMobVlanState AvWlanSwitchNotifAuxLimitsMap ', 'v4: Following updates are done: Added more values in AvWlanSwitchModel. Added AvWlanLoadBalanceMetric.', 'v3: Added AvWlanPacketCaptureFilterMask TC for packet capture module. Added captureProfile component to AvWlanConfigSyncComponents', 'v2: Added ap8120-O to AvWlanAPModel TC. Changed ap8120E to ap8120-E Added AvWlanRadioAntenna, AvWlanRadioAntennaOrNone Added AvWlanRadioExtCableOrNone Added AvWlanCountryCode Added AvWlanCpProfileUpdateFileTypeOrNone Added AvWlanCpProfileUpdateActionStatus Added more channels to AvWlanRadioChannel and AvWlanRadioChannelOrZero Added more components to AvWlanConfigSyncComponents', 'v2: Added ap8120E to AvWlanAPModel TC.', 'v1: Initial version.',))
if mibBuilder.loadTexts: avayaWlanTcMib.setLastUpdated('201107230000Z')
if mibBuilder.loadTexts: avayaWlanTcMib.setOrganization('Avaya, Inc')
if mibBuilder.loadTexts: avayaWlanTcMib.setContactInfo('Avaya, Inc')
if mibBuilder.loadTexts: avayaWlanTcMib.setDescription("Avaya WLAN Textual Conventions MIB Copyright 2010 - 2011 Avaya, Inc. All rights reserved. This Avaya SNMP Management Information Base Specification (Specification) embodies Avaya's confidential and proprietary intellectual property. Avaya retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS,' and Avaya makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class AvWlanDomainRole(TextualConvention, Integer32):
    description = 'This TC indicates the status of an MDC(Mobility Domain Controller).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("activeMdc", 1), ("backupMdc", 2), ("peerWc", 3), ("standalone", 4))

class AvWlanControllerModel(TextualConvention, Integer32):
    description = 'This TC indicates a Wireless Controller type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("wc8180", 1))

class AvWlanSwitchModel(TextualConvention, Integer32):
    description = 'This TC indicates a Mobility Switch type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("wc8180", 1), ("wsp8180", 2), ("ers8800", 3))

class AvWlanNumberAPsPerWC(TextualConvention, Unsigned32):
    description = 'This TC indicates the range of APs possible per WC(Wireless Controller).'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 512)

class AvWlanAPModel(TextualConvention, Integer32):
    description = 'This TC indicates the AP models that WC supports. - ap8120 : indoor AP8120 - ap8120-E: indoor AP8120 with external antenna(s) - ap8120-O: outdoor AP8120 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4))
    namedValues = NamedValues(("ap8120", 2), ("ap8120-E", 3), ("ap8120-O", 4))

class AvWlanAPModelOrNone(TextualConvention, Integer32):
    description = 'This TC indicates the AP models that WC supports. The meaning of the special value none(255) must be specified by any object using this TC in its SYNTAX clause.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 255))
    namedValues = NamedValues(("ap8120", 2), ("ap8120-E", 3), ("ap8120-O", 4), ("none", 255))

class AvWlanAPStatus(TextualConvention, Integer32):
    description = 'This TC indicates the status of an AP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("managed", 1), ("unknown", 2), ("standalone", 3), ("rogue", 4), ("knownForeign", 5))

class AvWlanRadioChannel(TextualConvention, Integer32):
    description = 'This TC indicates a wireless radio channel.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(1, 14), ValueRangeConstraint(34, 34), ValueRangeConstraint(36, 36), ValueRangeConstraint(38, 38), ValueRangeConstraint(40, 40), ValueRangeConstraint(42, 42), ValueRangeConstraint(44, 44), ValueRangeConstraint(46, 46), ValueRangeConstraint(48, 48), ValueRangeConstraint(52, 52), ValueRangeConstraint(56, 56), ValueRangeConstraint(60, 60), ValueRangeConstraint(64, 64), ValueRangeConstraint(100, 100), ValueRangeConstraint(104, 104), ValueRangeConstraint(108, 108), ValueRangeConstraint(112, 112), ValueRangeConstraint(116, 116), ValueRangeConstraint(120, 120), ValueRangeConstraint(124, 124), ValueRangeConstraint(128, 128), ValueRangeConstraint(132, 132), ValueRangeConstraint(136, 136), ValueRangeConstraint(140, 140), ValueRangeConstraint(149, 149), ValueRangeConstraint(153, 153), ValueRangeConstraint(157, 157), ValueRangeConstraint(161, 161), ValueRangeConstraint(165, 165), ValueRangeConstraint(184, 184), ValueRangeConstraint(188, 188), ValueRangeConstraint(192, 192), ValueRangeConstraint(196, 196), ValueRangeConstraint(200, 200), ValueRangeConstraint(204, 204), ValueRangeConstraint(208, 208), ValueRangeConstraint(212, 212), ValueRangeConstraint(216, 216), )
class AvWlanRadioChannelOrZero(TextualConvention, Integer32):
    description = 'This TC indicates a wireless radio channel. The special value 0 must have its meaning described by any objects of this type.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 14), ValueRangeConstraint(34, 34), ValueRangeConstraint(36, 36), ValueRangeConstraint(38, 38), ValueRangeConstraint(40, 40), ValueRangeConstraint(42, 42), ValueRangeConstraint(44, 44), ValueRangeConstraint(46, 46), ValueRangeConstraint(48, 48), ValueRangeConstraint(52, 52), ValueRangeConstraint(56, 56), ValueRangeConstraint(60, 60), ValueRangeConstraint(64, 64), ValueRangeConstraint(100, 100), ValueRangeConstraint(104, 104), ValueRangeConstraint(108, 108), ValueRangeConstraint(112, 112), ValueRangeConstraint(116, 116), ValueRangeConstraint(120, 120), ValueRangeConstraint(124, 124), ValueRangeConstraint(128, 128), ValueRangeConstraint(132, 132), ValueRangeConstraint(136, 136), ValueRangeConstraint(140, 140), ValueRangeConstraint(149, 149), ValueRangeConstraint(153, 153), ValueRangeConstraint(157, 157), ValueRangeConstraint(161, 161), ValueRangeConstraint(165, 165), ValueRangeConstraint(184, 184), ValueRangeConstraint(188, 188), ValueRangeConstraint(192, 192), ValueRangeConstraint(196, 196), ValueRangeConstraint(200, 200), ValueRangeConstraint(204, 204), ValueRangeConstraint(208, 208), ValueRangeConstraint(212, 212), ValueRangeConstraint(216, 216), )
class AvWlanRadioPower(TextualConvention, Integer32):
    description = 'This TC indicates a wireless radio power setting.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 100)

class AvWlanRadioAntenna(TextualConvention, Integer32):
    description = 'This TC indicates a type of antenna attached on a radio in AP. - wl81AT070E6: Avaya AP external antenna (70 degree) - wl81AT180E6: Avaya AP external antenna (180 degree)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 4))
    namedValues = NamedValues(("wl81AT070E6", 2), ("wl81AT180E6", 4))

class AvWlanRadioAntennaOrNone(TextualConvention, Integer32):
    description = 'This TC indicates a type of antenna attached on a radio in AP. - wl81AT070E6: Avaya AP external antenna (70 degree) - wl81AT180E6: Avaya AP external antenna (180 degree) The meaning of the special value none(255) must be specified by any object using this TC in its SYNTAX clause.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 4, 255))
    namedValues = NamedValues(("wl81AT070E6", 2), ("wl81AT180E6", 4), ("none", 255))

class AvWlanRadioExtCable(TextualConvention, Integer32):
    description = 'This TC indicates a type of extension cable used to attach an antenna for a radio in AP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ft3", 1), ("ft10", 2))

class AvWlanRadioExtCableOrNone(TextualConvention, Integer32):
    description = 'This TC indicates a type of extension cable used to attach an antenna for a radio in AP. The meaning of the special value none(255) must be specified by any object using this TC in its SYNTAX clause.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 255))
    namedValues = NamedValues(("ft3", 1), ("ft10", 2), ("none", 255))

class AvWlanRadioOperationMode(TextualConvention, Integer32):
    description = 'The operation mode of a radio with respect to access and WIDS/WIPS functionality. accessWids(1): The radio provides both access and WIDS functionality widsWips(2): The radio provides only WIDS functionality (no access). If both avWlanWidpsApDeauthenticationAttack and avWlanWidpsClientThreatMitigation in AVAYA-WLAN-WIDPS-MIB are enabled, it also provides WIPS functionality.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("accessWids", 1), ("widsWips", 2))

class AvWlanRadioInterface(TextualConvention, Integer32):
    description = 'Identifies a radio interface.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 3)

class AvWlanRadioInterfaceOrZero(TextualConvention, Integer32):
    description = 'Identifies a radio interface. The meaning of the special value 0 must be defined be any object using this TC in its SYNTAX clause.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 3)

class AvWlanDataRateSet(TextualConvention, OctetString):
    description = 'An object of this type represents a set of data rates in the range of 1 Mbps through 63.5 Mbps, in increments of 0.5 Mbps (500 Kbps). The value of an object of this type contains a string of bits, where each bit corresponds to a particular data rate. Bits start with the high order bit of the first octet, representing 0.5 Mbps, and are contiguous representing increasing data rates in increments of 0.5 Mbps. For example, the following bits correspond to the following data rates: Octet Bit Mbps 0 0x80 1 0 0x40 1.5 0 0x20 2 0 0x10 2.5 0 0x08 3 0 0x04 3.5 0 0x02 4 0 0x01 4.5 1 0x80 5 1 0x40 5.5 . . . . 15 0x20 63.5 If the bit corresponding to a particular data rate is set, that rate is considered to be a member of the set of data rates. The bit position BP for a particular data rate DR can be found using the following formula: BP = (DR * 2) - 2 The bit value corresponding to a particular data rate can be found using the following formula, where BP is the bit position as above, and O is the array of octets returned as the value of an object of this type: bitValue = (O[BP/8] >> (7 - (BP % 8))) & 0x01 Similarly, the bit for a particular data rate can be set as follows: O[BP/8] |= 0x80 >> (BP % 8) And cleared as follows: O[BP/8] &= ~(0x80 >> (BP % 8)) Any trailing octets whose value is 0x00 may be truncated from the value of an object of this type.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 16)

class AvWlanChannelSet(TextualConvention, OctetString):
    description = 'An object of this type represents a set of wireless channels in the range of 1 through 255. The value of an object of this type contains a string of bits, where each bit corresponds to a particular channel. Bits start with the high order bit of the first octet, representing channel 1, and are contiguous representing increasing channel numbers. For example, the following bits correspond to the following channels: Octet Bit Channel 0 0x80 1 0 0x40 2 0 0x20 3 0 0x10 4 0 0x08 5 0 0x04 6 0 0x02 7 0 0x01 8 1 0x80 9 1 0x40 10 . . . . 31 0x02 255 If the bit corresponding to a particular channel is set, that channel is considered to be a member of the set of channels. The bit value corresponding to a particular channel CH can be found using the following formula, where O is the array of octets returned as the value of an object of this type: bitValue = (O[(CH-1)/8] >> (7 - ((CH-1) % 8))) & 0x01 Similarly, the bit for a particular channel can be set as follows: O[(CH-1)/8] |= 0x80 >> ((CH-1) % 8) And cleared as follows: O[(CH-1)/8] &= ~(0x80 >> ((CH-1) % 8)) Any trailing octets whose value is 0x00 may be truncated from the value of an object of this type.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class AvWlanRPTimeOfDay(TextualConvention, OctetString):
    description = "This TC indicates one or more ranges of time during which access to the network is allowed or denied. The format can be any of the following: 1. An empty string which indicates access is always allowed. 2. The string 'never', which indicates access is always denied. 3. The string 'any', which indicates access is always allowed. 4. The string 'al', which indicates access is always allowed. 5. A comma separated list of one or more strings in the format '<day><hhmm-hhmm>', each of which indicates that access is allowed on the specified day during the specified range of times. The valid strings for '<day>' are: 'mo' - Monday 'tu' - Tuesday 'we' - Wednesday 'th' - Thursday 'fr' - Friday 'sa' - Saturday 'su' - Sunday 'wk' - Indicates all days of the week Note that no whitespace characters or other special characters other than those noted above are allowed."
    status = 'current'
    displayHint = '255t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class AvWlanOui(TextualConvention, OctetString):
    description = '24-bit Organizationally Unique Identifier. Information on OUIs can be found in IEEE 802-2001 [802-2001] Clause 9.'
    status = 'current'
    displayHint = '1x:'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(3, 3)
    fixedLength = 3

class AvWlanTspecSuppAccessCategory(TextualConvention, Integer32):
    description = 'Access category (AC) used for TSPEC. Only those ACs that support mandatory admission control are listed here.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("voice", 1), ("video", 2))

class AvWlanConfigSyncComponents(TextualConvention, Bits):
    description = 'Enumerates WLAN configuration components that participate in the mobility domain configuration sync operation.'
    status = 'current'
    namedValues = NamedValues(("apDatabase", 0), ("apProfile", 1), ("radioProfile", 2), ("networkProfile", 3), ("autoRF", 4), ("domainConfig", 5), ("captivePortal", 6), ("qosAcl", 7), ("qosDiffserv", 8), ("radiusGlobal", 9), ("radiusAuth", 10), ("radiusAcct", 11), ("mobilityVlan", 12), ("e911Config", 13), ("widsWips", 14), ("widsKnownAp", 15), ("securityUserDb", 16), ("securityMacDb", 17), ("radiusProfile", 18), ("radiusProfileServer", 19), ("crypto", 20), ("captureProfile", 21))

class AvWlanAPLicenseCapacity(TextualConvention, Integer32):
    description = "This object identifies the maximum capacity of AP license of the controller. The capacity is either None, 16 Locked or Unlimited. When 'unlimited' is specified, the actual capacity is the validated and supported AP license count for that release. Please refer to the release notes for this count."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("none", 1), ("sixteenLocked", 2), ("unlimited", 3))

class AvWlanLogMsgLevel(TextualConvention, Integer32):
    description = 'This object identifies the severity level of log messages that will be saved in volatile memory or sent to a remote syslog server when they occur'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("critical", 1), ("serious", 2), ("informational", 3), ("none", 4))

class AvWlanCountryCode(SnmpAdminString):
    description = 'This TC indicates the country of operation for WLAN.'
    status = 'current'
    subtypeSpec = SnmpAdminString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class AvWlanImageFileOrNone(TextualConvention, Integer32):
    description = "This TC specifies the type of the file to be updated, usually used in 'Captive Portal Profile Customization' action. - all: all customizable files - account: accounting image file - brand: branding image file - background: background image file - logout: logout background image file - pkgfile: package file"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 255))
    namedValues = NamedValues(("all", 1), ("account", 2), ("brand", 3), ("background", 4), ("logout", 5), ("pkgfile", 6), ("none", 255))

class AvWlanFileUpdateStatus(TextualConvention, Integer32):
    description = "This TC specifies the status of the file update action, usually used in the 'Captive Portal Profile Customization Update Action'"
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("none", 1), ("success", 2), ("transferFailed", 3), ("inProgress", 4), ("fileProcFailed", 5), ("fileNotFound", 6), ("internalError", 7), ("noSuchProfile", 8), ("noSuchLocale", 9), ("noSuchController", 10), ("maxFileSizeExceed", 11), ("maxProfileSizeExceed", 12))

class AvWlanPacketCaptureFilterMask(TextualConvention, Bits):
    description = "Bit mask to represent the various filter criteria which can be applied for a remote packet capture event. Only five filters are supported in this release. Note that value 0 will be the MSB in the first octet and will be contiguosly numbered till the last bit in the lower octets. So when the number of bits is not a multiple of eight, the remaining bits will be in the final octet (filled by zero's). Usage examples: -------------- If we want to set the value for beacons(0), data(2) and mgmt(3), the value can be set in any of the following format: 10110000b or '10110000'B or 0xB0 or 'B0'h. "
    status = 'current'
    namedValues = NamedValues(("beacons", 0), ("probes", 1), ("data", 2), ("mgmt", 3), ("control", 4))

class AvWlanLoadBalanceMetric(TextualConvention, Integer32):
    description = 'This TC indicates a type of load balancing metric. This is mainly used only in status MIBs'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("preferred", 1), ("alternate", 2), ("leastLoad", 3), ("cbfs", 4))

class AvWlanMobVlanRole(TextualConvention, Integer32):
    description = 'This TC indicates the role of mobility vlan in a mobility domain. The following roles are supported for a mobility VLAN: - server: Mobilty VLAN server - staticClient: Static Mobility VLAN - dynamicClient: Learnt dynamic Mobility VLAN - none: No role '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("server", 1), ("staticClient", 2), ("dynamicClient", 3), ("none", 4))

class AvWlanMobVlanState(TextualConvention, Integer32):
    description = 'This TC indicates the state of mapped mobility vlan in the switch.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("inactive", 2))

class AvWlanSwitchNotifAuxLimitsMap(TextualConvention, Bits):
    description = 'This objects is included in the avWlanSwitchLimitsReached notification to indicate which limits have been reached. The meaning of each bit in this object, and the additional objects included in the notification when each bit is set, are described below. Objects corresponding to each bit will appear in the notification in the order of the bit values, i.e., the objects for bit 0, if set, will appear first, followed by the objects for bit 1, if set, and so on. The objects listed below, when included in avWlanSwitchLimitsReached, indicate the last values that were added to or attempted to be added to the table/list specified by each bit. The meaning of each object depends on the bit with which the object is associated in a generated notification, as described below: VlanMapTableFull(0) The current number of vlan mappings has reached the max limit. TunnelTableFull(1) The current number of tunnels has reached the max limit. MulticastTableFull(2) The current number of multicast groups has reached the max limit. '
    status = 'current'
    namedValues = NamedValues(("vlanMapTableFull", 0), ("tunnelTableFull", 1), ("multicastTableFull", 2))

mibBuilder.exportSymbols("AVAYA-WLAN-TC-MIB", AvWlanCountryCode=AvWlanCountryCode, AvWlanRadioAntenna=AvWlanRadioAntenna, AvWlanRadioInterfaceOrZero=AvWlanRadioInterfaceOrZero, AvWlanRadioExtCableOrNone=AvWlanRadioExtCableOrNone, AvWlanDomainRole=AvWlanDomainRole, AvWlanRadioExtCable=AvWlanRadioExtCable, AvWlanMobVlanState=AvWlanMobVlanState, AvWlanRadioInterface=AvWlanRadioInterface, AvWlanImageFileOrNone=AvWlanImageFileOrNone, AvWlanRPTimeOfDay=AvWlanRPTimeOfDay, AvWlanPacketCaptureFilterMask=AvWlanPacketCaptureFilterMask, AvWlanControllerModel=AvWlanControllerModel, avayaWlanTcMib=avayaWlanTcMib, AvWlanRadioOperationMode=AvWlanRadioOperationMode, AvWlanAPModelOrNone=AvWlanAPModelOrNone, AvWlanChannelSet=AvWlanChannelSet, AvWlanAPLicenseCapacity=AvWlanAPLicenseCapacity, AvWlanAPModel=AvWlanAPModel, AvWlanConfigSyncComponents=AvWlanConfigSyncComponents, AvWlanRadioPower=AvWlanRadioPower, PYSNMP_MODULE_ID=avayaWlanTcMib, AvWlanAPStatus=AvWlanAPStatus, AvWlanTspecSuppAccessCategory=AvWlanTspecSuppAccessCategory, AvWlanSwitchNotifAuxLimitsMap=AvWlanSwitchNotifAuxLimitsMap, AvWlanRadioChannelOrZero=AvWlanRadioChannelOrZero, AvWlanFileUpdateStatus=AvWlanFileUpdateStatus, AvWlanLogMsgLevel=AvWlanLogMsgLevel, AvWlanOui=AvWlanOui, AvWlanNumberAPsPerWC=AvWlanNumberAPsPerWC, AvWlanSwitchModel=AvWlanSwitchModel, AvWlanRadioAntennaOrNone=AvWlanRadioAntennaOrNone, AvWlanLoadBalanceMetric=AvWlanLoadBalanceMetric, AvWlanRadioChannel=AvWlanRadioChannel, AvWlanDataRateSet=AvWlanDataRateSet, AvWlanMobVlanRole=AvWlanMobVlanRole)
