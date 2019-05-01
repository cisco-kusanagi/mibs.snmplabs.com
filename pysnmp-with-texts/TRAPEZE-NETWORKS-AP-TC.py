#
# PySNMP MIB module TRAPEZE-NETWORKS-AP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/TRAPEZE-NETWORKS-AP-TC
# Produced by pysmi-0.3.4 at Wed May  1 15:27:06 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, Counter32, Gauge32, ObjectIdentity, Integer32, ModuleIdentity, TimeTicks, NotificationType, MibIdentifier, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, Unsigned32, iso = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "Counter32", "Gauge32", "ObjectIdentity", "Integer32", "ModuleIdentity", "TimeTicks", "NotificationType", "MibIdentifier", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "Unsigned32", "iso")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
trpzMibs, = mibBuilder.importSymbols("TRAPEZE-NETWORKS-ROOT-MIB", "trpzMibs")
trpzApTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 14525, 4, 3))
trpzApTc.setRevisions(('2011-10-05 02:32', '2011-01-28 02:20', '2011-01-28 02:10', '2010-11-30 02:01', '2010-11-29 01:31', '2009-07-21 01:03', '2008-12-02 01:01', '2008-11-27 01:00', '2008-11-26 00:51', '2008-10-06 00:50', '2008-05-07 00:41', '2008-02-14 00:32', '2007-12-03 00:30', '2007-07-06 00:23', '2007-07-05 00:22', '2006-07-10 00:15', '2006-03-30 00:14',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: trpzApTc.setRevisionsDescriptions(("v2.3.2: New AP state (enum value in TrpzApState): 'redundant(10)'. New AP transitions (enum values in TrpzApTransition): 'setBackupConn(10)', 'startHandoverReconfiguring(11)'. (for 7.6 release)", 'v2.2.0: Added eight new AP Radio 11n transmission rates, MCS 16 to MCS 23 (enum values in TrpzRadioRateEx). (for 7.5 release)', "v2.1.0: Added fail detail value 'adminRequest(92)' (for 7.5 release)", "v2.0.1: Extending the AP state machine model for the WAN Outage feature: New AP state (enum value in TrpzApState): 'connOutage(20)'. New AP transitions (enum values in TrpzApTransition): 'connLost(20)', 'connRestored(21)', 'connOutageExtendedTimeout(22)'. Renamed AP state (7) from 'configured' to 'operational' to make clear how it is related to the AP Status traps: AP Non-Operational Status (trpzApNonOperStatusTrap) and AP Operational - Radio Status (trpzApOperRadioStatusTrap). (for 7.5 release)", "v1.8.1: Added Crypto Type enum value 'sms4(8)' (for 7.5 release)", 'v1.5.3: Introduced TCs: TrpzApPowerMode, TrpzRadioAntennaLocation, TrpzApLedMode (for 7.1 release)', "v1.5.1: Added bias value 'sticky(3)' (for 7.1 release)", 'v1.5.0: Introduced a new Radio identifier, not limited to two radios per AP: TrpzApRadioIndex and TrpzApRadioIndexOrZero (for 7.1 release)', "v1.4.1: Removed range from 'TrpzPowerLevel' (it was wrong already: too small, maximum power is at least 23, not 18). Added format where needed (DISPLAY-HINT). This will be published in 7.1 release.", 'v1.4.0: Introduced TrpzRadioRateEx (for 7.1 release)', 'v1.3.1: Introduced TrpzCryptoType (for 7.0 release)', 'v1.2.2: In order to support 802.11n, added radio types NA, NG and introduced TrpzRadioChannelWidth, TrpzRadioMimoState (for 7.0 release)', 'v1.2.0: Obsoleted TrpzRadioEnable and TrpzApPortOrDapNum (previously deprecated). This will be published in 7.0 release.', "v1.1.3: Introduced TrpzRadioMode in order to replace TrpzRadioEnable (in 6.2, a new administrative mode 'sentry' was added)", 'v1.1.2: Introduced TrpzApNum in order to replace TrpzApPortOrDapNum. (In 6.0, direct- and network-attached APs were unified.)', 'v1.0.1: Disallow illegal TrpzRadioRate values 1..9 while keeping zero (that means unknown rate)', 'v1.0: Initial version, for 4.1 release',))
if mibBuilder.loadTexts: trpzApTc.setLastUpdated('201110050232Z')
if mibBuilder.loadTexts: trpzApTc.setOrganization('Trapeze Networks')
if mibBuilder.loadTexts: trpzApTc.setContactInfo('Trapeze Networks Technical Support www.trapezenetworks.com US: 866.TRPZ.TAC International: 925.474.2400 support@trapezenetworks.com')
if mibBuilder.loadTexts: trpzApTc.setDescription("Textual Conventions used by Trapeze Networks wireless switches. AP = Access Point; AC = Access Controller (wireless switch), the device that runs a SNMP Agent using these TCs. Copyright 2006-2011 Trapeze Networks, Inc. All rights reserved. This Trapeze Networks SNMP Management Information Base Specification (Specification) embodies Trapeze Networks' confidential and proprietary intellectual property. Trapeze Networks retains all title and ownership in the Specification, including any revisions. This Specification is supplied 'AS IS' and Trapeze Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class TrpzAccessType(TextualConvention, Integer32):
    description = "Describes the access type used by client or an AP. Value 'ap(1)' indicates access point that is directly attached to the switch. Value 'dap(2)' indicates distributed access point with attachment to the switch through the intermediate network. Value 'wired(3)' indicates a client that is directly attached to the switch (no access point is involved)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ap", 1), ("dap", 2), ("wired", 3))

class TrpzApAttachType(TextualConvention, Integer32):
    description = 'Type of AP attachment to AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("directAttach", 1), ("networkAttach", 2))

class TrpzApPortOrDapNum(TextualConvention, Unsigned32):
    description = 'AP Port, for directly attached APs, otherwise DAP Number (arbitrary number assigned when configuring the DAP on the AC). A zero value means unknown. Obsoleted by TrpzApNum. (In 6.0, direct- and network-attached APs were unified.)'
    status = 'obsolete'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class TrpzApNum(TextualConvention, Unsigned32):
    description = 'AP Number: arbitrary number assigned when configuring the AP on the AC. It is unique (on same AC), regardless of the type of AP attachment. A zero value means unknown.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9999)

class TrpzApState(TextualConvention, Integer32):
    description = 'AP State, as seen by the AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 10, 20))
    namedValues = NamedValues(("cleared", 1), ("init", 2), ("bootStarted", 3), ("imageDownloaded", 4), ("connectFailed", 5), ("configuring", 6), ("operational", 7), ("redundant", 10), ("connOutage", 20))

class TrpzApTransition(TextualConvention, Integer32):
    description = "AP state Transition, as seen by the AC. Usually reported via 'trpzApNonOperStatusTrap'. Transition to operational state is reported by 'trpzApOperRadioStatusTrap' (multiple PDUs may be sent, one for each radio of that AP). Another transition to operational state is 'connRestored(21)', which may not be followed by 'trpzApOperRadioStatusTrap' unless radio status also changed."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 10, 11, 20, 21, 22))
    namedValues = NamedValues(("clear", 1), ("timeout", 2), ("reset", 3), ("bootSuccess", 4), ("startConfiguring", 5), ("connectFail", 6), ("setBackupConn", 10), ("startHandoverReconfiguring", 11), ("connLost", 20), ("connRestored", 21), ("connOutageExtendedTimeout", 22))

class TrpzApFailDetail(TextualConvention, Integer32):
    description = "Detailed failure codes for some of the transitions specified in 'TrpzApTransition'. - 'normalTransition' (91) means the corresponding transition is not a failure; it is a transition towards operational state or it is an internally required transition (for example, a major configuration change occurred, like cluster being enabled). - 'adminRequest' (92) means the corresponding transition is not a failure, it was caused by an administrative request; for example, AP was cleared (removed from the switch configuration). - 'failUnknown' (99) means there are no details available; the transition may be normal or undesirable/unexpected."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 11, 12, 91, 92, 99))
    namedValues = NamedValues(("secureHandshakeFailure", 2), ("fingerprintRequired", 3), ("fingerprintMismatch", 4), ("portLinkUp", 11), ("portLinkDown", 12), ("normalTransition", 91), ("adminRequest", 92), ("failUnknown", 99))

class TrpzApConnectSecurityType(TextualConvention, Integer32):
    description = 'Security level of the connection between AP and AC: secure(1) - fingerprint matching; insecure(2) - fingerprint not configured, or optional and not matching; auto(3) - Auto-DAP is intrinsically insecure: could not check fingerprint since no specific DAP is configured.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("secure", 1), ("insecure", 2), ("auto", 3))

class TrpzApServiceAvailability(TextualConvention, Integer32):
    description = 'Level of wireless service availability.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fullService", 1), ("noService", 2), ("degradedService", 3))

class TrpzApBias(TextualConvention, Integer32):
    description = 'Bias of AP attachment to this AC. Setting an APs bias on an AC switch to high causes the switch to be preferred over switches with low bias, for booting and managing the AP. Bias applies only to AC switches that are indirectly attached to the AP through an intermediate Layer 2 or Layer 3 network. An AP always attempts to boot on AP port 1 first, and if an AC switch is directly attached on AP port 1, the AP boots from it regardless of the bias settings.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("high", 1), ("low", 2), ("sticky", 3))

class TrpzApSerialNum(TextualConvention, OctetString):
    description = 'The value is a zero length string if unknown or unavailable. Otherwise the value is a serial number, which consists of printable ASCII characters between 0x21 (!), and 0x7d (}) with no leading, embedded, or trailing space.'
    status = 'current'
    displayHint = '255a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TrpzApFingerprint(TextualConvention, OctetString):
    description = 'Represents a RSA key fingerprint (binary value), which is the MD5 hash of the public key of the RSA key pair. Or a zero length string if not known or unavailable.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class TrpzRadioNum(TextualConvention, Integer32):
    description = 'Enumeration for multi-radio APs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("radio-1", 1), ("radio-2", 2), ("not-applicable", 3))

class TrpzApRadioIndex(TextualConvention, Unsigned32):
    description = 'A unique value, greater than zero, for each Radio on the AP. Intended to replace TrpzRadioNum.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class TrpzApRadioIndexOrZero(TextualConvention, Unsigned32):
    description = "This textual convention is an extension of the TrpzApRadioIndex convention. The latter defines a greater than zero value used to identify each Radio on the AP. This extension permits the additional value of zero. A zero value means 'none', 'unknown radio' or 'not applicable'. Each object using this textual convention should document the meaning of Radio Index zero."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
class TrpzPowerLevel(TextualConvention, Unsigned32):
    description = 'The current level of transmit power expressed in dbm.'
    status = 'current'
    displayHint = 'd'

class TrpzRadioPowerChangeType(TextualConvention, Integer32):
    description = 'Enumerations for why the power level was changed, which occurs due to auto-tune operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("dup-pkts-threshold-exceed", 1), ("retransmit-threshold-exceed", 2), ("clients-optimal-performance-reached", 3), ("def-power-threshold-exceed", 4))

class TrpzChannelChangeType(TextualConvention, Integer32):
    description = 'Enumerations for why the channel was changed, which occurs due to auto-tune operation'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("util-index", 1), ("rexmit-pkt-offset", 2), ("noise-offset", 3), ("noise", 4), ("utilization", 5), ("phy-error-offset", 6), ("crc-errors-offset", 7), ("radar-detected", 8))

class TrpzChannelNum(TextualConvention, Unsigned32):
    description = 'Channel Number'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class TrpzRadioEnable(TextualConvention, Integer32):
    description = 'Radio mode (administratively enabled or disabled). Obsoleted by TrpzRadioMode.'
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class TrpzRadioMode(TextualConvention, Integer32):
    description = 'Configured mode of an AP radio. There are three administratively controlled values: - enabled: radio may provide service to clients; - sentry: radio will not provide service, but can be used for RF scanning and can run countermeasures; - disabled: radio will not emit at all (thus cannot run countermeasures), can only be used for RF scanning. Obsoletes TrpzRadioEnable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("sentry", 3))

class TrpzRadioConfigState(TextualConvention, Integer32):
    description = 'Radio Configuration State, as seen by the AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("configInit", 1), ("configFail", 2), ("configOk", 3))

class TrpzRadioRate(TextualConvention, Unsigned32):
    description = 'The possible transmission rates of an AP radio. Both a and b/g rates are covered; a specific radio will report the applicable transmission rates (either a or b/g). Here are the possible rates, in Mbps: - 802.11g radios: 54, 48, 36, 24, 18, 12, 11, 9, 6, 5.5, 2, or 1; - 802.11b radios: 11, 5.5, 2, or 1; - 802.11a radios: 54, 48, 36, 24, 18, 12, 9, or 6. The value in MIB is specified as the rate in Mbps times 10, in order to have only integer values, zero meaning unknown rate.'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 540), )
class TrpzRadioRateEx(TextualConvention, Integer32):
    description = 'Radio Rates Extended (covering 11n MCS rates): The possible transmission rates of an AP radio. 11a, 11b/g, 11na and 11ng rates are included; a specific radio will report the applicable transmission rates (either a, b/g, na, ng). Here are the possible rates, in Mbps: - 802.11g radios: 54, 48, 36, 24, 18, 12, 11, 9, 6, 5.5, 2, or 1; - 802.11b radios: 11, 5.5, 2, or 1; - 802.11a radios: 54, 48, 36, 24, 18, 12, 9, or 6; - 802.11ng radios: MCS0-MCS15 and all 11g rates; - 802.11na radios: MCS0-MCS15 and all 11a rates.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43))
    namedValues = NamedValues(("rateUnknown", 1), ("rate1", 2), ("rate2", 3), ("rate5-5", 4), ("rate6", 5), ("rate9", 6), ("rate11", 7), ("rate12", 8), ("rate18", 9), ("rate24", 10), ("rate36", 11), ("rate48", 12), ("rate54", 13), ("rateMCS0", 20), ("rateMCS1", 21), ("rateMCS2", 22), ("rateMCS3", 23), ("rateMCS4", 24), ("rateMCS5", 25), ("rateMCS6", 26), ("rateMCS7", 27), ("rateMCS8", 28), ("rateMCS9", 29), ("rateMCS10", 30), ("rateMCS11", 31), ("rateMCS12", 32), ("rateMCS13", 33), ("rateMCS14", 34), ("rateMCS15", 35), ("rateMCS16", 36), ("rateMCS17", 37), ("rateMCS18", 38), ("rateMCS19", 39), ("rateMCS20", 40), ("rateMCS21", 41), ("rateMCS22", 42), ("rateMCS23", 43))

class TrpzRadioType(TextualConvention, Integer32):
    description = 'Enumeration to indicate the Radio Type, as seen by AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("typeUnknown", 1), ("typeA", 2), ("typeB", 3), ("typeG", 4), ("typeNA", 5), ("typeNG", 6))

class TrpzRssi(TextualConvention, Integer32):
    description = 'RSSI (Received Signal Strength Indicator) for last packet received, in decibels referred to 1 milliwatt (dBm). A higher value indicates a stronger signal.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-100, 0)

class TrpzApWasOperational(TextualConvention, Integer32):
    description = 'Enumeration to indicate whether the AP was operational before a transition occurred. Normally used in notifications.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oper", 1), ("nonOper", 2))

class TrpzRadioChannelWidth(TextualConvention, Integer32):
    description = 'Enumeration to indicate the administratively controlled Radio Channel Width.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("channelWidth20MHz", 1), ("channelWidth40MHz", 2))

class TrpzRadioMimoState(TextualConvention, Integer32):
    description = 'Enumeration to indicate the MIMO state of the Radio (Multiple Input Multiple Output), as seen by the AC. This depends on radio type and power supplied to the radio. mimo1x1: radio uses one transmit chain and one receive chain; mimo2x3: radio uses two transmit chains and three receive chains; mimo3x3: radio uses three transmit chains and three receive chains.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mimoOther", 1), ("mimo1x1", 2), ("mimo2x3", 3), ("mimo3x3", 4))

class TrpzApPowerMode(TextualConvention, Integer32):
    description = 'Enumerations of the modes in which power is supplied by the AP to its components (mainly radios). There are two administratively controlled values: - auto: the power is managed automatically by sensing the power level on the AP; - high: all radios operate at the maximum power available.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("auto", 1), ("high", 2))

class TrpzApLedMode(TextualConvention, Integer32):
    description = 'Enumeration to indicate the administratively controlled LED mode for an AP.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("auto", 1), ("static", 2), ("off", 3))

class TrpzRadioAntennaLocation(TextualConvention, Integer32):
    description = 'Enumeration to indicate the administratively controlled Radio Antenna Location.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("indoors", 1), ("outdoors", 2))

class TrpzCryptoType(TextualConvention, Integer32):
    description = 'Enumeration of Crypto Types: - clear: Cleartext (unencrypted communication); - wep: Wired Equivalent Privacy; - wep40: WEP with 40-bit keys; - wep104: WEP with 104-bit keys; - tkip: Temporal Key Integrity Protocol; - aesCcmp: Advanced Encryption Standard, Counter mode with CBC MAC Protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("other", 1), ("clear", 2), ("wep", 3), ("wep40", 4), ("wep104", 5), ("tkip", 6), ("aesCcmp", 7), ("sms4", 8))

mibBuilder.exportSymbols("TRAPEZE-NETWORKS-AP-TC", TrpzRadioMimoState=TrpzRadioMimoState, TrpzRadioRate=TrpzRadioRate, TrpzRadioType=TrpzRadioType, TrpzRadioEnable=TrpzRadioEnable, TrpzRadioPowerChangeType=TrpzRadioPowerChangeType, TrpzApBias=TrpzApBias, PYSNMP_MODULE_ID=trpzApTc, trpzApTc=trpzApTc, TrpzRadioMode=TrpzRadioMode, TrpzApNum=TrpzApNum, TrpzApConnectSecurityType=TrpzApConnectSecurityType, TrpzApServiceAvailability=TrpzApServiceAvailability, TrpzApFailDetail=TrpzApFailDetail, TrpzRssi=TrpzRssi, TrpzApTransition=TrpzApTransition, TrpzApAttachType=TrpzApAttachType, TrpzCryptoType=TrpzCryptoType, TrpzApSerialNum=TrpzApSerialNum, TrpzRadioNum=TrpzRadioNum, TrpzRadioRateEx=TrpzRadioRateEx, TrpzApPowerMode=TrpzApPowerMode, TrpzAccessType=TrpzAccessType, TrpzPowerLevel=TrpzPowerLevel, TrpzRadioAntennaLocation=TrpzRadioAntennaLocation, TrpzApFingerprint=TrpzApFingerprint, TrpzApLedMode=TrpzApLedMode, TrpzChannelNum=TrpzChannelNum, TrpzApWasOperational=TrpzApWasOperational, TrpzRadioConfigState=TrpzRadioConfigState, TrpzApState=TrpzApState, TrpzApRadioIndex=TrpzApRadioIndex, TrpzRadioChannelWidth=TrpzRadioChannelWidth, TrpzApPortOrDapNum=TrpzApPortOrDapNum, TrpzApRadioIndexOrZero=TrpzApRadioIndexOrZero, TrpzChannelChangeType=TrpzChannelChangeType)
