#
# PySNMP MIB module BTI7800-EQUIPMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BTI7800-EQUIPMENT-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 17:24:45 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
ObjectIdentity, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity, Unsigned32, Counter32, iso, MibIdentifier, Bits, enterprises, TimeTicks, NotificationType, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity", "Unsigned32", "Counter32", "iso", "MibIdentifier", "Bits", "enterprises", "TimeTicks", "NotificationType", "Integer32", "Counter64")
TruthValue, DateAndTime, DisplayString, TextualConvention, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "TruthValue", "DateAndTime", "DisplayString", "TextualConvention", "RowStatus")
bTI7800_EQUIPMENT_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1)).setLabel("bTI7800-EQUIPMENT-MIB")
bTI7800_EQUIPMENT_MIB.setRevisions(('2012-06-25 00:00',))
if mibBuilder.loadTexts: bTI7800_EQUIPMENT_MIB.setLastUpdated('201206250000Z')
if mibBuilder.loadTexts: bTI7800_EQUIPMENT_MIB.setOrganization('@ORGANIZATION')
class UnsignedByte(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ConfdString(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class Ipv4Prefix(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1d.1d.1d.1d/1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class InetAddressIP(TextualConvention, OctetString):
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class String(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class CurrentDBStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("ready-to-backup", 1), ("backup-inprogress", 2), ("ready-to-restore", 3), ("restore-inprogress", 4), ("restore-success", 5), ("restore-failed", 6), ("ready-to-remove", 8), ("remove-inprogress", 9), ("remove-success", 10), ("remove-failed", 11), ("clear-inprogress", 12), ("clear-success", 13), ("clear-failed", 14))

class BicType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("sfp-bic", 1), ("cfp-bic", 2), ("qsfp-bic", 3), ("qsfp28-bic", 4))

class DolOchIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class ObsoleteName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class UfmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("dual-bic-switching", 0), ("dual-bic-non-switching", 1), ("msa-switching", 2), ("msa-non-switching", 3), ("msa400-10g-client", 4), ("msa400-10g-100g-client", 5))

class AmpModule(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class TransportType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("udp", 1), ("tcp", 2))

class Role(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("btiuser", 0), ("provisioning", 1), ("superuser", 2), ("surveillance", 3))

class DolFconnEndpt1Type(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DolFconnEndpt2Type(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DebugLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("trace", 1), ("debug", 2), ("off", 3))

class FeGroupNum(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class PasswdStr(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class RoadmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("a2-port", 0), ("a9-port", 1), ("a20-port", 2))

class StatisticPointType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228))
    namedValues = NamedValues(("opr", 1), ("opr-min", 2), ("opr-max", 3), ("opr-avg", 4), ("opt", 5), ("opt-min", 6), ("opt-max", 7), ("opt-avg", 8), ("opt-back-ref-power", 9), ("opr-std-avg", 10), ("opt-std-avg", 11), ("opl-rx", 12), ("opl-tx", 13), ("ltemp", 14), ("ltemp-min", 15), ("ltemp-max", 16), ("ltemp-avg", 17), ("lbc", 18), ("lbc-min", 19), ("lbc-max", 20), ("lbc-avg", 21), ("volt", 22), ("volt-min", 23), ("volt-max", 24), ("volt-avg", 25), ("mod-temp", 26), ("mod-temp-min", 27), ("mod-temp-max", 28), ("mod-temp-avg", 29), ("fec-1cr", 30), ("fec-0cr", 31), ("fec-bitcr", 32), ("fec-symcr", 33), ("fec-ucrcw", 34), ("fec-ber", 35), ("fec-ber-min", 36), ("fec-ber-max", 37), ("fec-ber-avg", 38), ("cd", 39), ("cd-min", 40), ("cd-max", 41), ("cd-avg", 42), ("snr", 43), ("snr-min", 44), ("snr-max", 45), ("snr-avg", 46), ("cfo", 47), ("cfo-min", 48), ("cfo-max", 49), ("cfo-avg", 50), ("dgd", 51), ("dgd-min", 52), ("dgd-max", 53), ("dgd-avg", 54), ("otu-eb", 55), ("otu-bbe", 56), ("otu-es", 57), ("otu-ses", 58), ("otu-ofs", 59), ("otu-uas", 60), ("otu-ber", 61), ("otu-ber-min", 62), ("otu-ber-max", 63), ("otu-ber-avg", 64), ("odu-eb", 65), ("odu-bbe", 66), ("odu-es", 67), ("odu-ses", 68), ("odu-uas", 69), ("odu-ber", 70), ("odu-ber-min", 71), ("odu-ber-max", 72), ("odu-ber-avg", 73), ("odu-lat", 74), ("odu-lat-min", 75), ("odu-lat-max", 76), ("odu-lat-avg", 77), ("pcs-ib", 78), ("pcs-ish", 79), ("pcs-es", 80), ("pcs-ses", 81), ("pcs-uas", 82), ("pcs-ber", 83), ("pcs-ber-min", 84), ("pcs-ber-max", 85), ("pcs-ber-avg", 86), ("octs-rx", 87), ("octs-tx", 88), ("octs-ok-rx", 89), ("octs-ok-tx", 90), ("pkts-rx", 91), ("pkts-tx", 92), ("pkts-ok-rx", 93), ("pkts-ok-tx", 94), ("bcast-pkts-rx", 95), ("bcast-pkts-tx", 96), ("mcast-pkts-rx", 97), ("mcast-pkts-tx", 98), ("fcse-pkts-rx", 99), ("fcse-pkts-tx", 100), ("drp-pkts-rx", 101), ("drp-pkts-tx", 102), ("usize-pkts-rx", 103), ("usize-pkts-tx", 104), ("osize-pkts-rx", 105), ("osize-pkts-tx", 106), ("fragments-rx", 107), ("fragments-tx", 108), ("jabbers-rx", 109), ("jabbers-tx", 110), ("pkts-64-oct-rx", 111), ("pkts-64-oct-tx", 112), ("pkts-65-127-oct-rx", 113), ("pkts-65-127-oct-tx", 114), ("pkts-128-255-oct-rx", 115), ("pkts-128-255-oct-tx", 116), ("pkts-256-511-oct-rx", 117), ("pkts-256-511-oct-tx", 118), ("pkts-512-1023-oct-rx", 119), ("pkts-512-1023-oct-tx", 120), ("pkts-1024-1518-oct-rx", 121), ("pkts-1024-1518-oct-tx", 122), ("pkts-over-1518-oct-rx", 123), ("pkts-over-1518-oct-tx", 124), ("pkts-paus-rx", 125), ("pkts-paus-tx", 126), ("cv-s", 127), ("es-s", 128), ("ses-s", 129), ("sefs-s", 130), ("uas-s", 131), ("ber-s", 132), ("ber-min-s", 133), ("ber-max-s", 134), ("ber-avg-s", 135), ("cv-l", 136), ("es-l", 137), ("ses-l", 138), ("uas-l", 139), ("fc-l", 140), ("ber-l", 141), ("ber-min-l", 142), ("ber-max-l", 143), ("ber-avg-l", 144), ("rs-eb", 145), ("rs-bbe", 146), ("rs-es", 147), ("rs-ses", 148), ("rs-ofs", 149), ("rs-uas", 150), ("rs-ber", 151), ("rs-ber-min", 152), ("rs-ber-max", 153), ("rs-ber-avg", 154), ("ms-eb", 155), ("ms-bbe", 156), ("ms-es", 157), ("ms-ses", 158), ("ms-uas", 159), ("ms-ber", 160), ("ms-ber-min", 161), ("ms-ber-max", 162), ("ms-ber-avg", 163), ("cpu-load-avg", 164), ("cpu-load-min", 165), ("cpu-load-max", 166), ("apr", 167), ("apr-min", 168), ("apr-max", 169), ("apr-avg", 170), ("apr-std-avg", 171), ("opl-rx-min", 172), ("opl-rx-max", 173), ("opl-rx-avg", 174), ("opl-tx-min", 175), ("opl-tx-max", 176), ("opl-tx-avg", 177), ("fan-rpm-avg", 178), ("fan-rpm-min", 179), ("fan-rpm-max", 180), ("pem-presence-avg", 181), ("pem-presence-min", 182), ("pem-presence-max", 183), ("osnr", 184), ("osnr-min", 185), ("osnr-max", 186), ("osnr-avg", 187), ("prbs-lsss", 188), ("prbs-be", 189), ("prbs-ber", 190), ("prbs-ber-min", 191), ("prbs-ber-max", 192), ("prbs-ber-avg", 193), ("span-lngth", 194), ("ipv4-ihl-excp", 195), ("ipv4-pkt-len-excp", 196), ("ipv4-rx-ttl0-excp", 197), ("ipv4-sip-eq-dip-excp", 198), ("ipv4-dip0-excp", 199), ("ipv4-sip-mc-excp", 200), ("ipv4-mpls-ttl0-excp", 201), ("ipv4-mpls-ttl1-excp", 202), ("ip-pkts-rx", 203), ("ip-pkts-tx", 204), ("ip-octs-rx", 205), ("ip-octs-tx", 206), ("mpls-pkts-rx", 207), ("mpls-pkts-tx", 208), ("mpls-octs-rx", 209), ("mpls-octs-tx", 210), ("ipv4-hdr-chksum-excp", 211), ("snr-x", 212), ("snr-x-min", 213), ("snr-x-max", 214), ("snr-x-avg", 215), ("snr-y", 216), ("snr-y-min", 217), ("snr-y-max", 218), ("snr-y-avg", 219), ("opt-total", 220), ("opt-total-min", 221), ("opt-total-max", 222), ("opt-total-avg", 223), ("opt-back-ref-ratio", 224), ("opt-back-ref-ratio-min", 225), ("opt-back-ref-ratio-max", 226), ("opt-back-ref-ratio-avg", 227), ("opt-back-ref-ratio-std-avg", 228))

class GroupIdType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class FeDegreeNum(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class MsaName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class PreamplifierName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class AlarmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conditionRaise", 1), ("conditionClear", 2))

class RevertiveTimeType(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(600, 600)

class RemoteUrl(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class Modulereload(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class CurrentStateType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("not-initiated", 1), ("url-set", 2), ("download-inprogress", 3), ("download-success", 4), ("download-failed", 5), ("commit-inprogress", 6), ("commit-success", 7), ("commit-failed", 8), ("cancel-inprogress", 9), ("rollback-inprogress", 10), ("rollback-success", 11), ("rollback-failed", 12))

class BicName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class StatValueType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("counter64", 1), ("decimal64", 2), ("float", 3))

class OscIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class OdccIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class WdmIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class PortIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DolFiberType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ssmf", 1), ("leaf", 2), ("twrs", 3), ("ndsf", 4), ("teralight", 5))

class Files1(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class UpgradeStatusObjectType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("system-upgrade-status", 1), ("module-upgrade-status", 2))

class CustomValType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class GroupConfigType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("noEqlzTerm", 2), ("eqlzTerm", 3), ("noEqlzLine", 4), ("eqlzLine", 5), ("roadm", 6))

class Wavelength(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class ValueUnion(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class Wavelength1(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class TimeOut(TextualConvention, Unsigned32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class SysNameType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class Validity(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notAvailable", 1), ("partial", 2), ("complete", 3))

class MetaCliDebugLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("trace", 1), ("debug", 2), ("info", 3), ("warning", 4), ("error", 5))

class GlobalDebugLevel(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class MacAddr(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class ModuleName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DolSupportingEquipType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("mdeq", 1), ("roadm2", 2), ("roadm9", 3), ("roadm20", 4), ("ila", 5), ("preamp", 6))

class WavelengthProtectionPortIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class SyslogLocalFacility(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("local0", 1), ("local1", 2), ("local2", 3), ("local3", 4), ("local4", 5), ("local5", 6), ("local6", 7), ("local7", 8))

class UpgradeLocation(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class ChassisName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class EqptDegreeType(TextualConvention, Unsigned32):
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4)

class NumSpectSlicesType(TextualConvention, Integer32):
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 384)

class PortGridType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ghz100", 1), ("ghz50", 2), ("flex", 3))

class CustomValType255(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class DolPortIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class WavelengthProtectionGroupIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class RemoteLocation(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class CustomIdType32(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TransceiverName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class ThresholdType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("warningAlert", 1), ("alarmHigh", 2), ("alarmLow", 3))

class ProfileNameType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class PassStr(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class BinLengths(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 15, 1440))
    namedValues = NamedValues(("unTimed", 0), ("a1Minute", 1), ("a15Minute", 15), ("a1Day", 1440))

class Files(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class ChassisType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("a14-Slot", 0), ("a6-Slot", 1), ("a2-Slot", 2), ("a1-Slot", 3))

class EqptConnType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eqDuplex", 1), ("loopback", 2))

class PortDwdmType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("native", 1), ("alien", 2))

class ShmmAutoUpgradeStatus(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class InventoryName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class FePortIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DolOchXconSrcType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DolModule(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DolConnectionType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class ThresholdEntityType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("a10ge", 1), ("a40ge", 2), ("a100ge", 3), ("otu2", 4), ("otu4", 5), ("odu2", 6), ("odu3", 7), ("odu4", 8), ("oc192", 9), ("stm64", 10), ("wanoc192", 11), ("wanstm64", 12), ("osc", 13), ("line", 14), ("client", 15), ("dcm", 16), ("otu2e", 17), ("odu2e", 18), ("och", 19))

class EntityNameType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DolFixedGridChannelName(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class CustomIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class PortType(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("line", 1), ("client", 2), ("dcm", 3), ("chlport", 4), ("expport", 5))

class DolOscIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

class DolOmsIdType(TextualConvention, OctetString):
    status = 'current'
    displayHint = '1t'

chassisTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1), )
if mibBuilder.loadTexts: chassisTable.setStatus('current')
chassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1), ).setIndexNames((1, "BTI7800-EQUIPMENT-MIB", "chassisName"))
if mibBuilder.loadTexts: chassisEntry.setStatus('current')
chassisName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 1), String())
if mibBuilder.loadTexts: chassisName.setStatus('current')
chassisType = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 2), ChassisType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisType.setStatus('current')
chassisPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 3), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisPEC.setStatus('current')
chassisAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisAdminStatus.setStatus('current')
chassisCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisCustom1.setStatus('current')
chassisCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisCustom2.setStatus('current')
chassisCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 7), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisCustom3.setStatus('current')
chassisOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisOperationalStatus.setStatus('current')
chassisLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 9), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisLocation.setStatus('current')
moduleTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2), )
if mibBuilder.loadTexts: moduleTable.setStatus('current')
moduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (1, "BTI7800-EQUIPMENT-MIB", "moduleName"))
if mibBuilder.loadTexts: moduleEntry.setStatus('current')
moduleName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 1), String())
if mibBuilder.loadTexts: moduleName.setStatus('current')
modulePEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: modulePEC.setStatus('current')
moduleAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleAdminStatus.setStatus('current')
moduleCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleCustom1.setStatus('current')
moduleCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleCustom2.setStatus('current')
moduleCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleCustom3.setStatus('current')
moduleOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleOperationalStatus.setStatus('current')
moduleType = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 8), UfmType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleType.setStatus('current')
msaXcvrTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3), )
if mibBuilder.loadTexts: msaXcvrTable.setStatus('current')
msaXcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (0, "BTI7800-EQUIPMENT-MIB", "moduleName"), (1, "BTI7800-EQUIPMENT-MIB", "msaXcvrName"))
if mibBuilder.loadTexts: msaXcvrEntry.setStatus('current')
msaXcvrName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 1), String())
if mibBuilder.loadTexts: msaXcvrName.setStatus('current')
msaXcvrPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrPEC.setStatus('current')
msaXcvrAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrAdminStatus.setStatus('current')
msaXcvrCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrCustom1.setStatus('current')
msaXcvrCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrCustom2.setStatus('current')
msaXcvrCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrCustom3.setStatus('current')
msaXcvrOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: msaXcvrOperationalStatus.setStatus('current')
msaXcvrOpticalFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("fixedX1", 0), ("fixedX4", 1), ("fixedX10", 2), ("tunableX1", 3), ("tunableX4", 4), ("tunableX10", 5), ("tunableX2", 6), ("none", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrOpticalFormat.setStatus('current')
bicTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4), )
if mibBuilder.loadTexts: bicTable.setStatus('current')
bicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (0, "BTI7800-EQUIPMENT-MIB", "moduleName"), (1, "BTI7800-EQUIPMENT-MIB", "bicName"))
if mibBuilder.loadTexts: bicEntry.setStatus('current')
bicName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 1), String())
if mibBuilder.loadTexts: bicName.setStatus('current')
bicPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicPEC.setStatus('current')
bicAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicAdminStatus.setStatus('current')
bicCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicCustom1.setStatus('current')
bicCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicCustom2.setStatus('current')
bicCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicCustom3.setStatus('current')
bicOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bicOperationalStatus.setStatus('current')
bicType = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 8), BicType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicType.setStatus('current')
xcvrTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5), )
if mibBuilder.loadTexts: xcvrTable.setStatus('current')
xcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (0, "BTI7800-EQUIPMENT-MIB", "moduleName"), (0, "BTI7800-EQUIPMENT-MIB", "bicName"), (1, "BTI7800-EQUIPMENT-MIB", "xcvrName"))
if mibBuilder.loadTexts: xcvrEntry.setStatus('current')
xcvrName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 1), String())
if mibBuilder.loadTexts: xcvrName.setStatus('current')
xcvrPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrPEC.setStatus('current')
xcvrAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrAdminStatus.setStatus('current')
xcvrCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrCustom1.setStatus('current')
xcvrCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrCustom2.setStatus('current')
xcvrCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrCustom3.setStatus('current')
xcvrOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xcvrOperationalStatus.setStatus('current')
xcvrOpticalFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("fixedX1", 0), ("fixedX4", 1), ("fixedX10", 2), ("tunableX1", 3), ("tunableX4", 4), ("tunableX10", 5), ("tunableX2", 6), ("none", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrOpticalFormat.setStatus('current')
preamplifierTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6), )
if mibBuilder.loadTexts: preamplifierTable.setStatus('current')
preamplifierEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (0, "BTI7800-EQUIPMENT-MIB", "moduleName"), (1, "BTI7800-EQUIPMENT-MIB", "preamplifierName"))
if mibBuilder.loadTexts: preamplifierEntry.setStatus('current')
preamplifierName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 1), String())
if mibBuilder.loadTexts: preamplifierName.setStatus('current')
preamplifierPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierPEC.setStatus('current')
preamplifierAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierAdminStatus.setStatus('current')
preamplifierCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierCustom1.setStatus('current')
preamplifierCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierCustom2.setStatus('current')
preamplifierCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierCustom3.setStatus('current')
preamplifierOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: preamplifierOperationalStatus.setStatus('current')
mibBuilder.exportSymbols("BTI7800-EQUIPMENT-MIB", bicType=bicType, StatValueType=StatValueType, PortGridType=PortGridType, MetaCliDebugLevel=MetaCliDebugLevel, msaXcvrEntry=msaXcvrEntry, PortDwdmType=PortDwdmType, ShmmAutoUpgradeStatus=ShmmAutoUpgradeStatus, InventoryName=InventoryName, MacAddr=MacAddr, msaXcvrCustom3=msaXcvrCustom3, Validity=Validity, RemoteUrl=RemoteUrl, msaXcvrOperationalStatus=msaXcvrOperationalStatus, CustomValType255=CustomValType255, DolPortIdType=DolPortIdType, String=String, moduleTable=moduleTable, CurrentStateType=CurrentStateType, DolSupportingEquipType=DolSupportingEquipType, preamplifierTable=preamplifierTable, DebugLevel=DebugLevel, Modulereload=Modulereload, ProfileNameType=ProfileNameType, chassisName=chassisName, DolOmsIdType=DolOmsIdType, moduleEntry=moduleEntry, xcvrPEC=xcvrPEC, preamplifierEntry=preamplifierEntry, InetAddressIP=InetAddressIP, SysNameType=SysNameType, chassisOperationalStatus=chassisOperationalStatus, UfmType=UfmType, DolOchXconSrcType=DolOchXconSrcType, xcvrCustom1=xcvrCustom1, msaXcvrOpticalFormat=msaXcvrOpticalFormat, TransportType=TransportType, xcvrCustom3=xcvrCustom3, TransceiverName=TransceiverName, AlarmType=AlarmType, EntityNameType=EntityNameType, ObsoleteName=ObsoleteName, EqptDegreeType=EqptDegreeType, bicCustom3=bicCustom3, xcvrOpticalFormat=xcvrOpticalFormat, UpgradeStatusObjectType=UpgradeStatusObjectType, preamplifierOperationalStatus=preamplifierOperationalStatus, Files=Files, chassisTable=chassisTable, CurrentDBStateType=CurrentDBStateType, bicTable=bicTable, DolModule=DolModule, xcvrEntry=xcvrEntry, StatisticPointType=StatisticPointType, xcvrOperationalStatus=xcvrOperationalStatus, WavelengthProtectionPortIdType=WavelengthProtectionPortIdType, Files1=Files1, moduleCustom3=moduleCustom3, moduleType=moduleType, DolOchIdType=DolOchIdType, NumSpectSlicesType=NumSpectSlicesType, DolFconnEndpt2Type=DolFconnEndpt2Type, PortIdType=PortIdType, PassStr=PassStr, bTI7800_EQUIPMENT_MIB=bTI7800_EQUIPMENT_MIB, ModuleName=ModuleName, bicName=bicName, MsaName=MsaName, moduleCustom1=moduleCustom1, BicType=BicType, SyslogLocalFacility=SyslogLocalFacility, FeDegreeNum=FeDegreeNum, chassisCustom1=chassisCustom1, Ipv4Prefix=Ipv4Prefix, BicName=BicName, modulePEC=modulePEC, xcvrAdminStatus=xcvrAdminStatus, UnsignedShort=UnsignedShort, ConfdString=ConfdString, RemoteLocation=RemoteLocation, RevertiveTimeType=RevertiveTimeType, GlobalDebugLevel=GlobalDebugLevel, chassisType=chassisType, GroupIdType=GroupIdType, WavelengthProtectionGroupIdType=WavelengthProtectionGroupIdType, DolOscIdType=DolOscIdType, DolFiberType=DolFiberType, PortType=PortType, bicCustom2=bicCustom2, preamplifierCustom2=preamplifierCustom2, DolFconnEndpt1Type=DolFconnEndpt1Type, moduleAdminStatus=moduleAdminStatus, BinLengths=BinLengths, chassisCustom3=chassisCustom3, PasswdStr=PasswdStr, AmpModule=AmpModule, GroupConfigType=GroupConfigType, UnsignedByte=UnsignedByte, msaXcvrCustom2=msaXcvrCustom2, xcvrName=xcvrName, FePortIdType=FePortIdType, CustomIdType32=CustomIdType32, chassisAdminStatus=chassisAdminStatus, OdccIdType=OdccIdType, EqptConnType=EqptConnType, preamplifierCustom3=preamplifierCustom3, ValueUnion=ValueUnion, bicPEC=bicPEC, bicAdminStatus=bicAdminStatus, OscIdType=OscIdType, WdmIdType=WdmIdType, moduleName=moduleName, msaXcvrCustom1=msaXcvrCustom1, moduleCustom2=moduleCustom2, ChassisType=ChassisType, TimeOut=TimeOut, ThresholdType=ThresholdType, Wavelength1=Wavelength1, preamplifierCustom1=preamplifierCustom1, RoadmType=RoadmType, preamplifierAdminStatus=preamplifierAdminStatus, Role=Role, msaXcvrPEC=msaXcvrPEC, CustomIdType=CustomIdType, chassisPEC=chassisPEC, bicCustom1=bicCustom1, chassisEntry=chassisEntry, PreamplifierName=PreamplifierName, Wavelength=Wavelength, msaXcvrAdminStatus=msaXcvrAdminStatus, xcvrTable=xcvrTable, DolConnectionType=DolConnectionType, UpgradeLocation=UpgradeLocation, msaXcvrName=msaXcvrName, msaXcvrTable=msaXcvrTable, ChassisName=ChassisName, CustomValType=CustomValType, FeGroupNum=FeGroupNum, chassisCustom2=chassisCustom2, bicOperationalStatus=bicOperationalStatus, moduleOperationalStatus=moduleOperationalStatus, chassisLocation=chassisLocation, DolFixedGridChannelName=DolFixedGridChannelName, bicEntry=bicEntry, xcvrCustom2=xcvrCustom2, preamplifierName=preamplifierName, ThresholdEntityType=ThresholdEntityType, preamplifierPEC=preamplifierPEC, PYSNMP_MODULE_ID=bTI7800_EQUIPMENT_MIB)
