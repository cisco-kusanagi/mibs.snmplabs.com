#
# PySNMP MIB module MEF-SOAM-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MEF-SOAM-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:11:07 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsUnion, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsUnion", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
IpAddress, Integer32, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, enterprises, Unsigned32, ModuleIdentity, Counter64, NotificationType, MibIdentifier, Bits, TimeTicks, iso, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Integer32", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "enterprises", "Unsigned32", "ModuleIdentity", "Counter64", "NotificationType", "MibIdentifier", "Bits", "TimeTicks", "iso", "Counter32", "ObjectIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mefSoamTcMib = ModuleIdentity((1, 3, 6, 1, 4, 1, 15007, 1, 1))
mefSoamTcMib.setRevisions(('2012-01-10 00:00', '2010-10-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mefSoamTcMib.setRevisionsDescriptions(('Updated text to add textual conventions for the SOAM PM MIB.', 'Initial Version.',))
if mibBuilder.loadTexts: mefSoamTcMib.setLastUpdated('201201100000Z')
if mibBuilder.loadTexts: mefSoamTcMib.setOrganization('Metro Ethernet Forum')
if mibBuilder.loadTexts: mefSoamTcMib.setContactInfo('Web URL: http://metroethernetforum.org/ E-mail: mibs@metroethernetforum.org Postal: Metro Ethernet Forum 6033 W. Century Boulevard, Suite 830 Los Angeles, CA 90045 U.S.A. Phone: +1 310-642-2800 Fax: +1 310-642-2808')
if mibBuilder.loadTexts: mefSoamTcMib.setDescription('This MIB module defines the textual conventions used throughout the Ethernet Services Operations, Administration and Maintenance MIB modules. Copyright 2010 Metro Ethernet Forum. All rights reserved.')
class MefSoamTcAvailabilityType(TextualConvention, Integer32):
    description = 'This enumeration data type defines the availability of a session, measured by a loss measurement session. The valid enumerated values associated with this type are: available(1) indicates the MEP is available. unavailable(2) indicates the MEP is unavailable. unknown(3) indicates the availability is not known, for instance because insufficient time has passed to make an availability calculation, the time has been excluded because of a maintenance interval, or because availability measurement is not enabled. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("available", 1), ("unavailable", 2), ("unknown", 3))

class MefSoamTcConnectivityStatusType(TextualConvention, Integer32):
    reference = '[MEF17] 9.2 and [MEF7.1] III.2 Enumeration'
    description = 'This enumeration data type defines the connectivity status of a Maintenance Entity (ME) or a Maintenance Entity Group (MEG). The valid enumerated values associated with this type are: inactive(1) indicates an inactive connectivity state of a group and refers to the inability to exchange SOAM PDU frame among any of the entities in a group. active(2) indicates an active connectivity state of a group and refers to the ability to exchange SOAM PDU frames among all the entities in a group partiallyActive(3) indicates a partially active connectivity state of a group and refers to the ability to exchange SOAM PDU frames among some entities of a group. This enumerated value is only applicable for Multipoint-to-Multipoint MEG. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("inactive", 1), ("active", 2), ("partiallyActive", 3))

class MefSoamTcDataPatternType(TextualConvention, Integer32):
    description = 'This enumeration data type indicates the type of data pattern to be sent in an OAM PDU Data TLV. The valid enumerated values associated with this type are: zeroPattern(1) indicates the Data TLV contains all zeros onesPattern(2) indicates the Data TLV contains all ones '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("zeroPattern", 1), ("onesPattern", 2))

class MefSoamTcDelayMeasurementBinType(TextualConvention, Integer32):
    description = 'This enumeration data type is used to distinguish between measurement bins for Frame Delay, Frame Delay Range, and Inter-frame Delay variation. The valid enumerated values associated with this type are: twoWayFrameDelay(1) indicates a measurement bin for two-way Frame Delay. forwardFrameDelay(2) indicates a measurement bin for one-way Frame Delay in the forward direction. backwardFrameDelay(3) indicates a measurement bin for one-way Frame Delay in the backward direction. twoWayIfdv(4) indicates a measurement bin for two-way Inter-frame Delay Variation. forwardIfdv(5) indicates a measurement bin for one-way Inter-frame Delay Variation in the forward direction. backwardIfdv(6) indicates a measurement bin for one-way Inter-frame Delay Variation in the backward direction. twoWayFrameDelayRange(7) indicates a measurement bin for two-way Frame Delay Range. forwardFrameDelayRange(8) indicates a measurement bin for one-way Frame Delay Range in the forward direction. backwardFrameDelayRange(9) indicates a measurement bin for one-way Frame Delay Range in the backward direction. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9))
    namedValues = NamedValues(("twoWayFrameDelay", 1), ("forwardFrameDelay", 2), ("backwardFrameDelay", 3), ("twoWayIfdv", 4), ("forwardIfdv", 5), ("backwardIfdv", 6), ("twoWayFrameDelayRange", 7), ("forwardFrameDelayRange", 8), ("backwardFrameDelayRange", 9))

class MefSoamTcIntervalTypeAisLck(TextualConvention, Integer32):
    reference = '[MEF7.1] III.2 Enumeration, [Y.1731] 7.4, 7.6'
    description = 'This enumeration data type defines the AIS/LCK transmission time interval for an Alarm Indication Signal (AIS) or LCK frame. The valid enumerated values associated with this type are: oneSecond(1) indicates a one second transmission interval. oneMinute(2) indicates a one minute transmission interval. '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("oneSecond", 1), ("oneMinute", 2))

class MefSoamTcMeasurementPeriodType(TextualConvention, Unsigned32):
    reference = '[MEF SOAM-PM] R56'
    description = 'Indicates the transmission time between the SOAM PM frames for a PM session, in ms. '
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(3, 3600000)

class MefSoamTcMegIdType(TextualConvention, Integer32):
    reference = '[Y.1731] Table A-1, [CFM] 17.5, 21.6.5.1'
    description = 'This enumeration data type indicates the format of the MEG ID that is sent in the OAM PDUs. Types 1-4 are more fully explained in [CFM] 17.5. Type 32 is from [Y.1731] Annex A. The valid enumerated values associated with this type are: primaryVid(1) Primary VLAN ID. 12 bits represented in a 2-octet integer: - 4 least significant bits of the first byte contains the 4 most significant bits of the 12 bits primary VID - second byte contains the 8 least significant bits of the primary VID 0 1 2 3 4 5 6 7 8 +-+-+-+-+-+-+-+-+ |0 0 0 0| (MSB) | +-+-+-+-+-+-+-+-+ | VID LSB | +-+-+-+-+-+-+-+-+ charString(2) RFC2579 DisplayString, except that the character codes 0-31 (decimal) are not used. (1..45) octets unsignedInt16 (3) 2-octet integer/big endian rfc2865VpnId(4) RFC 2685 VPN ID 3 octet VPN authority Organizationally Unique Identifier followed by 4 octet VPN index identifying VPN according to the OUI: 0 1 2 3 4 5 6 7 8 +-+-+-+-+-+-+-+-+ | VPN OUI (MSB) | +-+-+-+-+-+-+-+-+ | VPN OUI | +-+-+-+-+-+-+-+-+ | VPN OUI (LSB) | +-+-+-+-+-+-+-+-+ |VPN Index (MSB)| +-+-+-+-+-+-+-+-+ | VPN Index | +-+-+-+-+-+-+-+-+ | VPN Index | +-+-+-+-+-+-+-+-+ |VPN Index (LSB)| +-+-+-+-+-+-+-+-+ iccBased (32) ICC-based MEG ID Format, thirteen octet field '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 32))
    namedValues = NamedValues(("primaryVid", 1), ("charString", 2), ("unsignedInt16", 3), ("rfc2865VpnId", 4), ("iccBased", 32))

class MefSoamTcOperationTimeType(TextualConvention, Integer32):
    reference = '[SOAM-PM] R2, [SOAM-FM] 8.7'
    description = 'This enumeration data type indicates the operation type start or end time to indicate when an OAM operation is initiated or stopped. The valid enumerated values associated with this type are: none(1) The operation is never started or is stopped immediately if used to indicate a start time, or the operation never ends if it is used to indicate an end time immediate(2) The operation is to begin immediately relative(3) The operation is to begin at a relative time from the current time or stop a relative time after it has started fixed(4) The operation is to begin/stop at the given UTC time/date '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("none", 1), ("immediate", 2), ("relative", 3), ("fixed", 4))

class MefSoamTcSessionType(TextualConvention, Integer32):
    description = 'This enumeration data type defines the status of PM session of a MEP. The valid enumerated values associated with this type are: proactive(1) indicates the measurement instance is Proactive onDemand(2) indicates the measurement instance is On-demand '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("proactive", 1), ("onDemand", 2))

class MefSoamTcStatusType(TextualConvention, Integer32):
    description = 'This enumeration data type defines the status of PM session of a MEP. The valid enumerated values associated with this type are: active(1) indicates the measurement instance is active notActive(2) indicates the measurement instance is not active '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("active", 1), ("notActive", 2))

class MefSoamTcTestPatternType(TextualConvention, Integer32):
    reference = '[MEF7.1], Appendix III.2 Enumeration, [Y.1731] 7.7'
    description = 'This enumeration data type indicates the type of test pattern to be sent in an OAM PDU Test TLV. The valid enumerated values associated with this type are: null(1) Null signal without CRC-32 nullCrc32(2) Null signal with CRC-32 prbs(3) PRBS 2^31-1 without CRC-32 prbsCrc32(4) PRBS 2^31-1 with CRC-32 '
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("null", 1), ("nullCrc32", 2), ("prbs", 3), ("prbsCrc32", 4))

mibBuilder.exportSymbols("MEF-SOAM-TC-MIB", PYSNMP_MODULE_ID=mefSoamTcMib, MefSoamTcMegIdType=MefSoamTcMegIdType, MefSoamTcDataPatternType=MefSoamTcDataPatternType, MefSoamTcTestPatternType=MefSoamTcTestPatternType, MefSoamTcIntervalTypeAisLck=MefSoamTcIntervalTypeAisLck, MefSoamTcStatusType=MefSoamTcStatusType, MefSoamTcSessionType=MefSoamTcSessionType, MefSoamTcDelayMeasurementBinType=MefSoamTcDelayMeasurementBinType, MefSoamTcMeasurementPeriodType=MefSoamTcMeasurementPeriodType, MefSoamTcAvailabilityType=MefSoamTcAvailabilityType, MefSoamTcOperationTimeType=MefSoamTcOperationTimeType, MefSoamTcConnectivityStatusType=MefSoamTcConnectivityStatusType, mefSoamTcMib=mefSoamTcMib)
