#
# PySNMP MIB module PPVPN-TC (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PPVPN-TC
# Produced by pysmi-0.3.4 at Wed May  1 14:41:54 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueSizeConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, Counter32, Gauge32, MibIdentifier, Counter64, NotificationType, ModuleIdentity, IpAddress, Unsigned32, TimeTicks, Bits, iso, ObjectIdentity = mibBuilder.importSymbols("SNMPv2-SMI", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "Counter32", "Gauge32", "MibIdentifier", "Counter64", "NotificationType", "ModuleIdentity", "IpAddress", "Unsigned32", "TimeTicks", "Bits", "iso", "ObjectIdentity")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
class VPNId(TextualConvention, OctetString):
    reference = "RFC 2685, Fox & Gleeson, 'Virtual Private Networks Identifier', September 1999."
    description = 'The purpose of a VPN-ID is to identify a VPN. The global VPN Identifier format is: 3 octet VPN Authority, Organizationally Unique Identifier followed by 4 octet VPN index identifying VPN according to OUI'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 7)

mibBuilder.exportSymbols("PPVPN-TC", VPNId=VPNId)
