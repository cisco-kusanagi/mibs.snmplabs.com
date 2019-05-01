#
# PySNMP MIB module PPVPN-TC-MIB (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/PPVPN-TC-MIB
# Produced by pysmi-0.3.4 at Wed May  1 14:14:57 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueSizeConstraint, ValueRangeConstraint, ConstraintsUnion = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueSizeConstraint", "ValueRangeConstraint", "ConstraintsUnion")
ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "NotificationGroup")
NotificationType, ObjectIdentity, ModuleIdentity, Bits, Counter64, MibIdentifier, iso, Unsigned32, IpAddress, Gauge32, MibScalar, MibTable, MibTableRow, MibTableColumn, Integer32, TimeTicks, experimental, Counter32 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ObjectIdentity", "ModuleIdentity", "Bits", "Counter64", "MibIdentifier", "iso", "Unsigned32", "IpAddress", "Gauge32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Integer32", "TimeTicks", "experimental", "Counter32")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ppvpnTcMIB = ModuleIdentity((1, 3, 6, 1, 3, 1111))
ppvpnTcMIB.setRevisions(('2001-02-28 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ppvpnTcMIB.setRevisionsDescriptions(('Initial draft version.',))
if mibBuilder.loadTexts: ppvpnTcMIB.setLastUpdated('200102281200Z')
if mibBuilder.loadTexts: ppvpnTcMIB.setOrganization('Provider Provisioned Virtual Private Networks Working Group.')
if mibBuilder.loadTexts: ppvpnTcMIB.setContactInfo(' Benson Schliesser bensons@savvis.net Thomas D. Nadeau tnadeau@cisco.com Comments and discussion to ppvpn@ietf.org')
if mibBuilder.loadTexts: ppvpnTcMIB.setDescription('This MIB contains TCs for PPVPN.')
class VPNId(TextualConvention, OctetString):
    reference = "RFC 2685, Fox & Gleeson, 'Virtual Private Networks Identifier', September 1999."
    description = 'The purpose of a VPN-ID is to identify a VPN. The global VPN Identifier format is: 3 octet VPN Authority, Organizationally Unique Identifier followed by 4 octet VPN index identifying VPN according to OUI'
    status = 'current'
    subtypeSpec = OctetString.subtypeSpec + ValueSizeConstraint(0, 7)

mibBuilder.exportSymbols("PPVPN-TC-MIB", PYSNMP_MODULE_ID=ppvpnTcMIB, ppvpnTcMIB=ppvpnTcMIB, VPNId=VPNId)
