#
# PySNMP MIB module CM-COMMON-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CM-COMMON-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:25:09 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
fsp150cm, = mibBuilder.importSymbols("ADVA-MIB", "fsp150cm")
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ObjectIdentity, Bits, Gauge32, IpAddress, MibScalar, MibTable, MibTableRow, MibTableColumn, Counter64, Integer32, MibIdentifier, Counter32, NotificationType, Unsigned32, TimeTicks, iso, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "Gauge32", "IpAddress", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Counter64", "Integer32", "MibIdentifier", "Counter32", "NotificationType", "Unsigned32", "TimeTicks", "iso", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
cmCommonMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1))
cmCommonMIB.setRevisions(('2016-07-11 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmCommonMIB.setRevisionsDescriptions(('Notes from release 201607110000Z (1) renamed FlowSecureState to FlowSecState since it cannot be moved from fsp150cm-connectguard.mib Notes from release 201607080000Z (1) moved FlowSecureState from fsp150cm-connectguard.mib Notes from release 201502040000Z (1) add xg210c subproduct Notes from release 201412010000Z, (1) Added new Textual Convention: Decimal32 Notes from release 201405210000Z, (1) Added new EthernetMediaType literals: - auto, - none. Notes from release 201311280000Z (1) Added new Secondary State literal - mon-tx Notes from release 201202150000Z (post GE20x R5.2.3CC) (1) Added speed-auto-detect to EthernetPortSpeed Notes from release 201108010000Z (1) Post EG-X merge (R5.1.1) Notes from release 201107080000Z (1)Moved CmPmIntervalType from fsp150cm-perf.mib to this MIB (2)Added interval-5min to TC CmPmIntervalType Notes from release 201002120000Z (1)New Textual Conventions : ClassOfServiceType and SignalDirectionType (2)New product OIDs (used for sysOid) : ge201 and ge201se Notes from release 200803160000Z, (1)EthernetPortSpeed textual convention now has additional literals, speed-auto-1000MB-full-master and speed-auto-1000MB-full-slave (2)Added textual convention SfpMediaType Notes from release 200803030000Z, (1)MIB version ready for release FSP150CM.',))
if mibBuilder.loadTexts: cmCommonMIB.setLastUpdated('201607110000Z')
if mibBuilder.loadTexts: cmCommonMIB.setOrganization('ADVA Optical Networking')
if mibBuilder.loadTexts: cmCommonMIB.setContactInfo(' Raghav Trivedi ADVA Optical Networking, Inc. Tel: +1 972 759-1239 E-mail: rtrivedi@advaoptical.com Postal: 2301 N. Greenville Ave. #300 Richardson, TX USA 75082')
if mibBuilder.loadTexts: cmCommonMIB.setDescription('This module defines the Common MIB definitions used by the FSP150CM and FSP150CC product lines. Copyright (C) ADVA Optical Networking.')
subproducts = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1))
f3Capabilities = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 2))
nemihubshelf = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 1))
ge101 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 2))
ge206 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 3))
ge201 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 4))
ge201se = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 5))
ge206f = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 6))
cmagg = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 7))
ge112 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 8))
ge114 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 9))
ge206v = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 10))
xg210 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 11))
t1804 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 12))
t3204 = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 13))
gesyncprobe = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 14))
ge114H = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 15))
ge114PH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 16))
ge114S = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 17))
ge114SH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 18))
sh1pcs = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 19))
ge112Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 20))
ge112ProM = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 21))
ge114Pro = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 22))
ge114ProC = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 23))
ge114ProSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 24))
ge114ProCSH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 25))
ge114ProHE = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 26))
xg210c = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 27))
ge112ProH = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 28))
ge114G = MibIdentifier((1, 3, 6, 1, 4, 1, 2544, 1, 12, 1, 1, 29))
class PortType(TextualConvention, Integer32):
    description = 'Enumerations for types of ports. eth-access - Ethernet Access Port, eth-network - Ethernet Network Port.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("eth-access", 1), ("eth-network", 2))

class TrafficDirection(TextualConvention, Integer32):
    description = 'Enumerations for direction of traffic. a2n - Access to Network direction, n2a - Network to Access direction, ingress - Entering system direction, egress - Away from system direction, n2n - Network to Network direction.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("a2n", 1), ("n2a", 2), ("ingress", 3), ("egress", 4), ("n2n", 5))

class VlanId(TextualConvention, Integer32):
    description = 'Textual Convention for the Vlan Id.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 4095)

class VlanPriority(TextualConvention, Integer32):
    description = 'Textual Convention for the Vlan Priority.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 7)

class VlanTagType(TextualConvention, Integer32):
    description = 'Textual Convention for the Type of VLAN Tag.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("inner-vlantag", 1), ("outer-vlantag", 2), ("n2a-priorityMapping", 3), ("mplsLabel", 4), ("vcLabel", 5), ("encapOuterVlanTag", 6))

class AdminState(TextualConvention, Integer32):
    description = "Administrative State used for FSP150CM entities. in-service - represents normal, in-service, traffic passing state of the Entity; management - represents the traffic passing state, however, alarms are not reported maintenance- represents the mandatory state of operating loopbacks, ECPA test as well as Etherjack diagnosis operations, alarms are not reported disabled - represents the disabled state, user traffic is not passed, management traffic is passed, alarms are not reported unassigned - represents the disabled state, traffic(user or management) is not passed, alarms are not monitored. monitored - represents the monitored state. Used for retrieving performance monitoring on entity, but entity can't be used for normal operation. Alarms are reported "
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("in-service", 1), ("management", 2), ("maintenance", 3), ("disabled", 4), ("unassigned", 5), ("monitored", 6))

class OperationalState(TextualConvention, Integer32):
    description = 'Operational State used for FSP150CM entities. normal - represents operational state UP, outage - represents operational state DOWN.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("normal", 1), ("outage", 2))

class SecondaryState(TextualConvention, Bits):
    description = 'Secondary state used for FSP150CM entities. active - Active, automaticinservice - Automatic In Service, facilityfailure - Facility Failure, fault - Fault, loopback - Loopback, maintenance - Maintenance, mismatchedeqpt - Mismatched Equipment, standbyhot - Standby Hot, supportingentityoutage - Supporting Entity Outage, unassigned - Unassigned, unequipped - Unequipped, disabled - Disabled, forcedoffline - Forced offline, initializing - Initializing, prtcl - Protocol, blckd - Blocked, mon-tx - Monitor TX, mir-rx - Mirror RX, cema - CEMA, lkdo - LKDO'
    status = 'current'
    namedValues = NamedValues(("not-applicable", 0), ("active", 1), ("automaticinservice", 2), ("facilityfailure", 3), ("fault", 4), ("loopback", 5), ("maintenance", 6), ("mismatchedeqpt", 7), ("standbyhot", 8), ("supportingentityoutage", 9), ("unassigned", 10), ("unequipped", 11), ("disabled", 12), ("forcedoffline", 13), ("initializing", 14), ("prtcl", 15), ("blckd", 16), ("mon-tx", 17), ("mir-rx", 18), ("cema", 19), ("lkdo", 20))

class EthernetPortSpeed(TextualConvention, Integer32):
    description = 'Describes the Ethernet Port Speed. speed-unknown : speed unknown speed-10MB-full : fixed speed 10MB full duplex speed-10MB-half : fixed speed 10MB half duplex speed-100MB-full : fixed speed 100MB full duplex speed-100MB-half : fixed speed 100MB half duplex speed-1000MB-full : fixed speed 1000MB full duplex speed-1000MB-half : fixed speed 1000MB half duplex speed-auto : Auto negotiation, advertise all speeds speed-auto-10MB-full : Auto negotiation, advertise 10MB full duplex speed-auto-10MB-half : Auto negotiation, advertise 10MB half duplex speed-auto-100MB-full: Auto negotiation, advertise 100MB full duplex speed-auto-100MB-half: Auto negotiation, advertise 100MB half duplex speed-auto-1000MB-full: Auto negotiation, advertise 1000MB full duplex speed-auto-1000MB-half: Auto negotiation, advertise 1000MB half duplex speed-negotiating : Auto negotiating, transient state speed-auto-1000MB-full-master : Auto negotiation, advertise 1000MB full duplex, sync master speed-auto-1000MB-full-slave : Auto negotiation, advertise 1000MB full duplex, sync slave speed-none : Used to denote speed, when negotiating speed-auto-1000MB-full-master-preferred : Auto negotiation, advertise 1000MB full duplex, preferred sync master speed-auto-1000MB-full-slave-preferred : Auto negotiation, advertise 1000MB full duplex, preferred sync slave speed-10G-full : fixed speed 10G full duplex speed-auto-detect : Auto detect speed; iterate through available speeds and test the link with remote end - if link is up at given speed, this speed is configured .'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21))
    namedValues = NamedValues(("speed-unknown", 0), ("speed-10MB-full", 1), ("speed-10MB-half", 2), ("speed-100MB-full", 3), ("speed-100MB-half", 4), ("speed-1000MB-full", 5), ("speed-1000MB-half", 6), ("speed-auto", 7), ("speed-auto-10MB-full", 8), ("speed-auto-10MB-half", 9), ("speed-auto-100MB-full", 10), ("speed-auto-100MB-half", 11), ("speed-auto-1000MB-full", 12), ("speed-auto-1000MB-half", 13), ("speed-negotiating", 14), ("speed-auto-1000MB-full-master", 15), ("speed-auto-1000MB-full-slave", 16), ("speed-none", 17), ("speed-auto-1000MB-full-master-preferred", 18), ("speed-auto-1000MB-full-slave-preferred", 19), ("speed-10G-full", 20), ("speed-auto-detect", 21))

class EthernetMediaType(TextualConvention, Integer32):
    description = 'Describes the Ethernet Port Media Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5))
    namedValues = NamedValues(("not-applicable", 0), ("copper", 1), ("fiber", 2), ("coppersfp", 3), ("auto", 4), ("none", 5))

class PerfCounter64(TextualConvention, Counter64):
    description = 'This type represents a non-negative 64-bit integer. The initial value of this integer will be 0. It will increment with time, however, the value will revert back to 0 when the time period for history interval elapses. Typically, this will be noticed at 15minute intervals and 1 day intervals. Only the rollover interval periods will keep counting to a maximum 64-bit value and will wrap to 0 when this occurs.'
    status = 'current'

class PerfCounter32(TextualConvention, Counter32):
    description = 'This type represents a non-negative 32-bit integer. The initial value of this integer will be 0. It will increment with time, however, the value will revert back to 0 when the time period for history interval elapses. Typically, this will be noticed at 15minute intervals and 1 day intervals. Only the rollover interval periods will keep counting to a maximum 32-bit value and will wrap to 0 when this occurs.'
    status = 'current'

class IpVersion(TextualConvention, Integer32):
    description = 'This type allows choice of IPv4 or IPv6 address specification.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("ipv4", 1), ("ipv6", 2))

class IpPriorityMapMode(TextualConvention, Integer32):
    description = 'This type allows choice of IP Priority Mapping Mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("not-applicable", 0), ("none", 1), ("priomap-tos", 2), ("priomap-dscp", 3))

class PriorityMapMode(TextualConvention, Integer32):
    description = 'This type allows choice of Priority Mapping Mode.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("priomap-none", 1), ("priomap-tos", 2), ("priomap-dscp", 3), ("priomap-8021p", 4), ("priomap-8021p-inner", 5))

class SfpConnectorValue(TextualConvention, Integer32):
    description = 'This lists the SFP connector values.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16))
    namedValues = NamedValues(("not-applicable", 0), ("unknown", 1), ("sc", 2), ("fcs1cu", 3), ("fcs2cu", 4), ("bnc-tnc", 5), ("fccoaxhdr", 6), ("fjack", 7), ("lc", 8), ("mt-rj", 9), ("mu", 10), ("sg", 11), ("optpigtail", 12), ("hssdc", 13), ("cupigtail", 14), ("vendorspecific", 15), ("rj45", 16))

class RestartType(TextualConvention, Integer32):
    description = 'Restart Type used across all card types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-applicable", 0), ("warm-start", 1), ("cold-start", 2))

class SfpMediaType(TextualConvention, Integer32):
    description = 'Describes the SFP Media Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4))
    namedValues = NamedValues(("not-applicable", 0), ("singlemode", 1), ("multimode", 2), ("multimode62-5", 3), ("copper", 4))

class ScheduleType(TextualConvention, Integer32):
    description = 'Describes the Schedule Type of a scheduled operation.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("periodic", 1), ("one-shot", 2))

class SchedActivityStatus(TextualConvention, Integer32):
    description = 'Scheduled Group Activity Status.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("initial", 1), ("active", 2), ("suspended", 3), ("completed", 4))

class SchedActivityAction(TextualConvention, Integer32):
    description = 'Scheduled Activity Action.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-applicable", 0), ("suspend", 1), ("resume", 2))

class MepDestinationType(TextualConvention, Integer32):
    description = 'Destination MEP Types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("not-applicable", 0), ("mepid", 1), ("macaddress", 2))

class ClassOfServiceType(TextualConvention, Integer32):
    description = 'Class of Service Types.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3, 4, 5, 6, 7, 8))
    namedValues = NamedValues(("cos-not-applicable", 0), ("cos-zero", 1), ("cos-one", 2), ("cos-two", 3), ("cos-three", 4), ("cos-four", 5), ("cos-five", 6), ("cos-six", 7), ("cos-seven", 8))

class SignalDirectionType(TextualConvention, Integer32):
    description = 'Signal Direction Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("input", 1), ("output", 2))

class AfpTagControl(TextualConvention, Integer32):
    description = 'Describes the Afp Tag Control.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("ctag", 1), ("stag", 2), ("both", 3))

class CmP2PFlowType(TextualConvention, Integer32):
    description = 'Describes the Agg Flow Type,incluing e-line.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1))
    namedValues = NamedValues(("eline", 1))

class CmTrafficACLPriorityType(TextualConvention, Integer32):
    description = 'Describes the Traffic acl priority type, including tos, dscp and traffic class.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notApplicable", 0), ("acl-tos", 1), ("acl-dscp", 2))

class CmTrafficAclFilterActionType(TextualConvention, Integer32):
    description = 'Enumerations for Access Control List permit - Permit access, deny - Deny access.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("permit", 1), ("deny", 2))

class CmTrafficAclFilterType(TextualConvention, Integer32):
    description = 'Describes the Traffic acl filter type, including MAC IPV4 IPV6.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("mac", 1), ("ipv4", 2), ("ipv6", 3))

class CmTrafficAclProtocolType(TextualConvention, Integer32):
    description = 'Describes the Traffic acl protocol type, including tcp udp.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2))
    namedValues = NamedValues(("notApplicable", 0), ("tcp", 1), ("udp", 2))

class VlanEthertype(TextualConvention, Integer32):
    description = 'Describes the Vlan Ether Type, cvlan, svlan.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("cvlan", 1), ("svlan", 2))

class CmPmBinAction(TextualConvention, Integer32):
    description = 'Provides ability to clear the contents of PM bin.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1))
    namedValues = NamedValues(("not-applicable", 0), ("clear", 1))

class CmPmIntervalType(TextualConvention, Integer32):
    description = 'Describes the Performance Monitoring Interval Type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("interval-15min", 1), ("interval-1day", 2), ("rollover", 3), ("interval-5min", 4))

class TDMFrequencySourceType(TextualConvention, Integer32):
    description = 'Enumerations for TDM Frequency Source loopTiming, systemTiming, lineTiming'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(0, 1, 2, 3))
    namedValues = NamedValues(("notApplicable", 0), ("loopTiming", 1), ("systemTiming", 2), ("lineTiming", 3))

class F3DisplayString(TextualConvention, OctetString):
    description = 'This object is similar with DisplayString, and the difference is its length is 2047. Any object defined using this syntax may not exceed 2047 characters in length.'
    status = 'current'
    displayHint = '2047a'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 2047)

class Decimal32(TextualConvention, Unsigned32):
    description = 'The value is encoded in a Decimal32 interchange format. The decimal value should be calculated as follows: (−1)^sign x 10^(exponent−101) x mantissa The individual components of the equation are coded in two different formats depending on the range of the mantissa. Format A: Second and third bits can be: 00, 01 or 10 s EEeeeeee mmmmmmm mmmmmmmm mmmmmmmm sign: coded on a 1 bit - s exponent: coded on 8 bits - EEeeeeee where EE: 00, 01 or 10 mantissa: coded on 24 bits - 0mmmmmmm mmmmmmmm mmmmmmmm Format B: For a larger mantissa. Second and third bits are: 11 s 11 EEeeeeee mmmmm mmmmmmmm mmmmmmmm sign: coded on a 1 bit - s exponent: coded on 8 bits - EEeeeeee where EE: 00, 01 or 10 mantissa: coded on 24 bits - 100mmmmm mmmmmmmm mmmmmmmm'
    status = 'current'

class UserInterfaceType(TextualConvention, Integer32):
    description = 'Denotes used user interface type.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cli", 1), ("gui", 2), ("netconf", 3), ("snmp", 4))

class FlowSecState(TextualConvention, Integer32):
    description = 'Flow secure state.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("secureNormal", 1), ("secureBlocked", 2), ("unsecureNormal", 3), ("unsecureBlocked", 4))

mibBuilder.exportSymbols("CM-COMMON-MIB", OperationalState=OperationalState, ge112Pro=ge112Pro, sh1pcs=sh1pcs, IpVersion=IpVersion, SfpMediaType=SfpMediaType, ge114SH=ge114SH, nemihubshelf=nemihubshelf, CmP2PFlowType=CmP2PFlowType, PortType=PortType, FlowSecState=FlowSecState, EthernetPortSpeed=EthernetPortSpeed, ge114ProC=ge114ProC, TrafficDirection=TrafficDirection, Decimal32=Decimal32, ge114PH=ge114PH, CmTrafficAclProtocolType=CmTrafficAclProtocolType, AfpTagControl=AfpTagControl, TDMFrequencySourceType=TDMFrequencySourceType, ge206=ge206, ge206v=ge206v, CmPmBinAction=CmPmBinAction, gesyncprobe=gesyncprobe, ge114ProSH=ge114ProSH, ge201se=ge201se, cmagg=cmagg, ge114H=ge114H, ge114ProCSH=ge114ProCSH, SfpConnectorValue=SfpConnectorValue, cmCommonMIB=cmCommonMIB, AdminState=AdminState, SignalDirectionType=SignalDirectionType, ge112=ge112, VlanEthertype=VlanEthertype, CmPmIntervalType=CmPmIntervalType, ge101=ge101, CmTrafficAclFilterType=CmTrafficAclFilterType, VlanPriority=VlanPriority, EthernetMediaType=EthernetMediaType, PerfCounter32=PerfCounter32, PYSNMP_MODULE_ID=cmCommonMIB, F3DisplayString=F3DisplayString, VlanTagType=VlanTagType, SecondaryState=SecondaryState, t1804=t1804, SchedActivityAction=SchedActivityAction, ge206f=ge206f, RestartType=RestartType, ClassOfServiceType=ClassOfServiceType, PerfCounter64=PerfCounter64, ScheduleType=ScheduleType, t3204=t3204, VlanId=VlanId, SchedActivityStatus=SchedActivityStatus, ge114ProHE=ge114ProHE, ge114G=ge114G, UserInterfaceType=UserInterfaceType, CmTrafficAclFilterActionType=CmTrafficAclFilterActionType, PriorityMapMode=PriorityMapMode, ge112ProM=ge112ProM, xg210=xg210, subproducts=subproducts, ge114=ge114, ge114S=ge114S, ge112ProH=ge112ProH, IpPriorityMapMode=IpPriorityMapMode, xg210c=xg210c, f3Capabilities=f3Capabilities, MepDestinationType=MepDestinationType, CmTrafficACLPriorityType=CmTrafficACLPriorityType, ge114Pro=ge114Pro, ge201=ge201)
