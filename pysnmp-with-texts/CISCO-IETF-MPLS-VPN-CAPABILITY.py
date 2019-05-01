#
# PySNMP MIB module CISCO-IETF-MPLS-VPN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-MPLS-VPN-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:00:36 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
OctetString, Integer, ObjectIdentifier = mibBuilder.importSymbols("ASN1", "OctetString", "Integer", "ObjectIdentifier")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, ConstraintsUnion, SingleValueConstraint, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "ConstraintsUnion", "SingleValueConstraint", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Counter32, Counter64, Unsigned32, Integer32, Gauge32, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, iso, TimeTicks, IpAddress, NotificationType, MibIdentifier, ObjectIdentity, Bits = mibBuilder.importSymbols("SNMPv2-SMI", "Counter32", "Counter64", "Unsigned32", "Integer32", "Gauge32", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "iso", "TimeTicks", "IpAddress", "NotificationType", "MibIdentifier", "ObjectIdentity", "Bits")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoMplsVpnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 308))
ciscoMplsVpnCapability.setRevisions(('2003-06-25 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoMplsVpnCapability.setRevisionsDescriptions(('Initial version.',))
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setLastUpdated('200306251200Z')
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: mpls-mib@cisco.com')
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setDescription('Agent capabilities for MPLS-VPN-MIB')
ciscoMplsVpnCapabilityV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 308, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMplsVpnCapabilityV12 = ciscoMplsVpnCapabilityV12.setProductRelease('Cisco IOS 12.0(21)ST, Cisco IOS 12.2(21)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMplsVpnCapabilityV12 = ciscoMplsVpnCapabilityV12.setStatus('current')
if mibBuilder.loadTexts: ciscoMplsVpnCapabilityV12.setDescription('MPLS Virtual Private Network MIB capabilities')
mibBuilder.exportSymbols("CISCO-IETF-MPLS-VPN-CAPABILITY", ciscoMplsVpnCapabilityV12=ciscoMplsVpnCapabilityV12, ciscoMplsVpnCapability=ciscoMplsVpnCapability, PYSNMP_MODULE_ID=ciscoMplsVpnCapability)
