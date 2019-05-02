#
# PySNMP MIB module IANA-SMF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-SMF-MIB
# Produced by pysmi-0.3.4 at Wed May  1 13:50:29 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, OctetString, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "Integer", "OctetString", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueSizeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueSizeConstraint", "SingleValueConstraint")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
iso, Integer32, ObjectIdentity, Gauge32, Unsigned32, Bits, mib_2, Counter32, ModuleIdentity, IpAddress, Counter64, MibIdentifier, TimeTicks, MibScalar, MibTable, MibTableRow, MibTableColumn, NotificationType = mibBuilder.importSymbols("SNMPv2-SMI", "iso", "Integer32", "ObjectIdentity", "Gauge32", "Unsigned32", "Bits", "mib-2", "Counter32", "ModuleIdentity", "IpAddress", "Counter64", "MibIdentifier", "TimeTicks", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "NotificationType")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ianaSmfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 225))
ianaSmfMIB.setRevisions(('2014-10-10 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ianaSmfMIB.setRevisionsDescriptions(("Initial version of this MIB as published in RFC 7367. Copyright (c) 2014 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info). ",))
if mibBuilder.loadTexts: ianaSmfMIB.setLastUpdated('201410100000Z')
if mibBuilder.loadTexts: ianaSmfMIB.setOrganization('IANA')
if mibBuilder.loadTexts: ianaSmfMIB.setContactInfo('Internet Assigned Numbers Authority Postal: ICANN 12025 Waterfront Drive, Suite 300 Los Angeles, CA 90094-2536 United States Tel: +1 310 301 5800 EMail: iana@iana.org')
if mibBuilder.loadTexts: ianaSmfMIB.setDescription('This MIB module defines the IANAsmfOpModeIdTC and IANAsmfRssaIdTC Textual Conventions, and thus the enumerated values of the smfCapabilitiesOpModeID and smfCapabilitiesRssaID objects defined in the SMF-MIB.')
class IANAsmfOpModeIdTC(TextualConvention, Integer32):
    reference = "See Section 7.2 'Reduced Relay Set Forwarding', and the Appendices A, B, and C in RFC 6621 - 'Simplified Multicast Forwarding', Macker, J., Ed., May 2012."
    description = "An index that identifies through reference to a specific SMF operations mode. There are basically three styles of SMF operation with reduced relay sets currently identified: Independent operation 'independent(1)' - SMF performs its own relay set selection using information from an associated MANET NHDP process. CDS-aware unicast routing operation 'routing(2)'- a coexistent unicast routing protocol provides dynamic relay set state based upon its own control plane Connected Dominating Set (CDS) or neighborhood discovery information. Cross-layer operation 'crossLayer(3)' - SMF operates using neighborhood status and triggers from a cross-layer information base for dynamic relay set selection and maintenance. IANA MUST update this Textual Convention accordingly. The definition of this Textual Convention with the addition of newly assigned values is updated periodically by the IANA, in the IANA-maintained registries. (The latest arrangements can be obtained by contacting the IANA.) Requests for new values SHOULD be made to IANA via email (iana@iana.org)."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("independent", 1), ("routing", 2), ("crossLayer", 3))

class IANAsmfRssaIdTC(TextualConvention, Integer32):
    reference = "For example, see: Section 8.1.1. 'SMF Message TLV Type' and the Appendices A, B, and C in RFC 6621 - 'Simplified Multicast Forwarding', Macker, J., Ed., May 2012. RFC 3626 - Clausen, T., Ed., and P. Jacquet, Ed., 'Optimized Link State Routing Protocol (OLSR)', October 2003. RFC 5614 - Ogier, R. and P. Spagnolo, 'Mobile Ad Hoc Network (MANET) Extension of OSPF Using Connected Dominating Set (CDS) Flooding', August 2009. RFC 7181 - Clausen, T., Dearlove, C., Jacquet, P., and U. Herberg, 'The Optimized Link State Routing Protocol Version 2', April 2014."
    description = 'An index that identifies through reference to specific RSSAs. Several are currently defined in the Appendices A, B, and C of RFC 6621. Examples of RSSAs already identified within this Textual Convention (TC) are: Classical Flooding (cF(1)) - is the standard flooding algorithm where each node in the next retransmits the information on each of its interfaces. Source-Based Multipoint Relay (sMPR(2)) - this algorithm is used by Optimized Link State Routing (OLSR) and OLSR version 2 (OLSRv2) protocols for the relay of link state updates and other control information (RFC 3626, RFC 7181). Since each router picks its neighboring relays independently, sMPR forwarders depend upon previous hop information (e.g., source Media Access Control (MAC) address) to operate correctly. Essential Connected Dominating Set (eCDS(3)) - defined in RFC 5614, this algorithm forms a single CDS mesh for the SMF operating region. Its packet-forwarding rules are not dependent upon previous hop knowledge in contrast to sMPR. Multipoint Relay Connected Dominating Set (mprCDS(4)) - This algorithm is an extension to the basic sMPR election algorithm that results in a shared (non-source-specific) SMF CDS. Thus, its forwarding rules are not dependent upon previous hop information, similar to eCDS. IANA MUST update this Textual Convention accordingly. The definition of this Textual Convention with the addition of newly assigned values is updated periodically by the IANA, in the IANA-maintained registries. (The latest arrangements can be obtained by contacting the IANA.) Requests for new values SHOULD be made to IANA via email (iana@iana.org).'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cF", 1), ("sMPR", 2), ("eCDS", 3), ("mprCDS", 4))

mibBuilder.exportSymbols("IANA-SMF-MIB", IANAsmfOpModeIdTC=IANAsmfOpModeIdTC, IANAsmfRssaIdTC=IANAsmfRssaIdTC, PYSNMP_MODULE_ID=ianaSmfMIB, ianaSmfMIB=ianaSmfMIB)
