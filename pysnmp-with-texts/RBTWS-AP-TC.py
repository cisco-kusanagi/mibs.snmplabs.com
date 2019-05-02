#
# PySNMP MIB module RBTWS-AP-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RBTWS-AP-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:53:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint")
rbtwsMibs, = mibBuilder.importSymbols("RBTWS-ROOT-MIB", "rbtwsMibs")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Unsigned32, ModuleIdentity, Counter32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, MibIdentifier, Bits, TimeTicks, Integer32, Counter64, iso, NotificationType, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Unsigned32", "ModuleIdentity", "Counter32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "MibIdentifier", "Bits", "TimeTicks", "Integer32", "Counter64", "iso", "NotificationType", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
rbtwsApTc = ModuleIdentity((1, 3, 6, 1, 4, 1, 52, 4, 15, 1, 4, 3))
rbtwsApTc.setRevisions(('2008-05-07 00:41', '2008-02-14 00:32', '2007-12-03 00:30', '2007-07-06 00:23', '2007-07-05 00:22', '2006-07-10 00:15', '2006-03-30 00:14',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: rbtwsApTc.setRevisionsDescriptions(('v1.3.1: Introduced RbtwsCryptoType (for 7.0 release)', 'v1.2.2: In order to support 802.11n, added radio types NA, NG and introduced RbtwsRadioChannelWidth, RbtwsRadioMimoState (for 7.0 release)', 'v1.2.0: Obsoleted RbtwsRadioEnable and RbtwsApPortOrDapNum (previously deprecated). This will be published in 7.0 release.', "v1.1.3: Introduced RbtwsRadioMode in order to replace RbtwsRadioEnable (in 6.2, a new administrative mode 'sentry' was added)", 'v1.1.2: Introduced RbtwsApNum in order to replace RbtwsApPortOrDapNum. (In 6.0, direct- and network-attached APs were unified.)', 'v1.0.1: Disallow illegal RbtwsRadioRate values 1..9 while keeping zero (that means unknown rate)', 'v1.0: Initial version, for 4.1 release',))
if mibBuilder.loadTexts: rbtwsApTc.setLastUpdated('200805081148Z')
if mibBuilder.loadTexts: rbtwsApTc.setOrganization('Enterasys Networks')
if mibBuilder.loadTexts: rbtwsApTc.setContactInfo('www.enterasys.com')
if mibBuilder.loadTexts: rbtwsApTc.setDescription("Textual Conventions used by Enterasys Networks wireless switches. AP = Access Point; AC = Access Controller (wireless switch), the device that runs a SNMP Agent using these TCs. Copyright 2008 Enterasys Networks, Inc. All rights reserved. This SNMP Management Information Base Specification (Specification) embodies confidential and proprietary intellectual property. This Specification is supplied 'AS IS' and Enterasys Networks makes no warranty, either express or implied, as to the use, operation, condition, or performance of the Specification.")
class RbtwsAccessType(TextualConvention, Integer32):
    description = "Describes the access type used by client or an AP. Value 'ap(1)' indicates access point that is directly attached to the switch. Value 'dap(2)' indicates distributed access point with attachment to the switch through the intermediate network. Value 'wired(3)' indicates a client that is directly attached to the switch (no access point is involved)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ap", 1), ("dap", 2), ("wired", 3))

class RbtwsApAttachType(TextualConvention, Integer32):
    description = 'Type of AP attachment to AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("directAttach", 1), ("networkAttach", 2))

class RbtwsApPortOrDapNum(TextualConvention, Unsigned32):
    description = 'AP Port, for directly attached APs, otherwise DAP Number (arbitrary number assigned when configuring the DAP on the AC). A zero value means unknown. Obsoleted by RbtwsApNum. (In 6.0, direct- and network-attached APs were unified.)'
    status = 'obsolete'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 1000)

class RbtwsApNum(TextualConvention, Unsigned32):
    description = 'AP Number: arbitrary number assigned when configuring the AP on the AC. It is unique (on same AC), regardless of the type of AP attachment. A zero value means unknown.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 9999)

class RbtwsApState(TextualConvention, Integer32):
    description = 'AP State, as seen by the AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("cleared", 1), ("init", 2), ("bootStarted", 3), ("imageDownloaded", 4), ("connectFailed", 5), ("configuring", 6), ("configured", 7))

class RbtwsApTransition(TextualConvention, Integer32):
    description = 'AP state Transition, as seen by the AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("clear", 1), ("timeout", 2), ("reset", 3), ("bootSuccess", 4), ("startConfiguring", 5), ("connectFail", 6))

class RbtwsApFailDetail(TextualConvention, Integer32):
    description = "Detailed failure codes for some of the transitions specified in 'RbtwsApTransition'. - 'normalTransition' (91) means the corresponding transition is not a failure; could be caused by an explicit request (for example, AP was cleared) or it is a transition towards operational state. - 'failUnknown' (99) means there are no details available; the transition may be normal or undesirable/unexpected."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(2, 3, 4, 11, 12, 91, 99))
    namedValues = NamedValues(("secureHandshakeFailure", 2), ("fingerprintRequired", 3), ("fingerprintMismatch", 4), ("portLinkUp", 11), ("portLinkDown", 12), ("normalTransition", 91), ("failUnknown", 99))

class RbtwsApConnectSecurityType(TextualConvention, Integer32):
    description = 'Security level of the connection between AP and AC: secure(1) - fingerprint matching; insecure(2) - fingerprint not configured, or optional and not matching; auto(3) - Auto-DAP is intrinsically insecure: could not check fingerprint since no specific DAP is configured.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("secure", 1), ("insecure", 2), ("auto", 3))

class RbtwsApServiceAvailability(TextualConvention, Integer32):
    description = 'Level of wireless service availability.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("fullService", 1), ("noService", 2), ("degradedService", 3))

class RbtwsApBias(TextualConvention, Integer32):
    description = 'Bias of AP attachment to this AC. Setting an APs bias on an AC switch to high causes the switch to be preferred over switches with low bias, for booting and managing the AP. Bias applies only to AC switches that are indirectly attached to the AP through an intermediate Layer 2 or Layer 3 network. An AP always attempts to boot on AP port 1 first, and if an AC switch is directly attached on AP port 1, the AP boots from it regardless of the bias settings.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("high", 1), ("low", 2))

class RbtwsApSerialNum(TextualConvention, OctetString):
    description = 'The value is a zero length string if unknown or unavailable. Otherwise the value is a serial number, which consists of printable ASCII characters between 0x21 (!), and 0x7d (}) with no leading, embedded, or trailing space.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class RbtwsApFingerprint(TextualConvention, OctetString):
    description = 'Represents a RSA key fingerprint (binary value), which is the MD5 hash of the public key of the RSA key pair. Or a zero length string if not known or unavailable.'
    status = 'current'
    displayHint = '2x:'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(16, 16), )
class RbtwsRadioNum(TextualConvention, Integer32):
    description = 'Enumeration for multi-radio APs.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("radio-1", 1), ("radio-2", 2), ("not-applicable", 3))

class RbtwsPowerLevel(TextualConvention, Unsigned32):
    description = 'The current level of transmit power expressed in dbm.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 18)

class RbtwsRadioPowerChangeType(TextualConvention, Integer32):
    description = 'Enumerations for why the power level was changed, which occurs due to auto-tune operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("dup-pkts-threshold-exceed", 1), ("retransmit-threshold-exceed", 2), ("clients-optimal-performance-reached", 3), ("def-power-threshold-exceed", 4))

class RbtwsChannelChangeType(TextualConvention, Integer32):
    description = 'Enumerations for why the channel was changed, which occurs due to auto-tune operation'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("util-index", 1), ("rexmit-pkt-offset", 2), ("noise-offset", 3), ("noise", 4), ("utilization", 5), ("phy-error-offset", 6), ("crc-errors-offset", 7), ("radar-detected", 8))

class RbtwsChannelNum(TextualConvention, Unsigned32):
    description = 'Channel Number'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 1024)

class RbtwsRadioEnable(TextualConvention, Integer32):
    description = 'Radio mode (administratively enabled or disabled). Obsoleted by RbtwsRadioMode.'
    status = 'obsolete'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2))

class RbtwsRadioMode(TextualConvention, Integer32):
    description = 'Configured mode of an AP radio. There are three administratively controlled values: - enabled: radio may provide service to clients; - sentry: radio will not provide service, but can be used for RF scanning and can run countermeasures; - disabled: radio will not emit at all (thus cannot run countermeasures), can only be used for RF scanning. Obsoletes RbtwsRadioEnable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("enabled", 1), ("disabled", 2), ("sentry", 3))

class RbtwsRadioConfigState(TextualConvention, Integer32):
    description = 'Radio Configuration State, as seen by the AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("configInit", 1), ("configFail", 2), ("configOk", 3))

class RbtwsRadioRate(TextualConvention, Unsigned32):
    description = 'The possible transmission rates of an AP radio. Both a and b/g rates are covered; a specific radio will report the applicable transmission rates (either a or b/g). Here are the possible rates, in Mbps: - 802.11g radios: 54, 48, 36, 24, 18, 12, 11, 9, 6, 5.5, 2, or 1; - 802.11b radios: 11, 5.5, 2, or 1; - 802.11a radios: 54, 48, 36, 24, 18, 12, 9, or 6. The value in MIB is specified as the rate in Mbps times 10, in order to have only integer values, zero meaning unknown rate.'
    status = 'current'
    displayHint = 'd-1'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(10, 540), )
class RbtwsRadioType(TextualConvention, Integer32):
    description = 'Enumeration to indicate the Radio Type, as seen by AC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("typeUnknown", 1), ("typeA", 2), ("typeB", 3), ("typeG", 4), ("typeNA", 5), ("typeNG", 6))

class RbtwsRssi(TextualConvention, Integer32):
    description = 'RSSI (Received Signal Strength Indicator) for last packet received, in decibels referred to 1 milliwatt (dBm). A higher value indicates a stronger signal.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(-100, 0)

class RbtwsApWasOperational(TextualConvention, Integer32):
    description = 'Enumeration to indicate whether the AP was operational before a transition occured. Normally used in notifications.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oper", 1), ("nonOper", 2))

class RbtwsRadioChannelWidth(TextualConvention, Integer32):
    description = 'Enumeration to indicate the administratively controlled Radio Channel Width.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("channelWidth20MHz", 1), ("channelWidth40MHz", 2))

class RbtwsRadioMimoState(TextualConvention, Integer32):
    description = 'Enumeration to indicate the MIMO state of the Radio (Multiple Input Multiple Output), as seen by the AC. This depends on radio type and power supplied to the radio. mimo1x1: radio uses one transmit chain and one receive chain; mimo2x3: radio uses two transmit chains and three receive chains; mimo3x3: radio uses three transmit chains and three receive chains.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("mimoOther", 1), ("mimo1x1", 2), ("mimo2x3", 3), ("mimo3x3", 4))

class RbtwsCryptoType(TextualConvention, Integer32):
    description = 'Enumeration of Crypto Types: - clear: Cleartext (unencrypted communication); - wep: Wired Equivalent Privacy; - wep40: WEP with 40-bit keys; - wep104: WEP with 104-bit keys; - tkip: Temporal Key Integrity Protocol; - aesCcmp: Advanced Encryption Standard, Counter mode with CBC MAC Protocol.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("clear", 2), ("wep", 3), ("wep40", 4), ("wep104", 5), ("tkip", 6), ("aesCcmp", 7))

mibBuilder.exportSymbols("RBTWS-AP-TC", RbtwsRadioConfigState=RbtwsRadioConfigState, RbtwsApAttachType=RbtwsApAttachType, RbtwsApNum=RbtwsApNum, RbtwsApBias=RbtwsApBias, RbtwsRadioEnable=RbtwsRadioEnable, RbtwsApState=RbtwsApState, RbtwsRadioPowerChangeType=RbtwsRadioPowerChangeType, RbtwsApFailDetail=RbtwsApFailDetail, RbtwsPowerLevel=RbtwsPowerLevel, RbtwsRadioChannelWidth=RbtwsRadioChannelWidth, RbtwsChannelNum=RbtwsChannelNum, RbtwsApFingerprint=RbtwsApFingerprint, PYSNMP_MODULE_ID=rbtwsApTc, RbtwsApConnectSecurityType=RbtwsApConnectSecurityType, RbtwsRadioRate=RbtwsRadioRate, RbtwsApServiceAvailability=RbtwsApServiceAvailability, RbtwsRadioNum=RbtwsRadioNum, RbtwsApWasOperational=RbtwsApWasOperational, RbtwsRssi=RbtwsRssi, RbtwsRadioType=RbtwsRadioType, RbtwsAccessType=RbtwsAccessType, RbtwsCryptoType=RbtwsCryptoType, RbtwsApSerialNum=RbtwsApSerialNum, RbtwsApPortOrDapNum=RbtwsApPortOrDapNum, RbtwsApTransition=RbtwsApTransition, RbtwsRadioMimoState=RbtwsRadioMimoState, RbtwsRadioMode=RbtwsRadioMode, RbtwsChannelChangeType=RbtwsChannelChangeType, rbtwsApTc=rbtwsApTc)
