#
# PySNMP MIB module NTWS-AP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/NTWS-AP-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:25:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ntwsMibs, = mibBuilder.importSymbols("NTWS-ROOT-MIB", "ntwsMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Counter64, ObjectIdentity, Gauge32, Unsigned32, NotificationType, Counter32, Bits, MibIdentifier, TimeTicks, Integer32, ModuleIdentity, iso = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Counter64", "ObjectIdentity", "Gauge32", "Unsigned32", "NotificationType", "Counter32", "Bits", "MibIdentifier", "TimeTicks", "Integer32", "ModuleIdentity", "iso")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ntwsApTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 45, 6, 1, 4, 3))
ntwsApTc.setRevisions(('2009-07-21 01:03', '2008-12-02 01:01', '2008-11-27 01:00', '2008-11-26 00:51', '2008-10-06 00:50', '2008-05-07 00:41', '2008-02-14 00:32', '2007-12-03 00:30', '2007-09-25 00:24', '2007-07-06 00:23', '2007-07-05 00:22', '2006-07-10 00:15', '2006-03-30 00:14',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ntwsApTc.setRevisionsDescriptions(('v1.5.3: Introduced TCs: NtwsApPowerMode, NtwsRadioAntennaLocation, NtwsApLedMode.', "v1.5.1: Added bias value 'sticky(3)'.", 'v1.5.0: Introduced a new Radio identifier, not limited to two radios per AP: NtwsApRadioIndex and NtwsApRadioIndexOrZero.', "v1.4.1: Removed range from 'NtwsPowerLevel' (it was wrong already: too small, maximum power is at least 23, not 18). Added format where needed (DISPLAY-HINT).", 'v1.4.0: Introduced NtwsRadioRateEx.', 'v1.3.1: Introduced NtwsCryptoType.', 'v1.2.2: In order to support 802.11n, added radio types NA, NG and introduced NtwsRadioChannelWidth, NtwsRadioMimoState.', 'v1.2.0: Obsoleted NtwsRadioEnable and NtwsApPortOrDapNum (previously deprecated).', 'v1.1.4, MRT v3.2: Made changes in order to make MIB comply with corporate MIB conventions.', "v1.1.3: Introduced NtwsRadioMode in order to replace NtwsRadioEnable (in 6.2, a new administrative mode 'sentry' was added)", 'v1.1.2: Introduced NtwsApNum in order to replace NtwsApPortOrDapNum. (In 6.0, direct- and network-attached APs were unified.)', 'v1.0.1: Disallow illegal NtwsRadioRate values 1..9 while keeping zero (that means unknown rate)', 'v1.0: Initial version',))
if mibBuilder.loadTexts: ntwsApTc.setLastUpdated('200907210103Z')
if mibBuilder.loadTexts: ntwsApTc.setOrganization('Nortel Networks')
if mibBuilder.loadTexts: ntwsApTc.setContactInfo('www.nortelnetworks.com')
if mibBuilder.loadTexts: ntwsApTc.setDescription("Textual Conventions used by Nortel Networks wireless switches. AP = Access Point; AC = Access Controller (wireless switch), the device that runs a SNMP Agent using these TCs. Copyright 2009 Nortel Networks. All rights reserved. This Nortel Networks SNMP Management Information Base Specification (Specification) embodies Nortel Networks' confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Nortel Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class NtwsAccessType(TextualConvention, Integer32):
    description = "Describes the access type used by client or an AP. Value 'ap(1)' indicates access point that is directly attached to the switch. Value 'dap(2)' indicates distributed access point with attachment to the switch through the intermediate network. Value 'wired(3)' indicates a client that is directly attached to the switch (no access point is involved)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ap", 1), ("dap", 2), ("wired", 3))

class NtwsApAttachType(TextualConvention, Integer32):
    description = 'Type of AP attachment to AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("directAttach", 1), ("networkAttach", 2))

class NtwsApPortOrDapNum(TextualConvention, Unsigned32):
    description = 'AP Port, for directly attached APs, otherwise DAP Number (arbitrary number assigned when configuring the DAP on the AC). A zero value means unknown. Obsoleted by NtwsApNum. (In 6.0, direct- and network-attached APs were unified.)'
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class NtwsApNum(TextualConvention, Unsigned32):
    description = 'AP Number: arbitrary number assigned when configuring the AP on the AC. It is unique (on same AC), regardless of the type of AP attachment. A zero value means unknown.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9999)

class NtwsApState(TextualConvention, Integer32):
    description = 'AP State, as seen by the AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("init", 2), ("bootStarted", 3), ("imageDownloaded", 4), ("connectFailed", 5), ("configuring", 6), ("configured", 7))

class NtwsApTransition(TextualConvention, Integer32):
    description = 'AP state Transition, as seen by the AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("clear", 1), ("timeout", 2), ("reset", 3), ("bootSuccess", 4), ("startConfiguring", 5), ("connectFail", 6))

class NtwsApFailDetail(TextualConvention, Integer32):
    description = "Detailed failure codes for some of the transitions specified in 'NtwsApTransition'. - 'normalTransition' (91) means the corresponding transition is not a failure; could be caused by an explicit request (for example, AP was cleared) or it is a transition towards operational state. - 'failUnknown' (99) means there are no details available; the transition may be normal or undesirable/unexpected."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 11, 12, 91, 99))
    namedValues = NamedValues(("secureHandshakeFailure", 2), ("fingerprintRequired", 3), ("fingerprintMismatch", 4), ("portLinkUp", 11), ("portLinkDown", 12), ("normalTransition", 91), ("failUnknown", 99))

class NtwsApConnectSecurityType(TextualConvention, Integer32):
    description = 'Security level of the connection between AP and AC: secure(1) - fingerprint matching; insecure(2) - fingerprint not configured, or optional and not matching; auto(3) - Auto-DAP is intrinsically insecure: could not check fingerprint since no specific DAP is configured.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("secure", 1), ("insecure", 2), ("auto", 3))

class NtwsApServiceAvailability(TextualConvention, Integer32):
    description = 'Level of wireless service availability.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fullService", 1), ("noService", 2), ("degradedService", 3))

class NtwsApBias(TextualConvention, Integer32):
    description = 'Bias of AP attachment to this AC. Setting an APs bias on an AC switch to high causes the switch to be preferred over switches with low bias, for booting and managing the AP. Bias applies only to AC switches that are indirectly attached to the AP through an intermediate Layer 2 or Layer 3 network. An AP always attempts to boot on AP port 1 first, and if an AC switch is directly attached on AP port 1, the AP boots from it regardless of the bias settings.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("high", 1), ("low", 2), ("sticky", 3))

class NtwsApSerialNum(TextualConvention, OctetString):
    description = 'The value is a zero length string if unknown or unavailable. Otherwise the value is a serial number, which consists of printable ASCII characters between 0x21 (!), and 0x7d (}) with no leading, embedded, or trailing space.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class NtwsApFingerprint(TextualConvention, OctetString):
    description = 'Represents a RSA key fingerprint (binary value), which is the MD5 hash of the public key of the RSA key pair. Or a zero length string if not known or unavailable.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class NtwsRadioNum(TextualConvention, Integer32):
    description = 'Enumeration for multi-radio APs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("radio-1", 1), ("radio-2", 2), ("not-applicable", 3))

class NtwsApRadioIndex(TextualConvention, Unsigned32):
    description = 'A unique value, greater than zero, for each Radio on the AP. Intended to replace NtwsRadioNum.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class NtwsApRadioIndexOrZero(TextualConvention, Unsigned32):
    description = "This textual convention is an extension of the NtwsApRadioIndex convention. The latter defines a greater than zero value used to identify each Radio on the AP. This extension permits the additional value of zero. A zero value means 'none', 'unknown radio' or 'not applicable'. Each object using this textual convention should document the meaning of Radio Index zero."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class NtwsPowerLevel(TextualConvention, Unsigned32):
    description = 'The current level of transmit power expressed in dbm.'
    status = 'current'
    displayHint = 'd'

class NtwsRadioPowerChangeType(TextualConvention, Integer32):
    description = 'Enumerations for why the power level was changed, which occurs due to auto-tune operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("dup-pkts-threshold-exceed", 1), ("retransmit-threshold-exceed", 2), ("clients-optimal-performance-reached", 3), ("def-power-threshold-exceed", 4))

class NtwsChannelChangeType(TextualConvention, Integer32):
    description = 'Enumerations for why the channel was changed, which occurs due to auto-tune operation'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("util-index", 1), ("rexmit-pkt-offset", 2), ("noise-offset", 3), ("noise", 4), ("utilization", 5), ("phy-error-offset", 6), ("crc-errors-offset", 7), ("radar-detected", 8))

class NtwsChannelNum(TextualConvention, Unsigned32):
    description = 'Channel Number'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class NtwsRadioEnable(TextualConvention, Integer32):
    description = 'Radio mode (administratively enabled or disabled). Obsoleted by NtwsRadioMode.'
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class NtwsRadioMode(TextualConvention, Integer32):
    description = 'Configured mode of an AP radio. There are three administratively controlled values: - enabled: radio may provide service to clients; - sentry: radio will not provide service, but can be used for RF scanning and can run countermeasures; - disabled: radio will not emit at all (thus cannot run countermeasures), can only be used for RF scanning. Obsoletes NtwsRadioEnable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("sentry", 3))

class NtwsRadioConfigState(TextualConvention, Integer32):
    description = 'Radio Configuration State, as seen by the AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("configInit", 1), ("configFail", 2), ("configOk", 3))

class NtwsRadioRate(TextualConvention, Unsigned32):
    description = 'The possible transmission rates of an AP radio. Both a and b/g rates are covered; a specific radio will report the applicable transmission rates (either a or b/g). Here are the possible rates, in Mbps: - 802.11g radios: 54, 48, 36, 24, 18, 12, 11, 9, 6, 5.5, 2, or 1; - 802.11b radios: 11, 5.5, 2, or 1; - 802.11a radios: 54, 48, 36, 24, 18, 12, 9, or 6. The value in MIB is specified as the rate in Mbps times 10, in order to have only integer values, zero meaning unknown rate.'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 540), )
class NtwsRadioRateEx(TextualConvention, Integer32):
    description = 'Radio Rates Extended (covering 11n MCS rates): The possible transmission rates of an AP radio. 11a, 11b/g, 11na and 11ng rates are included; a specific radio will report the applicable transmission rates (either a, b/g, na, ng). Here are the possible rates, in Mbps: - 802.11g radios: 54, 48, 36, 24, 18, 12, 11, 9, 6, 5.5, 2, or 1; - 802.11b radios: 11, 5.5, 2, or 1; - 802.11a radios: 54, 48, 36, 24, 18, 12, 9, or 6; - 802.11ng radios: MCS0-MCS15 and all 11g rates; - 802.11na radios: MCS0-MCS15 and all 11a rates.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35))
    namedValues = NamedValues(("rateUnknown", 1), ("rate1", 2), ("rate2", 3), ("rate5-5", 4), ("rate6", 5), ("rate9", 6), ("rate11", 7), ("rate12", 8), ("rate18", 9), ("rate24", 10), ("rate36", 11), ("rate48", 12), ("rate54", 13), ("rateMCS0", 20), ("rateMCS1", 21), ("rateMCS2", 22), ("rateMCS3", 23), ("rateMCS4", 24), ("rateMCS5", 25), ("rateMCS6", 26), ("rateMCS7", 27), ("rateMCS8", 28), ("rateMCS9", 29), ("rateMCS10", 30), ("rateMCS11", 31), ("rateMCS12", 32), ("rateMCS13", 33), ("rateMCS14", 34), ("rateMCS15", 35))

class NtwsRadioType(TextualConvention, Integer32):
    description = 'Enumeration to indicate the Radio Type, as seen by AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("typeUnknown", 1), ("typeA", 2), ("typeB", 3), ("typeG", 4), ("typeNA", 5), ("typeNG", 6))

class NtwsRssi(TextualConvention, Integer32):
    description = 'RSSI (Received Signal Strength Indicator) for last packet received, in decibels referred to 1 milliwatt (dBm). A higher value indicates a stronger signal.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-100, 0)

class NtwsApWasOperational(TextualConvention, Integer32):
    description = 'Enumeration to indicate whether the AP was operational before a transition occurred. Normally used in notifications.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oper", 1), ("nonOper", 2))

class NtwsRadioChannelWidth(TextualConvention, Integer32):
    description = 'Enumeration to indicate the administratively controlled Radio Channel Width.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("channelWidth20MHz", 1), ("channelWidth40MHz", 2))

class NtwsRadioMimoState(TextualConvention, Integer32):
    description = 'Enumeration to indicate the MIMO state of the Radio (Multiple Input Multiple Output), as seen by the AC. This depends on radio type and power supplied to the radio. mimo1x1: radio uses one transmit chain and one receive chain; mimo2x3: radio uses two transmit chains and three receive chains; mimo3x3: radio uses three transmit chains and three receive chains.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mimoOther", 1), ("mimo1x1", 2), ("mimo2x3", 3), ("mimo3x3", 4))

class NtwsApPowerMode(TextualConvention, Integer32):
    description = 'Enumerations of the modes in which power is supplied by the AP to its components (mainly radios). There are two administratively controlled values: - auto: the power is managed automatically by sensing the power level on the AP; - high: all radios operate at the maximum power available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("high", 2))

class NtwsApLedMode(TextualConvention, Integer32):
    description = 'Enumeration to indicate the administratively controlled LED mode for an AP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("auto", 1), ("static", 2), ("off", 3))

class NtwsRadioAntennaLocation(TextualConvention, Integer32):
    description = 'Enumeration to indicate the administratively controlled Radio Antenna Location.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("indoors", 1), ("outdoors", 2))

class NtwsCryptoType(TextualConvention, Integer32):
    description = 'Enumeration of Crypto Types: - clear: Cleartext (unencrypted communication); - wep: Wired Equivalent Privacy; - wep40: WEP with 40-bit keys; - wep104: WEP with 104-bit keys; - tkip: Temporal Key Integrity Protocol; - aesCcmp: Advanced Encryption Standard, Counter mode with CBC MAC Protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("clear", 2), ("wep", 3), ("wep40", 4), ("wep104", 5), ("tkip", 6), ("aesCcmp", 7))

mibBuilder.exportSymbols("NTWS-AP-TC", ntwsApTc=ntwsApTc, NtwsRadioChannelWidth=NtwsRadioChannelWidth, NtwsRadioMode=NtwsRadioMode, NtwsRadioNum=NtwsRadioNum, NtwsApRadioIndex=NtwsApRadioIndex, NtwsRadioRate=NtwsRadioRate, NtwsApState=NtwsApState, NtwsAccessType=NtwsAccessType, NtwsRadioType=NtwsRadioType, NtwsApWasOperational=NtwsApWasOperational, NtwsApLedMode=NtwsApLedMode, NtwsApFingerprint=NtwsApFingerprint, NtwsChannelChangeType=NtwsChannelChangeType, NtwsRadioPowerChangeType=NtwsRadioPowerChangeType, NtwsRadioEnable=NtwsRadioEnable, NtwsRadioAntennaLocation=NtwsRadioAntennaLocation, NtwsApFailDetail=NtwsApFailDetail, NtwsApNum=NtwsApNum, NtwsApRadioIndexOrZero=NtwsApRadioIndexOrZero, NtwsRssi=NtwsRssi, NtwsRadioMimoState=NtwsRadioMimoState, NtwsApSerialNum=NtwsApSerialNum, NtwsApServiceAvailability=NtwsApServiceAvailability, NtwsApBias=NtwsApBias, PYSNMP_MODULE_ID=ntwsApTc, NtwsApTransition=NtwsApTransition, NtwsCryptoType=NtwsCryptoType, NtwsApPortOrDapNum=NtwsApPortOrDapNum, NtwsRadioConfigState=NtwsRadioConfigState, NtwsApConnectSecurityType=NtwsApConnectSecurityType, NtwsRadioRateEx=NtwsRadioRateEx, NtwsApAttachType=NtwsApAttachType, NtwsPowerLevel=NtwsPowerLevel, NtwsChannelNum=NtwsChannelNum, NtwsApPowerMode=NtwsApPowerMode)
