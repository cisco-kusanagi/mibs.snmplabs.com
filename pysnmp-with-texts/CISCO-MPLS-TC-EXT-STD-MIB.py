#
# PySNMP MIB module CISCO-MPLS-TC-EXT-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-MPLS-TC-EXT-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 12:00:30 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueRangeConstraint, SingleValueConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueRangeConstraint", "SingleValueConstraint")
ciscoExperiment, = mibBuilder.importSymbols("CISCO-SMI", "ciscoExperiment")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
MibIdentifier, IpAddress, Gauge32, Unsigned32, ObjectIdentity, Integer32, Counter32, Counter64, Bits, TimeTicks, iso, NotificationType, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "MibIdentifier", "IpAddress", "Gauge32", "Unsigned32", "ObjectIdentity", "Integer32", "Counter32", "Counter64", "Bits", "TimeTicks", "iso", "NotificationType", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
cmplsTcExtStdMIB = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 10, 144))
cmplsTcExtStdMIB.setRevisions(('2012-02-22 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: cmplsTcExtStdMIB.setRevisionsDescriptions(('MPLS Textual Convention Extensions',))
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setLastUpdated('201202220000Z')
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setOrganization('Multiprotocol Label Switching (MPLS) Working Group')
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setContactInfo('Venkatesan Mahalingam Dell Inc, 350 Holger way, San Jose, CA, USA Email: venkat.mahalingams@gmail.com Kannan KV Sampath Aricent, India Email: Kannan.Sampath@aricent.com Sam Aldrin Huawei Technologies 2330 Central Express Way, Santa Clara, CA 95051, USA Email: aldrin.ietf@gmail.com Thomas D. Nadeau CA Technologies 273 Corporate Drive, Portsmouth, NH, USA Email: thomas.nadeau@ca.com')
if mibBuilder.loadTexts: cmplsTcExtStdMIB.setDescription('Copyright (c) 2012 IETF Trust and the persons identified as the document authors. All rights reserved. This MIB module contains Textual Conventions for MPLS based transport networks.')
class CMplsGlobalId(TextualConvention, OctetString):
    description = "This object contains the Textual Convention of IP based operator unique identifier (Global_ID), the Global_ID can contain the 2-octet or 4-octet value of the operator's Autonomous System Number (ASN). It is expected that the Global_ID will be derived from the globally unique ASN of the autonomous system hosting the PEs containing the actual AIIs. The presence of a Global_ID based on the operator's ASN ensures that the AII will be globally unique. When the Global_ID is derived from a 2-octet AS number, the two high-order octets of this 4-octet identifier MUST be set to zero. Further ASN 0 is reserved. A Global_ID of zero means that no Global_ID is present. Note that a Global_ID of zero is limited to entities contained within a single operator and MUST NOT be used across an NNI. A non-zero Global_ID MUST be derived from an ASN owned by the operator."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(4, 4)
    fixedLength = 4

class CMplsNodeId(TextualConvention, Unsigned32):
    description = "The Node_ID is assigned within the scope of the Global_ID. The value 0(or 0.0.0.0 in dotted decimal notation) is reserved and MUST NOT be used. When IPv4 addresses are in use, the value of this object can be derived from the LSR's /32 IPv4 loop back address. When IPv6 addresses are in use, the value of this object can be a 32-bit value unique within the scope of a Global_ID. Note that, when IP reach ability is not needed, the 32-bit Node_ID is not required to have any association with the IPv4 address space."
    status = 'current'
    displayHint = 'd'

class CMplsIccId(TextualConvention, OctetString):
    description = 'The ICC is a string of one to six characters, each character being either alphabetic (i.e. A-Z) or numeric (i.e. 0-9) characters. Alphabetic characters in the ICC SHOULD be represented with upper case letters.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(1, 6)

class CMplsLocalId(TextualConvention, Unsigned32):
    description = "This textual convention is used in accommodating the bigger size Global_Node_ID and/or ICC with lower size LSR identifier in order to index the mplsTunnelTable. The Local Identifier is configured between 1 and 16777215, as valid IP address range starts from 16777216(01.00.00.00). This range is chosen to identify the mplsTunnelTable's Ingress/Egress LSR-id is IP address or Local identifier, if the configured range is not IP address, administrator is expected to retrieve the complete information (Global_Node_ID or ICC) from mplsNodeConfigTable. This way, existing mplsTunnelTable is reused for bidirectional tunnel extensions for MPLS based transport networks. This Local Identifier allows the administrator to assign a unique identifier to map Global_Node_ID and/or ICC."
    status = 'current'
    displayHint = 'd'
    subtypeSpec = Unsigned32.subtypeSpec + ValueRangeConstraint(1, 16777215)

mibBuilder.exportSymbols("CISCO-MPLS-TC-EXT-STD-MIB", CMplsIccId=CMplsIccId, CMplsNodeId=CMplsNodeId, CMplsLocalId=CMplsLocalId, cmplsTcExtStdMIB=cmplsTcExtStdMIB, PYSNMP_MODULE_ID=cmplsTcExtStdMIB, CMplsGlobalId=CMplsGlobalId)
