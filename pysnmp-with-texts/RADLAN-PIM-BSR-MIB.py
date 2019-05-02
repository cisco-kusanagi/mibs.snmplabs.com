#
# PySNMP MIB module RADLAN-PIM-BSR-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/RADLAN-PIM-BSR-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:48:05 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint")
IANAipRouteProtocol, = mibBuilder.importSymbols("IANA-RTPROTO-MIB", "IANAipRouteProtocol")
InterfaceIndexOrZero, InterfaceIndex = mibBuilder.importSymbols("IF-MIB", "InterfaceIndexOrZero", "InterfaceIndex")
InetAddressPrefixLength, InetAddress, InetVersion, InetAddressType = mibBuilder.importSymbols("INET-ADDRESS-MIB", "InetAddressPrefixLength", "InetAddress", "InetVersion", "InetAddressType")
rnd, = mibBuilder.importSymbols("RADLAN-MIB", "rnd")
NotificationGroup, ModuleCompliance, ObjectGroup = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "ObjectGroup")
ObjectIdentity, Bits, NotificationType, Gauge32, ModuleIdentity, IpAddress, MibIdentifier, Unsigned32, Counter32, Integer32, Counter64, iso, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "Bits", "NotificationType", "Gauge32", "ModuleIdentity", "IpAddress", "MibIdentifier", "Unsigned32", "Counter32", "Integer32", "Counter64", "iso", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention, TruthValue, RowStatus = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention", "TruthValue", "RowStatus")
class AdminStatus(TextualConvention, Integer32):
    description = 'The desired administrative state of a MIB row.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("adminStatusUp", 1), ("adminStatusDown", 2))

class OperStatus(TextualConvention, Integer32):
    description = 'The current operational state of a MIB row. This set of values is used by many Data Connection products written before 2006.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5))
    namedValues = NamedValues(("operStatusUp", 1), ("operStatusDown", 2), ("operStatusGoingUp", 3), ("operStatusGoingDown", 4), ("operStatusActFailed", 5))

rlPimBsrCandidateRPTable = MibTable((1, 3, 6, 1, 4, 1, 89, 220), )
if mibBuilder.loadTexts: rlPimBsrCandidateRPTable.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPTable.setDescription('The (conceptual) table listing the IP multicast group prefixes for which the local router is to advertise itself as a Candidate-RP.')
rlPimBsrCandidateRPEntry = MibTableRow((1, 3, 6, 1, 4, 1, 89, 220, 1), ).setIndexNames((0, "RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddressType"), (0, "RADLAN-PIM-BSR-MIB", "rlPimBsrCandidateRPAddress"))
if mibBuilder.loadTexts: rlPimBsrCandidateRPEntry.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPEntry.setDescription('An entry (conceptual row) in the rlPimBsrCandidateRPTable.')
rlPimBsrCandidateRPAddressType = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 1), InetAddressType())
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddressType.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddressType.setDescription('The Inet address type of the Candidate-RP.')
rlPimBsrCandidateRPAddress = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 2), InetAddress().subtype(subtypeSpec=ConstraintsUnion(ValueSizeConstraint(4, 4), ValueSizeConstraint(8, 8), ValueSizeConstraint(16, 16), )))
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddress.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPAddress.setDescription('The (unicast) address that will be advertised as a Candidate-RP. The InetAddressType is given by the rlPimBsrCandidateRPAddressType object. If this is not an address on the local router, DC-PIM will not advertise it as an C-RP address.')
rlPimBsrCandidateRPGroupPrefixList = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 3), DisplayString()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPGroupPrefixList.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPGroupPrefixList.setDescription("Identifies a standard access list containing the set of IP multicast group prefixes for which the local router will advertise itself as a Candidate-RP with the given RP address. If there is any rule in the list with aallStdAccessListIncluded set to 'false', DC-PIM does not advertise this RP address as a Candidate-RP. Otherwise DC-PIM advertises the RP address as a Candidate-RP for every IP multicast group prefix corresponding to a rule in the access list with row status 'active' and admin status 'up'. rlPimBsrCandidateRPGroupPrefixList defaults to an empty string, which indicates that no access list has yet been specified. rlPimBsrCandidateRPStatus can only be set to 'active' if a non-empty string has been specified for rlPimBsrCandidateRPGroupPrefixList.")
rlPimBsrCandidateRPBidir = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 5), TruthValue().clone('false')).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPBidir.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPBidir.setDescription('If this object is set to TRUE, this group range is advertised with this RP as a BIDIR-PIM group range. If it is set to FALSE, it is advertised as a PIM-SM group range. DC-PIM only supports the value FALSE for this object.')
rlPimBsrCandidateRPAdvTimer = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 6), TimeTicks()).setMaxAccess("readonly")
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvTimer.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvTimer.setDescription('The time remaining before the local router next sends a Candidate-RP-Advertisement to the elected BSR. This will be zero if the C-RP is shutting down or any of the following conditions are true: - the entity is not active - the row is inactive - the group prefix list is invalid - the configured C-RP address is not local.')
rlPimBsrCandidateRPPriority = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 7), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 255)).clone(192)).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPPriority.setReference('I-D.ietf-rlPim-sm-bsr section 3.2')
if mibBuilder.loadTexts: rlPimBsrCandidateRPPriority.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPPriority.setDescription('The priority for this Candidate RP advertised in Candidate-RP-Advertisements. Numerically higher values for this object indicate lower priorities, with the value zero denoting the highest priority.')
rlPimBsrCandidateRPAdvInterval = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 8), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(1, 26214)).clone(60)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvInterval.setReference('I-D.ietf-rlPim-sm-bsr section 3.2 and section 5')
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvInterval.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPAdvInterval.setDescription('A Candidate RP generates Candidate-RP-Advertisements periodically. This object represents the time interval in seconds between two consecutive advertisements.')
rlPimBsrCandidateRPHoldtime = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 9), Unsigned32().subtype(subtypeSpec=ValueRangeConstraint(0, 65535)).clone(150)).setUnits('seconds').setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPHoldtime.setReference('I-D.ietf-rlPim-sm-bsr section 4.2')
if mibBuilder.loadTexts: rlPimBsrCandidateRPHoldtime.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPHoldtime.setDescription('Holdtime for this Candidate RP. The amount of time (in seconds) this Candidate-RP entry is valid.')
rlPimBsrCandidateRPStatus = MibTableColumn((1, 3, 6, 1, 4, 1, 89, 220, 1, 10), RowStatus()).setMaxAccess("readcreate")
if mibBuilder.loadTexts: rlPimBsrCandidateRPStatus.setStatus('current')
if mibBuilder.loadTexts: rlPimBsrCandidateRPStatus.setDescription('The status of this row, by which new entries may be created, or old entries deleted from this table. All writable objects in this entry can be modified when the status of this entry is active(1).')
mibBuilder.exportSymbols("RADLAN-PIM-BSR-MIB", rlPimBsrCandidateRPBidir=rlPimBsrCandidateRPBidir, rlPimBsrCandidateRPAdvInterval=rlPimBsrCandidateRPAdvInterval, AdminStatus=AdminStatus, rlPimBsrCandidateRPAddress=rlPimBsrCandidateRPAddress, rlPimBsrCandidateRPHoldtime=rlPimBsrCandidateRPHoldtime, rlPimBsrCandidateRPAdvTimer=rlPimBsrCandidateRPAdvTimer, rlPimBsrCandidateRPTable=rlPimBsrCandidateRPTable, rlPimBsrCandidateRPStatus=rlPimBsrCandidateRPStatus, rlPimBsrCandidateRPEntry=rlPimBsrCandidateRPEntry, rlPimBsrCandidateRPGroupPrefixList=rlPimBsrCandidateRPGroupPrefixList, OperStatus=OperStatus, rlPimBsrCandidateRPPriority=rlPimBsrCandidateRPPriority, rlPimBsrCandidateRPAddressType=rlPimBsrCandidateRPAddressType)
