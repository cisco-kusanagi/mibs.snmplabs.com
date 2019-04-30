#
# PySNMP MIB module IANA-SMF-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/IANA-SMF-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 19:38:52 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ValueSizeConstraint, SingleValueConstraint, ConstraintsIntersection, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsIntersection", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
Counter32, NotificationType, iso, ObjectIdentity, MibIdentifier, mib_2, ModuleIdentity, Bits, TimeTicks, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, Integer32, Counter64, IpAddress = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "NotificationType", "iso", "ObjectIdentity", "MibIdentifier", "mib-2", "ModuleIdentity", "Bits", "TimeTicks", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "Integer32", "Counter64", "IpAddress")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ianaSmfMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 225))
ianaSmfMIB.setRevisions(('2014-10-10 00:00',))
if mibBuilder.loadTexts: ianaSmfMIB.setLastUpdated('201410100000Z')
if mibBuilder.loadTexts: ianaSmfMIB.setOrganization('IANA')
class IANAsmfOpModeIdTC(TextualConvention, Integer32):
    reference = "See Section 7.2 'Reduced Relay Set Forwarding', and the Appendices A, B, and C in RFC 6621 - 'Simplified Multicast Forwarding', Macker, J., Ed., May 2012."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3))
    namedValues = NamedValues(("independent", 1), ("routing", 2), ("crossLayer", 3))

class IANAsmfRssaIdTC(TextualConvention, Integer32):
    reference = "For example, see: Section 8.1.1. 'SMF Message TLV Type' and the Appendices A, B, and C in RFC 6621 - 'Simplified Multicast Forwarding', Macker, J., Ed., May 2012. RFC 3626 - Clausen, T., Ed., and P. Jacquet, Ed., 'Optimized Link State Routing Protocol (OLSR)', October 2003. RFC 5614 - Ogier, R. and P. Spagnolo, 'Mobile Ad Hoc Network (MANET) Extension of OSPF Using Connected Dominating Set (CDS) Flooding', August 2009. RFC 7181 - Clausen, T., Dearlove, C., Jacquet, P., and U. Herberg, 'The Optimized Link State Routing Protocol Version 2', April 2014."
    status = 'current'
    subtypeSpec = Integer32.subtypeSpec + ConstraintsUnion(SingleValueConstraint(1, 2, 3, 4))
    namedValues = NamedValues(("cF", 1), ("sMPR", 2), ("eCDS", 3), ("mprCDS", 4))

mibBuilder.exportSymbols("IANA-SMF-MIB", IANAsmfRssaIdTC=IANAsmfRssaIdTC, IANAsmfOpModeIdTC=IANAsmfOpModeIdTC, ianaSmfMIB=ianaSmfMIB, PYSNMP_MODULE_ID=ianaSmfMIB)
