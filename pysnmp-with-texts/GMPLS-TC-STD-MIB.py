#
# PySNMP MIB module GMPLS-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GMPLS-TC-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:19:37 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Unsigned32, TimeTicks, Counter32, Integer32, ModuleIdentity, MibIdentifier, Gauge32, ObjectIdentity, NotificationType, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, IpAddress, iso, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "Unsigned32", "TimeTicks", "Counter32", "Integer32", "ModuleIdentity", "MibIdentifier", "Gauge32", "ObjectIdentity", "NotificationType", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "IpAddress", "iso", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
gmplsTCStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 12))
gmplsTCStdMIB.setRevisions(('2007-02-28 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: gmplsTCStdMIB.setRevisionsDescriptions(('Initial version published as part of RFC 4801.',))
if mibBuilder.loadTexts: gmplsTCStdMIB.setLastUpdated('200702280000Z')
if mibBuilder.loadTexts: gmplsTCStdMIB.setOrganization('IETF Common Control and Measurement Plane (CCAMP) Working Group')
if mibBuilder.loadTexts: gmplsTCStdMIB.setContactInfo(' Thomas D. Nadeau Cisco Systems, Inc. Email: tnadeau@cisco.com Adrian Farrel Old Dog Consulting Email: adrian@olddog.co.uk Comments about this document should be emailed directly to the CCAMP working group mailing list at ccamp@ops.ietf.org')
if mibBuilder.loadTexts: gmplsTCStdMIB.setDescription('Copyright (C) The IETF Trust (2007). This version of this MIB module is part of RFC 4801; see the RFC itself for full legal notices. This MIB module defines TEXTUAL-CONVENTIONs for concepts used in Generalized Multiprotocol Label Switching (GMPLS) networks.')
class GmplsFreeformLabelTC(TextualConvention, OctetString):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.2.'
    description = 'This TEXTUAL-CONVENTION can be used as the syntax of an object that contains any GMPLS Label. Objects with this syntax can be used to represent labels that have label types that are not defined in any RFCs. The freeform GMPLS Label may also be used by systems that do not wish to represent labels that have label types defined in RFCs using type-specific syntaxes.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class GmplsLabelTypeTC(TextualConvention, Integer32):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3. 2. Definition of Textual Conventions and for Multiprotocol Label Switching (MPLS) Management, RFC 3811, section 3. 3. Generalized Multi-Protocol Label Switching (GMPLS) Extensions for Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH) Control, RFC 4606.'
    description = 'Determines the interpretation that should be applied to an object that encodes a label. The possible types are: gmplsMplsLabel(1) - The label is an MPLS Packet, Cell, or Frame Label and is encoded as described for the TEXTUAL- CONVENTION MplsLabel defined in RFC 3811. gmplsPortWavelengthLabel(2) - The label is a Port or Wavelength Label as defined in RFC 3471. gmplsFreeformLabel(3) - The label is any form of label encoded as an OCTET STRING using the TEXTUAL-CONVENTION GmplsFreeformLabel. gmplsSonetLabel(4) - The label is a Synchronous Optical Network (SONET) Label as defined in RFC 4606. gmplsSdhLabel(5) - The label is a Synchronous Digital Hierarchy (SDH) Label as defined in RFC 4606. gmplsWavebandLabel(6) - The label is a Waveband Label as defined in RFC 3471.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("gmplsMplsLabel", 1), ("gmplsPortWavelengthLabel", 2), ("gmplsFreeformGeneralizedLabel", 3), ("gmplsSonetLabel", 4), ("gmplsSdhLabel", 5), ("gmplsWavebandLabel", 6))

class GmplsSegmentDirectionTC(TextualConvention, Integer32):
    description = "The direction of data flow on an Label Switched Path (LSP) segment with respect to the head of the LSP. Where an LSP is signaled using a conventional signaling protocol, the 'head' of the LSP is the source of the signaling (also known as the ingress) and the 'tail' is the destination (also known as the egress). For unidirectional LSPs, this usually matches the direction of flow of data. For manually configured unidirectional LSPs, the direction of the LSP segment matches the direction of flow of data. For manually configured bidirectional LSPs, an arbitrary decision must be made about which LER is the 'head'."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("forward", 1), ("reverse", 2))

mibBuilder.exportSymbols("GMPLS-TC-STD-MIB", PYSNMP_MODULE_ID=gmplsTCStdMIB, gmplsTCStdMIB=gmplsTCStdMIB, GmplsLabelTypeTC=GmplsLabelTypeTC, GmplsFreeformLabelTC=GmplsFreeformLabelTC, GmplsSegmentDirectionTC=GmplsSegmentDirectionTC)
