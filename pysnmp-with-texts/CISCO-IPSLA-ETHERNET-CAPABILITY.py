#
# PySNMP MIB module CISCO-IPSLA-ETHERNET-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-IPSLA-ETHERNET-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 12:02:38 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, OctetString, Integer = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "OctetString", "Integer")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueRangeConstraint, SingleValueConstraint, ConstraintsUnion, ValueSizeConstraint, ConstraintsIntersection = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueRangeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ValueSizeConstraint", "ConstraintsIntersection")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
NotificationGroup, ModuleCompliance, AgentCapabilities = mibBuilder.importSymbols("SNMPv2-CONF", "NotificationGroup", "ModuleCompliance", "AgentCapabilities")
NotificationType, ModuleIdentity, iso, Counter32, Unsigned32, ObjectIdentity, MibIdentifier, Bits, MibScalar, MibTable, MibTableRow, MibTableColumn, Gauge32, TimeTicks, IpAddress, Integer32, Counter64 = mibBuilder.importSymbols("SNMPv2-SMI", "NotificationType", "ModuleIdentity", "iso", "Counter32", "Unsigned32", "ObjectIdentity", "MibIdentifier", "Bits", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn", "Gauge32", "TimeTicks", "IpAddress", "Integer32", "Counter64")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoIpSlaEthernetCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 498))
ciscoIpSlaEthernetCapability.setRevisions(('2006-02-08 00:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setRevisionsDescriptions(('Initial Creation',))
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setLastUpdated('200602080000Z')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setContactInfo(' Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-ipsla@cisco.com')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapability.setDescription('Agent capabilities for CISCO-IPSLA-ETHERNET-MIB')
ciscoIpSlaEthernetCapabilityRev1 = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 498, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaEthernetCapabilityRev1 = ciscoIpSlaEthernetCapabilityRev1.setProductRelease('Cisco IOS 12.2(01)SRB')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoIpSlaEthernetCapabilityRev1 = ciscoIpSlaEthernetCapabilityRev1.setStatus('current')
if mibBuilder.loadTexts: ciscoIpSlaEthernetCapabilityRev1.setDescription('Cisco IP SLA ETHERNET MIB capabilities')
mibBuilder.exportSymbols("CISCO-IPSLA-ETHERNET-CAPABILITY", PYSNMP_MODULE_ID=ciscoIpSlaEthernetCapability, ciscoIpSlaEthernetCapabilityRev1=ciscoIpSlaEthernetCapabilityRev1, ciscoIpSlaEthernetCapability=ciscoIpSlaEthernetCapability)
