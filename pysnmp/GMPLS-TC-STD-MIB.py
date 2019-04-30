#
# PySNMP MIB module GMPLS-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/GMPLS-TC-STD-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:06:13 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint, SingleValueConstraint, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint", "SingleValueConstraint", "ValueSizeConstraint")
mplsStdMIB, = mibBuilder.importSymbols("MPLS-TC-STD-MIB", "mplsStdMIB")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
NotificationType, Gauge32, IpAddress, MibIdentifier, Bits, Unsigned32, Integer32, ModuleIdentity, iso, Counter64, MibScalar, MibTable, MibTableRow, MibTableColumn, TimeTicks, Counter32, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "Gauge32", "IpAddress", "MibIdentifier", "Bits", "Unsigned32", "Integer32", "ModuleIdentity", "iso", "Counter64", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "TimeTicks", "Counter32", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
gmplsTCStdMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 10, 166, 12))
gmplsTCStdMIB.setRevisions(('2007-02-28 00:00',))
if mibBuilder.loadTexts: gmplsTCStdMIB.setLastUpdated('200702280000Z')
if mibBuilder.loadTexts: gmplsTCStdMIB.setOrganization('IETF Common Control and Measurement Plane (CCAMP) Working Group')
class GmplsFreeformLabelTC(TextualConvention, OctetString):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3.2.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 64)

class GmplsLabelTypeTC(TextualConvention, Integer32):
    reference = '1. Generalized Multi-Protocol Label Switching (GMPLS) Signaling Functional Description, RFC 3471, section 3. 2. Definition of Textual Conventions and for Multiprotocol Label Switching (MPLS) Management, RFC 3811, section 3. 3. Generalized Multi-Protocol Label Switching (GMPLS) Extensions for Synchronous Optical Network (SONET) and Synchronous Digital Hierarchy (SDH) Control, RFC 4606.'
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4, 5, 6))
    namedValues = NamedValues(("gmplsMplsLabel", 1), ("gmplsPortWavelengthLabel", 2), ("gmplsFreeformGeneralizedLabel", 3), ("gmplsSonetLabel", 4), ("gmplsSdhLabel", 5), ("gmplsWavebandLabel", 6))

class GmplsSegmentDirectionTC(TextualConvention, Integer32):
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2))
    namedValues = NamedValues(("forward", 1), ("reverse", 2))

mibBuilder.exportSymbols("GMPLS-TC-STD-MIB", GmplsSegmentDirectionTC=GmplsSegmentDirectionTC, GmplsLabelTypeTC=GmplsLabelTypeTC, gmplsTCStdMIB=gmplsTCStdMIB, GmplsFreeformLabelTC=GmplsFreeformLabelTC, PYSNMP_MODULE_ID=gmplsTCStdMIB)
