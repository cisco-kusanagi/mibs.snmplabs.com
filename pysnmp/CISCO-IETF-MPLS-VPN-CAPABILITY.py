#
# PySNMP MIB module CISCO-IETF-MPLS-VPN-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IETF-MPLS-VPN-CAPABILITY
# Produced by pysmi-0.3.4 at Mon Apr 29 17:43:26 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
Integer, ObjectIdentifier, OctetString = mibBuilder.importSymbols("ASN1", "Integer", "ObjectIdentifier", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
SingleValueConstraint, ConstraintsIntersection, ValueRangeConstraint, ConstraintsUnion, ValueSizeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "SingleValueConstraint", "ConstraintsIntersection", "ValueRangeConstraint", "ConstraintsUnion", "ValueSizeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
AgentCapabilities, ModuleCompliance, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "AgentCapabilities", "ModuleCompliance", "NotificationGroup")
Gauge32, ObjectIdentity, TimeTicks, NotificationType, Counter64, Counter32, iso, ModuleIdentity, MibScalar, MibTable, MibTableRow, MibTableColumn, Unsigned32, MibIdentifier, IpAddress, Bits, Integer32 = mibBuilder.importSymbols("SNMPv2-SMI", "Gauge32", "ObjectIdentity", "TimeTicks", "NotificationType", "Counter64", "Counter32", "iso", "ModuleIdentity", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Unsigned32", "MibIdentifier", "IpAddress", "Bits", "Integer32")
TextualConvention, DisplayString = mibBuilder.importSymbols("SNMPv2-TC", "TextualConvention", "DisplayString")
ciscoMplsVpnCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 308))
ciscoMplsVpnCapability.setRevisions(('2003-06-25 12:00',))
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setLastUpdated('200306251200Z')
if mibBuilder.loadTexts: ciscoMplsVpnCapability.setOrganization('Cisco Systems, Inc.')
ciscoMplsVpnCapabilityV12 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 308, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMplsVpnCapabilityV12 = ciscoMplsVpnCapabilityV12.setProductRelease('Cisco IOS 12.0(21)ST, Cisco IOS 12.2(21)T')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoMplsVpnCapabilityV12 = ciscoMplsVpnCapabilityV12.setStatus('current')
mibBuilder.exportSymbols("CISCO-IETF-MPLS-VPN-CAPABILITY", ciscoMplsVpnCapabilityV12=ciscoMplsVpnCapabilityV12, ciscoMplsVpnCapability=ciscoMplsVpnCapability, PYSNMP_MODULE_ID=ciscoMplsVpnCapability)
