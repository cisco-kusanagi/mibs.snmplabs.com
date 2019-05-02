#
# PySNMP MIB module HP-SN-MPLS-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/HP-SN-MIBS
# Produced by pysmi-0.3.4 at Wed May  1 13:36:22 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion")
snMpls, = mibBuilder.importSymbols("HP-SN-ROOT-MIB", "snMpls")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
Bits, MibIdentifier, TimeTicks, Integer32, Unsigned32, NotificationType, iso, Counter64, Gauge32, ObjectIdentity, Counter32, IpAddress, transmission, MibScalar, MibTable, MibTableRow, MibTableColumn, ModuleIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "Bits", "MibIdentifier", "TimeTicks", "Integer32", "Unsigned32", "NotificationType", "iso", "Counter64", "Gauge32", "ObjectIdentity", "Counter32", "IpAddress", "transmission", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "ModuleIdentity")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsTCMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15, 1))
mplsTCMIB.setRevisions(('2001-01-04 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsTCMIB.setRevisionsDescriptions(('Initial version published as part of RFC XXXX.',))
if mibBuilder.loadTexts: mplsTCMIB.setLastUpdated('200101041200Z')
if mibBuilder.loadTexts: mplsTCMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsTCMIB.setContactInfo(' Thomas D. Nadeau Cisco Systems, Inc. tnadeau@cisco.com Joan Cucchiara Crescent Networks jcucchiara@crescentnetworks.com Cheenu Srinivasan Parama Networks, Inc. cheenu@paramanet.com Arun Viswanathan Force10 Networks, Inc. arun@force10networks.com Hans Sjostrand ipUnplugged hans@ipunplugged.com Email comments to the MPLS WG Mailing List at mpls@uu.net.')
if mibBuilder.loadTexts: mplsTCMIB.setDescription('This MIB module defines Textual Conventions and OBJECT-IDENTITIES for use in documents defining management information bases (MIBs) for managing MPLS networks.')
mplsMIB = MibIdentifier((1, 3, 6, 1, 4, 1, 11, 2, 3, 7, 11, 12, 2, 15, 15))
class MplsAtmVcIdentifier(TextualConvention, Integer32):
    reference = 'Definitions of Textual Conventions and OBJECT- IDENTITIES for ATM Management, RFC 2514, Feb. 1999.'
    description = 'The VCI value for a VCL. The maximum VCI value cannot exceed the value allowable by atmInterfaceMaxVciBits defined in ATM-MIB. The minimum value is 32, values 0 to 31 are reserved for other uses by the ITU and ATM Forum. 32 is typically the default value for the Control VC.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(32, 65535)

class MplsBitRate(TextualConvention, Integer32):
    description = "An estimate of bandwidth in units of 1,000 bits per second. If this object reports a value of 'n' then the rate of the object is somewhere in the range of 'n-500' to 'n+499'. For objects which do not vary in bit rate, or for those where no accurate estimation can be made, this object should contain the nominal bit rate."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 2147483647)

class MplsBurstSize(TextualConvention, Unsigned32):
    description = 'The number of octets of MPLS data that the stream may send back-to-back without concern for policing.'
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 4294967295)

class MplsExtendedTunnelId(TextualConvention, Unsigned32):
    reference = '1. Awduche, D., et al., RSVP-TE: Extensions to RSVP for LSP Tunnels, RFC 3209, December 2001. 2. Constraint-Based LSP Setup using LDP, Jamoussi, B., et al., draft-ietf-mpls-cr-ldp-06.txt, November 2001.'
    description = 'A unique identifier for an MPLS Tunnel. This MAY represent an IpV4 address of the ingress or egress LSR for the tunnel. This value is derived from the Extended Tunnel Id in RSVP or the Ingress Router ID for CR-LDP.'
    status = 'current'

class MplsInitialCreationSource(TextualConvention, Integer32):
    description = 'The entity that originally created the object in question. The values of this enumeration are defined as follows: other(1) - This is used when an entity which has not been enumerated in this textual convention but which is known by the agent. snmp(2) - The Simple Network Management Protocol was used to configure this object initially. ldp(3 - The Label Distribution Protocol was used to configure this object initially. rsvp(4) - The Resource Reservation Protocol was used to configure this object initially. crldp(5) - The Constraint-Based Label Distribution Protocol was used to configure this object initially. policyAgent(6) - A policy agent (perhaps in combination with one of the above protocols) was used to configure this object initially. unknown(7) - the agent cannot discern which component created the object.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6, 7))
    namedValues = NamedValues(("other", 1), ("snmp", 2), ("ldp", 3), ("rsvp", 4), ("crldp", 5), ("policyAgent", 6), ("unknown", 7))

class MplsLSPID(TextualConvention, OctetString):
    description = 'An identifier that is assigned to each LSP and is used to uniquely identify it. This is assigned at the head end of the LSP and can be used by all LSRs to identify this LSP. This value is piggybacked by the signaling protocol when this LSP is signaled within the network. This identifier can then be used at each LSR to identify which labels are being swapped to other labels for this LSP. For IPv4 addresses this results in a 6-octet long cookie.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 31)

class MplsLabel(TextualConvention, Unsigned32):
    reference = '1. Multiprotocol Label Switching Architecture, Rosen et al, RFC 3031, August 1999. 2. MPLS Label Stack Encoding, Rosen et al, RFC 3032, January 2001. 3. Use of Label Switching on Frame Relay Networks, Conta et al, RFC 3034, January 2001. 4. MPLS using LDP and ATM VC switching, Davie et al, RFC 3035, January 2001.'
    description = 'This value represents an MPLS label as defined in [RFC3031], [RFC3032], [RFC3034] and [RFC3035].'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 4294967295)

class MplsLdpGenAddr(TextualConvention, OctetString):
    description = 'The value of an network layer or data link layer address.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class MplsLdpIdentifier(TextualConvention, OctetString):
    description = 'The LDP identifier is a six octet quantity which is used to identify an Label Switch Router (LSR) label space. The first four octets identify the LSR and must be a globally unique value, such as a 32-bit router ID assigned to the LSR, and the last two octets identify a specific label space within the LSR.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(6, 6)
    fixedLength = 6

class MplsLdpLabelTypes(TextualConvention, Integer32):
    description = 'The Layer 2 label types which are defined for MPLS LDP/CRLDP are generic(1), atm(2), or frameRelay(3).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("generic", 1), ("atm", 2), ("frameRelay", 3))

class MplsLsrIdentifier(TextualConvention, OctetString):
    description = 'The Label Switch Router (LSR) identifier is the first 4 bytes of the Label Distribution Protocol (LDP) identifier.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsPathIndex(TextualConvention, Unsigned32):
    description = 'A unique identifier used to identify a specific path used by a tunnel.'
    status = 'current'

class MplsPathIndexOrZero(TextualConvention, Unsigned32):
    description = 'A unique identifier used to identify a specific path used by a tunnel. If this value is set to 0, it indicates that no path is in use.'
    status = 'current'

class MplsPortNumber(TextualConvention, Integer32):
    description = 'A TCP or UDP port number. Along with an IP address identifies a stream of IP traffic uniquely.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(0, 65535)

class MplsTunnelAffinity(TextualConvention, Unsigned32):
    description = 'Include-any, include-all, or exclude-all constraint for link selection.'
    status = 'current'

class MplsTunnelIndex(TextualConvention, Integer32):
    description = 'Index into mplsTunnelTable.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ValueRangeConstraint(1, 65535)

class MplsTunnelInstanceIndex(TextualConvention, Unsigned32):
    description = 'Instance index into mplsTunnelTable.'
    status = 'current'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(0, 65535)

mibBuilder.exportSymbols("HP-SN-MPLS-TC-MIB", MplsLSPID=MplsLSPID, MplsTunnelInstanceIndex=MplsTunnelInstanceIndex, mplsTCMIB=mplsTCMIB, MplsBurstSize=MplsBurstSize, MplsInitialCreationSource=MplsInitialCreationSource, MplsPortNumber=MplsPortNumber, MplsLdpIdentifier=MplsLdpIdentifier, MplsPathIndexOrZero=MplsPathIndexOrZero, PYSNMP_MODULE_ID=mplsTCMIB, MplsAtmVcIdentifier=MplsAtmVcIdentifier, MplsExtendedTunnelId=MplsExtendedTunnelId, MplsLdpGenAddr=MplsLdpGenAddr, MplsLdpLabelTypes=MplsLdpLabelTypes, MplsBitRate=MplsBitRate, mplsMIB=mplsMIB, MplsTunnelIndex=MplsTunnelIndex, MplsPathIndex=MplsPathIndex, MplsTunnelAffinity=MplsTunnelAffinity, MplsLabel=MplsLabel, MplsLsrIdentifier=MplsLsrIdentifier)
