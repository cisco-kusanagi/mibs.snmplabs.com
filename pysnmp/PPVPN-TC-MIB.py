#
# PySNMP MIB module PPVPN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PPVPN-TC-MIB
# Produced by pysmi-0.3.4 at Mon Apr 29 20:04:56 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, ValueRangeConstraint, ConstraintsIntersection, SingleValueConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "SingleValueConstraint", "ConstraintsUnion")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
ModuleIdentity, Integer32, NotificationType, Bits, Counter64, ObjectIdentity, MibIdentifier, Counter32, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, iso, Gauge32, IpAddress, experimental, TimeTicks = mibBuilder.importSymbols("SNMPv2-SMI", "ModuleIdentity", "Integer32", "NotificationType", "Bits", "Counter64", "ObjectIdentity", "MibIdentifier", "Counter32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "iso", "Gauge32", "IpAddress", "experimental", "TimeTicks")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ppvpnTcMIB = ModuleIdentity((1, 3, 6, 1, 3, 1111))
ppvpnTcMIB.setRevisions(('2001-02-28 12:00',))
if mibBuilder.loadTexts: ppvpnTcMIB.setLastUpdated('200102281200Z')
if mibBuilder.loadTexts: ppvpnTcMIB.setOrganization('Provider Provisioned Virtual Private Networks Working Group.')
class VPNId(TextualConvention, OctetString):
    reference = "RFC 2685, Fox & Gleeson, 'Virtual Private Networks Identifier', September 1999."
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 7)

mibBuilder.exportSymbols("PPVPN-TC-MIB", VPNId=VPNId, ppvpnTcMIB=ppvpnTcMIB, PYSNMP_MODULE_ID=ppvpnTcMIB)
