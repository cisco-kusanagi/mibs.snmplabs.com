#
# PySNMP MIB module MPLS-TC-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/MPLS-TC-EXT-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:14:14 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, ObjectIdentifier, Integer = mibBuilder.importSymbols("ASN1", "OctetString", "ObjectIdentifier", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ValueRangeConstraint, ConstraintsUnion, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsUnion", "ConstraintsIntersection")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Counter32, MibIdentifier, ModuleIdentity, IpAddress, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, Bits, ObjectIdentity, Unsigned32, TimeTicks, Integer32, Gauge32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Counter32", "MibIdentifier", "ModuleIdentity", "IpAddress", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Bits", "ObjectIdentity", "Unsigned32", "TimeTicks", "Integer32", "Gauge32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
mplsTcExtStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 17))
mplsTcExtStdMIB.setRevisions(('2015-02-02 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: mplsTcExtStdMIB.setRevisionsDescriptions(('MPLS Textual Convention Extensions',))
if mibBuilder.loadTexts: mplsTcExtStdMIB.setLastUpdated('201502020000Z')
if mibBuilder.loadTexts: mplsTcExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: mplsTcExtStdMIB.setContactInfo(' Venkatesan Mahalingam Dell Inc, 5450 Great America Parkway, Santa Clara, CA 95054, USA Email: venkat.mahalingams@gmail.com Kannan KV Sampath Redeem, India Email: kannankvs@gmail.com Sam Aldrin Huawei Technologies 2330 Central Express Way, Santa Clara, CA 95051, USA Email: aldrin.ietf@gmail.com Thomas D. Nadeau Email: tnadeau@lucidvision.com ')
if mibBuilder.loadTexts: mplsTcExtStdMIB.setDescription("This MIB module contains Textual Conventions for LSPs of MPLS- based transport networks. Copyright (c) 2015 IETF Trust and the persons identified as authors of the code. All rights reserved. Redistribution and use in source and binary forms, with or without modification, is permitted pursuant to, and subject to the license terms contained in, the Simplified BSD License set forth in Section 4.c of the IETF Trust's Legal Provisions Relating to IETF Documents (http://trustee.ietf.org/license-info).")
class MplsGlobalId(TextualConvention, OctetString):
    reference = 'MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370, Section 3'
    description = "This object contains the Textual Convention for an IP-based operator-unique identifier (Global_ID). The Global_ID can contain the 2-octet or 4-octet value of the operator's Autonomous System Number (ASN). When the Global_ID is derived from a 2-octet ASN, the two high-order octets of this 4-octet identifier MUST be set to zero (0x00). Further, ASN 0 is reserved. The size of the Global_ID string MUST be zero if the Global_ID is invalid. Note that a Global_ID of zero is limited to entities contained within a single operator and MUST NOT be used across a Network-to-Network Interface (NNI). A non-zero Global_ID MUST be derived from an ASN owned by the operator."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class MplsCcId(TextualConvention, OctetString):
    reference = 'MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3. International Reference Alphabet (IRA) (Formerly International Alphabet No. 5 or IA5) - Information technology - 7-bit coded character set for information exchange, ITU-T Recommendation T.50, September 1992.'
    description = 'The CC (Country Code) is a string of two characters, each being an uppercase Basic Latin alphabetic (i.e., A-Z). The characters are encoded using ITU-T Recommendation T.50. The size of the CC string MUST be zero if the CC identifier is invalid.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(2, 2), )
class MplsIccId(TextualConvention, OctetString):
    reference = 'MPLS-TP Identifiers Following ITU-T Conventions, RFC 6923, Section 3. International Reference Alphabet (IRA) (Formerly International Alphabet No. 5 or IA5) - Information technology - 7-bit coded character set for information exchange, ITU-T Recommendation T.50, September 1992.'
    description = 'The ICC is a string of one to six characters, each an uppercase Basic Latin alphabetic (i.e., A-Z) or numeric (i.e., 0-9). The characters are encoded using ITU-T Recommendation T.50. The size of the ICC string MUST be zero if the ICC identifier is invalid.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(1, 6), )
class MplsNodeId(TextualConvention, Unsigned32):
    reference = 'MPLS Transport Profile (MPLS-TP) Identifiers, RFC 6370, Section 4'
    description = "The Node_ID is assigned within the scope of the Global_ID/ICC_Operator_ID. When IPv4 addresses are in use, the value of this object can be derived from the LSR's IPv4 loopback address. When IPv6 addresses are in use, the value of this object can be a 32-bit value unique within the scope of a Global_ID. Note that, when IP reachability is not needed, the 32-bit Node_ID is not required to have any association with the IPv4 address space. The value of 0 indicates an invalid Node_ID."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ConstraintsUnion(ValueRangeConstraint(0, 0), ValueRangeConstraint(1, 4294967295), )
mibBuilder.exportSymbols("MPLS-TC-EXT-STD-MIB", MplsCcId=MplsCcId, PYSNMP_MODULE_ID=mplsTcExtStdMIB, MplsNodeId=MplsNodeId, MplsIccId=MplsIccId, mplsTcExtStdMIB=mplsTcExtStdMIB, MplsGlobalId=MplsGlobalId)
