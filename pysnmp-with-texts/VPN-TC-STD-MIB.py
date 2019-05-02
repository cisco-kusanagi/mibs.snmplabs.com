#
# PySNMP MIB module VPN-TC-STD-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/VPN-TC-STD-MIB
# Produced by pysmi-0.3.4 at Wed May  1 11:52:39 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ValueRangeConstraint, ConstraintsIntersection, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ValueRangeConstraint", "ConstraintsIntersection", "ConstraintsUnion", "ValueSizeConstraint")
NotificationGroup, ModuleCompliance = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance")
IpAddress, Gauge32, NotificationType, mib_2, Counter64, iso, Integer32, Counter32, ObjectIdentity, Unsigned32, TimeTicks, Bits, ModuleIdentity, MibIdentifier, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "IpAddress", "Gauge32", "NotificationType", "mib-2", "Counter64", "iso", "Integer32", "Counter32", "ObjectIdentity", "Unsigned32", "TimeTicks", "Bits", "ModuleIdentity", "MibIdentifier", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
vpnTcMIB = ModuleIdentity((1, 3, 6, 1, 2, 1, 129))
vpnTcMIB.setRevisions(('2005-11-15 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: vpnTcMIB.setRevisionsDescriptions(('Initial version, published as RFC 4265.',))
if mibBuilder.loadTexts: vpnTcMIB.setLastUpdated('200511150000Z')
if mibBuilder.loadTexts: vpnTcMIB.setOrganization('Layer 3 Virtual Private Networks (L3VPN) Working Group.')
if mibBuilder.loadTexts: vpnTcMIB.setContactInfo('Benson Schliesser bensons@savvis.net Thomas D. Nadeau tnadeau@cisco.com This TC MIB is a product of the PPVPN http://www.ietf.org/html.charters/ppvpn-charter.html and subsequently the L3VPN http://www.ietf.org/html.charters/l3vpn-charter.html working groups. Comments and discussion should be directed to l3vpn@ietf.org')
if mibBuilder.loadTexts: vpnTcMIB.setDescription('This MIB contains TCs for VPNs. Copyright (C) The Internet Society (2005). This version of this MIB module is part of RFC 4265; see the RFC itself for full legal notices.')
class VPNId(TextualConvention, OctetString):
    reference = "Fox, B. and Gleeson, B., 'Virtual Private Networks Identifier', RFC 2685, September 1999."
    description = 'The purpose of a VPN-ID is to uniquely identify a VPN. The Global VPN Identifier format is: 3 octet VPN Authority, Organizationally Unique Identifier followed by 4 octet VPN index identifying VPN according to OUI'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(7, 7)
    fixedLength = 7

class VPNIdOrZero(TextualConvention, OctetString):
    description = 'This textual convention is an extension of the VPNId textual convention that defines a non-zero-length OCTET STRING to identify a physical entity. This extension permits the additional value of a zero-length OCTET STRING. The semantics of the value zero-length OCTET STRING are object-specific and must therefore be defined as part of the description of any object that uses this syntax. Examples of usage of this extension are situations where none or all VPN IDs need to be referenced.'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ConstraintsUnion(ValueSizeConstraint(0, 0), ValueSizeConstraint(7, 7), )
mibBuilder.exportSymbols("VPN-TC-STD-MIB", VPNIdOrZero=VPNIdOrZero, PYSNMP_MODULE_ID=vpnTcMIB, VPNId=VPNId, vpnTcMIB=vpnTcMIB)
