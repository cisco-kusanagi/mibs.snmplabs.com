#
# PySNMP MIB module CISCO-ETHER-WIS-CAPABILITY (http://snmplabs.com/pysmi)
# ASN.1 source file:///Users/davwang4/Dev/mibs.snmplabs.com/asn1/CISCO-ETHER-WIS-CAPABILITY
# Produced by pysmi-0.3.4 at Wed May  1 11:57:33 2019
# On host DAVWANG4-M-1475 platform Darwin version 18.5.0 by user davwang4
# Using Python version 3.7.3 (default, Mar 27 2019, 09:23:15) 
#
ObjectIdentifier, Integer, OctetString = mibBuilder.importSymbols("ASN1", "ObjectIdentifier", "Integer", "OctetString")
NamedValues, = mibBuilder.importSymbols("ASN1-ENUMERATION", "NamedValues")
ValueSizeConstraint, SingleValueConstraint, ConstraintsUnion, ConstraintsIntersection, ValueRangeConstraint = mibBuilder.importSymbols("ASN1-REFINEMENT", "ValueSizeConstraint", "SingleValueConstraint", "ConstraintsUnion", "ConstraintsIntersection", "ValueRangeConstraint")
ciscoAgentCapability, = mibBuilder.importSymbols("CISCO-SMI", "ciscoAgentCapability")
ModuleCompliance, AgentCapabilities, NotificationGroup = mibBuilder.importSymbols("SNMPv2-CONF", "ModuleCompliance", "AgentCapabilities", "NotificationGroup")
ObjectIdentity, NotificationType, iso, MibIdentifier, Bits, Counter32, IpAddress, Unsigned32, TimeTicks, ModuleIdentity, Counter64, Gauge32, Integer32, MibScalar, MibTable, MibTableRow, MibTableColumn = mibBuilder.importSymbols("SNMPv2-SMI", "ObjectIdentity", "NotificationType", "iso", "MibIdentifier", "Bits", "Counter32", "IpAddress", "Unsigned32", "TimeTicks", "ModuleIdentity", "Counter64", "Gauge32", "Integer32", "MibScalar", "MibTable", "MibTableRow", "MibTableColumn")
DisplayString, TextualConvention = mibBuilder.importSymbols("SNMPv2-TC", "DisplayString", "TextualConvention")
ciscoEtherWisCapability = ModuleIdentity((1, 3, 6, 1, 4, 1, 9, 7, 531))
ciscoEtherWisCapability.setRevisions(('2007-01-23 12:00',))

if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    if mibBuilder.loadTexts: ciscoEtherWisCapability.setRevisionsDescriptions(('Initial version of this MIB module.',))
if mibBuilder.loadTexts: ciscoEtherWisCapability.setLastUpdated('200701231200Z')
if mibBuilder.loadTexts: ciscoEtherWisCapability.setOrganization('Cisco Systems, Inc.')
if mibBuilder.loadTexts: ciscoEtherWisCapability.setContactInfo('Cisco Systems Customer Service Postal: 170 W Tasman Drive San Jose, CA 95134 USA Tel: +1 800 553-NETS E-mail: cs-snmp@cisco.com')
if mibBuilder.loadTexts: ciscoEtherWisCapability.setDescription('The Agent Capabilities for ETHER-WIS.')
ciscoEtherWisCapabilityV120S = AgentCapabilities((1, 3, 6, 1, 4, 1, 9, 7, 531, 1))
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherWisCapabilityV120S = ciscoEtherWisCapabilityV120S.setProductRelease('Cisco IOS 12.0S for GSR.')
if getattr(mibBuilder, 'version', (0, 0, 0)) > (4, 4, 0):
    ciscoEtherWisCapabilityV120S = ciscoEtherWisCapabilityV120S.setStatus('current')
if mibBuilder.loadTexts: ciscoEtherWisCapabilityV120S.setDescription('ETHER-WIS capabilities for GSR platform.')
mibBuilder.exportSymbols("CISCO-ETHER-WIS-CAPABILITY", ciscoEtherWisCapabilityV120S=ciscoEtherWisCapabilityV120S, PYSNMP_MODULE_ID=ciscoEtherWisCapability, ciscoEtherWisCapability=ciscoEtherWisCapability)
