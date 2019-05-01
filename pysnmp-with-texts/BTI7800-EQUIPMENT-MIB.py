#
# PySNMP MIB module BTI7800-EQUIPMENT-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/BTI7800-EQUIPMENT-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:41:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Bits, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, IpAddress, ModuleIdentity, enterprises, Counter32, Gauge32, Unsigned32, NotificationType, TimeTicks, Counter64, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "IpAddress", "ModuleIdentity", "enterprises", "Counter32", "Gauge32", "Unsigned32", "NotificationType", "TimeTicks", "Counter64", "iso", "ObjectIdentity")
DisplayString, TextualConvention, RowStatus, TruthValue, DateAndTime = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "RowStatus", "TruthValue", "DateAndTime")
bTI7800_EQUIPMENT_MIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1)).setLabel("bTI7800-EQUIPMENT-MIB")
bTI7800_EQUIPMENT_MIB.setRevisions(('2012-06-25 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: bTI7800_EQUIPMENT_MIB.setRevisionsDescriptions(('@REVISION-DESCRIPTION',))
if mibBuilder.loadTexts: bTI7800_EQUIPMENT_MIB.setLastUpdated('201206250000Z')
if mibBuilder.loadTexts: bTI7800_EQUIPMENT_MIB.setOrganization('@ORGANIZATION')
if mibBuilder.loadTexts: bTI7800_EQUIPMENT_MIB.setContactInfo('@CONTACT-INFO')
if mibBuilder.loadTexts: bTI7800_EQUIPMENT_MIB.setDescription('This YANG module provides the managed object definitions for operations, administration and management of the BTI Systems Atlas system. The current version of the Atlas module includes these sub-modules: types - definition of commonly used types system - configuration and status of system-wide attributes in addition to those defined by the ietf-system module equipment - configuration and status of provisioned and inventoried equipment logging - configuration of remote logging sinks, enabling the trace levels for the modules and actions pertaining to log notif - notification-related data conditions - retrieval of active alarms and conditions statistics - retrieval of current and historical statistics and performance monitoring counts and values debug - retrieval of debug information for all sub system')
class UnsignedByte(TextualConvention, Unsigned32):
    description = 'xs:unsignedByte'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class UnsignedShort(TextualConvention, Unsigned32):
    description = 'xs:unsignedShort'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

class ConfdString(TextualConvention, OctetString):
    description = 'xs: and confd: types mapped to strings'
    status = 'current'
    displayHint = '1t'

class Ipv4Prefix(TextualConvention, OctetString):
    description = 'confd:ipv4Prefix'
    status = 'current'
    displayHint = '1d.1d.1d.1d/1d'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(5, 5)
    fixedLength = 5

class InetAddressIP(TextualConvention, OctetString):
    description = 'confd:inetAddressIP'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(16, 16), )
class String(TextualConvention, OctetString):
    description = 'xs:string'
    status = 'current'
    displayHint = '1t'

class CurrentDBStateType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14))
    namedValues = NamedValues(("ready-to-backup", 1), ("backup-inprogress", 2), ("ready-to-restore", 3), ("restore-inprogress", 4), ("restore-success", 5), ("restore-failed", 6), ("ready-to-remove", 8), ("remove-inprogress", 9), ("remove-success", 10), ("remove-failed", 11), ("clear-inprogress", 12), ("clear-success", 13), ("clear-failed", 14))

class BicType(TextualConvention, Integer32):
    description = ' sfp-bic - can hold sfp and sfpPlus transceivers. cfp-bic - can hold cfp transceivers qsfp-bic - can hold qsfp transceivers qsfp28-bic - can hold qsfp28 transceivers'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("sfp-bic", 1), ("cfp-bic", 2), ("qsfp-bic", 3), ("qsfp28-bic", 4))

class DolOchIdType(TextualConvention, OctetString):
    description = 'och:<chassis-number>/<slot-number>/<oms-number>/channel-id, where channel-id is an alphanumeric sequence up to 32 characters long'
    status = 'current'
    displayHint = '1t'

class ObsoleteName(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class UfmType(TextualConvention, Integer32):
    description = 'The type of universal forwarding module : msa with on board switching-UFM1(msa-switching) dual BIC with on board switching-UFM2(dual-bic-switching) dual BIC without on board switching-UFM3(dual-bic-non-switching) msa without on board switching-UFM4(msa-non-switching) msa400 without on board switching and 10x10g client ports-UFM6(msa400-10g-client) msa400 without on board switching and 10x10g/4x100g client ports-UFM6-I02(msa400-10g-100g-client)'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("dual-bic-switching", 0), ("dual-bic-non-switching", 1), ("msa-switching", 2), ("msa-non-switching", 3), ("msa400-10g-client", 4), ("msa400-10g-100g-client", 5))

class AmpModule(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class TransportType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("udp", 1), ("tcp", 2))

class Role(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("btiuser", 0), ("provisioning", 1), ("superuser", 2), ("surveillance", 3))

class DolFconnEndpt1Type(TextualConvention, OctetString):
    description = 'source of fiber connect is one of: 1) The line port of a module 2) The line port of a muxdemux port:0/<md-number>/0/L1 3) A client port of a module port:<chassis-number>/<slot-number>/<module-number>/<port-type><port-number> 4) Interface <interface-name>:<chassis-number>/<slot-number>/<module-number><interface-number>'
    status = 'current'
    displayHint = '1t'

class DolFconnEndpt2Type(TextualConvention, OctetString):
    description = 'source of fiber connect is one of:1) The line port of a module2) The line port of a muxdemux port:0/<md-number>/0/L13) A client port of a module port:<chassis-number>/<slot-number>/<module-number>/<port-type><port-number>4) Interface <interface-name>:<chassis-number>/<slot-number>/<module-number><interface-number> add @ip-address to indicate that the endpoint is not local to this node'
    status = 'current'
    displayHint = '1t'

class DebugLevel(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("trace", 1), ("debug", 2), ("off", 3))

class FeGroupNum(TextualConvention, Unsigned32):
    description = ''
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 255)

class PasswdStr(TextualConvention, OctetString):
    description = '<string: Password >'
    status = 'current'
    displayHint = '1t'

class RoadmType(TextualConvention, Integer32):
    description = 'A type of an ROADM card determined by the number of client port on the card (2, 8 or 20).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("a2-port", 0), ("a9-port", 1), ("a20-port", 2))

class StatisticPointType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151, 152, 153, 154, 155, 156, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 168, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 182, 183, 184, 185, 186, 187, 188, 189, 190, 191, 192, 193, 194, 195, 196, 197, 198, 199, 200, 201, 202, 203, 204, 205, 206, 207, 208, 209, 210, 211, 212, 213, 214, 215, 216, 217, 218, 219, 220, 221, 222, 223, 224, 225, 226, 227, 228))
    namedValues = NamedValues(("opr", 1), ("opr-min", 2), ("opr-max", 3), ("opr-avg", 4), ("opt", 5), ("opt-min", 6), ("opt-max", 7), ("opt-avg", 8), ("opt-back-ref-power", 9), ("opr-std-avg", 10), ("opt-std-avg", 11), ("opl-rx", 12), ("opl-tx", 13), ("ltemp", 14), ("ltemp-min", 15), ("ltemp-max", 16), ("ltemp-avg", 17), ("lbc", 18), ("lbc-min", 19), ("lbc-max", 20), ("lbc-avg", 21), ("volt", 22), ("volt-min", 23), ("volt-max", 24), ("volt-avg", 25), ("mod-temp", 26), ("mod-temp-min", 27), ("mod-temp-max", 28), ("mod-temp-avg", 29), ("fec-1cr", 30), ("fec-0cr", 31), ("fec-bitcr", 32), ("fec-symcr", 33), ("fec-ucrcw", 34), ("fec-ber", 35), ("fec-ber-min", 36), ("fec-ber-max", 37), ("fec-ber-avg", 38), ("cd", 39), ("cd-min", 40), ("cd-max", 41), ("cd-avg", 42), ("snr", 43), ("snr-min", 44), ("snr-max", 45), ("snr-avg", 46), ("cfo", 47), ("cfo-min", 48), ("cfo-max", 49), ("cfo-avg", 50), ("dgd", 51), ("dgd-min", 52), ("dgd-max", 53), ("dgd-avg", 54), ("otu-eb", 55), ("otu-bbe", 56), ("otu-es", 57), ("otu-ses", 58), ("otu-ofs", 59), ("otu-uas", 60), ("otu-ber", 61), ("otu-ber-min", 62), ("otu-ber-max", 63), ("otu-ber-avg", 64), ("odu-eb", 65), ("odu-bbe", 66), ("odu-es", 67), ("odu-ses", 68), ("odu-uas", 69), ("odu-ber", 70), ("odu-ber-min", 71), ("odu-ber-max", 72), ("odu-ber-avg", 73), ("odu-lat", 74), ("odu-lat-min", 75), ("odu-lat-max", 76), ("odu-lat-avg", 77), ("pcs-ib", 78), ("pcs-ish", 79), ("pcs-es", 80), ("pcs-ses", 81), ("pcs-uas", 82), ("pcs-ber", 83), ("pcs-ber-min", 84), ("pcs-ber-max", 85), ("pcs-ber-avg", 86), ("octs-rx", 87), ("octs-tx", 88), ("octs-ok-rx", 89), ("octs-ok-tx", 90), ("pkts-rx", 91), ("pkts-tx", 92), ("pkts-ok-rx", 93), ("pkts-ok-tx", 94), ("bcast-pkts-rx", 95), ("bcast-pkts-tx", 96), ("mcast-pkts-rx", 97), ("mcast-pkts-tx", 98), ("fcse-pkts-rx", 99), ("fcse-pkts-tx", 100), ("drp-pkts-rx", 101), ("drp-pkts-tx", 102), ("usize-pkts-rx", 103), ("usize-pkts-tx", 104), ("osize-pkts-rx", 105), ("osize-pkts-tx", 106), ("fragments-rx", 107), ("fragments-tx", 108), ("jabbers-rx", 109), ("jabbers-tx", 110), ("pkts-64-oct-rx", 111), ("pkts-64-oct-tx", 112), ("pkts-65-127-oct-rx", 113), ("pkts-65-127-oct-tx", 114), ("pkts-128-255-oct-rx", 115), ("pkts-128-255-oct-tx", 116), ("pkts-256-511-oct-rx", 117), ("pkts-256-511-oct-tx", 118), ("pkts-512-1023-oct-rx", 119), ("pkts-512-1023-oct-tx", 120), ("pkts-1024-1518-oct-rx", 121), ("pkts-1024-1518-oct-tx", 122), ("pkts-over-1518-oct-rx", 123), ("pkts-over-1518-oct-tx", 124), ("pkts-paus-rx", 125), ("pkts-paus-tx", 126), ("cv-s", 127), ("es-s", 128), ("ses-s", 129), ("sefs-s", 130), ("uas-s", 131), ("ber-s", 132), ("ber-min-s", 133), ("ber-max-s", 134), ("ber-avg-s", 135), ("cv-l", 136), ("es-l", 137), ("ses-l", 138), ("uas-l", 139), ("fc-l", 140), ("ber-l", 141), ("ber-min-l", 142), ("ber-max-l", 143), ("ber-avg-l", 144), ("rs-eb", 145), ("rs-bbe", 146), ("rs-es", 147), ("rs-ses", 148), ("rs-ofs", 149), ("rs-uas", 150), ("rs-ber", 151), ("rs-ber-min", 152), ("rs-ber-max", 153), ("rs-ber-avg", 154), ("ms-eb", 155), ("ms-bbe", 156), ("ms-es", 157), ("ms-ses", 158), ("ms-uas", 159), ("ms-ber", 160), ("ms-ber-min", 161), ("ms-ber-max", 162), ("ms-ber-avg", 163), ("cpu-load-avg", 164), ("cpu-load-min", 165), ("cpu-load-max", 166), ("apr", 167), ("apr-min", 168), ("apr-max", 169), ("apr-avg", 170), ("apr-std-avg", 171), ("opl-rx-min", 172), ("opl-rx-max", 173), ("opl-rx-avg", 174), ("opl-tx-min", 175), ("opl-tx-max", 176), ("opl-tx-avg", 177), ("fan-rpm-avg", 178), ("fan-rpm-min", 179), ("fan-rpm-max", 180), ("pem-presence-avg", 181), ("pem-presence-min", 182), ("pem-presence-max", 183), ("osnr", 184), ("osnr-min", 185), ("osnr-max", 186), ("osnr-avg", 187), ("prbs-lsss", 188), ("prbs-be", 189), ("prbs-ber", 190), ("prbs-ber-min", 191), ("prbs-ber-max", 192), ("prbs-ber-avg", 193), ("span-lngth", 194), ("ipv4-ihl-excp", 195), ("ipv4-pkt-len-excp", 196), ("ipv4-rx-ttl0-excp", 197), ("ipv4-sip-eq-dip-excp", 198), ("ipv4-dip0-excp", 199), ("ipv4-sip-mc-excp", 200), ("ipv4-mpls-ttl0-excp", 201), ("ipv4-mpls-ttl1-excp", 202), ("ip-pkts-rx", 203), ("ip-pkts-tx", 204), ("ip-octs-rx", 205), ("ip-octs-tx", 206), ("mpls-pkts-rx", 207), ("mpls-pkts-tx", 208), ("mpls-octs-rx", 209), ("mpls-octs-tx", 210), ("ipv4-hdr-chksum-excp", 211), ("snr-x", 212), ("snr-x-min", 213), ("snr-x-max", 214), ("snr-x-avg", 215), ("snr-y", 216), ("snr-y-min", 217), ("snr-y-max", 218), ("snr-y-avg", 219), ("opt-total", 220), ("opt-total-min", 221), ("opt-total-max", 222), ("opt-total-avg", 223), ("opt-back-ref-ratio", 224), ("opt-back-ref-ratio-min", 225), ("opt-back-ref-ratio-max", 226), ("opt-back-ref-ratio-avg", 227), ("opt-back-ref-ratio-std-avg", 228))

class GroupIdType(TextualConvention, Unsigned32):
    description = ''
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class FeDegreeNum(TextualConvention, Unsigned32):
    description = ''
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4)

class MsaName(TextualConvention, OctetString):
    description = 'The name of the MSA transceiver. The format of which is: msa:<chassis_number>/<slot_id>/1/1; where slot_id = ufm slot msa400:<chassis_number>/<slot_id>/2/1; where slot_id = ufm slot qsfp:<chassis_number>/<slot_id>/1/<port_id>; where slot_id = ufm slot and port_id is between 1 and 10 qsfp28:<chassis_number>/<slot_id>/1/<port_id>; where slot_id = ufm slot and port_id is 1,2,6,7 '
    status = 'current'
    displayHint = '1t'

class PreamplifierName(TextualConvention, OctetString):
    description = 'The name of the preamplifier. The format of which is: pre:<chassis_number>/<slot_id>/<sub_module>; where slot_id = roadm or ila slot and sub_module is 1 for the pluggable preamplifier module '
    status = 'current'
    displayHint = '1t'

class AlarmType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("conditionRaise", 1), ("conditionClear", 2))

class RevertiveTimeType(TextualConvention, Unsigned32):
    description = ''
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(600, 600)

class RemoteUrl(TextualConvention, OctetString):
    description = '<string: <sftp|ftp>://[username@]<host>[:port]/[file-path]/[file-name] >'
    status = 'current'
    displayHint = '1t'

class Modulereload(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class CurrentStateType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12))
    namedValues = NamedValues(("not-initiated", 1), ("url-set", 2), ("download-inprogress", 3), ("download-success", 4), ("download-failed", 5), ("commit-inprogress", 6), ("commit-success", 7), ("commit-failed", 8), ("cancel-inprogress", 9), ("rollback-inprogress", 10), ("rollback-success", 11), ("rollback-failed", 12))

class BicName(TextualConvention, OctetString):
    description = 'The name of the bic. The format of which is: bic:<chassis_number>/<slot_id>/<bic>; where slot_id = ufm slot and bic is either 1 or 2 '
    status = 'current'
    displayHint = '1t'

class StatValueType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("counter64", 1), ("decimal64", 2), ("float", 3))

class OscIdType(TextualConvention, OctetString):
    description = '<type>:<chassis-number>/<slot-number>/BIC-1/<portNum>.<oscNum>'
    status = 'current'
    displayHint = '1t'

class OdccIdType(TextualConvention, OctetString):
    description = '<type>:<chassis-number>/<slot-number>/BIC-1/<portNum>.<oscNum>.<odccNum>'
    status = 'current'
    displayHint = '1t'

class WdmIdType(TextualConvention, OctetString):
    description = '<type>:<chassis-number>/<slot-number>/BIC-1/<lineNum>'
    status = 'current'
    displayHint = '1t'

class PortIdType(TextualConvention, OctetString):
    description = '<port-type>:<chassis-number>/<slot-number>'
    status = 'current'
    displayHint = '1t'

class DolFiberType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("ssmf", 1), ("leaf", 2), ("twrs", 3), ("ndsf", 4), ("teralight", 5))

class Files1(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class UpgradeStatusObjectType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("system-upgrade-status", 1), ("module-upgrade-status", 2))

class CustomValType(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class GroupConfigType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("none", 1), ("noEqlzTerm", 2), ("eqlzTerm", 3), ("noEqlzLine", 4), ("eqlzLine", 5), ("roadm", 6))

class Wavelength(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class ValueUnion(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class Wavelength1(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class TimeOut(TextualConvention, Unsigned32):
    description = 'default 5 seconds, range 1 to 255'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 255)

class SysNameType(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 20)

class Validity(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("notAvailable", 1), ("partial", 2), ("complete", 3))

class MetaCliDebugLevel(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("trace", 1), ("debug", 2), ("info", 3), ("warning", 4), ("error", 5))

class GlobalDebugLevel(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("enable", 1), ("disable", 2))

class MacAddr(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class ModuleName(TextualConvention, OctetString):
    description = '< module:<chassis_number>/<slot_id>; The module name and location>'
    status = 'current'
    displayHint = '1t'

class DolSupportingEquipType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("mdeq", 1), ("roadm2", 2), ("roadm9", 3), ("roadm20", 4), ("ila", 5), ("preamp", 6))

class WavelengthProtectionPortIdType(TextualConvention, OctetString):
    description = 'wpsport:<chassis-number>/<slot-number>/<L or C><group-number><A or B or blank>'
    status = 'current'
    displayHint = '1t'

class SyslogLocalFacility(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("local0", 1), ("local1", 2), ("local2", 3), ("local3", 4), ("local4", 5), ("local5", 6), ("local6", 7), ("local7", 8))

class UpgradeLocation(TextualConvention, OctetString):
    description = '<string: <sftp|ftp>://[username@]<host>[:port]/[file-path]/[file-name] >'
    status = 'current'
    displayHint = '1t'

class ChassisName(TextualConvention, OctetString):
    description = 'The name of the chassis or passive component. The format of which is: chassis:<chassis_number>; where chassis_number is between 1 and 16 muxdemux:0/<number>; This is the 96 ch multiplexer/demultiplexer with 1610 coupler md:0/<number>; This is the 96 multiplexer/demultiplexer dcmeqpt:0/<number>; This is the dispersion compensation module The number must be between 1 and 255. The passive elements cannot use the same <number>. i.e. you cannot have both a dcmeqpt:0/1 and a muxdemux:0/1 '
    status = 'current'
    displayHint = '1t'

class EqptDegreeType(TextualConvention, Unsigned32):
    description = ''
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4)

class NumSpectSlicesType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 384)

class PortGridType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ghz100", 1), ("ghz50", 2), ("flex", 3))

class CustomValType255(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 255)

class DolPortIdType(TextualConvention, OctetString):
    description = 'port:<chassis-number>/<slot-number>/<module-number>/<sub-module>/ <port-type><port-number>, where sub-module is 0 for the main module and port-types are C-client, L-line, PRE-preamplifier'
    status = 'current'
    displayHint = '1t'

class WavelengthProtectionGroupIdType(TextualConvention, OctetString):
    description = 'wpsgroup:<chassis-number>/<slot-number>/<group-number>'
    status = 'current'
    displayHint = '1t'

class RemoteLocation(TextualConvention, OctetString):
    description = '<string: <sftp|ftp>://[username@]<host>[:port]/[file-path]/[file-name] >'
    status = 'current'
    displayHint = '1t'

class CustomIdType32(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class TransceiverName(TextualConvention, OctetString):
    description = 'The name of the transceiver. The format of which is: sfpPlus:<chassis_number>/<slot_id>/<bic>/<port_id>; where slot_id = ufm slot and bic is either 1 or 2 and port_id is between 1 and 12 [sfp+] cfp:<chassis_number>/<slot_id>/<bic>/<port_id>; where slot_id = ufm slot and bic is either 1 or 2 and port_id is 1 [cfp] qsfp:<chassis_number>/<slot_id>/<bic>/<port_id>; where slot_id = ufm slot and bic is either 1 or 2 and port_id is between 1 and 3 [qsfp] qsfp28:<chassis_number>/<slot_id>/<bic/port-group>/<port_id>; where slot_id = ufm slot and bic/port-group is either 1 or 2, and port_id is 1 [qsfp28] '
    status = 'current'
    displayHint = '1t'

class ThresholdType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("warningAlert", 1), ("alarmHigh", 2), ("alarmLow", 3))

class ProfileNameType(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class PassStr(TextualConvention, OctetString):
    description = '<string: Password >'
    status = 'current'
    displayHint = '1t'

class BinLengths(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 15, 1440))
    namedValues = NamedValues(("unTimed", 0), ("a1Minute", 1), ("a15Minute", 15), ("a1Day", 1440))

class Files(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class ChassisType(TextualConvention, Integer32):
    description = 'The type of chassis: based on number of slots (1, 2, 6, or 14).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("a14-Slot", 0), ("a6-Slot", 1), ("a2-Slot", 2), ("a1-Slot", 3))

class EqptConnType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eqDuplex", 1), ("loopback", 2))

class PortDwdmType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("native", 1), ("alien", 2))

class ShmmAutoUpgradeStatus(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("disabled", 1), ("enabled", 2))

class InventoryName(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class FePortIdType(TextualConvention, OctetString):
    description = 'source of fiber connect is one of:1) The line port of a module2) The line port of a muxdemux port:0/<md-number>/0/L13) A client port of a module port:<chassis-number>/<slot-number>/<module-number>/<port-type><port-number>4) Interface <interface-name>:<chassis-number>/<slot-number>/<module-number><interface-number> add @ip-address to indicate that the endpoint is not local to this node'
    status = 'current'
    displayHint = '1t'

class DolOchXconSrcType(TextualConvention, OctetString):
    description = 'source of och cross connect is one of:1) OCH on a module <module-type>:<chassis-number>/<slot-number>/<module-number>/<port-type><port-number>/channel-id>2) Interface <interface-name>:<chassis-number>/<slot-number>/<module-number><interface-number>'
    status = 'current'
    displayHint = '1t'

class DolModule(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class DolConnectionType(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class ThresholdEntityType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19))
    namedValues = NamedValues(("a10ge", 1), ("a40ge", 2), ("a100ge", 3), ("otu2", 4), ("otu4", 5), ("odu2", 6), ("odu3", 7), ("odu4", 8), ("oc192", 9), ("stm64", 10), ("wanoc192", 11), ("wanstm64", 12), ("osc", 13), ("line", 14), ("client", 15), ("dcm", 16), ("otu2e", 17), ("odu2e", 18), ("och", 19))

class EntityNameType(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class DolFixedGridChannelName(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'

class CustomIdType(TextualConvention, OctetString):
    description = ''
    status = 'current'
    displayHint = '1t'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 32)

class PortType(TextualConvention, Integer32):
    description = ''
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("line", 1), ("client", 2), ("dcm", 3), ("chlport", 4), ("expport", 5))

class DolOscIdType(TextualConvention, OctetString):
    description = 'osc:<chassis-number>/<slot-number>/<module-number>/<port-type><port-number> where port-type is C-client, L-line'
    status = 'current'
    displayHint = '1t'

class DolOmsIdType(TextualConvention, OctetString):
    description = 'oms:<chassis-number>/<slot-number>/<module-number>/<port-type><port-number> where port-type is C-client, L-line'
    status = 'current'
    displayHint = '1t'

chassisTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1), )
if mibBuilder.loadTexts: chassisTable.setStatus('current')
if mibBuilder.loadTexts: chassisTable.setDescription('System components (chassis, module, BIC, transceiver, preamplifier, etc)')
chassisEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1), ).setIndexNames((1, "BTI7800-EQUIPMENT-MIB", "chassisName"))
if mibBuilder.loadTexts: chassisEntry.setStatus('current')
if mibBuilder.loadTexts: chassisEntry.setDescription('')
chassisName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 1), String())
if mibBuilder.loadTexts: chassisName.setStatus('current')
if mibBuilder.loadTexts: chassisName.setDescription('')
chassisType = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 2), ChassisType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisType.setStatus('current')
if mibBuilder.loadTexts: chassisType.setDescription('Type of chassis based on [PamS] number of backplane slots')
chassisPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 3), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisPEC.setStatus('current')
if mibBuilder.loadTexts: chassisPEC.setDescription('Product equipment code assigned by BTI')
chassisAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 4), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisAdminStatus.setStatus('current')
if mibBuilder.loadTexts: chassisAdminStatus.setDescription('Administrative Status of the chassis')
chassisCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisCustom1.setStatus('current')
if mibBuilder.loadTexts: chassisCustom1.setDescription("Customizable textual field for operator's use")
chassisCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisCustom2.setStatus('current')
if mibBuilder.loadTexts: chassisCustom2.setDescription("Customizable textual field for operator's use")
chassisCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 7), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisCustom3.setStatus('current')
if mibBuilder.loadTexts: chassisCustom3.setDescription("Customizable textual field for operator's use")
chassisOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: chassisOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: chassisOperationalStatus.setDescription('The operational status of the equipment item')
chassisLocation = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 1, 1, 9), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: chassisLocation.setStatus('current')
if mibBuilder.loadTexts: chassisLocation.setDescription('The physical location of the chassis')
moduleTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2), )
if mibBuilder.loadTexts: moduleTable.setStatus('current')
if mibBuilder.loadTexts: moduleTable.setDescription('The module type and location')
moduleEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (1, "BTI7800-EQUIPMENT-MIB", "moduleName"))
if mibBuilder.loadTexts: moduleEntry.setStatus('current')
if mibBuilder.loadTexts: moduleEntry.setDescription('')
moduleName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 1), String())
if mibBuilder.loadTexts: moduleName.setStatus('current')
if mibBuilder.loadTexts: moduleName.setDescription('')
modulePEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: modulePEC.setStatus('current')
if mibBuilder.loadTexts: modulePEC.setDescription('Product equipment code assigned by BTI')
moduleAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleAdminStatus.setStatus('current')
if mibBuilder.loadTexts: moduleAdminStatus.setDescription('Administrative Status of the chassis')
moduleCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleCustom1.setStatus('current')
if mibBuilder.loadTexts: moduleCustom1.setDescription("Customizable textual field for operator's use")
moduleCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleCustom2.setStatus('current')
if mibBuilder.loadTexts: moduleCustom2.setDescription("Customizable textual field for operator's use")
moduleCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleCustom3.setStatus('current')
if mibBuilder.loadTexts: moduleCustom3.setDescription("Customizable textual field for operator's use")
moduleOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: moduleOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: moduleOperationalStatus.setDescription('The operational status of the equipment item')
moduleType = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 2, 1, 8), UfmType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: moduleType.setStatus('current')
if mibBuilder.loadTexts: moduleType.setDescription('Type of ufm based on msa and BIC and switching')
msaXcvrTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3), )
if mibBuilder.loadTexts: msaXcvrTable.setStatus('current')
if mibBuilder.loadTexts: msaXcvrTable.setDescription('The transceiver type and location')
msaXcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (0, "BTI7800-EQUIPMENT-MIB", "moduleName"), (1, "BTI7800-EQUIPMENT-MIB", "msaXcvrName"))
if mibBuilder.loadTexts: msaXcvrEntry.setStatus('current')
if mibBuilder.loadTexts: msaXcvrEntry.setDescription('')
msaXcvrName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 1), String())
if mibBuilder.loadTexts: msaXcvrName.setStatus('current')
if mibBuilder.loadTexts: msaXcvrName.setDescription('')
msaXcvrPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrPEC.setStatus('current')
if mibBuilder.loadTexts: msaXcvrPEC.setDescription('Product equipment code assigned by BTI')
msaXcvrAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrAdminStatus.setStatus('current')
if mibBuilder.loadTexts: msaXcvrAdminStatus.setDescription('Administrative Status of the chassis')
msaXcvrCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrCustom1.setStatus('current')
if mibBuilder.loadTexts: msaXcvrCustom1.setDescription("Customizable textual field for operator's use")
msaXcvrCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrCustom2.setStatus('current')
if mibBuilder.loadTexts: msaXcvrCustom2.setDescription("Customizable textual field for operator's use")
msaXcvrCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrCustom3.setStatus('current')
if mibBuilder.loadTexts: msaXcvrCustom3.setDescription("Customizable textual field for operator's use")
msaXcvrOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: msaXcvrOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: msaXcvrOperationalStatus.setDescription('The operational status of the equipment item')
msaXcvrOpticalFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 3, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("fixedX1", 0), ("fixedX4", 1), ("fixedX10", 2), ("tunableX1", 3), ("tunableX4", 4), ("tunableX10", 5), ("tunableX2", 6), ("none", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: msaXcvrOpticalFormat.setStatus('current')
if mibBuilder.loadTexts: msaXcvrOpticalFormat.setDescription('Transceiver format fixed or tunable')
bicTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4), )
if mibBuilder.loadTexts: bicTable.setStatus('current')
if mibBuilder.loadTexts: bicTable.setDescription('A BTI interface card location')
bicEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (0, "BTI7800-EQUIPMENT-MIB", "moduleName"), (1, "BTI7800-EQUIPMENT-MIB", "bicName"))
if mibBuilder.loadTexts: bicEntry.setStatus('current')
if mibBuilder.loadTexts: bicEntry.setDescription('')
bicName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 1), String())
if mibBuilder.loadTexts: bicName.setStatus('current')
if mibBuilder.loadTexts: bicName.setDescription('')
bicPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicPEC.setStatus('current')
if mibBuilder.loadTexts: bicPEC.setDescription('Product equipment code assigned by BTI')
bicAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicAdminStatus.setStatus('current')
if mibBuilder.loadTexts: bicAdminStatus.setDescription('Administrative Status of the chassis')
bicCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicCustom1.setStatus('current')
if mibBuilder.loadTexts: bicCustom1.setDescription("Customizable textual field for operator's use")
bicCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicCustom2.setStatus('current')
if mibBuilder.loadTexts: bicCustom2.setDescription("Customizable textual field for operator's use")
bicCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicCustom3.setStatus('current')
if mibBuilder.loadTexts: bicCustom3.setDescription("Customizable textual field for operator's use")
bicOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: bicOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: bicOperationalStatus.setDescription('The operational status of the equipment item')
bicType = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 4, 1, 8), BicType()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: bicType.setStatus('current')
if mibBuilder.loadTexts: bicType.setDescription('12x SFP+ or 1x CFP or 3x QSFP or 1x QSFP28')
xcvrTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5), )
if mibBuilder.loadTexts: xcvrTable.setStatus('current')
if mibBuilder.loadTexts: xcvrTable.setDescription('The transceiver type and location')
xcvrEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (0, "BTI7800-EQUIPMENT-MIB", "moduleName"), (0, "BTI7800-EQUIPMENT-MIB", "bicName"), (1, "BTI7800-EQUIPMENT-MIB", "xcvrName"))
if mibBuilder.loadTexts: xcvrEntry.setStatus('current')
if mibBuilder.loadTexts: xcvrEntry.setDescription('')
xcvrName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 1), String())
if mibBuilder.loadTexts: xcvrName.setStatus('current')
if mibBuilder.loadTexts: xcvrName.setDescription('')
xcvrPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrPEC.setStatus('current')
if mibBuilder.loadTexts: xcvrPEC.setDescription('Product equipment code assigned by BTI')
xcvrAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrAdminStatus.setStatus('current')
if mibBuilder.loadTexts: xcvrAdminStatus.setDescription('Administrative Status of the chassis')
xcvrCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrCustom1.setStatus('current')
if mibBuilder.loadTexts: xcvrCustom1.setDescription("Customizable textual field for operator's use")
xcvrCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrCustom2.setStatus('current')
if mibBuilder.loadTexts: xcvrCustom2.setDescription("Customizable textual field for operator's use")
xcvrCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrCustom3.setStatus('current')
if mibBuilder.loadTexts: xcvrCustom3.setDescription("Customizable textual field for operator's use")
xcvrOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: xcvrOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: xcvrOperationalStatus.setDescription('The operational status of the equipment item')
xcvrOpticalFormat = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 5, 1, 8), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7))).clone(namedValues=NamedValues(("fixedX1", 0), ("fixedX4", 1), ("fixedX10", 2), ("tunableX1", 3), ("tunableX4", 4), ("tunableX10", 5), ("tunableX2", 6), ("none", 7)))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: xcvrOpticalFormat.setStatus('current')
if mibBuilder.loadTexts: xcvrOpticalFormat.setDescription('Transceiver format fixed or tunable')
preamplifierTable = MibTable((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6), )
if mibBuilder.loadTexts: preamplifierTable.setStatus('current')
if mibBuilder.loadTexts: preamplifierTable.setDescription('The pluggable preamplifier type and location')
preamplifierEntry = MibTableRow((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1), ).setIndexNames((0, "BTI7800-EQUIPMENT-MIB", "chassisName"), (0, "BTI7800-EQUIPMENT-MIB", "moduleName"), (1, "BTI7800-EQUIPMENT-MIB", "preamplifierName"))
if mibBuilder.loadTexts: preamplifierEntry.setStatus('current')
if mibBuilder.loadTexts: preamplifierEntry.setDescription('')
preamplifierName = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 1), String())
if mibBuilder.loadTexts: preamplifierName.setStatus('current')
if mibBuilder.loadTexts: preamplifierName.setDescription('')
preamplifierPEC = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 2), String()).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierPEC.setStatus('current')
if mibBuilder.loadTexts: preamplifierPEC.setDescription('Product equipment code assigned by BTI')
preamplifierAdminStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 3), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(1, 2, 3))).clone(namedValues=NamedValues(("up", 1), ("down", 2), ("testing", 3))).clone('up')).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierAdminStatus.setStatus('current')
if mibBuilder.loadTexts: preamplifierAdminStatus.setDescription('Administrative Status of the chassis')
preamplifierCustom1 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 4), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierCustom1.setStatus('current')
if mibBuilder.loadTexts: preamplifierCustom1.setDescription("Customizable textual field for operator's use")
preamplifierCustom2 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 5), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierCustom2.setStatus('current')
if mibBuilder.loadTexts: preamplifierCustom2.setDescription("Customizable textual field for operator's use")
preamplifierCustom3 = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 6), String().subtype(subtypeSpec=ValueSizeConstraint(0, 255))).setMaxAccess("readwrite")
if mibBuilder.loadTexts: preamplifierCustom3.setStatus('current')
if mibBuilder.loadTexts: preamplifierCustom3.setDescription("Customizable textual field for operator's use")
preamplifierOperationalStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 18070, 2, 9, 3, 1, 6, 1, 7), Integer32().subtype(subtypeSpec=ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 5, 6, 7))).clone(namedValues=NamedValues(("unknown", 0), ("up", 1), ("down", 2), ("testing", 3), ("dormant", 5), ("notPresent", 6), ("lowerLayerDown", 7)))).setMaxAccess("readonly")
if mibBuilder.loadTexts: preamplifierOperationalStatus.setStatus('current')
if mibBuilder.loadTexts: preamplifierOperationalStatus.setDescription('The operational status of the equipment item')
mibBuilder.exportSymbols("BTI7800-EQUIPMENT-MIB", PortType=PortType, Validity=Validity, OdccIdType=OdccIdType, FePortIdType=FePortIdType, chassisLocation=chassisLocation, Ipv4Prefix=Ipv4Prefix, chassisTable=chassisTable, StatValueType=StatValueType, CurrentStateType=CurrentStateType, preamplifierCustom2=preamplifierCustom2, PortIdType=PortIdType, PreamplifierName=PreamplifierName, DolOscIdType=DolOscIdType, ShmmAutoUpgradeStatus=ShmmAutoUpgradeStatus, DolOchXconSrcType=DolOchXconSrcType, BicType=BicType, DolOmsIdType=DolOmsIdType, AlarmType=AlarmType, UpgradeStatusObjectType=UpgradeStatusObjectType, Wavelength1=Wavelength1, moduleName=moduleName, bTI7800_EQUIPMENT_MIB=bTI7800_EQUIPMENT_MIB, moduleType=moduleType, RemoteUrl=RemoteUrl, DolConnectionType=DolConnectionType, DolModule=DolModule, WavelengthProtectionGroupIdType=WavelengthProtectionGroupIdType, bicName=bicName, chassisName=chassisName, bicOperationalStatus=bicOperationalStatus, xcvrName=xcvrName, WavelengthProtectionPortIdType=WavelengthProtectionPortIdType, Role=Role, FeDegreeNum=FeDegreeNum, SyslogLocalFacility=SyslogLocalFacility, GlobalDebugLevel=GlobalDebugLevel, msaXcvrName=msaXcvrName, PYSNMP_MODULE_ID=bTI7800_EQUIPMENT_MIB, AmpModule=AmpModule, TransportType=TransportType, preamplifierAdminStatus=preamplifierAdminStatus, GroupConfigType=GroupConfigType, chassisEntry=chassisEntry, bicCustom1=bicCustom1, BinLengths=BinLengths, xcvrPEC=xcvrPEC, UfmType=UfmType, UnsignedByte=UnsignedByte, msaXcvrOperationalStatus=msaXcvrOperationalStatus, RoadmType=RoadmType, ThresholdEntityType=ThresholdEntityType, CustomValType255=CustomValType255, modulePEC=modulePEC, InventoryName=InventoryName, msaXcvrCustom2=msaXcvrCustom2, MsaName=MsaName, Files=Files, chassisCustom2=chassisCustom2, DolPortIdType=DolPortIdType, DolFixedGridChannelName=DolFixedGridChannelName, xcvrCustom3=xcvrCustom3, DolOchIdType=DolOchIdType, NumSpectSlicesType=NumSpectSlicesType, moduleAdminStatus=moduleAdminStatus, MacAddr=MacAddr, preamplifierTable=preamplifierTable, chassisPEC=chassisPEC, TimeOut=TimeOut, ThresholdType=ThresholdType, Files1=Files1, DolFiberType=DolFiberType, ChassisType=ChassisType, bicTable=bicTable, InetAddressIP=InetAddressIP, bicEntry=bicEntry, xcvrOperationalStatus=xcvrOperationalStatus, Wavelength=Wavelength, moduleTable=moduleTable, EqptDegreeType=EqptDegreeType, PortGridType=PortGridType, SysNameType=SysNameType, bicType=bicType, xcvrEntry=xcvrEntry, xcvrCustom2=xcvrCustom2, preamplifierPEC=preamplifierPEC, ModuleName=ModuleName, EntityNameType=EntityNameType, WdmIdType=WdmIdType, ValueUnion=ValueUnion, moduleEntry=moduleEntry, msaXcvrPEC=msaXcvrPEC, chassisAdminStatus=chassisAdminStatus, xcvrCustom1=xcvrCustom1, moduleCustom2=moduleCustom2, String=String, chassisType=chassisType, RevertiveTimeType=RevertiveTimeType, CustomIdType=CustomIdType, OscIdType=OscIdType, preamplifierEntry=preamplifierEntry, xcvrOpticalFormat=xcvrOpticalFormat, msaXcvrTable=msaXcvrTable, StatisticPointType=StatisticPointType, DebugLevel=DebugLevel, preamplifierCustom1=preamplifierCustom1, RemoteLocation=RemoteLocation, msaXcvrOpticalFormat=msaXcvrOpticalFormat, BicName=BicName, FeGroupNum=FeGroupNum, msaXcvrCustom1=msaXcvrCustom1, CurrentDBStateType=CurrentDBStateType, ChassisName=ChassisName, chassisCustom1=chassisCustom1, DolSupportingEquipType=DolSupportingEquipType, chassisOperationalStatus=chassisOperationalStatus, moduleCustom1=moduleCustom1, PasswdStr=PasswdStr, msaXcvrEntry=msaXcvrEntry, msaXcvrAdminStatus=msaXcvrAdminStatus, preamplifierName=preamplifierName, ConfdString=ConfdString, Modulereload=Modulereload, preamplifierOperationalStatus=preamplifierOperationalStatus, xcvrAdminStatus=xcvrAdminStatus, msaXcvrCustom3=msaXcvrCustom3, bicCustom3=bicCustom3, UnsignedShort=UnsignedShort, bicAdminStatus=bicAdminStatus, bicPEC=bicPEC, TransceiverName=TransceiverName, GroupIdType=GroupIdType, CustomIdType32=CustomIdType32, chassisCustom3=chassisCustom3, DolFconnEndpt2Type=DolFconnEndpt2Type, DolFconnEndpt1Type=DolFconnEndpt1Type, ProfileNameType=ProfileNameType, PortDwdmType=PortDwdmType, UpgradeLocation=UpgradeLocation, EqptConnType=EqptConnType, CustomValType=CustomValType, bicCustom2=bicCustom2, ObsoleteName=ObsoleteName, PassStr=PassStr, moduleOperationalStatus=moduleOperationalStatus, xcvrTable=xcvrTable, preamplifierCustom3=preamplifierCustom3, MetaCliDebugLevel=MetaCliDebugLevel, moduleCustom3=moduleCustom3)
